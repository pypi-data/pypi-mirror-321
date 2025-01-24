from abc import ABC, abstractmethod
from typing import Callable
import tkinter as tk
from dataclasses import dataclass, field
from DLMS_SPODES.types import cdt
from .base import CDT, Simple
from tKot.common import Point


@dataclass
class ID(Simple, ABC):
    source: bool = True
    width: int = 100
    type: int = 0

    def __post_init__(self):
        self._font_height = self.font_.metrics('linespace')
        self.methods: tuple[Callable[[Point, str], None], ...] = (
            self.create_rectangle,
            self.create_oval,
            self.create_triangle,
            self.create_star
        )
        self.colors: tuple[str, ...] = (
            "black",
            "red",
            "blue",
            "green",
            "brown"
        )

    def create_rectangle(self, p: Point, color: str):
        self.can.create_rectangle(
            *p,
            p.x + self._font_height, p.y + self._font_height,
            fill=color)

    def create_oval(self, p: Point, color: str):
        self.can.create_oval(
            *p,
            p.x + self._font_height, p.y + self._font_height,
            fill=color)

    def create_triangle(self, p: Point, color: str):
        self.can.create_polygon(
            (p.x, y1 := p.y + self._font_height),
            (p.x, y2 := p.y + int(self._font_height * 0.7)),
            (p.x + self._font_height // 2, p.y),
            (x1 := p.x + self._font_height, y2),
            (x1, y1),
            (p.x, y1),
            fill=color)

    def create_star(self, p: Point, color: str):
        self.can.create_polygon(
            (x0 := int(0.50 * self._font_height) + p.x, int(-0.20 * self._font_height) + p.y),
            (int(0.71 * self._font_height) + p.x, y1 := int(0.22 * self._font_height) + p.y),
            (int(1.17 * self._font_height) + p.x, y2 := int(0.28 * self._font_height) + p.y),
            (int(0.83 * self._font_height) + p.x, y3 := int(0.61 * self._font_height) + p.y),
            (int(0.91 * self._font_height) + p.x, y4 := int(1.07 * self._font_height) + p.y),
            (x0, int(0.85 * self._font_height) + p.y),
            (int(0.09 * self._font_height) + p.x, y4),
            (int(0.17 * self._font_height) + p.x, y3),
            (int(-0.17 * self._font_height) + p.x, y2),
            (int(0.29 * self._font_height) + p.x, y1),
            fill=color)

    def place2(self, p: Point, data: cdt.CommonDataTypes) -> Point:
        self.methods[self.type % 4](p, self.colors[self.type % 5])
        self.can.create_text(
            p.x + self._font_height // 2, p.y + self._font_height // 2,
            text="ID" if self.source else "id",
            fill="white")
        return self.place3(p, data)

    @abstractmethod
    def place3(self, p: Point, data: cdt.Digital) -> Point:
        """place data content"""


@dataclass
class DigitalID(ID):

    def place3(self, p: Point, data: cdt.Digital) -> Point:
        self.can.create_text(
            p.x + (self.width + self._font_height) // 2, p.y + self._font_height // 2,
            text=str(data),
        )
        return Point(self.width, self._font_height)


@dataclass
class OctetStringID(ID):

    def __crop_text(self, source: str) -> str:
        if (res := self.font_.measure(source)) < self.width:
            return source
        else:
            return F"{source[:int((self.width / res) * len(source)) - 1]}..."

    def place3(self, p: Point, data: cdt.OctetString) -> Point:
        size = Point(self.width, 2 * self._font_height)
        self.can.create_line(
            p.x + int(size.x * 0.1), p.y + size.y // 2,
            p.x + int(size.x * 0.9), p.y + size.y // 2,
        )
        self.can.create_text(
            p.x + size.x // 2, p.y,
            anchor=tk.N,
            text=self.__crop_text(str(data)),
        )
        self.can.create_text(
            p.x + size.x // 2, p.y + self._font_height,
            anchor=tk.N,
            fill="red",
            text=self.__crop_text(data.contents.decode(encoding="utf-8", errors="replace")))
        return size
