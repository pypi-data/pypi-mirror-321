from datetime import datetime
from src.KPZConfigurerView import interfaces_setting
from src.KPZConfigurerView.interfaces_setting import InterfaceSetting, MyScaleCanvas, MyEntry, LoadingBar
from DLMS_SPODES_client.client import Client
import ConfigurerControl.parameters as p
import copy
from tkinter import *
from tkinter import ttk, IntVar
import tkinter as tk
from PIL import Image, ImageTk
import os
from ConfigurerControl.widgets.script_table import Script
from tKot.common import Point
from DLMS_SPODES.cosem_interface_classes import script_table
from ConfigurerControl.widgets.action_calendar import DaySchedule
from DLMS_SPODES.cosem_interface_classes import activity_calendar
from src.KPZConfigurerView.widgets.time import Time
from src.KPZConfigurerView.widgets.Try import  DateTime_Try
from src.KPZConfigurerView.widgets.date import Date
from src.KPZConfigurerView.widgets.datetime import DateTime
from DLMS_SPODES.types import cdt




def delete():
    selection = listbox.curselection()
    listbox.delete(selection[0])


def add():
    new_language = language_entry.get()
    listbox.insert(0, new_language)

def start():
    progressbar.start(1)
    progressbar2.start(2)

def stop():
    progressbar.stop()
    progressbar2.stop()


client = Client()
main_root = Tk()
w = main_root.winfo_screenwidth()
h = main_root.winfo_screenheight()
w = w // 2
h = h // 2
w = w - 800
h = h - 450
main_root.geometry(f"1600x700+{w}+{h}")
main_root.title("Тест стилей")
main_root.columnconfigure(index=0, weight=4)
main_root.columnconfigure(index=1, weight=1)
main_root.rowconfigure(index=0, weight=1)
main_root.rowconfigure(index=1, weight=3)
main_root.rowconfigure(index=2, weight=1)


label = ttk.Label(main_root, text='Тест стилей Style Test !@#$%^&&*(0123456789)')
label.place(x=50, y=10)

call_button = ttk.Button(master=main_root, text="Интерфейс", command=lambda: call_interface_setting(client))
call_button.place(x=50, y=40)

call_button2 = ttk.Button(master=main_root, text="Иконки", command=lambda: IconTesterApp())
call_button2.place(x=250, y=40)

check_var = IntVar()
checkbutton = ttk.Checkbutton(text="Чекчиабатта", variable=check_var)
checkbutton.place(x=50, y=70)

left = "Left"
right = "Right"
direction = StringVar(value=right)
header = ttk.Label(textvariable=direction)
header.place(x=75, y=100)

left_btn = ttk.Radiobutton(text=left, value=left, variable=direction)
left_btn.place(x=50, y=130)

right_btn = ttk.Radiobutton(text=right, value=right, variable=direction)
right_btn.place(x=100, y=130)

frame = ttk.Frame(borderwidth=1, relief=SOLID, width=400, height=240)
frame.place(x=20, y=160)

language_entry = ttk.Entry(master=frame, width=45)
language_entry.place(x=10, y=10)
ttk.Button(master=frame, text="Добавить", command=add).place(x=300, y=10)

listbox = Listbox(master=frame)
listbox.place(x=10, y=40, width=350, height=150)

listbox.insert(END, "9876543210")
listbox.insert(END, "0123456789")
listbox.insert(END, "9876543210")
listbox.insert(END, "0123456789")
listbox.insert(END, "9876543210")
listbox.insert(END, "0123456789")
listbox.insert(END, "9876543210")
listbox.insert(END, "0123456789")
listbox.insert(END, "9876543210")
listbox.insert(END, "0123456789")

ttk.Button(master=frame, text="Удалить", command=delete).place(x=150, y=200)

scrollbar = ttk.Scrollbar(master=frame, orient="vertical", command=listbox.yview)
scrollbar.place(x=370, y=50, height=120)
listbox["yscrollcommand"]=scrollbar.set

scale_num = StringVar()
scale_num.set('0.00')
horizontalScale = ttk.Scale(orient=HORIZONTAL, length=400, command=lambda s:scale_num.set('%0.2f' % float(s)), from_=1, to=1000, variable=scale_num)
horizontalScale.place(x=20, y=430)
scale_num_header = ttk.Label(textvariable=scale_num)
scale_num_header.place(x=220, y=460)

nums_box = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
combobox = ttk.Combobox(values=nums_box, width=64)
combobox.place(x=20, y=490)

