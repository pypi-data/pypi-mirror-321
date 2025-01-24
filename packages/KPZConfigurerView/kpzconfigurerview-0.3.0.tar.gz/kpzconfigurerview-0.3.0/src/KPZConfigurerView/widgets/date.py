from dataclasses import dataclass
from .base import CDT
from DLMS_SPODES.types import cdt
from tKot.common import Point


@dataclass
class Date(CDT):
    data_color: str = "#FEF502"
    data_color_2: str = "#EC7E37"
    background_color: str = "#164980"
    width: int = 350

    def post_init(self):
        pass

    def place2(self, p: Point, data: cdt.Date) -> Point:
        year = data.year if data.year != 0xFFFF else None
        month = data.month if data.month not in {0xFF, 0xFE, 0xFD} else None
        day = data.day if data.day not in {0xFF, 0xFE, 0xFD} else None
        week_day = data.weekday if data.weekday != 0xFF else None

        points = self.draw_background_and_points(p)
        height = self.width // 6
        widget_size = Point(self.width, height)
        positions = {
            "day": (points[0], points[1]),
            "separator1": points[2],
            "month": (points[3], points[4]),
            "separator2": points[5],
            "year": [points[6], points[7], points[8], points[9]],
            "week_day": points[10],
        }

        # Отрисовка дня
        if day is not None:
            self.draw_digit(day // 10, Point(*positions["day"][0]))
            self.draw_digit(day % 10, Point(*positions["day"][1]))
        else:
            self.draw_n(Point(*positions["day"][0]))
            self.draw_n(Point(*positions["day"][1]))

        # Отрисовка первого разделителя '.'
        self.draw_separator(Point(*positions["separator1"]))

        # Отрисовка месяца
        if month is not None:
            self.draw_digit(month // 10, Point(*positions["month"][0]))
            self.draw_digit(month % 10, Point(*positions["month"][1]))
        else:
            self.draw_n(Point(*positions["month"][0]))
            self.draw_n(Point(*positions["month"][1]))

        # Отрисовка второго разделителя '.'
        self.draw_separator(Point(*positions["separator2"]))

        # Отрисовка года
        if year is not None:
            for i, digit in enumerate(str(year).zfill(4)):
                self.draw_digit(int(digit), Point(*positions["year"][i]))
        else:
            for pos in positions["year"]:
                self.draw_n(Point(*pos))

        # Отрисовка дня недели
        if week_day is not None:
            self.draw_week_day(week_day, Point(*positions["week_day"]))
        else:
            self.draw_n(Point(*positions["week_day"]))

        return widget_size

    def draw_digit(self, digit: int, position: Point):
        scale = self.width / 400
        digits_coords = {
            0: ((4, 0), (24, 0), (24, 4), (13, 4), (13, 9), (10, 9), (10, 33), (27, 33), (27, 9), (13, 9),
                (13, 4), (24, 4), (24, 0), (33, 0), (37, 4), (37, 38), (33, 42), (4, 42), (0, 38), (0, 4)),
            1: ((11, 0), (18, 0), (18, 33), (26, 33), (26, 42), (0, 42), (0, 33), (8, 33), (8, 9), (0, 9), (0, 4)),
            2: ((4, 0), (33, 0), (37, 4), (37, 22), (33, 26), (10, 26), (10, 33), (37, 33), (37, 42), (0, 42),
                (0, 20), (4, 16), (27, 16), (27, 9), (10, 9), (10, 11), (0, 11), (0, 4)),
            3: ((4, 0), (33, 0), (37, 4), (37, 17), (34, 20), (37, 23), (37, 38), (33, 42), (4, 42), (0, 38),
                (0, 28), (9, 28), (9, 33), (27, 33), (27, 24), (12, 24), (12, 16), (27, 16), (27, 9), (9, 9),
                (9, 13), (0, 13), (0, 4)),
            4: ((19, 0), (33, 0), (33, 21), (41, 21), (41, 30), (33, 30), (33, 42), (23, 42), (23, 10), (10, 21),
                (23, 21), (23, 30), (0, 30), (0, 19)),
            5: ((0, 0), (37, 0), (37, 9), (10, 9), (10, 16), (34, 16), (38, 20), (38, 38), (34, 42), (4, 42),
                (0, 38), (0, 30), (10, 30), (10, 33), (27, 33), (27, 26), (4, 26), (0, 22)),
            6: ((4, 0), (34, 0), (38, 4), (38, 12), (27, 12), (27, 9), (10, 9), (10, 33), (27, 33), (27, 25),
                (13, 25), (13, 17), (34, 17), (38, 21), (38, 38), (34, 42), (4, 42), (0, 38), (0, 4)),
            7: ((0, 0), (39, 0), (39, 10), (17, 42), (7, 42), (27, 10), (9, 10), (9, 14), (0, 14)),
            8: ((4, 0), (34, 0), (37, 3), (17, 3), (17, 9), (10, 9), (10, 16), (17, 16), (17, 26), (10, 26),
                (10, 33), (27, 33), (27, 26), (17, 26), (17, 16), (27, 16), (27, 9), (17, 9), (17, 3), (37, 3),
                (37, 18), (34, 21), (37, 23), (37, 38), (34, 42), (4, 42), (0, 38), (0, 23), (3, 21), (0, 18), (0, 4)),
            9: ((4, 0), (34, 0), (38, 4), (38, 38), (34, 42), (4, 42), (0, 38), (0, 30), (10, 30), (10, 33),
                (28, 33), (28, 9), (10, 9), (10, 16), (28, 16), (28, 25), (4, 25), (0, 21), (0, 4))
        }

        coords = [
            (x * scale + position.x, y * scale + position.y) for x, y in digits_coords[digit]
        ]
        self.can.create_polygon(coords, fill=self.data_color, outline="")

    def draw_separator(self, position: Point):
        scale = self.width / 350
        radius = 3 * scale

        self.can.create_rectangle(
            position.x - radius, position.y - radius,
            position.x + radius, position.y + radius,
            fill=self.data_color_2, outline=""
        )

    def draw_n(self, position: Point):
        scale = self.width / 400
        n_coords = [(0, 0), (10, 0), (25, 24), (25, 0), (35, 0), (35, 42),
                    (25, 42), (10, 18), (10, 42), (0, 42)]
        coords = [
            (x * scale + position.x, y * scale + position.y) for x, y in n_coords
        ]
        self.can.create_polygon(coords, fill=self.data_color, outline="")

    def draw_week_day(self, week_day: int, position: Point):
        scale = (self.width / 350) / 2  # Масштаб в 2 раза меньше
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

    def draw_background_and_points(self, start: Point):
        height = self.width // 6
        x1, y1 = start.x, start.y
        x2, y2 = x1 + self.width, y1 + height

        self.can.create_rectangle(x1, y1, x2, y2, fill=self.background_color, outline="")

        segment_width = self.width // 10  # Расстояние между точками
        half_segment_width = segment_width // 2
        points = [
            (x1 + half_segment_width // 2 + i * segment_width, y1 + height // 7)
            for i in range(0, 11)
        ]
        # Сдвиг точек для разделителей
        points[2] = (
            points[2][0],
            points[2][1] + height // 3 * 2
        )
        points[3] = (
            points[3][0] - segment_width // 4 * 3,
            points[3][1]
        )
        points[4] = (
            points[4][0] - segment_width // 4 * 3,
            points[4][1]
        )
        points[5] = (
            points[5][0] - segment_width // 4 * 3,
            points[5][1] + height // 3 * 2
        )
        points[6] = (
            points[6][0] - segment_width // 2 * 3,
            points[6][1]
        )
        points[7] = (
            points[7][0] - segment_width // 2 * 3,
            points[7][1]
        )
        points[8] = (
            points[8][0] - segment_width // 2 * 3,
            points[8][1]
        )
        points[9] = (
            points[9][0] - segment_width // 2 * 3,
            points[9][1]
        )
        points[10] = (
            points[10][0] - segment_width // 2 * 3,
            points[10][1]
        )
        return points

    def get_select2(self, cids: tuple[int, ...], cidpar: list):
        pass