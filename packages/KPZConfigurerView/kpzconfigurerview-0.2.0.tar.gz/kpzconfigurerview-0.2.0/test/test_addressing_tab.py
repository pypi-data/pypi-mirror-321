from src.KPZConfigurerView import interfaces_setting
import ConfigurerControl.parameters as p
from ConfigurerControl.actions import HandleAction
from DLMS_SPODES_client.client import Client
import copy
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror
import random

from src.KPZConfigurerView.interfaces_setting import InterfaceSetting

main_root = Tk()
x = int((main_root.winfo_screenwidth() - main_root.winfo_reqwidth()) / 2-350)
y = int((main_root.winfo_screenheight() - main_root.winfo_reqheight()) / 2-200)
main_root.geometry(f"350x200+{x}+{y}")
main_root.title("Тест")

def generate_random_host():
    numbers = ".".join([str(random.randint(1, 255)) for _ in range(4)])
    return numbers

def generate_random_MAC():
    numbers = ":".join([str(random.randint(10, 99)) for _ in range(6)])
    return numbers

EXPECTED_TRANSPORT = "SerialPort"
EXPECTED_PORT = f"COM{random.randint(1, 99)}"
EXPECTED_BAUDRATE = f"{random.randint(1, 9999)}"
EXPECTED_TRANSPORT2 = "RS485"
EXPECTED_PORT2 = f"COM{random.randint(1, 99)}"
EXPECTED_BAUDRATE2 = f"{random.randint(1, 9999)}"
EXPECTED_TRANSPORT3 = "Network"
EXPECTED_HOST = f"{generate_random_host()}"
EXPECTED_PORT3 = f"{random.randint(1, 9999)}"
EXPECTED_TRANSPORT4 = "KPZBLE1"
EXPECTED_MAC = f"{generate_random_MAC()}"
instructions_list = [
    [
        "Введите следующие данные:",
        "Транспорт: Оптопорт",
        f"Имя порта: {EXPECTED_PORT}",
        f"Скорость: {EXPECTED_BAUDRATE}",
        "Нажмите на кнопку Сохранить",
    ],
    [
        "Введите следующие данные:",
        "Транспорт: RS485",
        f"Имя порта: {EXPECTED_PORT2}",
        f"Скорость: {EXPECTED_BAUDRATE2}",
        "Нажмите на кнопку Сохранить",
    ],
    [
        "Введите следующие данные:",
        "Транспорт: TCP/IP",
        f"Хост: {EXPECTED_HOST}",
        f"Порт: {EXPECTED_PORT3}",
        "Нажмите на кнопку Сохранить",
    ],
    [
        "Введите следующие данные:",
        "Транспорт: BLE",
        f"MAC: {EXPECTED_MAC}",
        "Нажмите на кнопку Сохранить",
    ],
]
all_errors = []
current_instruction = 0

def force_close():
    main_root.destroy()

def update_instructions():
    global current_instruction
    global all_errors
    for widget in main_root.winfo_children():
        widget.destroy()

    if current_instruction < len(instructions_list):
        for i, text in enumerate(instructions_list[current_instruction]):
            ttk.Label(main_root, font=("Arial", 10), text=text).grid(row=i, column=0, sticky="EW")
    else:
        ttk.Label(main_root, font=("Arial", 10), text="Все тесты завершены!").grid(row=0, column=0, sticky="EW")
        ttk.Label(main_root, font=("Arial", 10), text="Закройте это окно для завершения").grid(row=1, column=0, sticky="EW")


def test_callback(action: HandleAction, parameters: p.Parameters):
    global current_instruction

    errors = []
    if current_instruction == 0:
        errors = test_1(action, parameters)
    elif current_instruction == 1:
        errors = test_2(action, parameters)
    elif current_instruction == 2:
        errors = test_3(action, parameters)
    elif current_instruction == 3:
        errors = test_4(action, parameters)

    if action == HandleAction.SET:
        if errors:
            showerror(title="Ошибки ввода", message="\n".join(errors))
            client = Client()
            interface = call_interface_setting(client)
            move_window_right_of_main(main_root, interface.top)
        else:
            current_instruction += 1
            update_instructions()
            if current_instruction < len(instructions_list):
                client = Client()
                interface = call_interface_setting(client)
                move_window_right_of_main(main_root, interface.top)
    else:
        client = Client()
        interface = call_interface_setting(client)
        move_window_right_of_main(main_root, interface.top)


