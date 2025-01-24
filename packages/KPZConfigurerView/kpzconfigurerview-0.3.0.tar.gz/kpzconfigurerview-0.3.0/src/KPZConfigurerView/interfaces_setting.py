from dataclasses import dataclass
from typing import Self
from collections import deque
from itertools import count
import tkinter as tk
from tkinter import ttk
from tkinter import font, messagebox
from DLMS_SPODES.cosem_interface_classes.association_ln import mechanism_id
from DLMS_SPODES.types import cdt
from DLMS_SPODES.types.implementations import enums
from tKot.common import Point
from tKot.messagebox import Toast
import ConfigurerControl.parameters as p
from ConfigurerControl.actions import HandleAction
from ConfigurerControl.images import images
from DLMS_SPODES.types.implementations import bitstrings
from DLMS_SPODES_client.client import Client
from tkinter import *
from PIL import Image, ImageTk
from typing import Callable
# from test.styles import StyleManager
from typing import Optional, Any, Callable
import json


def add_Variable(data: dataclass, f: str) -> tk.Variable:
    def set(value1: dataclass, param: str, value2: tk.Variable):
        match value1.__dict__[param]:
            case int() | str() | float(): value1.__dict__[param] = value2.get()
            case bytes(): value1.__dict__[param] = value1.__dict__[param].__class__.from_str(value2.get())  # special for Secret class
            case other: raise ValueError(F"can't set from {value2} to {other}")

    match value := data.__dict__[f]:
        case int(): t = tk.IntVar
        case str(): t = tk.StringVar
        case float(): t = tk.DoubleVar
        case p.Secret(): t = tk.StringVar
        case err: raise ValueError(F"in function add_Variable, unknown type {data.__class__.__name__}.{f}: {err}")
    var = t(value=str(value))
    var.trace_add("write", lambda *_: set(data, f, var))
    return var


class ComboBox:
    """ Entry widget for List Row """
    extern_id: int
    cb_set_to_source: Callable[[int, str], None]
    cb_get_from_source: Callable[[int], cdt.Enum]
    __cbs_destroy: list[Callable[[], None]]

    def __init__(self, master, font,
                 extern_id: int = None,
                 width: int = None,
                 cb_set_to_source: Callable[[int, str], None] = None,
                 cb_get_from_source: Callable[[int], cdt.Enum] = None,
                 cbs_destroy: list[Callable[[], None]] = None,
                 cb_focus_out: Callable = None):
        self.master = master

        self.extern_id = extern_id
        """ extern ID """

        self.cb_set_to_source = cb_set_to_source
        """ external callable setter """

        self.cb_get_from_source = cb_get_from_source
        """ external callable getter data type"""

        self.__cbs_destroy = list() if cbs_destroy is None else cbs_destroy
        """ external callable container self widget destroyer """

        self.width = width
        """ TODO: """

        self.cb_focus_out = cb_focus_out
        """ external callback after widget FocusOut """

        self.__post = False

        master.option_add("*TCombobox*Listbox*Font", font)
        self.widget = ttk.Combobox(master=master,
                                   values=self.cb_get_from_source(extern_id).get_values(),
                                   font=font,
                                   width=self.width,
                                   postcommand=self.__set_post)
        self.widget.bind('<<ComboboxSelected>>', self.set_and_destroy)
        if cb_focus_out:
            self.widget.focus_set()
            self.widget.bind('<FocusOut>', self.__call_cb_focus_out)
        self.__set_value()

    def __set_post(self):
        self.__post = True

    def __call_cb_focus_out(self, e):
        if not self.__post:
            self.cb_focus_out()
        self.__post = False

    def set_and_destroy(self, e):
        """ setting value to source and self destroying """
        try:
            self.cb_set_to_source(self.extern_id, self.widget.get())
            for func in self.__cbs_destroy:
                func()
        except ValueError as e:
            self.__set_value()
            messagebox.showerror(title='Ошибка смены параметра',
                                 message=F'{e}',
                                 parent=self.master)

    def __set_value(self):
        self.widget.set(str(self.cb_get_from_source(self.extern_id)))

    def destroy(self):
        self.widget.destroy()

    def grid(self, *args, **kwargs):
        self.widget.grid(*args, **kwargs)

    def pack(self, *args, **kwargs):
        self.widget.pack(*args, **kwargs)


class Singleton:
    instance: Self | None = None
    top: tk.Toplevel

    def __new__(cls, *args):
        if cls.instance is not None and hasattr(cls.instance, "top"):
            cls.instance.top.focus_set()
        else:
            cls.instance = super().__new__(cls)
            return cls.instance

    @classmethod
    def reset_instance(cls):
        cls.instance = None

