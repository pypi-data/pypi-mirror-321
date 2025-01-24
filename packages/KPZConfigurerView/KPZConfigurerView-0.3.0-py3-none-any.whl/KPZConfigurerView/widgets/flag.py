import tkinter as tk
from copy import copy
from dataclasses import dataclass
from .base import CidPar, CDT, Array, Simple, Sequence, Cid, Piece
from DLMS_SPODES.types.common_data_types import IntegerFlag
from tKot.common import Point, Size, Box, Polygon


check = Polygon(20, 10, 50, 100, 100, 0, 50, 75)


@dataclass
class IntegerFlag(Piece):

    def __post_init__(self):
        self._font_height = self.font_.metrics('linespace')
        self._check = check.reshape(Size(self._font_height, self._font_height))
        self._box = Box(0, 0, *self._check.size)

    def place2(self, p: Point, data: IntegerFlag) -> Size:
        self.el_cids: list[Cid] = [-1] * data.LENGTH * 8
        """cids for fields according by names of bits"""
        max_x: int = 0
        cursor = copy(p)
        for i, name in data.NAMES.items():
            self.el_cids[i] = self.can.create_rectangle(
                *(self._box+cursor),
                fill="white"
            )
            if data[i]:
                self.can.create_polygon(*(self._check + cursor))
            msg = F"{i}. {name}"
            self.can.create_text(
                *(cursor + Point(x=self._font_height)),
                text=msg,
                anchor=tk.NW
            )
            cursor.y += self._font_height
            max_x = max(self.font_.measure(msg), max_x)
        return Size(max_x, cursor.y - p.y)
