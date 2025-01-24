from src.KPZConfigurerView import interfaces_setting
from src.KPZConfigurerView.interfaces_setting import InterfaceSetting, MyScaleCanvas
from DLMS_SPODES_client.client import Client
import ConfigurerControl.parameters as p
from ConfigurerControl.actions import HandleAction
import copy
from tkinter import *
from tkinter import ttk, IntVar
import tkinter as tk



def delete():
    selection = listbox.curselection()
    listbox.delete(selection[0])


def add():
    new_language = language_entry.get()
    listbox.insert(0, new_language)

def start():
    progressbar.start(100)
    progressbar2.start(10)

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
main_root.geometry(f"500x700+{w}+{h}")
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
progressbar =  ttk.Progressbar(orient="horizontal", variable=value_var, length=400)
progressbar.place(x=20, y=550)

progressbar2 =  ttk.Progressbar(orient="horizontal", mode="indeterminate", length=400)
progressbar2.place(x=20, y=580)

start_btn = ttk.Button(text="Стартуем", command=start)
start_btn.place(x=100, y=610)
stop_btn = ttk.Button(text="Стоп", command=stop)
stop_btn.place(x=250, y=610)

def change_black():
    main_root.configure(bg='black')

black = ttk.Button(text="Black", command=change_black)
black.place(x=100, y=640)

def change_white():
    main_root.configure(bg='white')

white = ttk.Button(text="White", command=change_white)
white.place(x=250, y=640)

scale_frame = tk.Frame(main_root, height=100, width=300)
scale_frame.place(x=100, y=670)

scale = MyScaleCanvas(scale_frame, x=0, y=0, width=300, height=100, values=[0, 25, 50, 75, 100], init_value=50)

def test_callback(action: HandleAction, parameters: p.Parameters):
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
print(style.theme_names())
print(style.theme_use())

if __name__ == "__main__":
    client = Client()
    call_interface_setting(client)
    main_root.mainloop()


