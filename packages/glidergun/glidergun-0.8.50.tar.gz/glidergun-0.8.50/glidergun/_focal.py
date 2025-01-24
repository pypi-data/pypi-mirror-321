from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable, List, Optional, Union, cast

import numpy as np
from numpy import ndarray
from numpy.lib.stride_tricks import sliding_window_view

if TYPE_CHECKING:
    from glidergun._grid import Grid


@dataclass(frozen=True)
class Focal:
    def focal(
        self,
        func: Callable[[ndarray], Any],
        buffer: int,
        circle: bool,
        max_workers: int,
    ) -> "Grid":
        def f(g: "Grid") -> "Grid":
            size = 2 * buffer + 1
            mask = _mask(buffer) if circle else np.full((size, size), True)
            array = sliding_window_view(_pad(g.data, buffer), (size, size))
            result = func(array[:, :, mask])
            return g.local(result)

        return _batch(f, buffer, cast("Grid", self), max_workers)

    def focal_generic(
        self,
        func: Callable[[List[float]], float],
        buffer: int = 1,
        circle: bool = False,
        ignore_nan: bool = True,
        max_workers: int = 1,
    ) -> "Grid":
        def f(a):
            values = [n for n in a if n != np.nan] if ignore_nan else list(a)
            return func(values)

        return self.focal(
            lambda a: np.apply_along_axis(f, 2, a), buffer, circle, max_workers
        )

    def focal_count(
        self,
        value: Union[float, int],
        buffer: int = 1,
        circle: bool = False,
        max_workers: int = 1,
        **kwargs,
    ):
        return self.focal(
            lambda a: np.count_nonzero(a == value, axis=2, **kwargs),
            buffer,
            circle,
            max_workers,
        )

    def focal_ptp(
        self, buffer: int = 1, circle: bool = False, max_workers: int = 1, **kwargs
    ):
        return self.focal(
            lambda a: np.ptp(a, axis=2, **kwargs), buffer, circle, max_workers
        )

    def focal_median(
        self,
        buffer: int = 1,
        circle: bool = False,
        ignore_nan: bool = True,
        max_workers: int = 1,
        **kwargs,
    ):
        f = np.nanmedian if ignore_nan else np.median
        return self.focal(lambda a: f(a, axis=2, **kwargs), buffer, circle, max_workers)

    def focal_mean(
        self,
        buffer: int = 1,
        circle: bool = False,
        ignore_nan: bool = True,
        max_workers: int = 1,
        **kwargs,
    ):
        f = np.nanmean if ignore_nan else np.mean
        return self.focal(lambda a: f(a, axis=2, **kwargs), buffer, circle, max_workers)

    def focal_std(
        self,
        buffer: int = 1,
        circle: bool = False,
        ignore_nan: bool = True,
        max_workers: int = 1,
        **kwargs,
    ):
        f = np.nanstd if ignore_nan else np.std
        return self.focal(lambda a: f(a, axis=2, **kwargs), buffer, circle, max_workers)

    def focal_var(
        self,
        buffer: int = 1,
        circle: bool = False,
        ignore_nan: bool = True,
        max_workers: int = 1,
        **kwargs,
    ):
        f = np.nanvar if ignore_nan else np.var
        return self.focal(lambda a: f(a, axis=2, **kwargs), buffer, circle, max_workers)

    def focal_min(
        self,
        buffer: int = 1,
        circle: bool = False,
        ignore_nan: bool = True,
        max_workers: int = 1,
        **kwargs,
    ):
        f = np.nanmin if ignore_nan else np.min
        return self.focal(lambda a: f(a, axis=2, **kwargs), buffer, circle, max_workers)

    def focal_max(
        self,
        buffer: int = 1,
        circle: bool = False,
        ignore_nan: bool = True,
        max_workers: int = 1,
        **kwargs,
    ):
        f = np.nanmax if ignore_nan else np.max
        return self.focal(lambda a: f(a, axis=2, **kwargs), buffer, circle, max_workers)

    def focal_sum(
        self,
        buffer: int = 1,
        circle: bool = False,
        ignore_nan: bool = True,
        max_workers: int = 1,
        **kwargs,
    ):
        f = np.nansum if ignore_nan else np.sum
        return self.focal(lambda a: f(a, axis=2, **kwargs), buffer, circle, max_workers)

    def fill_nan(self, max_exponent: int = 4, max_workers: int = 1):
        if not cast("Grid", self).has_nan:
            return self

        def f(g: "Grid"):
            n = 0
            while g.has_nan and n <= max_exponent:
                g = g.is_nan().then(g.focal_mean(2**n, True), g)
                n += 1
            return g

        return _batch(f, 2**max_exponent, cast("Grid", self), max_workers)


def _mask(buffer: int) -> ndarray:
    size = 2 * buffer + 1
    rows = []
    for y in range(size):
        row = []
        for x in range(size):
            d = ((x - buffer) ** 2 + (y - buffer) ** 2) ** (1 / 2)
            row.append(d <= buffer)
        rows.append(row)
    return np.array(rows)


def _pad(data: ndarray, buffer: int):
    row = np.zeros((buffer, data.shape[1])) * np.nan
    col = np.zeros((data.shape[0] + 2 * buffer, buffer)) * np.nan
    return np.hstack([col, np.vstack([row, data, row]), col], dtype="float32")


def _batch(
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

    with ThreadPoolExecutor(max_workers or 1) as executor:
        for r in executor.map(f, tiles):
            result = result.mosaic(r) if result else r

    assert result
    return result
