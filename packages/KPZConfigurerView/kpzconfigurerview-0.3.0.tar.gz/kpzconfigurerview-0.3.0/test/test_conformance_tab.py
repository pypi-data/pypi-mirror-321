from DLMS_SPODES.types.implementations import bitstrings
from DLMS_SPODES.types.implementations.bitstrings import Conformance

from src.KPZConfigurerView import interfaces_setting
from src.KPZConfigurerView.interfaces_setting import InterfaceSetting
import ConfigurerControl.parameters as p
from ConfigurerControl.actions import HandleAction
from DLMS_SPODES_client.client import Client
import copy
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror, showinfo
import random


def select_random_conformance(conformance_keys, num_elements=9):
    selected_index = sorted(random.sample(range(len(conformance_keys)), num_elements))
    CONFORMANCE_NAMES = [conformance_keys[i] for i in selected_index]
    CONFORMANCE_NUMS = selected_index
    return CONFORMANCE_NAMES, CONFORMANCE_NUMS


def create_conformance_string(conformance_keys, conformance_nums):
    bit_string = ['0'] * len(conformance_keys)
    for index in sorted(conformance_nums):
        bit_string[index] = '1'
    return ''.join(bit_string)

conformance_keys = bitstrings.Conformance.get_values()
CONFORMANCE_NAMES, CONFORMANCE_NUMS = select_random_conformance(conformance_keys)
EXPECTED_CONFORMANCE = create_conformance_string(conformance_keys, CONFORMANCE_NUMS)
main_root = Tk()
main_root.geometry("320x300")
main_root.title("Тест")
instructions = [
    "Откройте вкладку Соглосование",
    "Выберите следующие чекбоксы:",
    "",
    f"{CONFORMANCE_NAMES[0]}",
    f"{CONFORMANCE_NAMES[1]}",
    f"{CONFORMANCE_NAMES[2]}",
    f"{CONFORMANCE_NAMES[3]}",
    f"{CONFORMANCE_NAMES[4]}",
    f"{CONFORMANCE_NAMES[5]}",
    f"{CONFORMANCE_NAMES[6]}",
    f"{CONFORMANCE_NAMES[7]}",
    f"{CONFORMANCE_NAMES[8]}",
    "",
    f"Нажмите на кнопку Сохранить"
]

for i, text in enumerate(instructions):
    ttk.Label(main_root, font=("Arial", 10), text=text).grid(row=i, column=0, sticky="EW")

def test_callback(action: HandleAction, parameters: p.Parameters):
    errors = []

    if action == HandleAction.SET:
        if str(parameters.conformance) != EXPECTED_CONFORMANCE:
            errors.append(f"Параметр 'Имя порта' не совпадает: "
                          f"ожидалось '{EXPECTED_CONFORMANCE}', "
                          f"передано '{parameters.conformance}'")

        if not errors:
            showinfo(title="Успешно", message="Данные совпадают")
        else:
            showerror(title="Ошибка", message=f"Ошибки: {', '.join(errors)}")

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
    InterfaceSetting.conformance(interface)
    return interface

if __name__ == "__main__":
    client = Client()
    call_interface_setting(client)
    main_root.mainloop()