spinbox = ttk.Spinbox(from_=1.0, to=100.0, width=64)
spinbox.place(x=20, y=520)

value_var = IntVar()
progressbar =  LoadingBar(main_root, mode="indeterminate", x=20, y=550, width=400, height=10, bg="#C6CFE3", fill="#1F2430")
progressbar2 = LoadingBar(main_root, mode="indeterminate", x=20, y=570, width=400, height=30, bg="#1F2430", fill="#C6CFE3")

start_btn = ttk.Button(text="Стартуем", command=start)
start_btn.place(x=100, y=610)
stop_btn = ttk.Button(text="Стоп", command=stop)
stop_btn.place(x=250, y=610)

def change_black():
    main_root.configure(bg='black')
    scale_frame.configure(background="black")


black = ttk.Button(text="Black", command=change_black)
black.place(x=100, y=640)

def change_white():
    main_root.configure(bg='white')
    scale_frame.configure(background="white")


white = ttk.Button(text="White", command=change_white)
white.place(x=250, y=640)

def change_dark():
    main_root.configure(bg='#535D75')
    scale_frame.configure(background="#535D75")


dark = ttk.Button(text="Dark", command=change_dark)
dark.place(x=100, y=670)

def change_light():
    main_root.configure(bg='#EBF1FD')
    scale_frame.configure(background="#EBF1FD")

light = ttk.Button(text="Light", command=change_light)
light.place(x=250, y=670)

scale_frame = tk.Frame(main_root, height=46, width=296)
scale_frame.place(x=200, y=70)

scale = MyScaleCanvas(scale_frame, x=-2, y=-2, width=300, height=50, values=[0, 25, 50, 75, 100], bg="#535D75", fg="#EBF1FD", init_value=50)
pass_entry = MyEntry(main_root, bg= "#535D75", mg="black", fg="white")
pass_entry.place(x=200, y=120)


canvas = Canvas(main_root ,bg="white", width=750, height=1000)
canvas.place(x=500, y=100)

# canvas2 = Canvas(main_root ,bg="white", width=750, height=250)
# canvas2.place(x=500, y=400)

canvas3 = Canvas(main_root ,bg="white", width=250, height=250)
canvas3.place(x=1300, y=100)

canvas4 = Canvas(main_root ,bg="white", width=250, height=250)
canvas4.place(x=1300, y=400)

# canvas5 = Canvas(main_root ,bg="white", width=250, height=250)
# canvas5.place(x=1100, y=400)
#
# canvas6 = Canvas(main_root ,bg="white", width=250, height=250)
# canvas6.place(x=1100, y=100)
font = tk.font.Font(family="Helvetica", size=12)

data = script_table.Script(script_table.Script())
script = Script(can=canvas3, font_=font, param=b'\x02', name="Test")
start_point = Point(0, 0)
new_point = script.place2(start_point, data)
start_point2 = Point(50, 50)
new_point2 = script.place2(start_point2, data)



data2 = activity_calendar.DaySchedule([
    activity_calendar.DayProfileAction()])
schedule = DaySchedule(can=canvas4, font_=font, param=b'\x01')
start_point = Point(50, 50)
start_point2 = Point(0, 0)
start_point3 = Point(100, 75)
new_size = schedule.place2(start_point, data2)
new_size2 = schedule.place2(start_point2, data2)
new_size3 = schedule.place2(start_point3, data2)

now = datetime.now()

data3 = cdt.Time(b'\x1b\xFF\x17\x10\x00')                                       #(b'Тэг\Часы\Минуты\Секунды\Доли)
data_try = cdt.Date('09.08.2020-7')
data5 = cdt.Date(b'\x1a\x07\xe8\xFF\x01\x02')                                   #(b'Тэг\Год\Год\Месяц\День\День недели)
data6 = cdt.DateTime(b'\x19\x07\xe8\x02\x02\x05\x15\x24\x36\x00\x00\xb4\xff')
                    #(b'Тэг\Год\Год\Мес\Чис\Ден\Час\Мин\Сек\Доли)

data4 = cdt.Time("16:45:30")
print("-------------------------Widgets -------------------------")

clock = Time(can=canvas, font_=font, param=b'\x01', width=250)
start_point = Point(0, 0)
new_clock = clock.place2(start_point, data3)
print(f"Размеры виджета Время: {new_clock}")

day_num = Date(can=canvas, font_=font, param=b'\x1a', width=250)
day_point = Point(250, 41)
new_day_num = day_num.place2(day_point, data5)
print(f"Размеры виджета Дата: {new_day_num}")

