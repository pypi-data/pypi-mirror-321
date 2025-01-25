import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import TYPE_CHECKING, Callable, Optional, Union

import numpy as np
from numpy import ndarray
from rasterio.crs import CRS

if TYPE_CHECKING:
    from glidergun._grid import Grid


def create_parent_directory(file_path: str):
    directory = "/".join(re.split(r"/|\\", file_path)[0:-1])
    Path(directory).mkdir(parents=True, exist_ok=True)


def get_crs(crs: Union[int, CRS]):
    return CRS.from_epsg(crs) if isinstance(crs, int) else crs


def format_type(data: ndarray):
    if data.dtype == "float64":
        return np.asanyarray(data, dtype="float32")
    if data.dtype == "int64":
        return np.asanyarray(data, dtype="int32")
    if data.dtype == "uint64":
        return np.asanyarray(data, dtype="uint32")
    return data


def get_nodata_value(dtype: str) -> Union[float, int, None]:
    if dtype == "bool":
        return None
    if dtype.startswith("float"):
        return float(np.finfo(dtype).min)
    if dtype.startswith("uint"):
        return np.iinfo(dtype).max
    return np.iinfo(dtype).min


def batch_process(
    func: Callable[["Grid"], "Grid"], buffer: int, grid: "Grid", max_workers: int
) -> "Grid":
    def tile():
        stride = 8000 // buffer
        for x in range(0, grid.width // stride + 1):
            xmin, xmax = x * stride, min((x + 1) * stride, grid.width)
            if xmin < xmax:
                for y in range(0, grid.height // stride + 1):
                    ymin, ymax = y * stride, min((y + 1) * stride, grid.height)
                    if ymin < ymax:
                        yield xmin, ymin, xmax, ymax

    tiles = list(tile())

    if len(tiles) <= 4:
        return func(grid)

    result: Optional["Grid"] = None
    cell_size = grid.cell_size

    def f(tile):
        xmin, ymin, xmax, ymax = tile
        g = func(
            grid.clip(
                grid.xmin + (xmin - buffer) * cell_size.x,
                grid.ymin + (ymin - buffer) * cell_size.y,
                grid.xmin + (xmax + buffer) * cell_size.x,
                grid.ymin + (ymax + buffer) * cell_size.y,
            )
        )
        return g.clip(
            grid.xmin + xmin * cell_size.x,
            grid.ymin + ymin * cell_size.y,
            grid.xmin + xmax * cell_size.x,
            grid.ymin + ymax * cell_size.y,
        )

    if max_workers > 1:
        with ThreadPoolExecutor(max_workers or 1) as executor:
            for r in executor.map(f, tiles):
                result = result.mosaic(r) if result else r
    else:
        for r in map(f, tiles):
            result = result.mosaic(r) if result else r

    assert result
    return result
