import copy
import datetime
from abc import ABC, abstractmethod
import tkinter as tk
import math
from typing import Optional
from tkinter import font
from dataclasses import dataclass, field
from DLMS_SPODES.cosem_interface_classes import activity_calendar
from DLMS_SPODES.types import cdt
from .base import CDT, Array, Simple, CidPar, IndexData, Sequence
from tKot.common import Point
from . import colors
from . import id_


@dataclass
class DaySchedule(CDT):
    with_time: bool = True
    day_c_id: int = field(init=False)

    def __post_init__(self):
        self._day_width = self.font_.measure("00:00")
        self._day_height = self._day_width * 7
        """ width of one day widget """
        self._font_height = self.font_.metrics('linespace')
        self.actions_cids: list[int] = list()
        """sort according with timestamp"""
        self.actions_label_cids: list[int] = list()
        """sort according with timestamp"""
        self.output_indexes: list[int] = list()
        """according with input value"""
        self.action_sel: int | None = None

    def place2(self, p: Point, data: activity_calendar.DaySchedule) -> Point:
        d_p_a: activity_calendar.DayProfileAction

        def get_pos(value: datetime.time, width: int) -> int:
            """ return position coordinate by width """
            return round((value.hour * 60 + value.minute) / 1440 * width)

        size = Point(self._day_width, self._day_height)
        self.day_c_id = self.can.create_rectangle(
            *p,
            *(p + size),
            width=2,
            fill='white')
        for d_p_a in sorted(data):
            action_p = p + Point(y=get_pos(t := d_p_a.start_time.decode(), self._day_height))
            color = colors.day_profile_action_color.get(int(d_p_a.script_selector), colors.DEFAULT)
            self.actions_cids.insert(0, self.can.create_rectangle(  # big time is first for action select
                *action_p,
                *(p + size),
                fill=color.back,
            ))
            self.output_indexes.append(data.values.index(d_p_a))
            if self.with_time:
                self.actions_label_cids.insert(0, self.can.create_text(
                    *action_p,
                    text=t.isoformat('minutes'),
                    anchor=tk.NW,
                    fill=color.fill,
                    font=self.font_
                ))
        self.output_indexes.reverse()
        return size

    def get_select2(self, cids: tuple[int, ...], cidpar: list[CidPar]):
        i: int
        for i, cid, l_cid in zip(self.output_indexes, self.actions_cids, self.actions_label_cids):
            if cid in cids:
                if self.action_sel is not None:
                    self.can.itemconfigure(
                        tagOrId=self.actions_cids[self.action_sel],
                        width=1)
                    print(F"{self.action_sel=}")
                self.action_sel = i
                self.can.itemconfigure(
                    tagOrId=cid,
                    width=3)
                cidpar.append(CidPar(self.cid, self.param + i.to_bytes(1, "big")))  # return cid all Schedule
            if l_cid in cids:
                cidpar.append(CidPar(l_cid, self.param + i.to_bytes(1, "big") + b'\x00'))  # add start_time


@dataclass
class DayProfile(Sequence):
    elements: tuple[id_.DigitalID, DaySchedule] = field(init=False)

    def place2(self, p: Point, data: activity_calendar.DayProfile) -> Point:
        self.elements = (
            id_.DigitalID(
                can=self.can,
                param=self.param + b'\x00',
                font_=self.font_,
                width=self.font_.measure("00:00"),
                type=3),
            DaySchedule(
                can=self.can,
                param=self.param + b'\x01',
                font_=self.font_)
        )
        self.elements[0].place(p, data.day_id)
        self.elements[1].place(p + Point(y=self.elements[0].size.y), data.day_schedule)
        return Point(
            self.elements[0].size.x,
            self.elements[0].size.y + self.elements[1].size.y)


@dataclass
class DayProfileTable(Array):
    elements: list[DayProfile] = field(init=False, default_factory=list)
    el_t: CDT = field(init=False, default=DayProfile)

    def place2(self, p: Point, data: activity_calendar.DayProfileTable) -> Point:
        return self.place_horizontal(p, data)


