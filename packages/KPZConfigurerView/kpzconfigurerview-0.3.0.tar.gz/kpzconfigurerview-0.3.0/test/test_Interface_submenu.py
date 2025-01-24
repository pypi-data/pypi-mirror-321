from src.KPZConfigurerView import interfaces_setting
import ConfigurerControl.parameters as p
from ConfigurerControl.actions import HandleAction
from DLMS_SPODES_client.client import Client
import copy
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror, showinfo
import random



def generate_random_password():
    numbers = "".join([str(random.randint(0, 9)) for _ in range(16)])
    return numbers

time_int = [3, 5, 10, 30, 60, 120]
EXPECTED_SECRET = f"{generate_random_password()}"
EXPECTED_TIMEOUT = random.choice(time_int)
EXPECTED_PORT = f"COM{random.randint(1, 99)}"
EXPECTED_BAUDRATE = f"{random.randint(1, 9999)}"

main_root = Tk()
main_root.geometry("380x200")
main_root.title("Тест")
instructions = [
    "Введите следующие данные:",
    f"Пароль: {EXPECTED_SECRET}",
    "Для разрешения ввода пароля измените параметр 'Механизм ",
    "безопасности' на второй вкладке на отличный от 'Низший'",
    f"Таймаут: {EXPECTED_TIMEOUT}",
    f"Транспорт: Оптопорт",
    f"Имя порта: {EXPECTED_PORT}",
    f"Скорость: {EXPECTED_BAUDRATE}",
    f"Закройте окно подключения и сохраните изменения"
]

for i, text in enumerate(instructions):
    ttk.Label(main_root, font=("Arial", 10), text=text).grid(row=i, column=0, sticky="EW")
def test_callback(action: HandleAction, parameters: p.Parameters):
    errors = []

    if action == HandleAction.SET:
        if parameters.secret != EXPECTED_SECRET.encode('utf-8'):
            errors.append(f"Параметр secret не совпадает, "
                          f"должно быть: {EXPECTED_SECRET} (str), "
                          f"передано: {parameters.secret.decode('utf-8')} (str)")
        if parameters.response_timeout != EXPECTED_TIMEOUT:
            errors.append(f"Параметр response_timeout не совпадает, "
                          f"должно быть: {EXPECTED_TIMEOUT} (int), "
                          f"передано: {parameters.response_timeout} ({type(parameters.response_timeout).__name__})")
        if parameters.communication_transport.port != EXPECTED_PORT:
            errors.append(f"Параметр port не совпадает, "
                          f"должно быть: {EXPECTED_PORT} (str), "
                          f"передано: {parameters.communication_transport.port} ({type(parameters.communication_transport.port).__name__})")
        if parameters.communication_transport.baudrate != EXPECTED_BAUDRATE:
            errors.append(f"Параметр baudrate не совпадает, "
                          f"должно быть: {EXPECTED_BAUDRATE} (str), "
                          f"передано: {parameters.communication_transport.baudrate} ({type(parameters.communication_transport.baudrate).__name__})")

        if not errors:
            showinfo(title="Успешно", message="Данные совпадают")
        else:
            showerror(title="Ошибка", message=f"Ошибки: {', '.join(errors)}")

def call_interface_setting(client: Client):
    interfaces_setting.InterfaceSetting(main_root, "Name", p.Parameters(
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

if __name__ == "__main__":
    client = Client()
    call_interface_setting(client)
    main_root.mainloop()
