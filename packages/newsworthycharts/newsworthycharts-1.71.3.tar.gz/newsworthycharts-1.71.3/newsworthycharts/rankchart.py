"""
A chart showing ranking over time (like ”most popular baby names”)
"""
from .serialchart import SerialChart
from .lib.utils import to_date
import numpy as np


class BumpChart(SerialChart):
    """Plot a rank chart

        Data should be a list of iterables of (rank, date string) tuples, eg:
    `[ [("2010-01-01", 2), ("2011-01-01", 3)] ]`, combined with a list of
    labels in the same order
    """

    def __init__(self, *args, **kwargs):
        super(BumpChart, self).__init__(*args, **kwargs)

        if self.line_width is None:
            self.line_width = 0.9
        self.label_placement = 'none'
        self.type = "line"
        self.decimals = 0
        self.revert_value_axis = True
        self.ymin = 1
        self.allow_broken_y_axis = False
        self.grid = False
        self.accentuate_baseline = False

        self.line_marker = "o-"
        self.line_marker_size = 5

    def _get_line_colors(self, i, *args):
        if not self.data:
            # Don't waste time
            return None
        if self.highlight and self.highlight in self.labels and i == self.labels.index(self.highlight):
            return self._nwc_style["strong_color"]
        elif self.colors and i < len(self.colors):
            return self.colors[i]
        return self._nwc_style["neutral_color"]

    def _after_add_data(self):
        # Print out every rank
        if self.data.max_val < 30:
            _range = list(range(1, int(self.data.max_val) + 1))
            self.ax.yaxis.set_ticks(_range, _range)
        # Add labels
        slots_occupied = {
            to_date(k): [] for k in self.data.x_points
        }
        for i, serie in enumerate(self.data):
            values = np.array(self.serie_values[i], dtype=np.float64)
            dates = [to_date(x[0]) for x in serie]
            color = self._get_line_colors(i)

            endpoints = [
                (d, values[idx])
                for (idx, d) in enumerate(dates) if idx == len(dates) - 1 or np.isnan(values[idx + 1])
            ]
            for ep in endpoints:
                position = ep[1]
                while position in slots_occupied[ep[0]]:
                    position += 1
                slots_occupied[ep[0]].append(position)
                self._annotate_point(
                    self.labels[i],
                    (ep[0], position),
                    "right",
                    offset=15,
                    color=color,
                    va="center",
                    # arrowprops=dict(arrowstyle="->", color=color),
                )
        """
        labels = []
        for i, serie in enumerate(self.data):
            values = np.array(self.serie_values[i], dtype=np.float64)
            dates = [to_date(x[0]) for x in serie]
            color = self._get_line_colors(i)

            endpoints = [
                (d, values[idx])
                for (idx, d) in enumerate(dates) if idx == len(dates) - 1 or np.isnan(values[idx + 1])
            ]
            for ep in endpoints:
                lbl = self._annotate_point(
                    self.labels[i],
                    (ep[0], ep[1]),
                    "right",
                    offset=15,
                    color=color,
                    va="center",
                    # arrowprops=dict(arrowstyle="->", color=color),
                )
                loops = 0
                overlap = True if len(labels) > 0 else False
                while overlap:
                    for i, bb in enumerate(labels):
                        if i == len(labels) - 1:
                            overlap = False
                            break
                        bbox1 = lbl.get_window_extent()
                        bbox2 = labels[i].get_window_extent()
                        print(bbox1, bbox2)
                        if bbox1.y1 < bbox2.y0 + 10 and bbox1.x1 > bbox2.x0 + 5:  # allow for some overlap
                            xy1 = lbl.xyann
                            lbl.xyann = (xy1[0], xy1[1] + 1)
                            break
                        loops += 1
                    if loops > 500:
                        break
                labels.append(lbl)
        """