@dataclass
class WeekProfile(Sequence):
    elements: list[id_.OctetStringID | id_.DigitalID] = field(init=False)

    def __post_init__(self):
        self.__days = ("пн", "вт", "ср", "чт", "пт", "сб", "вс")
        self.__size = self.font_.measure("0000")

    def place2(self, p: Point, data: tuple[activity_calendar.WeekProfile, activity_calendar.DayProfileTable]) -> Point:
        x, y = p
        w_p, d_p_t = data
        diam = int(self.__size * 5)
        big_diam = int(self.__size * 6)
        day_degree = 360 / 7
        """degree of one day"""
        day_rad = 2 * math.pi / 7
        """radians in one day"""
        i_r = int(diam*0.4)
        """index radius"""
        c2 = int(big_diam * 0.4)
        """for day_id"""
        x_off = x+self.__size
        """offset to x"""
        a_width = int(self.__size*1.2)
        """action color width"""
        self.elements = [id_.OctetStringID(
            can=self.can,
            param=self.param + b'\x00',
            font_=self.font_,
            width=big_diam,
            type=1)]
        self.elements[0].place(Point(x, y), w_p.week_profile_name)
        y_off = y + self.elements[0].size.y  # todo: make more accuracy(why __size?)
        """offset to y"""
        for i, v in zip(range(7), tuple(w_p)[1:]):
            r = day_rad * (i + 0.5)
            if d_p_t:
                offset = (big_diam - diam) // 2
                for d_p in d_p_t:
                    d_p: activity_calendar.DayProfile
                    if v == d_p.day_id:
                        for d_p_a in sorted(d_p.day_schedule):
                            d_p_a: activity_calendar.DayProfileAction
                            self.can.create_arc(
                                x+offset, y_off+offset, x+diam + offset, y_off+diam + offset,
                                extent=min(359.9, 360 - day_degree*(i+(d_p_a.start_time.hour * 60 + d_p_a.start_time.minute) / 1440)),
                                start=0,
                                outline=colors.day_profile_action_color.get(int(d_p_a.script_selector), colors.DEFAULT).back,
                                style=tk.ARC,
                                width=a_width)
            self.elements.append(
                id_.DigitalID(
                    can=self.can,
                    param=self.param + (i + 1).to_bytes(1),
                    font_=self.font_,
                    name=self.__days[i],
                    source=False,
                    width=big_diam // 6,
                    type=3))
            self.elements[-1].place(
                Point(
                    x + c2 + math.cos(r) * i_r,
                    y_off + c2 + math.sin(r) * i_r),
                v)
        return Point(big_diam, self.elements[0].size.y + big_diam)


@dataclass
class WeekProfileTable(Array):
    elements: list[WeekProfile] = field(init=False, default_factory=list)
    el_t: CDT = field(init=False, default=WeekProfile)

    def place2(self, p: Point, data: tuple[activity_calendar.WeekProfileTable, activity_calendar.DayProfileTable]) -> Point:
        ret = self.place_horizontal2(p, data)
        return ret


@dataclass
class DateTime(Simple):
    def __post_init__(self):
        self.__font_height = self.font_.metrics('linespace')
        self._width = self.font_.measure(" 00.00.0000 ")  # date width
        """height of cube"""

    def place2(self, p: Point, data: cdt.DateTime) -> Point:
        d_t = data.to_datetime()
        self.can.create_text(
            *p,
            text=F"{d_t.strftime("%H:%M:%S")}\n"
                 F"{d_t.strftime("%d.%m.%y")}",
            anchor=tk.NW,
            font=self.font_)
        return Point(self._width, self.__font_height * 2)


@dataclass
class Season(Sequence):
    def place2(self, p: Point, data: activity_calendar.Season) -> Point:
        end_p: Point = copy.copy(p)
        self.elements = [DateTime(
            can=self.can,
            param=self.param + b'\x01',
            font_=self.font_)]
        width = self.elements[0]._width
        self.elements.insert(
            0,
            id_.OctetStringID(
                can=self.can,
                param=self.param + b'\x00',
                font_=self.font_,
                width=width,
                type=2))
        self.elements.append(
            id_.OctetStringID(
                can=self.can,
                param=self.param + b'\x02',
                source=False,
                font_=self.font_,
                width=width,
                type=1))
        el: CDT
        for el, el_data in zip(self.elements, data):
            el.place(end_p, el_data)
            end_p.y += el.size.y
        return Point(width, end_p.y-p.y)


@dataclass
class SeasonProfile(Array):
    elements: list[Season] = field(init=False, default_factory=list)
    el_t: CDT = field(init=False, default=Season)

    def place2(self, p: Point, data: tuple[activity_calendar.SeasonProfile, datetime.datetime]) -> Point:
        s: activity_calendar.Season
        s_p, dt_now = data
        ll = list()
        for i, s in enumerate(s_p):
            if (el := s.season_start.get_left_nearest_datetime(dt_now)) is not None:
                ll.append((i, el))
            if (el := s.season_start.get_right_nearest_datetime(dt_now)) is not None:
                ll.append((i, el))
        ll.sort(key=lambda it: it[1])
        previous = (-1, None)
        z = list()
        while ll:
            if (current := ll.pop())[0] != previous[0]:
                s = s_p[current[0]].copy()
                s.season_start.set(current[1])
                z.insert(0, IndexData(current[0], s))
                previous = current
        return self.place_horizontal3(p, z)
