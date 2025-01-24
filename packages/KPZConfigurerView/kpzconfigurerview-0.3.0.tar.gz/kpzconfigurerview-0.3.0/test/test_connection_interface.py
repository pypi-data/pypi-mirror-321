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


con_type_int = [0, 1, 16, 32, 48, 64, 80, 96]
con_type_word = [
    "Отсутствует",
    "Процесс управления клиентами",
    "Публичный клиент",
    "Считыватель показаний",
    "Конфигуратор",
    "Инициативный",
    "Обновление ПО",
    "Домашний дисплей"]
con_type_mapping = dict(zip(con_type_int, con_type_word))
sec_mech_int = [0, 1, 2, 3, 4, 5, 6, 7]
sec_mech_word=[
    "Низший, без секретности",
    "Низкий, без шифрования с паролем",
    "Высокий",
    "Высокий, MD5",
    "Высокий, SHA1",
    "Высокий, GMAC",
    "Высокий, SHA256",
    "Высокий, ECDSAL"]
sec_mech_mapping = dict(zip(sec_mech_int, sec_mech_word))
address_int = [1,2,4]
EXPECTED_CONNECTION_TYPE = random.choice(con_type_int)
EXPECTED_SECURITY_MECH = random.choice(sec_mech_int)
EXPECTED_PHYSICAL_ADDRESS = (random.randint(1, 99))
EXPECTED_TIMEOUT = (random.randint(1, 120))
EXPECTED_ADDRESS = random.choice(address_int)
main_root = Tk()
main_root.geometry("380x170")
main_root.title("Тест")
instructions = [
    "Откройте вторую вкладку расширенных настроек соединения",
    f"Выберите следующие опции и введите следующие данные:",
    f"Тип соединения: ({EXPECTED_CONNECTION_TYPE}) {con_type_mapping[EXPECTED_CONNECTION_TYPE]}",
    f"Механизм безопасности: {EXPECTED_SECURITY_MECH} {sec_mech_mapping[EXPECTED_SECURITY_MECH]}",
    f"Физический адрес: {EXPECTED_PHYSICAL_ADDRESS}",
    f"Таймаут: {EXPECTED_TIMEOUT}",
    f"Адресация: {EXPECTED_ADDRESS}",
    f"Нажмите на кнопку Сохранить"
]

for i, text in enumerate(instructions):
    ttk.Label(main_root, font=("Arial", 10), text=text).grid(row=i, column=0, sticky="EW")
def test_callback(action: HandleAction, parameters: p.Parameters):
    errors = []

    if action == HandleAction.SET:

        current_sap = int(parameters.sap)
        if current_sap != EXPECTED_CONNECTION_TYPE:
             errors.append(f"Параметр Тип соединения не совпадает, "
                           f"должно быть: {EXPECTED_CONNECTION_TYPE},"
                           f"передано: {current_sap}")

        if int(parameters.m_id) != EXPECTED_SECURITY_MECH:
            errors.append(f"Параметр Механизм безопасности не совпадает, "
                          f"должно быть: {EXPECTED_SECURITY_MECH}, "
                          f"передано: {parameters.m_id} ({type(parameters.m_id).__name__})")
        if parameters.com_profile.device_address != EXPECTED_PHYSICAL_ADDRESS:
            errors.append(f"Параметр Физический адрес не совпадает, "
                          f"должно быть: {EXPECTED_PHYSICAL_ADDRESS}, ({type(EXPECTED_PHYSICAL_ADDRESS)}) "
                          f"передано: {parameters.com_profile.device_address} ({type(parameters.com_profile.device_address).__name__})")
        if parameters.response_timeout != EXPECTED_TIMEOUT:
            errors.append(f"Параметр Таймаут не совпадает, "
                          f"должно быть: {EXPECTED_TIMEOUT}, ({type(EXPECTED_TIMEOUT)})"
                          f"передано: {parameters.response_timeout} ({type(parameters.response_timeout).__name__})")
        if parameters.addr_size != EXPECTED_ADDRESS:
            errors.append(f"Параметр Адресация не совпадает, "
                          f"должно быть: {EXPECTED_ADDRESS} ({type(EXPECTED_ADDRESS)}), "
                          f"передано: {parameters.addr_size} ({type(parameters.addr_size).__name__})")

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
    InterfaceSetting.connection_interface(interface)
    return interface


if __name__ == "__main__":
    client = Client()
    call_interface_setting(client)
    main_root.mainloop()


