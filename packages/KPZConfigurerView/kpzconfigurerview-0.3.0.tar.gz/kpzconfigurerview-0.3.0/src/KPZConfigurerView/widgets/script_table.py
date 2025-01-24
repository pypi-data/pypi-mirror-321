from dataclasses import dataclass, field
from typing import Optional
from .base import CidPar, CDT, Array, Simple, Sequence
from DLMS_SPODES.cosem_interface_classes import script_table
from tKot.common import Point
from . import colors
from .id_ import DigitalID


@dataclass
class Script(Sequence):

    def __post_init__(self):
        self._height = self.font_.measure("00000")
        """height of cube"""
        self.label_cid: Optional[int] = None

    def place2(self, p: Point, data: script_table.Script) -> Point:
        size = Point(self._height, self._height)
        self.can.create_rectangle(
            *p,
            *(p+size),
            width=2,
            fill=colors.day_profile_action_color.get(int(data.script_identifier), colors.DEFAULT).back
        )
        self.elements = [DigitalID(
            can=self.can,
            param=self.param + b'\x00',
            font_=self.font_,
            width=size.y,
            type=0
        )]
        self.elements[-1].place(p, data.script_identifier)
        # self.label_cid = self.can.create_text(
        #     *(p + size // 4),
        #     text=str(data.script_identifier),
        #     fill=colors.day_profile_action_color.get(int(data.script_identifier), colors.DEFAULT).fill,
        #     font=self.font_)
        return size


@dataclass
class Scripts(Array):
    elements: list[Script] = field(init=False, default_factory=list)
    el_t: Script = field(init=False, default=Script)

    def place2(self, p: Point, data: script_table.Scripts) -> Point:
        return self.place_horizontal(p, data)
