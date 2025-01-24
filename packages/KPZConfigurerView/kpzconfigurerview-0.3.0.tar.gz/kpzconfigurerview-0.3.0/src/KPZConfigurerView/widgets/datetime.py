from dataclasses import dataclass
from . import CidPar
from .base import CDT, Cid
from DLMS_SPODES.types import cdt
from tKot.common import Point, Polygon


_digit_polygons: dict[str, Polygon] = {
    '0': Polygon(4, 0, 24, 0, 24, 4, 13, 4, 13, 9, 10, 9, 10, 33, 27, 33, 27, 9, 13, 9,
                 13, 4, 24, 4, 24, 0, 33, 0, 37, 4, 37, 38, 33, 42, 4, 42, 0, 38, 0, 4),
    '1': Polygon(11, 0, 18, 0, 18, 33, 26, 33, 26, 42, 0, 42, 0, 33, 8, 33, 8, 9, 0, 9, 0, 4),
    '2': Polygon(4, 0, 33, 0, 37, 4, 37, 22, 33, 26, 10, 26, 10, 33, 37, 33, 37, 42, 0, 42,
                 0, 20, 4, 16, 27, 16, 27, 9, 10, 9, 10, 11, 0, 11, 0, 4),
    '3': Polygon(4, 0, 33, 0, 37, 4, 37, 17, 34, 20, 37, 23, 37, 38, 33, 42, 4, 42, 0, 38,
                 0, 28, 9, 28, 9, 33, 27, 33, 27, 24, 12, 24, 12, 16, 27, 16, 27, 9, 9, 9,
                 9, 13, 0, 13, 0, 4),
    '4': Polygon(19, 0, 33, 0, 33, 21, 41, 21, 41, 30, 33, 30, 33, 42, 23, 42, 23, 10, 10, 21,
                 23, 21, 23, 30, 0, 30, 0, 19),
    '5': Polygon(0, 0, 37, 0, 37, 9, 10, 9, 10, 16, 34, 16, 38, 20, 38, 38, 34, 42, 4, 42,
                 0, 38, 0, 30, 10, 30, 10, 33, 27, 33, 27, 26, 4, 26, 0, 22),
    '6': Polygon(4, 0, 34, 0, 38, 4, 38, 12, 27, 12, 27, 9, 10, 9, 10, 33, 27, 33, 27, 25,
                 13, 25, 13, 17, 34, 17, 38, 21, 38, 38, 34, 42, 4, 42, 0, 38, 0, 4),
    '7': Polygon(0, 0, 39, 0, 39, 10, 17, 42, 7, 42, 27, 10, 9, 10, 9, 14, 0, 14),
    '8': Polygon(4, 0, 34, 0, 37, 3, 17, 3, 17, 9, 10, 9, 10, 16, 17, 16, 17, 26, 10, 26,
                 10, 33, 27, 33, 27, 26, 17, 26, 17, 16, 27, 16, 27, 9, 17, 9, 17, 3, 37, 3,
                 37, 18, 34, 21, 37, 23, 37, 38, 34, 42, 4, 42, 0, 38, 0, 23, 3, 21, 0, 18, 0, 4),
    '9': Polygon(4, 0, 34, 0, 38, 4, 38, 38, 34, 42, 4, 42, 0, 38, 0, 30, 10, 30, 10, 33,
                 28, 33, 28, 9, 10, 9, 10, 16, 28, 16, 28, 25, 4, 25, 0, 21, 0, 4)
}