daytime = DateTime(can=canvas, font_=font, param=b'\x01', width=500)
day_time_point = Point(0, 83)
new_day_time_point = daytime.place2(day_time_point, data6)
print(f"Размеры виджета Дата/Время: {new_day_time_point}")




def test_callback(action, parameters):
    return None

def call_interface_setting(client: Client):
    interface = interfaces_setting.InterfaceSetting(None, "Name", p.Parameters(
        client_id='d5',
        sap=client.SAP.copy(),
        conformance=client.proposed_conformance.copy(),
        communication_transport=p.SerialPort(port=p.SerialPort.port, baudrate=p.SerialPort.baudrate),
        secret=p.Secret(client.secret),
        m_id=client.m_id.copy(),
        addr_size=client.addr_size,
        response_timeout=client.response_timeout,
        com_profile=copy.copy(client.com_profile.parameters),
        callback=test_callback))
    InterfaceSetting.quick_connection_interface(interface)
    return interface
style = ttk.Style()



class IconTesterApp(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Icon Tester")
        self.geometry("350x250")

        self.styles = {
            1: {"path": "./ButtonAndIcons/Dark", "bg": "#1F2430"},
            2: {"path": "./ButtonAndIcons/TransparentDark", "bg": "#1F2430"},
            3: {"path": "./ButtonAndIcons/Light", "bg": "white"},
            4: {"path": "./ButtonAndIcons/TransparentLight", "bg": "white"},
            5: {"path": "./ButtonAndIcons/CompareLight", "bg": "white"},
            6: {"path": "./ButtonAndIcons/CompareDark", "bg": "#1F2430"}
        }
        self.image_files = [
            "ActivatedRegister.png",
            "ActivityCalendar.png",
            "Arbitrator.png",
            "AveragingRegister.png",
            "BinaryBlockTransfer.png",
            "ConnectionByLogicalName.png",
            "ControlRegister.png",
            "Data.png",
            "DataPackaging.png",
            "DisconnectionControl.png",
            "ExtendedRegister.png",
            "HDLCSettings.png",
            "InitiativeExitSettings.png",
            "Limiter.png",
            "OptoportSettings.png",
            "Register.png",
            "ScenarioTable.png",
            "Schedule.png",
            "SecuritySettings.png",
            "SingleActionSchedule.png",
            "SpecialDaysTable.png",
            "StatusDecoding.png",
            "TableRegister.png",
            "TCPUDPSettings.png",
            "UniversalProfile.png",
            "NTP Setup.png",
            "NTP Setup-1.png",
            "NTP Setup-2.png",
            "NTP Setup-3.png",

            "AveragingRegister2.png",
            "ConnectionByLogicalName2.png",
            "ExtendedRegister2.png",
            "InitiativeExitSettings2.png",
            "Limiter2.png",
            "SpecialDaysTable2.png",
            "StatusDecoding2.png",
            "TableRegister2.png",


        ]
        self.image_cache = []
        self.current_style = tk.IntVar(value=1)

        radiobutton_frame = tk.Frame(self)
        radiobutton_frame.pack(side=tk.TOP, pady=10)
        for style, name in zip(self.styles.keys(), ["Dark", "TrDark", "Light", "TrLight", "CompareLight", "CompareDark"]):
            ttk.Radiobutton(
                radiobutton_frame,
                text=name,
                variable=self.current_style,
                value=style,
                command=self.update_buttons
            ).pack(side=tk.LEFT)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(expand=True, fill=tk.BOTH)

        self.update_buttons()

    def update_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        self.image_cache.clear()

        style = self.styles[self.current_style.get()]
        self.button_frame.configure(bg=style["bg"])

        style_path = style["path"]
        row, col = 0, 0
        for image_name in self.image_files:
            image_path = os.path.join(style_path, image_name)
            if not os.path.exists(image_path):
                print(f"Файл не найден: {image_path}")
                continue
            try:
                img = Image.open(image_path).resize((20, 20), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.image_cache.append(photo)

                button = tk.Button(self.button_frame, image=photo, bg=style["bg"], borderwidth=0)
                button.grid(row=row, column=col, padx=5, pady=5)

                col += 1
                if col >= 8:
                    col = 0
                    row += 1
            except Exception as e:
                print(f"Ошибка загрузки изображения {image_path}: {e}")

if __name__ == "__main__":
    # client = Client()
    # call_interface_setting(client)
    main_root.mainloop()


