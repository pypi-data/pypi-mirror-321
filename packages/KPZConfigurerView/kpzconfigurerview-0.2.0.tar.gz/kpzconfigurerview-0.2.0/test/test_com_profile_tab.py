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



main_root = Tk()
main_root.geometry("320x300")
main_root.title("Тест")


EXPECTED_COMM_SPEED = random.randint(1, 9999)
EXPECTED_WIN_SIZE_TRANSMIT = random.randint(1, 10)
EXPECTED_WIN_SIZE_RECEIVE = random.randint(1, 10)
EXPECTED_MAX_INFO_TRANSMIT = random.randint(1, 128)
EXPECTED_MAX_INFO_RECEIVE = random.randint(1, 128)
EXPECTED_INTER_OCTET_TIMEOUT =random.randint(1, 120)
EXPECTED_INACTIVITY_TIMEOUT = random.randint(1, 120)
EXPECTED_DEVICE_ADDRESS = random.randint(1, 99)

instructions = [
    "Откройте вкладку Профиль",
    "Введите следующие данные:",
    "",
    f"Скорость соединения {EXPECTED_COMM_SPEED}",
    f"Размер окна передачи {EXPECTED_WIN_SIZE_TRANSMIT}",
    f"Размер окна приёма {EXPECTED_WIN_SIZE_RECEIVE}",
    f"Макс. длина инф. поля передачи {EXPECTED_MAX_INFO_TRANSMIT}",
    f"Макс. длина инф. поля приёма {EXPECTED_MAX_INFO_RECEIVE}",
    f"Таймаут межсимвольного интервала {EXPECTED_INTER_OCTET_TIMEOUT}",
    f"Таймаут неактивности {EXPECTED_INACTIVITY_TIMEOUT}",
    f"Адрес устройства {EXPECTED_DEVICE_ADDRESS}",
    "",
    f"Нажмите на кнопку Сохранить"
]

for i, text in enumerate(instructions):
    ttk.Label(main_root, font=("Arial", 10), text=text).grid(row=i, column=0, sticky="EW")

def test_callback(action: HandleAction, parameters: p.Parameters):
    errors = []

    if action == HandleAction.SET:
        if parameters.com_profile.comm_speed != EXPECTED_COMM_SPEED:
            errors.append(f"Параметр comm_speed не совпадает, "
                          f"должно быть: {EXPECTED_COMM_SPEED} (int), "
                          f"передано: {parameters.com_profile.comm_speed} ({type(parameters.com_profile.comm_speed).__name__})")

        if parameters.com_profile.window_size_transmit != EXPECTED_WIN_SIZE_TRANSMIT:
            errors.append(f"Параметр window_size_transmit не совпадает, "
                          f"должно быть: {EXPECTED_WIN_SIZE_TRANSMIT} (int), "
                          f"передано: {parameters.com_profile.window_size_transmit} ({type(parameters.com_profile.window_size_transmit).__name__})")

        if parameters.com_profile.window_size_receive != EXPECTED_WIN_SIZE_RECEIVE:
            errors.append(f"Параметр window_size_receive не совпадает, "
                          f"должно быть: {EXPECTED_WIN_SIZE_RECEIVE} (int), "
                          f"передано: {parameters.com_profile.window_size_receive} ({type(parameters.com_profile.window_size_receive).__name__})")

        if parameters.com_profile.max_info_field_length_transmit != EXPECTED_MAX_INFO_TRANSMIT:
            errors.append(f"Параметр max_info_field_length_transmit не совпадает, "
                          f"должно быть: {EXPECTED_MAX_INFO_TRANSMIT} (int), "
                          f"передано: {parameters.com_profile.max_info_field_length_transmit} ({type(parameters.com_profile.max_info_field_length_transmit).__name__})")

        if parameters.com_profile.max_info_field_length_receive != EXPECTED_MAX_INFO_RECEIVE:
            errors.append(f"Параметр max_info_field_length_receive не совпадает, "
                          f"должно быть: {EXPECTED_MAX_INFO_RECEIVE} (int), "
                          f"передано: {parameters.com_profile.max_info_field_length_receive} ({type(parameters.com_profile.max_info_field_length_receive).__name__})")

        if parameters.com_profile.inter_octet_time_out != EXPECTED_INTER_OCTET_TIMEOUT:
            errors.append(f"Параметр inter_octet_time_out не совпадает, "
                          f"должно быть: {EXPECTED_INTER_OCTET_TIMEOUT} (int), "
                          f"передано: {parameters.com_profile.inter_octet_time_out} ({type(parameters.com_profile.inter_octet_time_out).__name__})")

        if parameters.com_profile.inactivity_time_out != EXPECTED_INACTIVITY_TIMEOUT:
            errors.append(f"Параметр inactivity_time_out не совпадает, "
                          f"должно быть: {EXPECTED_INACTIVITY_TIMEOUT} (int), "
                          f"передано: {parameters.com_profile.inactivity_time_out} ({type(parameters.com_profile.inactivity_time_out).__name__})")

        if parameters.com_profile.device_address != EXPECTED_DEVICE_ADDRESS:
            errors.append(f"Параметр device_address не совпадает, "
                          f"должно быть: {EXPECTED_DEVICE_ADDRESS} (int), "
                          f"передано: {parameters.com_profile.device_address} ({type(parameters.com_profile.device_address).__name__})")

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
    InterfaceSetting.com_profile(interface)
    return interface

if __name__ == "__main__":
    client = Client()
    call_interface_setting(client)
    main_root.mainloop()


# comm_speed=9600,
# window_size_transmit=1,
# window_size_receive=1,
# max_info_field_length_transmit=128,
# max_info_field_length_receive=128,
# inter_octet_time_out=25,
# inactivity_time_out=120,
# device_address=16