@dataclass
class DateTime(CDT):
    data_color: str = "#FEF502"
    data_color_2: str = "#EC7E37"
    background_color: str = "#164980"

    def __post_init__(self):
        self.el_cids: list[Cid] = [-1] * 9
        """cids for fields according by: year, month, days, weekdays, hour, minute, second, hundredths, deviation"""

    def place2(self, p: Point, data: cdt.DateTime) -> Point:
        if self.size.x == 0:
            self.size.x = 350
        if self.size.y == 0:
            self.size.y = self.size.x // 4
        self.can.create_rectangle(*p, *(p+self.size), fill=self.background_color, outline="")  # draw background
        points = self.get_points(p)
        positions = {
            "hour": (points[0], points[1]),
            "separator1": points[2],
            "minute": (points[3], points[4]),
            "separator2": points[5],
            "second": (points[6], points[7]),
            "day": (points[8], points[9]),
            "separator3": points[10],
            "month": (points[11], points[12]),
            "separator4": points[13],
            "year": [points[14], points[15], points[16], points[17]],
            "week_day": points[18],
        }
        # Отрисовка года
        if data.year is not None:
            for i, digit in enumerate(str(data.year).zfill(4)):
                cid_ = self.draw_digit(digit, Point(*positions["year"][i]))
                if i == 0:
                    self.el_cids[0] = cid_
        else:
            for pos in positions["year"]:
                self.draw_n(Point(*pos))

        # Отрисовка часов
        if data.hour is not None:
            self.el_cids[4] = self.draw_digit(str(data.hour // 10), Point(*positions["hour"][0]))
            self.draw_digit(str(data.hour % 10), Point(*positions["hour"][1]))
        else:
            self.draw_n(Point(*positions["hour"][0]))
            self.draw_n(Point(*positions["hour"][1]))

        # Отрисовка разделителя ':'
        self.draw_double_separator(Point(*positions["separator1"]))

        # Отрисовка минут
        if data.minute is not None:
            self.el_cids[5] = self.draw_digit(str(data.minute // 10), Point(*positions["minute"][0]))
            self.draw_digit(str(data.minute % 10), Point(*positions["minute"][1]))
        else:
            self.draw_n(Point(*positions["minute"][0]))
            self.draw_n(Point(*positions["minute"][1]))

        # Отрисовка разделителя ':'
        self.draw_double_separator(Point(*positions["separator2"]))

        # Отрисовка секунд
        if data.second is not None:
            self.draw_digit(str(data.second // 10), Point(*positions["second"][0]))
            self.draw_digit(str(data.second % 10), Point(*positions["second"][1]))
        else:
            self.draw_n(Point(*positions["second"][0]))
            self.draw_n(Point(*positions["second"][1]))

        # Отрисовка дня
        if data.day is not None:
            self.el_cids[2] = self.draw_digit(str(data.day // 10), Point(*positions["day"][0]))
            self.draw_digit(str(data.day % 10), Point(*positions["day"][1]))
        else:
            self.draw_n(Point(*positions["day"][0]))
            self.draw_n(Point(*positions["day"][1]))

        # Отрисовка первого разделителя '.'
        self.draw_separator(Point(*positions["separator3"]))

        # Отрисовка месяца
        if data.month is not None:
            self.draw_digit(str(data.month // 10), Point(*positions["month"][0]))
            self.draw_digit(str(data.month % 10), Point(*positions["month"][1]))
        else:
            self.draw_n(Point(*positions["month"][0]))
            self.draw_n(Point(*positions["month"][1]))

        # Отрисовка второго разделителя '.'
        self.draw_separator(Point(*positions["separator4"]))

        # Отрисовка дня недели
        if data.weekday is not None:
            self.draw_week_day(data.weekday, Point(*positions["week_day"]))
        else:
            self.draw_n(Point(*positions["week_day"]))
        return self.size

    def draw_double_separator(self, position: Point):
        scale = self.size.x / 350
        radius = 3 * scale
        spacing = 10 * scale

        # Верхняя точка
        self.can.create_rectangle(
            position.x - radius, position.y - spacing - radius,
            position.x + radius, position.y - spacing + radius,
            fill=self.data_color_2, outline=""
        )
        # Нижняя точка
        self.can.create_rectangle(
            position.x - radius, position.y + spacing - radius,
            position.x + radius, position.y + spacing + radius,
            fill=self.data_color_2, outline=""
        )

    def draw_separator(self, position: Point):
        scale = self.size.x / 350
        radius = 3 * scale

        self.can.create_rectangle(
            position.x - radius, position.y - radius,
            position.x + radius, position.y + radius,
            fill=self.data_color_2, outline=""
        )

    def get_points(self, start: Point):
        height = self.size.x // 4  # Общая высота для DateTime

        x1, y1 = start.x, start.y
        # Верхняя часть для времени
        segment_width_time = self.size.x // 8
        half_segment_width_time = segment_width_time // 2
        time_points = [
            (x1 + half_segment_width_time // 4 + i * segment_width_time, y1 + height // 20)
            for i in range(0, 8)
        ]

        # Нижняя часть для даты
        segment_width_date = self.size.x // 10
        date_points = [
            (x1 + segment_width_date // 4 + i * segment_width_date, y1 + height // 1.9)
            for i in range(0, 11)
        ]
        # Объединяем все точки
        points = time_points + date_points
        # Смещение точек
        #Разделитель ":"
        points[2] = (
            points[2][0] + segment_width_time // 4,
            points[2][1] + height // 4
        )
        #Разделитель ":"
        points[5] = (
            points[5][0] + segment_width_time // 4,
            points[5][1] + height // 4
        )
        #Разделитель "."
        points[10] = (
            points[10][0] + segment_width_time // 15,
            points[10][1] + height // 7 * 3
        )
        # Месяц
        points[11] = (
            points[11][0] - segment_width_date // 5 * 4,
            points[11][1]
        )
        points[12] = (
            points[12][0] - segment_width_date // 5 * 4,
            points[12][1]
        )
        #Разделитель "."
        points[13] = (
            points[13][0] - segment_width_date // 7 * 5,
            points[13][1] + height // 7 * 3
        )
        # Год
        points[14] = (
            points[14][0] - segment_width_date * 3 // 2,
            points[14][1]
        )
        points[15] = (
            points[15][0] - segment_width_date * 3 // 2,
            points[15][1]
        )
        points[16] = (
            points[16][0] - segment_width_date * 3 // 2,
            points[16][1]
        )
        points[17] = (
            points[17][0] - segment_width_date * 3 // 2,
            points[17][1]
        )
        # День недели
        points[18] = (
            points[18][0] - segment_width_date // 5 * 7,
            points[18][1]
        )

        return points

    def draw_digit(self, digit: str, position: Point):
        scale = self.size.x / 400
        # Отрисовка цифры
        return self.can.create_polygon(
            *(_digit_polygons[digit] * scale + position),
            fill=self.data_color,
            outline=""
        )

    def draw_week_day(self, week_day: int, position: Point):
        scale = (self.size.x / 350) / 2  # Масштаб в 2 раза меньше
        week_day_coords = {
            1: ((6, 2), (36, 2), (40, 6), (40, 42), (50, 42), (50, 4), (52, 2), (58, 2), (60, 4), (60, 16),
                (78, 16), (78, 4), (80, 2), (86, 2), (88, 4), (88, 42), (86, 44), (80, 44), (78, 42), (78, 27),
                (60, 27), (60, 42), (58, 44), (52, 44), (50, 42), (40, 42), (38, 44), (32, 44), (30, 42), (30, 11),
                (12, 11), (12, 42), (10, 44), (4, 44), (2, 42), (2, 6)),
            2: ((6, 2), (36, 2), (39, 5), (39, 17), (35, 21), (31, 23), (35, 25), (39, 29), (39, 40), (36, 44),
                (61, 44), (59, 42), (59, 11), (51, 11), (49, 9), (49, 4), (51, 2), (77, 2), (79, 4), (79, 9),
                (77, 11), (69, 11), (69, 42), (67, 44), (21, 44), (21, 35), (29, 35), (29, 28), (21, 28), (21, 18),
                (29, 18), (29, 11), (12, 11), (12, 18), (21, 18), (21, 28), (12, 28), (12, 35), (21, 35), (21, 44),
                (6, 44), (2, 40), (2, 6)),
            3:((6, 2), (36, 2), (40, 6), (40, 13), (38, 15), (31, 15), (29, 13), (29, 11), (12, 11), (12, 35),
               (29, 35), (29, 32), (31, 30), (38, 30), (40, 32), (40, 40), (36, 44), (50, 44), (48, 42), (48, 6),
               (52, 2), (82, 2), (86, 6), (86, 23), (82, 27), (58, 27), (58, 18), (76, 18), (76, 11), (58, 11),
               (58, 42), (56, 44), (6, 44), (2, 40), (2, 6)),
            4:((4, 2), (10, 2), (12, 4), (12, 21), (21, 21), (21, 4), (23, 2), (29, 2), (31, 4), (31, 42),
               (51, 42), (51, 11), (43, 11), (41, 9), (41, 4), (43, 2), (69, 2), (71, 4), (71, 9), (69, 11),
               (61, 11), (61, 42), (59, 44), (53, 44), (51, 42), (31, 42), (29, 44), (23, 44), (21, 42), (21, 34),
               (19, 32), (7, 32), (2, 27), (2, 4)),
            5:((6, 1), (36, 1), (40, 5), (40, 41), (60, 41), (60, 10), (52, 10), (50, 8), (50, 3), (52, 1),
               (78, 1), (80, 3), (80, 8), (78, 10), (70, 10), (70, 41), (68, 43), (62, 43), (60, 41), (40, 41),
               (38, 43), (32, 43), (30, 41), (30, 10), (12, 10), (12, 41), (10, 43), (4, 43), (2, 41), (2, 5)),
            6:((6, 2), (36, 2), (40, 6), (40, 13), (38, 15), (31, 15), (29, 13), (29, 11), (12, 11), (12, 35),
               (29, 35), (29, 32), (31, 30), (38, 30), (40, 32), (40, 40), (36, 44), (54, 44), (50, 40), (50, 6),
               (54, 2), (86, 2), (88, 4), (88, 9), (86, 11), (60, 11), (60, 35), (77, 35), (77, 27), (60, 27),
               (60, 19), (84, 19), (88, 23), (88, 40), (84, 44), (6, 44), (2, 40), (2, 6)),
            7:((6, 2), (36, 2), (39, 5), (39, 17), (35, 21), (31, 23), (35, 25), (39, 29), (39, 40), (36, 44),
               (21, 44), (21, 35), (29, 35), (29, 28), (21, 28), (21, 18), (29, 18), (29, 11), (12, 11), (12, 18),
               (21, 18), (21, 28), (12, 28), (12, 35), (21, 35), (21, 44), (52, 44), (48, 40), (48, 6), (52, 2),
               (82, 2), (86, 6), (86, 13), (84, 15), (77, 15), (75, 13), (75, 11), (58, 11), (58, 35), (75, 35),
               (75, 32), (77, 30), (84, 30), (86, 32), (86, 40), (82, 44), (6, 44), (2, 40), (2, 6)),
        }

        coords = [
            (x * scale + position.x, y * scale + position.y) for x, y in week_day_coords[week_day]
        ]
        self.can.create_polygon(coords, fill=self.data_color_2, outline="")

    def draw_n(self, position: Point) -> Cid:
        scale = self.size.x / 400
        n_coords = [(0, 0), (10, 0), (25, 24), (25, 0), (35, 0), (35, 42),
                    (25, 42), (10, 18), (10, 42), (0, 42)]
        coords = [
            (x * scale + position.x, y * scale + position.y) for x, y in n_coords
        ]
        return self.can.create_polygon(coords, fill=self.data_color, outline="")

    def get_select2(self, cids: tuple[int, ...], cidpar: list[CidPar]):
        for i, el_cid in enumerate(self.el_cids):
            if el_cid in cids:
                cidpar.append(CidPar(
                    cid=el_cid,
                    par=self.param,
                    piece=i
                ))
