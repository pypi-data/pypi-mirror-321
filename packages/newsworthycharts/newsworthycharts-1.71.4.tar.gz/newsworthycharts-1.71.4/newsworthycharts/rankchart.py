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
        if self.line_marker_size is None:
            self.line_marker_size = 6
        self.label_placement = 'none'
        self.type = "line"
        self.decimals = 0
        self.revert_value_axis = True
        self.ymin = 1
        self.allow_broken_y_axis = False
        self.grid = False
        self.accentuate_baseline = False

        self.line_marker = "o-"

    def _get_line_colors(self, i, *args):
        if not self.data:
            # Don't waste time
            return None
        if self.highlight and self.highlight in self.labels and i == self.labels.index(self.highlight):
            return self._nwc_style["strong_color"]
        elif self.colors and i < len(self.colors):
            return self.colors[i]
        return self._nwc_style["neutral_color"]

    """
    def _get_marker_fill(self, i):
        pass
    """

    def _after_add_data(self):
        # Print out every rank
        if self.data.max_val < 30:
            _range = list(range(1, int(self.data.max_val) + 1))
            self.ax.yaxis.set_ticks(_range, _range)

        # Recolor markers with more than one line passing through
        # (MPL does not allow access to individual markers, so we'll overwrite them)

        for date in self.data.x_points:
            value_colors = {}
            for i, serie in enumerate(self.data):
                values = np.array(self.serie_values[i], dtype=np.float64)
                dates = [x[0] for x in serie]
                color = self._get_line_colors(i)
                if date not in dates:
                    continue
                idx = dates.index(date)
                if np.isnan(values[idx]):
                    continue
                val = int(values[idx])
                if val not in value_colors:
                    value_colors[val] = []
                value_colors[val].append(color)
            for val, colors in value_colors.items():
                if len(colors) < 2:
                    continue
                elif len(colors) == 2:
                    self.ax.plot(
                        to_date(date),
                        val,
                        self.line_marker,
                        markersize=self.line_marker_size,
                        color="None",
                        fillstyle="left",
                        markeredgewidth=0,
                        markerfacecolor=colors[0],
                        markerfacecoloralt=colors[1],
                        zorder=100,
                    )
                else:
                    self.ax.plot(
                        to_date(date),
                        val,
                        self.line_marker,
                        markersize=self.line_marker_size,
                        color=self._nwc_style["neutral_color"],
                        markeredgewidth=0,
                        zorder=100,
                    )
        # Add labels
        slots_occupied = {
            to_date(k): [] for k in self.data.x_points
        }
        # distance between rank ticks
        # y1 = self.ax.transData.transform((0, 1))
        # y2 = self.ax.transData.transform((0, 2))
        # dist = abs(y1[1] - y2[1])
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
                # pos_diff = position - ep[1]
                slots_occupied[ep[0]].append(position)
                self._annotate_point(
                    self.labels[i],
                    # (ep[0], ep[1]),
                    (ep[0], position),
                    "right",
                    offset=15,
                    color=color,
                    va="center",
                    # xytext=(15, -abs(y1[1] - y2[1]) * pos_diff),
                    # arrowprops=dict(arrowstyle="->", color=color) if pos_diff > 1 else None,
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
