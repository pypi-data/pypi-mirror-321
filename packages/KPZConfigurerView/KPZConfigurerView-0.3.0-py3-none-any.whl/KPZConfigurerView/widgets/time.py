from dataclasses import dataclass
from .base import CDT
from DLMS_SPODES.types import cdt
from tKot.common import Point


@dataclass
class Time(CDT):
    data_color: str = "#FEF502"
    data_color_2: str = "#EC7E37"
    background_color: str = "#164980"
    width: int = 350

    def post_init(self):
        pass

    def place2(self, p: Point, data: cdt.Time) -> Point:
        hour = data.hour if data.hour != 0xFF else None
        minute = data.minute if data.minute != 0xFF else None
        second = data.second if data.second != 0xFF else None

        points = self.draw_background_and_points(p)
        height = self.width // 6
        widget_size = Point(self.width, height)
        positions = {
            "hour": (points[0], points[1]),
            "separator1": points[2],
            "minute": (points[3], points[4]),
            "separator2": points[5],
            "second": (points[6], points[7]),
        }

        # Отрисовка часов
        if hour is not None:
            self.draw_digit(hour // 10, Point(*positions["hour"][0]))
            self.draw_digit(hour % 10, Point(*positions["hour"][1]))
        else:
            self.draw_n(Point(*positions["hour"][0]))
            self.draw_n(Point(*positions["hour"][1]))

        # Отрисовка разделителя ':'
        self.draw_separator(Point(*positions["separator1"]))

        # Отрисовка минут
        if minute is not None:
            self.draw_digit(minute // 10, Point(*positions["minute"][0]))
            self.draw_digit(minute % 10, Point(*positions["minute"][1]))
        else:
            self.draw_n(Point(*positions["minute"][0]))
            self.draw_n(Point(*positions["minute"][1]))

        # Отрисовка разделителя ':'
        self.draw_separator(Point(*positions["separator2"]))

        # Отрисовка секунд
        if second is not None:
            self.draw_digit(second // 10, Point(*positions["second"][0]))
            self.draw_digit(second % 10, Point(*positions["second"][1]))
        else:
            self.draw_n(Point(*positions["second"][0]))
            self.draw_n(Point(*positions["second"][1]))

        return widget_size

    def draw_digit(self, digit: int, position: Point):
        scale = self.width / 350
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

        # Масштабирование и смещение координат
        coords = [
            (x * scale + position.x, y * scale + position.y) for x, y in digits_coords[digit]
        ]
        # Отрисовка цифры
        self.can.create_polygon(coords, fill=self.data_color, outline="")

    def draw_separator(self, position: Point):
        scale = self.width / 350
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

    def draw_n(self, position: Point):
        scale = self.width / 350

        n_coords = [(0, 0), (10, 0), (25, 24), (25, 0), (35, 0), (35, 42),
                    (25, 42), (10, 18), (10, 42), (0, 42)]

        # Масштабирование и смещение координат
        coords = [
            (x * scale + position.x, y * scale + position.y) for x, y in n_coords
        ]

        # Отрисовка 'N'
        self.can.create_polygon(coords, fill=self.data_color, outline="")

    def draw_background_and_points(self, start: Point):
        # Вычисление высоты фона
        height = self.width // 6

        # Координаты для фона
        x1, y1 = start.x, start.y
        x2, y2 = x1 + self.width, y1 + height

        # Отрисовка фона
        self.can.create_rectangle(x1, y1, x2, y2, fill=self.background_color, outline="")

        segment_width = self.width // 8
        half_segment_width = segment_width // 2
        points = [
            (x1 + half_segment_width // 4 + i * segment_width, y1 + height // 7)
            for i in range(0, 8)
        ]
        # Сдвиг точек для разделителей
        points[2] = (
            points[2][0] + segment_width // 2,
            points[2][1] + height // 3
        )
        points[5] = (
            points[5][0] + segment_width // 2,
            points[5][1] + height // 3
        )

        return points

    def get_select2(self, cids: tuple[int, ...], cidpar: list):
        pass
