import tkinter as tk
from tkinter import ttk
import os
import json


class StyleManager:
    STYLE_FILE = "style_config.json"
    DEFAULT_STYLE = "Custom1"

    def __init__(self, root):
        self.root = root
        self.style = ttk.Style(self.root)
        self.default_themes = self.style.theme_names()
        self.custom_styles = {}
        self._define_styles()
        self.current_style = self._load_style()
        self.apply_style(self.current_style)

    def _define_styles(self):
        """Определение всех кастомных стилей."""
        self.custom_styles["Light"] = {
            "TLabel": {"font": ("Arial", 10),
                       "foreground": "#000000",
                       "background": "#D2E1FF",
                       "anchor": "w",
                       "relief": "flat"},

            "TButton": {"font": ("Arial", 10),
                       "foreground": "#000000",
                       "background": "#D2E1FF"},
            "TButton.active": {"background": "#ffffff"},
            "TButton.disabled": {"background": "white",
                                 "foreground": "gray"},

            "TEntry": {"font": ("Arial", 10),
                       "foreground": "#000000",
                       "background": "#D2E1FF",
                       "relief": "flat"},

            "TCheckbutton": {"font": ("Arial", 10),
                       "foreground": "#000000",
                       "background": "#D2E1FF",
                       "indicatorcolor": "#000000",
                       "selectcolor": "white"},

            "TOptionMenu": {"font": ("Arial", 10),  # Шрифт
                            "foreground": "#000000",  # Цвет текста
                            "background": "#D2E1FF",  # Цвет фона
                            "bordercolor": "#000000",  # Цвет границы
                            "relief": "flat"},  # Тип границы

            "TFrame": {"bordercolor": "white",  # Цвет границы
                       "relief": "flat"},  # Тип границы

            "TScrollbar": {"troughcolor": "white",  # Цвет канавки
                           "background": "#293140",  # Цвет ползунка
                           "arrowcolor": "#000000",  # Цвет стрелок
                           "bordercolor": "#000000",  # Цвет границы
                           "relief": "flat"},  # Тип границы

            "TListbox": {"font": ("Arial", 10),  # Шрифт
                         "foreground": "#000000",  # Цвет текста
                         "background": "#D2E1FF",  # Цвет фона
                         "selectbackground": "white",  # Цвет выделенного текста
                         "selectforeground": "white",  # Цвет текста в выделении
                         "relief": "flat"},  # Тип границы

            "TRadiobutton": {"font": ("Arial", 10),  # Шрифт
                             "foreground": "#000000",  # Цвет текста
                             "background": "#D2E1FF",  # Цвет фона
                             "indicatorcolor": "white",  # Цвет индикатора
                             "selectcolor": "#000000",  # Цвет выделения
                             "relief": "flat"},  # Тип границы

            "TScale": {"background": "#D2E1FF",  # Цвет фона
                       "troughcolor": "white",  # Цвет канавки
                       "slidercolor": "#000000",  # Цвет ползунка
                       "bordercolor": "#000000",  # Цвет границы
                       "relief": "flat"},  # Тип границы

            "TSpinbox": {"font": ("Arial", 10),  # Шрифт
                         "foreground": "#000000",  # Цвет текста
                         "background": "#D2E1FF",  # Цвет фона
                         "buttonbackground": "#000000",  # Цвет кнопок увеличения/уменьшения
                         "relief": "flat"},  # Тип границы

            "TProgressbar": {"background": "#293140",  # Цвет заполнения
                             "troughcolor": "#D2E1FF",  # Цвет канавки
                             "bordercolor": "#000000",  # Цвет границы
                             "relief": "flat"},  # Тип границы

        }
        self.custom_styles["Dark"] = {
            "TLabel": {"font": ("Arial", 10),
                       "foreground": "#ffffff",
                       "background": "#535D75",
                       "anchor": "w",
                       "relief": "flat"},

            "TButton": {"font": ("Arial", 10),
                       "foreground": "#000000",
                       "background": "#535D75"},
            "TButton.active": {"background": "#000000"},
            "TButton.disabled": {"background": "white",
                                 "foreground": "gray"},

            "TEntry": {"font": ("Arial", 10),
                       "foreground": "#000000",
                       "background": "#535D75",
                       "relief": "flat"},

            "TCheckbutton": {"font": ("Arial", 10),
                       "foreground": "#ffffff",
                       "background": "#535D75",
                       "indicatorcolor": "#ffffff",
                       "selectcolor": "#ffffff"},

            "TOptionMenu": {"font": ("Arial", 10),
                            "foreground": "#ffffff",
                            "background": "#535D75",
                            "bordercolor": "#ffffff",
                            "relief": "flat"},

            "TFrame": {"bordercolor": "white",
                       "relief": "flat"},

            "TScrollbar": {"troughcolor": "#ffffff",
                           "background": "#535D75",
                           "arrowcolor": "#ffffff",
                           "bordercolor": "#ffffff",
                           "relief": "flat"},

            "TListbox": {"font": ("Arial", 10),
                         "foreground": "#ffffff",
                         "background": "#535D75",
                         "selectbackground": "#ffffff",
                         "selectforeground": "#ffffff",
                         "relief": "flat"},

            "TRadiobutton": {"font": ("Arial", 10),
                             "foreground": "#ffffff",
                             "background": "#535D75",
                             "indicatorcolor": "#ffffff",
                             "selectcolor": "#ffffff",
                             "relief": "flat"},

            "TScale": {"background": "#535D75",
                       "troughcolor": "#ffffff",
                       "slidercolor": "#ffffff",
                       "bordercolor": "#ffffff",
                       "relief": "flat"},

            "TSpinbox": {"font": ("Arial", 10),
                         "foreground": "#ffffff",
                         "background": "#535D75",
                         "buttonbackground": "#ffffff",
                         "relief": "flat"},

            "TProgressbar": {"background": "#ffffff",
                             "troughcolor": "#1F2430",
                             "bordercolor": "#ffffff",
                             "relief": "flat"}
        }


    def apply_style(self, style_name):
        """Применяет стиль по имени."""
        if style_name in self.default_themes:
            self.style.theme_use(style_name)
        elif style_name in self.custom_styles:
            self._apply_custom_style(style_name)
        else:
            raise ValueError(f"Стиль '{style_name}' не найден.")
        self._save_style(style_name)

    def _apply_custom_style(self, style_name):
        """Применяет кастомный стиль."""
        config = self.custom_styles[style_name]
        for widget_type, style_config in config.items():
            self.style.configure(widget_type, **style_config)

    def get_styles(self):
        """Возвращает список всех доступных стилей (включая стандартные и кастомные)."""
        excluded_styles = ["alt", "classic", "xpnative", "default", "clam", "winnative", "vista"]
        # excluded_styles = []
        filtered_themes = [theme for theme in self.default_themes if theme not in excluded_styles]
        return filtered_themes + list(self.custom_styles.keys())

    def _load_style(self):
        """Загрузка текущего стиля из JSON файла. Если файла нет, используется стиль по умолчанию."""
        if os.path.exists(self.STYLE_FILE):
            try:
                with open(self.STYLE_FILE, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    return data.get("selected_style", self.DEFAULT_STYLE)
            except (json.JSONDecodeError, IOError):
                return self.DEFAULT_STYLE
        else:
            self._save_style(self.DEFAULT_STYLE)
            return self.DEFAULT_STYLE

    def _save_style(self, style_name):
        """Сохранение текущего стиля в JSON файл."""
        data = {"selected_style": style_name}
        with open(self.STYLE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)