def move_window_right_of_main(main_window, target_window, offset=5):
    main_window_x = main_window.winfo_x()
    main_window_y = main_window.winfo_y()
    main_window_width = main_window.winfo_width()
    new_window_x = main_window_x + main_window_width + offset
    new_window_y = main_window_y
    target_window.geometry(f"+{new_window_x}+{new_window_y}")


def call_interface_setting(client: Client):
    interface = interfaces_setting.InterfaceSetting(main_root, "Name", p.Parameters(
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
    InterfaceSetting.addressing(interface)
    return interface


def test_1(action: HandleAction, parameters: p.Parameters):
    errors = []
    if action == HandleAction.SET:
        if str(type(parameters.communication_transport).__name__) != EXPECTED_TRANSPORT:
            errors.append(f"Параметр 'Транспорт' не совпадает: "
                          f"ожидалось '{EXPECTED_TRANSPORT}', "
                          f"передано '{str(type(parameters.communication_transport).__name__)}'")
        if parameters.communication_transport.port != EXPECTED_PORT:
            errors.append(f"Параметр 'Имя порта' не совпадает: "
                          f"ожидалось '{EXPECTED_PORT}', "
                          f"передано '{parameters.communication_transport.port}'")
        if parameters.communication_transport.baudrate != EXPECTED_BAUDRATE:
            errors.append(f"Параметр 'Скорость' не совпадает: "
                          f"ожидалось '{EXPECTED_BAUDRATE}', "
                          f"передано '{parameters.communication_transport.baudrate}'")
    all_errors.append(errors)
    return errors


def test_2(action: HandleAction, parameters: p.Parameters):
    errors = []
    if action == HandleAction.SET:
        if str(type(parameters.communication_transport).__name__) != EXPECTED_TRANSPORT2:
            errors.append(f"Параметр 'Транспорт' не совпадает: "
                          f"ожидалось '{EXPECTED_TRANSPORT2}', "
                          f"передано '{str(type(parameters.communication_transport).__name__)}'")
        if parameters.communication_transport.port != EXPECTED_PORT2:
            errors.append(f"Параметр 'Имя порта' не совпадает: "
                          f"ожидалось '{EXPECTED_PORT2}', "
                          f"передано '{parameters.communication_transport.port}'")
        if parameters.communication_transport.baudrate != EXPECTED_BAUDRATE2:
            errors.append(f"Параметр 'Скорость' не совпадает: "
                          f"ожидалось '{EXPECTED_BAUDRATE2}', "
                          f"передано '{parameters.communication_transport.baudrate}'")
    all_errors.append(errors)
    return errors


def test_3(action: HandleAction, parameters: p.Parameters):
    errors = []
    if action == HandleAction.SET:
        if str(type(parameters.communication_transport).__name__) != EXPECTED_TRANSPORT3:
            errors.append(f"Параметр 'Транспорт' не совпадает: "
                          f"ожидалось '{EXPECTED_TRANSPORT3}', "
                          f"передано '{str(type(parameters.communication_transport).__name__)}'")
        if parameters.communication_transport.host != EXPECTED_HOST:
            errors.append(f"Параметр 'Хост' не совпадает: "
                          f"ожидалось '{EXPECTED_HOST}', "
                          f"передано '{parameters.communication_transport.host}'")
        if parameters.communication_transport.port != EXPECTED_PORT3:
            errors.append(f"Параметр 'Порт' не совпадает: "
                          f"ожидалось '{EXPECTED_PORT3}', "
                          f"передано '{parameters.communication_transport.port}'")
    all_errors.append(errors)
    return errors


def test_4(action: HandleAction, parameters: p.Parameters):
    errors = []
    if action == HandleAction.SET:
        if str(type(parameters.communication_transport).__name__) != EXPECTED_TRANSPORT4:
            errors.append(f"Параметр 'Транспорт' не совпадает: "
                          f"ожидалось '{EXPECTED_TRANSPORT4}', "
                          f"передано '{str(type(parameters.communication_transport).__name__)}'")
        if parameters.communication_transport.mac != EXPECTED_MAC:
            errors.append(f"Параметр 'MAC' не совпадает: "
                          f"ожидалось '{EXPECTED_MAC}', "
                          f"передано '{parameters.communication_transport.mac}'")
    all_errors.append(errors)
    return errors


if __name__ == "__main__":
    update_instructions()
    client = Client()
    call_interface_setting(client)
    main_root.mainloop()