class LoadingBar:
    def __init__(self, parent: tk.Widget,
                 mode: str ="indeterminate",
                 x: int = 0,
                 y: int=0,
                 width: int=400):
        self.parent: tk.Widget = parent
        self.mode = mode
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.progressbar = ttk.Progressbar(self.parent, orient="horizontal", mode=self.mode, length=self.width)
        self.progressbar.place(x=self.x, y=self.y, width=self.width)

    def start(self):
        if self.mode == "indeterminate":
            self.progressbar.start(10)
        else:
            self.progressbar.start()
    def stop(self):
        self.progressbar.stop()

    def destroy(self):
        self.progressbar.destroy()

    def set_progress(self, value: int):
        if self.mode == "determinate":
            self.progressbar['value'] = value

class MyEntry(tk.Canvas):
    def __init__(self, master: Optional[tk.Widget] = None,
                 width: int= 250,
                 height: int=20,
                 separator_interval: int=4,
                 text_var: Optional[StringVar] = None,
                 **kwargs: Any):
        super().__init__(master, width=width, height=height, bg="white", **kwargs)
        self.p = p.Parameters
        self.text: str = ""
        self.text_var: Optional[StringVar] = text_var
        self.separator_interval: int = separator_interval
        self.cursor_position: int = 0
        self.font: tuple[str, int] = ("Courier", 12)
        self.text_color: str = "black"
        self.separator_color: str = "gray"
        self.cursor_visible: bool = True

        if self.text_var and self.text_var.get():
            self.set(self.text_var.get())

        self.bind("<KeyPress>", self.on_key_press)
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.bind("<Button-1>", self.on_mouse_click)

        self.draw_entry()
        self.blink_cursor()

    def get_password(self) -> str:
        return self.text_var.get() if self.text_var else self.text

    def draw_entry(self) -> None:
        self.delete("all")
        for i, char in enumerate(self.text):
            x_position: int = 5 + i * 10
            self.create_text(x_position, 15, anchor="w", text=char, font=self.font, fill=self.text_color)

            if (i + 1) % self.separator_interval == 0:
                separator_x_position: int = 5 + (i + 1) * 10
                self.create_line(separator_x_position, 5, separator_x_position, 25, width=2, fill=self.separator_color)
        if self.cursor_visible:
            cursor_x: int = 5 + self.cursor_position * 10
            self.create_line(cursor_x, 5, cursor_x, 25, fill="black", width=2)

    def on_key_press(self, event: tk.Event) -> None:
        if event.keysym == "BackSpace":
            if self.cursor_position > 0:
                self.text = self.text[:self.cursor_position - 1] + self.text[self.cursor_position:]
                self.cursor_position -= 1
        elif event.keysym == "Delete":
            if self.cursor_position < len(self.text):
                self.text = self.text[:self.cursor_position] + self.text[self.cursor_position + 1:]
        elif event.keysym == "Left":
            self.cursor_position = max(0, self.cursor_position - 1)
        elif event.keysym == "Right":
            self.cursor_position = min(len(self.text), self.cursor_position + 1)
        elif len(event.char) == 1:
            self.text = self.text[:self.cursor_position] + event.char + self.text[self.cursor_position:]
            self.cursor_position += 1

        if self.text_var is not None:
            self.text_var.set(self.text)

        self.draw_entry()

    def on_focus_in(self, event: tk.Event) -> None:
        self.config(bg="white")
        self.draw_entry()

    def on_focus_out(self, event: tk.Event) -> None:
        self.config(bg="white")
        self.draw_entry()

    def get(self, text: str) -> str:
        return self.text

    def set(self, text: str) -> None:
        self.text = text
        self.cursor_position = len(text)
        self.draw_entry()

    def set_state(self, state: str) -> None:
        if state == "disabled":
            self.unbind("<KeyPress>")
            self.unbind("<Button-1>")
            self.config(bg="gray")
        elif state == "normal":
            self.bind("<KeyPress>", self.on_key_press)
            self.bind("<Button-1>", self.on_mouse_click)
            self.config(bg="white")
        self.draw_entry()

    def blink_cursor(self) -> None:
        if self.focus_get() == self:
            self.cursor_visible = not self.cursor_visible
            self.draw_entry()
        self.after(500, self.blink_cursor)

    def on_mouse_click(self, event: tk.Event) -> None:
        self.focus_set()
        click_position: int = event.x // 10
        self.cursor_position = min(click_position, len(self.text))
        self.draw_entry()

    def __update_entry_state(self) -> None:
        if self.p.m_id != mechanism_id.NONE:
            self.set_state("normal")
        else:
            self.set_state("disabled")


