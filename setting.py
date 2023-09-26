from PyQt5.QtWidgets import *

from PyQt5.QtCore import QMetaObject, Qt, QModelIndex
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore, QtWidgets

import minimalmodbus
from serial import SerialException
from classes.Auth import Auth
from classes.MysqlDb import MysqlDb

from ui_setting import Ui_SettingPage
class SettingPage(QMainWindow, Ui_SettingPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        
        self.comboPort = self.findChild(QComboBox, "widgetPort")
        self.comboPort.addItems(["COM5", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9"])

        self.comboBaud = self.findChild(QComboBox, "widgetBaud")  # Replace "combobox_name" with the actual name of the combobox in the .ui file
        self.comboBaud.addItems(["5", "4", "3", "2", "1"])

        self.baudButton3.clicked.connect(self.change_baudrate3)
        self.baudButton2.clicked.connect(self.change_baudrate2)
        self.baudButton1.clicked.connect(self.change_baudrate1)

        self.findBaud1.clicked.connect(self.find_rs485_baudrate1)
        self.findBaud2.clicked.connect(self.find_rs485_baudrate2)
        self.findBaud3.clicked.connect(self.find_rs485_baudrate3)



        self.createUserBtn.clicked.connect(self.submit_user)











    def find_rs485_baudrate(self, slave_address):
        baud_rates = [2400, 4800, 9600, 19200, 38400]  # List of common baud rates to check

        for baud_rate in baud_rates:
            try:
                port_baud = str(self.comboPort.currentText())
                instrument = minimalmodbus.Instrument(port_baud, slave_address)
                instrument.serial.baudrate = baud_rate
                instrument.serial.timeout = 1

                # Attempt to read a register from the device
                register_value = instrument.read_register(0, functioncode=3)
                return baud_rate
            except (minimalmodbus.ModbusException, SerialException, ValueError):
                pass

        return None

    def find_rs485_baudrate1(self):
        baud_rate = self.find_rs485_baudrate(1)
        if baud_rate:
            self.currentBaud1.setText(str(baud_rate))
        else:
            self.show_warning_dialog("پورت اشتباه")


    def find_rs485_baudrate2(self):
        baud_rate = self.find_rs485_baudrate(2)
        if baud_rate:
            self.currentBaud2.setText(str(baud_rate))
        else:
            self.show_warning_dialog("پورت اشتباه")

    def find_rs485_baudrate3(self):
        baud_rate = self.find_rs485_baudrate(3)
        if baud_rate:
            self.currentBaud3.setText(str(baud_rate))
        else:
            self.show_warning_dialog("پورت اشتباه")
        

    def show_warning_dialog(self, message):
        warning_box = QMessageBox()
        warning_box.setIcon(QMessageBox.Warning)
        warning_box.setWindowTitle("Warning")
        warning_box.setText(message)
        warning_box.setStandardButtons(QMessageBox.Ok)
        warning_box.exec()

    def change_baudrate3(self):
        try:
            port_baud = str(self.comboPort.currentText())
            slave_address = 3

            # Create an instance of the Instrument class
            instrument = minimalmodbus.Instrument(port_baud, slave_address)

            # Optionally, configure the serial communication parameters if needed
            instrument.serial.baudrate = str(self.currentBaud3.text())
            instrument.serial.bytesize = 8
            instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
            instrument.serial.stopbits = 1

            # Read the digital input value from the RS485 sensor
            register_address = 246
            # input_value = instrument.read_bit(register_address, functioncode=1)
            value = int(self.comboBaud.currentText())
            change = instrument.write_register(register_address, value)
            set = instrument.write_register(248, 20,signed=False)
            set = instrument.write_register(248, 10,signed=False)
            #verify = instrument.read_register(register_address, functioncode=3)
            # print(amperage)
            # print(amperage2)
        except minimalmodbus.ModbusException:
            pass


    def change_baudrate2(self):
        try:
            port_baud = str(self.comboPort.currentText())
            slave_address = 2

            # Create an instance of the Instrument class
            instrument = minimalmodbus.Instrument(port_baud, slave_address)

            # Optionally, configure the serial communication parameters if needed
            instrument.serial.baudrate = str(self.currentBaud2.text())
            instrument.serial.bytesize = 8
            instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
            instrument.serial.stopbits = 1

            # Read the digital input value from the RS485 sensor
            register_address = 246
            # input_value = instrument.read_bit(register_address, functioncode=1)
            value = int(self.comboBaud.currentText())
            change = instrument.write_register(register_address, value)
            set = instrument.write_register(248, 20,signed=False)
            set = instrument.write_register(248, 10)
            #verify = instrument.read_register(register_address, functioncode=3)
            # print(amperage)
            # print(amperage2)

        except minimalmodbus.ModbusException:
            pass


    def change_baudrate1(self):
        try:
            port_baud = str(self.comboPort.currentText())
            slave_address = 1

            # Create an instance of the Instrument class
            instrument = minimalmodbus.Instrument(port_baud, slave_address)

            # Optionally, configure the serial communication parameters if needed
            instrument.serial.baudrate = str(self.currentBaud1.text())
            instrument.serial.bytesize = 8
            instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
            instrument.serial.stopbits = 1

            register_address = 166
            # input_value = instrument.read_bit(register_address, functioncode=1)
            value = int(self.comboBaud.currentText())
            change = instrument.write_register(register_address, value)
            set = instrument.write_register(164, 20,)
        except minimalmodbus.ModbusException:
            pass

    def submit_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        auth_instance = Auth()  # Create an instance of Auth
        auth_instance.register_user(username, password)  # Call the method on the instance


        mysql_instance = MysqlDb()
        if self.standardCheck.isChecked():
            
            data ={"username": username, "permission": "نتظیمات"}
            
            print(data)
            mysql_instance.insert("acl", data)
            


        

        

        