class MyScaleCanvas(tk.Canvas):
    def __init__(self,
                 parent: tk.Widget,
                 x: int,
                 y: int,
                 width: int,
                 height: int,
                 values: list[int],
                 init_value: int,
                 font_size: int =8,
                 padding: int=20,
                 on_value_change: Optional[Callable[[int], None]] = None,
                 **kwargs: Any):
        super().__init__(parent, width=width, height=height, bg="#D2E1FF", **kwargs)
        self.place(x=x, y=y, width=width, height=height)
        self.values: list[int] = sorted(values)
        self.init_value: int = init_value
        self.font_size: int = font_size
        self.width: int = width
        self.height: int = height
        self.padding: int = padding
        self.current_value: tk.IntVar = tk.IntVar(value=init_value)
        self.slider: Optional[Callable[[int], None]] = None
        self._draw_scale()
        self.bind("<B1-Motion>", self._move_slider)
        self.bind("<ButtonRelease-1>", self._snap_to_nearest)
        self.on_value_change = on_value_change

    def _draw_scale(self) -> None:
        self.delete("scale")
        font_obj = font.Font(size=self.font_size)
        text_height = font_obj.metrics("linespace")
        vertical_padding = text_height + 10
        mid_y = (self.height - vertical_padding) // 2
        self.create_line(self.padding, mid_y, self.width - self.padding, mid_y, fill="black", tags="scale")
        num_values = len(self.values)
        step_x = (self.width - 2 * self.padding) / (num_values - 1)
        for i, value in enumerate(self.values):
            x = self.padding + i * step_x
            self.create_line(x, mid_y - 5, x, mid_y + 5, fill="black", tags="scale")
            if value == self.current_value.get():
                label_font = font.Font(size=self.font_size + 2)
            else:
                label_font = font.Font(size=self.font_size)
            self.create_text(x, mid_y + text_height + 5, text=str(value), font=label_font, tags="scale")
        if not self.slider:
            self.slider = self.create_oval(0, 0, 14, 14, fill="black", outline="black")

        self._update_slider_position(mid_y)

    def _move_slider(self, event: tk.Event) -> None:
        if self.padding <= event.x <= self.width - self.padding:
            self.coords(self.slider, event.x - 7, self.height // 2 - 7, event.x + 7, self.height // 2 + 7)

    def _snap_to_nearest(self, event: Optional[tk.Event] = None) -> None:
        x_pos = self.coords(self.slider)[0] + 7
        step_x = (self.width - 2 * self.padding) / (len(self.values) - 1)
        nearest_index = int(round((x_pos - self.padding) / step_x))
        nearest_index = max(0, min(nearest_index, len(self.values) - 1))
        nearest_value = self.values[nearest_index]
        self.current_value.set(nearest_value)
        self._draw_scale()
        if self.on_value_change:
            self.on_value_change(nearest_value)

    def _update_slider_position(self, mid_y: int) -> None:
        step_x = (self.width - 2 * self.padding) / (len(self.values) - 1)
        value = self.current_value.get()

        if value in self.values:
            value_index = self.values.index(value)
            x = self.padding + value_index * step_x
        else:
            lower_bound = max([v for v in self.values if v < value], default=self.values[0])
            upper_bound = min([v for v in self.values if v > value], default=self.values[-1])
            lower_index = self.values.index(lower_bound)
            upper_index = self.values.index(upper_bound)
            lower_x = self.padding + lower_index * step_x
            upper_x = self.padding + upper_index * step_x
            ratio = (value - lower_bound) / (upper_bound - lower_bound) if upper_bound != lower_bound else 0
            x = lower_x + ratio * (upper_x - lower_x)

        self.slider_y = mid_y
        self.coords(self.slider, x - 7, mid_y - 7, x + 7, mid_y + 7)



# ==========================================================================================================================================================================
class InterfaceSetting(Singleton):
    """ window for setting transport to selected device """
    c: Client
    transport_widgets: deque[tk.Widget | Entry]
    __parameter_tree: ttk.Treeview = None
    __toast: Toast

    def __init__(self, master,
                 name: str,
                 params: p.Parameters,
                 position: Point = Point()):
        self.p = params

        self.top: tk.Toplevel = tk.Toplevel(master)
        self.skip_confirmation: bool = False
        main_window_x: int = self.top.master.winfo_x()
        main_window_y: int = self.top.master.winfo_y()
        self.top.geometry(f"500x300+{main_window_x}+{main_window_y}")
        # self.style_manager: StyleManager = StyleManager(self.top)
        self.current_style: str = self.load_saved_style()

        self.top.bind('<Destroy>', self.__destroy)
        self.top.title(F'Настройки подключения к {name}')
        self.top.resizable(True, True)
        self.font = font.Font(root=master, family='courier', size=12)

        menu = tk.Menu(self.top)
        self.top.config(menu=menu)
        # style_menu = tk.Menu(menu, tearoff=0)
        # menu.add_cascade(label="Вид", menu=style_menu)
        # style_menu.add_command(label="Выбрать стиль", command=self.open_style_window)

        self.__is_ascii = tk.IntVar()
        self.__is_hidden = tk.IntVar()
        style = ttk.Style(self.top)
        style.configure('lefttab.TNotebook', tabposition='wn')
        self.main_canvas = tk.Canvas(self.top)
        self.main_canvas.place(x=45, y=0, width=450, height=400)
        self.loading_bar = None
        self.button_widgets = []
        self.create_buttons()
        self.secret_widgets: deque[tk.Widget] = deque()
        self.transport_widgets: deque[tk.Widget] = deque()
        self.sap_var = tk.StringVar(value=self.p.sap.get_report().msg)
        self.quick_connection_interface()
        self.__toast = Toast(self.top)

    # ==========================================================================================================================================================================
    def load_saved_style(self) -> str:
        """Загрузка сохранённого стиля из файла."""
        try:
            with open("style_config.json", "r") as file:
                config: dict[str, Any] = json.load(file)
                return config.get("selected_style", "Custom2")
        except (FileNotFoundError, json.JSONDecodeError):
            return "Custom2"

    def save_style(self, style_name: str):
        """Сохранение текущего стиля в файл."""
        with open("style_config.json", "w") as file:
            json.dump({"selected_style": style_name}, file)

    def open_style_window(self):
        submenu_window_x: int = self.top.winfo_x()
        submenu_window_y: int = self.top.winfo_y()
        style_window: tk.Toplevel = tk.Toplevel(self.top)
        style_window.title("Выбор стиля")
        style_window.geometry(f"200x330+{submenu_window_x+500}+{submenu_window_y}")

        style_display_names: dict[str, str] = {
            "winnative": "Стандартный",
            "vista": "Windows Vista",
            "Light": "Светлая",
            "Dark": "Тёмная"
        }

        for style_name in self.style_manager.get_styles():
            display_name: str = style_display_names.get(style_name, style_name)
            style_button = ttk.Button(style_window, text=display_name, command=lambda s=style_name: self.apply_style(s))
            style_button.pack(pady=2)

    def apply_style(self, style_name: str):
        try:
            self.style_manager.apply_style(style_name)
            self.current_style = style_name
            self.save_style(style_name)
            self.create_buttons()
        except ValueError as e:
            print(e)


    def create_buttons(self):
        button_texts = ["Быстрое подключение",
                        "Подключение",
                        "Адресация",
                        "Согласование",
                        "Коммуникационный профиль",
                        "Сохранить"]

        button_commands = [self.quick_connection_interface,
                           self.connection_interface,
                           self.addressing,
                           self.conformance,
                           self.com_profile,
                           self.save_all_parameters]

        button_images = [
            images["connected"],
            images["exchange"],
            images["sync"],
            images["group_select"],
            images["lupe"],
            images["load_file"],
        ]
            # match self.current_style:
        #     case "Light":
        #         button_images = [
        #             images["activate"],
        #             images["ready"],
        #             images["yellow_bagel"],
        #             images["key"],
        #             images["plus"],
        #             images["read"],
        #         ]
        #     case "Dark":
        #         button_images = [
        #             images["connected"],
        #             images["exchange"],
        #             images["sync"],
        #             images["group_select"],
        #             images["lupe"],
        #             images["load_file"],
        #         ]

        button_frame = tk.Frame(self.top,height=300, width=40)
        button_frame.place(x=3, y=0)

        button_width, button_height = 35, 35
        padding_y = 10

        def resize_image(image_, width: int, height: int):
            image_icone = image_.resize((width, height), Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(image_icone)


        for index, (text, command, image_) in enumerate(zip(button_texts, button_commands, button_images)):
            y_position = index * (button_height + padding_y)
            if image_:
                image = resize_image(image_, button_width, button_height)
            else:
                image = None
            button = tk.Button(button_frame, command=command, width=6, height=2, image=image, compound="top")
            button.image = image
            button.place(x=0, y=y_position, width=button_width, height=button_height)

            button.bind("<Button-3>", lambda e, t=text: self.__show_tooltip(e, t))
            self.button_widgets.append(button)

    def __show_tooltip(self, event, text):
        self.__toast.call(text)

    def quick_connection_interface(self):
        self.delete_all_widgets()
        self.__recreate_password_view()

        label2 = ttk.Label(self.main_canvas, text='Таймаут')
        label2.place(x=2, y=32, width=140)

        self.custom_scale = MyScaleCanvas(self.main_canvas, x=144, y=32, width=302, height=27, values=[3, 5, 10, 30, 60, 120],
                                          init_value=self.p.response_timeout, font_size=8, padding=15, on_value_change=self.update_response_timeout)

        ttk.Label(self.main_canvas, text='Транспорт').place(x=2, y=62, width=140)
        self.transport_names = {
            "Оптопорт": p.SerialPort,
            "RS485": p.RS485,
            "TCP/IP": p.Network,
            "BLE": p.KPZBLE1}
        for name, c in self.transport_names.items():
            if c == self.p.communication_transport.__class__:
                self.transport_var = tk.StringVar(value=name)
                break
            else:
                continue
        else:
            raise ValueError(F"not find communication transport: {self.p.communication_transport}")
        self.transport_var.trace_add("write", lambda *args: self.__change_transport(is_quick_access=True))

        self.transport_params: dict[str, tk.StringVar] = dict()
        tk.OptionMenu(self.main_canvas,
                      self.transport_var,
                      *self.transport_names.keys()
                      ).place(x=143, y=62, width=304)
        self.__recreate_transport_view(x_label=2, y_label=92, x_widget=142, y_widget=92)

    def update_response_timeout(self, value):
        self.p.response_timeout = value

    def connection_interface(self):
        self.delete_all_widgets()
        ttk.Label(self.main_canvas, text='Тип соединения').place(x=2, y=2, width=170)
        tk.OptionMenu(self.main_canvas,
                      self.sap_var,
                      *enums.ClientSAP.get_values()
                      ).place(x=173, y=2, width=275)
        ttk.Label(self.main_canvas, text="Механизм безопасности").place(x=2, y=32, width=170)
        self.mechanism_id_var = tk.StringVar(value=self.p.m_id.get_report().msg if self.p.m_id else mechanism_id.NONE.get_report().msg)
        self.mechanism_id_var.trace_add("write", self.__change_mechanism_id)

        tk.OptionMenu(self.main_canvas,
                      self.mechanism_id_var,
                      *mechanism_id.MechanismIdElement.get_values()
                      ).place(x=173, y=29, width=275)
        self.mechanism_id_var.trace_add("write", self.__change_mechanism_id)

        self.__create_row(add_Variable(self.p.com_profile, "device_address"), "Физический адрес", x_label=2, y_label=62, width_label=170 ,x_widget=175, y_widget=62, width_widget=270)
        self.__create_row(add_Variable(self.p, "response_timeout"),"Таймаут", x_label=2, y_label=92, width_label=170 ,x_widget=175, y_widget=92, width_widget=270)

        ttk.Label(self.main_canvas, text="Адресация").place(x=2, y=122, width=170)
        self.addr_size_var = tk.StringVar(
            value=str(self.p.addr_size))
        self.addr_size_var.trace_add("write", self.__change_addr_size)
        tk.OptionMenu(self.main_canvas,
                      self.addr_size_var,
                      *self.p.addr_size.get_values()
                      ).place(x=173, y=122, width=275)

    def addressing (self):
        self.delete_all_widgets()

        ttk.Label(self.main_canvas, text='Транспорт').place(x=2, y=4, width=140)
        self.transport_names = {
            "Оптопорт": p.SerialPort,
            "RS485": p.RS485,
            "TCP/IP": p.Network,
            "BLE": p.KPZBLE1}
        for name, c in self.transport_names.items():
            if c == self.p.communication_transport.__class__:
                self.transport_var = tk.StringVar(value=name)
                break
            else:
                continue
        else:
            raise ValueError(F"not find communication transport: {self.p.communication_transport}")
        self.transport_var.trace_add("write", lambda *args: self.__change_transport(is_quick_access=False))

        self.transport_params: dict[str, tk.StringVar] = dict()
        tk.OptionMenu(self.main_canvas,
                      self.transport_var,
                      *self.transport_names.keys()
                      ).place(x=143, y=2, width=300)
        self.__recreate_transport_view(x_label=2, y_label=32, x_widget=147, y_widget=32)

    def conformance(self):
        self.delete_all_widgets()
        print()
        checkbox_frame = ttk.Frame(self.main_canvas, relief="flat")
        checkbox_frame.bind("<Configure>", lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))
        scrollbar = tk.Scrollbar(self.main_canvas, orient="vertical", command=self.main_canvas.yview)
        scrollbar.place(x=432, y=0, height=290)
        self.main_canvas.configure(yscrollcommand=scrollbar.set)
        conformance_keys = bitstrings.Conformance.get_values()
        self.main_canvas.create_window((0, 0), window=checkbox_frame, anchor="nw", width=400, height=25+len(conformance_keys)*25)
        self.main_canvas.bind_all("<MouseWheel>", lambda event: self._on_mousewheel(event))
        self.checkbox_vars = []
        conformance_bits = str(self.p.conformance) if self.p.conformance else '0' * len(conformance_keys)
        self.checkbox_states = {key: int(conformance_bits[i]) for i, key in enumerate(conformance_keys)}

        for i, key in enumerate(conformance_keys):
            var = tk.BooleanVar(value=bool(self.checkbox_states[key]))
            self.checkbox_vars.append(var)

            def update_checkbutton(key=key, var=var):
                self.checkbox_states[key] = int(var.get())
                self.update_conformance()

            chk = ttk.Checkbutton(checkbox_frame, text=key, variable=var, command=update_checkbutton, width=300)
            chk.grid(row=i, column=0, sticky="w")

    def _on_mousewheel(self, event):
        self.main_canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def update_conformance(self):
        conformance_str = ''.join(str(self.checkbox_states[key]) for key in bitstrings.Conformance.get_values())
        self.p.conformance.set(conformance_str)
        print("Обновленные значения флагов:", self.p.conformance)

    def com_profile(self):
        self.delete_all_widgets()
        params = [
            "comm_speed",
            "window_size_transmit",
            "window_size_receive",
            "max_info_field_length_transmit",
            "max_info_field_length_receive",
            "inter_octet_time_out",
            "inactivity_time_out",
            "device_address"
        ]

        labels = [
            "Скорость соединения",
            "Размер окна передачи",
            "Размер окна приёма",
            "Макс. длина инф. поля передачи",
            "Макс. длина инф. поля приёма",
            "Таймаут межсимвольного интервала",
            "Таймаут неактивности",
            "Адрес устройства"
        ]

        for i, (param, label) in enumerate(zip(params, labels)):
            y_position = i * 30
            self.__create_row(add_Variable(self.p.com_profile, param), label, x_label=0, y_label=y_position, width_label= 250, x_widget=250, y_widget=y_position, width_widget=200)

        def default_com_profile_nums():
            print(self.p.com_profile)
            self.p.com_profile.comm_speed = 9600
            self.p.com_profile.comm_speed = 9600
            self.p.com_profile.window_size_transmit = 1
            self.p.com_profile.window_size_receive = 1
            self.p.com_profile.max_info_field_length_transmit = 128
            self.p.com_profile.max_info_field_length_receive = 128
            self.p.com_profile.inter_octet_time_out = 25
            self.p.com_profile.inactivity_time_out = 120
            self.p.com_profile.device_address = 16
            self.delete_all_widgets()
            self.com_profile()
            print(self.p.com_profile)


        default_nums = ttk.Button(master=self.main_canvas, text="Значения по умолчанию", command=default_com_profile_nums)
        default_nums.place(x=0, y=270)

    def save_all_parameters(self):
        self.skip_confirmation = True
        self.top.destroy()

    def delete_all_widgets(self):
        for widget in self.main_canvas.winfo_children():
            if isinstance(widget, (ttk.Label, tk.OptionMenu, tk.Canvas, ttk.Entry, tk.Scrollbar, ttk.Treeview, ttk.Button, ttk.Frame)):
                widget.destroy()
        if self.loading_bar:
            self.loading_bar.destroy()
            self.loading_bar = None


    def __destroy(self, event):
        """ reset instance used flag and call back function with device """
        if event.widget == self.top:
            InterfaceSetting.reset_instance()
            if not self.skip_confirmation:
                if messagebox.askyesno(
                    title="Закрытие окна установки интерфейса",
                    message="Сохранить изменения?"
                ):
                    self._save_changes()
            else:
                self._save_changes()
            self.p.callback(HandleAction.RELEASE_CLIENT, self.p.client_id)

    def _save_changes(self):
        """Сохраняет изменения"""
        self.p.sap.set(self.sap_var.get())
        if self.p.callback:
            self.p.callback(HandleAction.SET, self.p)

    def __change_transport(self, is_quick_access, *args):
        a = self.transport_names[self.transport_var.get()]
        self.p.communication_transport = a()
        if is_quick_access:
            self.__recreate_transport_view(x_label=0, y_label=90, x_widget=145, y_widget=90)
        else:
            self.__recreate_transport_view(x_label=0, y_label=30, x_widget=145, y_widget=30)

    def __change_mechanism_id(self, *args):
        self.p.m_id = mechanism_id.MechanismIdElement(self.mechanism_id_var.get())

    def __change_addr_size(self, *args):
        self.p.addr_size = self.p.addr_size.__class__.from_str(self.addr_size_var.get())

    def __recreate_password_view(self):
        password_var = tk.StringVar(value=self.p.secret.decode('utf-8') if self.p.secret else "")
        ttk.Label(self.main_canvas, text='Пароль').place(x=2, y=2, width=140)
        custom_entry = MyEntry(self.main_canvas, text_var=password_var)
        custom_entry.place(x=145, y=2, width=300)
        custom_entry.bind("<Button-3>", lambda e, t="Для ввода пароля, выберите другой тип безопасности": self.__show_tooltip(e, t))

        def update_secret(*args):
            self.p.secret = password_var.get().encode('utf-8')
        password_var.trace_add("write", update_secret)

        if self.p.m_id != mechanism_id.NONE:
            custom_entry.set_state("normal")
        else:
            custom_entry.set_state("disabled")


    def __create_row(self, name: cdt.SimpleDataType | tk.Variable, label_text: str, font_: font.Font | None = None,
                     x_label: int = 0, y_label: int = 300, width_label: int = 140,
                     x_widget: int = 145, y_widget: int = 300, width_widget: int = 300) -> tuple[ttk.Label, tk.Widget]:
        label = ttk.Label(self.main_canvas, text=label_text)
        label.place(x=x_label, y=y_label, width=width_label)

        match name:
            case cdt.Enum():
                widget = ComboBox(master=self.main_canvas,
                                      font=self.font if font_ is None else font_,
                                      width=300,
                                      cb_get_from_source=lambda _: name,
                                      cb_set_to_source=lambda _, value: name.set(value))
            case tk.Variable():
                widget = ttk.Entry(master=self.main_canvas,
                                      font=self.font if font_ is None else font_,
                                      width=250,
                                      textvariable=name)
            case _:
                raise TypeError(f"got unknown {name=} type {name.__class__.__name__}")

        widget.place(x=x_widget, y=y_widget, width=width_widget)
        return label, widget

    def __get_characteristic_ble(self, par: p.KPZBLE1, y_label):
        if self.loading_bar:
            self.loading_bar.destroy()
        self.loading_bar = LoadingBar(self.main_canvas
                                      , mode="indeterminate", x=5, y=y_label+60, width=440)
        self.loading_bar.start()
        self.ble_characteristic_button.configure(state="disabled")

        par.callback = self.__handle_ble_char
        self.p.callback(HandleAction.GET_BLE_CHARACTERISTICS, par)


    def __search_ble(self, par: p.KPZBLE1, y_label):
        def update_progressbar():
            nonlocal timeout_count
            t_c = next(timeout_count)
            progress_value = (5 - t_c) * 20
            self.loading_bar.set_progress(progress_value)

            if t_c == 0:
                self.loading_bar.destroy()
                self.search_button.configure(state="normal")
                return
            (self.main_canvas
             .after(1000, update_progressbar))

        timeout_count = count(5, -1)
        self.loading_bar = LoadingBar(self.main_canvas
                                      , mode="determinate", x=5, y=y_label+60, width=440)
        self.search_button.configure(state="disabled")
        update_progressbar()
        par.callback = self.__handle_searching
        self.p.callback(HandleAction.SEARCH, par)


    def __copy_mac(self):
        if self.selected_mac:
            self.p.communication_transport.mac = self.selected_mac
            print(f'MAC copied: {self.selected_mac}')
            # self.__recreate_transport_view()

        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите строку с MAC-адресом.")

    def __recreate_transport_view(self, x_label=0, y_label=0, x_widget=0, y_widget=0):
        while self.transport_widgets:
            self.transport_widgets.pop().destroy()
        self.transport_params.clear()

        match self.p.communication_transport:
            case p.SerialPort():
                self.transport_widgets.extend(
                    self.__create_row(add_Variable(self.p.communication_transport, "port"), "Имя порта",
                                      x_label=x_label, y_label=y_label, x_widget=145, y_widget=y_widget))
                self.transport_widgets.extend(
                    self.__create_row(add_Variable(self.p.communication_transport, "baudrate"),
                                    "Скорость", x_label=x_label, y_label=y_label+30, x_widget=145, y_widget=y_widget+30))
            case p.RS485():
                self.transport_widgets.extend(
                    self.__create_row(add_Variable(self.p.communication_transport, "port"), "Имя порта",
                                    x_label=x_label, y_label=y_label, x_widget=145, y_widget=y_widget))
                self.transport_widgets.extend(
                    self.__create_row(add_Variable(self.p.communication_transport, "baudrate"),
                                    "Скорость", x_label=x_label, y_label=y_label+30, x_widget=145, y_widget=y_widget+30))
            case p.Network():
                self.transport_widgets.extend(
                    self.__create_row(add_Variable(self.p.communication_transport, "host"), "Адрес",
                                    x_label=x_label, y_label=y_label, x_widget=145, y_widget=y_widget))
                self.transport_widgets.extend(self.__create_row(add_Variable(self.p.communication_transport, "port"), "Порт", font.NORMAL,
                                                              x_label=x_label, y_label=y_label+30, x_widget=145, y_widget=y_widget+30))
            case p.KPZBLE1():
                self.transport_widgets.extend(self.__create_row(add_Variable(self.p.communication_transport, "mac"), "MAC-aдрес", font.NORMAL,
                                                              x_label=x_label, y_label=y_label, x_widget=145, y_widget=y_widget))
                par = self.p.copy()
                self.search_button = ttk.Button(master=self.main_canvas, text="Поиск", command=lambda: self.__search_ble(par, y_label=y_label))
                self.search_button.place(x=2, y=y_label+30)
                self.ble_characteristic_button = ttk.Button(master=self.main_canvas, text="Показать параметры", command=lambda: self.__get_characteristic_ble(par, y_label=y_label))
                self.ble_characteristic_button.place(x=122, y=y_label+30)
                self.add_mac_button = ttk.Button(master=self.main_canvas, text="Копировать MAC", command=lambda: self.__copy_mac())
                self.add_mac_button.place(x=302, y=y_label+30)

                self.transport_widgets.extend((self.search_button, self.ble_characteristic_button, self.add_mac_button))

    def __handle_searching(self, par: list[p.KPZBLE1]):
        self.selected_mac = None

        def on_row_click(event: tk.Event):
            w = event.widget
            iid = w.identify_row(event.y)
            mac_address = w.item(iid, 'text')
            self.selected_mac = mac_address
            print(f'Selected MAC: {self.selected_mac}')

        def on_double_button_click(event: tk.Event):
            w = event.widget
            column = w.identify_column(event.x)
            iid = w.identify_row(event.y)
            region = w.identify_region(event.x, event.y)
            print(f'double button {column=} {iid=} {region=}')
            y_search_button = self.search_button.winfo_y() - 30

            if iid:
                self.selected_mac = w.item(iid, 'text')
                print(f'Set MAC from double click: {self.selected_mac}')
                self.p.communication_transport.mac = self.selected_mac
                w.destroy()
                y_flag= self.search_button.winfo_y()
                if y_flag == 60:
                    self.__recreate_transport_view(x_label=0, y_label=30, x_widget=145, y_widget=30)
                else:
                    self.__recreate_transport_view(x_label=0, y_label=90, x_widget=145, y_widget=90)

                # self.__recreate_transport_view(y_label=y_search_button)

        print("got: ", par)
        if len(par) == 0:
            messagebox.showwarning(title="Результат поиска BLE устройств",
                                   message="Не найдено ни одного BLE устройства КПЗ")
            return
        if isinstance(self.__parameter_tree, ttk.Treeview):
            self.__parameter_tree.destroy()
        x_button = self.search_button.winfo_x()
        y_button = self.search_button.winfo_y()
        y_treeview = y_button + 30
        self.__parameter_tree = ttk.Treeview(
            master=self.main_canvas
            ,
            selectmode='extended',
            columns=("#1", "#2", "#3"),
            height=min(len(par), 10))
        scroll_y = tk.Scrollbar(self.main_canvas
                                , orient=tk.VERTICAL, command=self.__parameter_tree.yview)
        scroll_y.place(x=430, y=y_treeview, height=230)

        self.__parameter_tree.configure(yscrollcommand=scroll_y.set)
        self.transport_widgets.extend((self.__parameter_tree, scroll_y))
        self.__parameter_tree.column("#0", width=50, minwidth=50, stretch=tk.YES, anchor=tk.CENTER)
        self.__parameter_tree.heading("#0", text="Mac", anchor=tk.W, command=lambda: print("#0"))
        self.__parameter_tree.column("#1", width=50, minwidth=10, stretch=tk.YES, anchor=tk.CENTER)
        self.__parameter_tree.heading("#1", text="Имя", anchor=tk.W, command=lambda: print("#1"))
        self.__parameter_tree.column("#2", width=50, minwidth=10, stretch=tk.YES, anchor=tk.CENTER)
        self.__parameter_tree.heading("#2", text="rssi", anchor=tk.W, command=lambda: print("#2"))
        self.__parameter_tree.column("#3", width=50, minwidth=50, stretch=tk.YES, anchor=tk.CENTER)
        self.__parameter_tree.heading("#3", text="Данные производителя", anchor=tk.W, command=lambda: print("#3"))
        self.__parameter_tree.place(x=x_button, y=y_treeview, width=420)
        for dev in par:
            iid = self.__parameter_tree.insert(parent="",
                                  index=tk.END,
                                  text=dev.mac,
                                  values=(dev.name, dev.rssi, dev.m_data.decode("utf-8", errors="replace")))
        self.__parameter_tree.bind('<Double-Button-1>', on_double_button_click)
        self.__parameter_tree.bind("<Button-1>", on_row_click)

    def __handle_ble_char(self, res: dict[str, bytes]):
        print("got: ", res)
        if len(res) == 0:
            messagebox.showwarning(title="Результат получения BLE параметров",
                                   message="Не найдено ни одной характеристики")
            self.loading_bar.destroy()
            self.ble_characteristic_button.configure(state="normal")
            return
        if isinstance(self.__parameter_tree, ttk.Treeview):
            self.__parameter_tree.destroy()
        x_button = self.search_button.winfo_x()
        y_button = self.search_button.winfo_y()
        y_treeview = y_button + 30
        self.__parameter_tree = ttk.Treeview(
            master=self.main_canvas
            ,
            columns=("#1",),
            height=min(len(res), 10))
        scroll_y = tk.Scrollbar(self.main_canvas
                                , orient=tk.VERTICAL, command=self.__parameter_tree.yview)
        scroll_y.place(x=430, y=y_treeview, height=230)
        self.__parameter_tree.configure(yscrollcommand=scroll_y.set)
        self.transport_widgets.extend((self.__parameter_tree, scroll_y))
        self.__parameter_tree.column("#0", width=200, minwidth=100, stretch=tk.YES, anchor=tk.W)
        self.__parameter_tree.heading("#0", text="Имя", anchor=tk.W, command=lambda: print("#0"))
        self.__parameter_tree.column("#1", width=228, minwidth=100, stretch=tk.YES, anchor=tk.W)
        self.__parameter_tree.heading("#1", text="Значение", anchor=tk.W, command=lambda: print("#1"))
        self.__parameter_tree.place(x=x_button, y=y_treeview)
        for name, value in res.items():
            try:
                value = value.decode("utf-8")
            except UnicodeDecodeError as e:
                value = value.hex(" ")
            iid = self.__parameter_tree.insert(
                parent="",
                index=tk.END,
                text=name,
                values=(value, ))
        self.loading_bar.destroy()
        self.ble_characteristic_button.configure(state="normal")

