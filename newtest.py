
import os
import sys
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
import minimalmodbus
import time
import datetime
import random
import barcode
from barcode import EAN13
from PIL import Image
from ui_newtest import Ui_NewTestPage
from jdatetime import datetime as jdatetime
import zpl
from zebra import Zebra

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import threading

from databasefile import *







class NewTestPage(QMainWindow, Ui_NewTestPage):
    def __init__(self):
        super().__init__()


        ###two way for importing ui
        #self.ui = Ui_MainWindow delete ui_mainwindow from class parameters
        #self.ui.setupUi(self)
        #self.ui.combostandard = self.findChild(QComboBox, "widgetStandard")  # Replace "combobox_name" with the actual name of the combobox in the .ui file
        self.setupUi(self)
        #uic.loadUi(os.path.join(os.path.dirname(os.path.abspath(__file__)), "qml/arya/newtest.ui"), self)




        # Find the QWidget objects named "plottemp1" and "plottemp2"
        self.plot_widget = self.findChild(QWidget, "frame")
        


        # Create a QGridLayout for the plots
        layout = QGridLayout()
        self.plot_widget.setLayout(layout)


        


        # Create Matplotlib figures and canvases for the plots
        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        layout.addWidget(self.canvas1, 1, 0, 1,1)

        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        layout.addWidget(self.canvas2, 1, 1, 1, 1)

        self.figure3 = Figure()
        self.canvas3 = FigureCanvas(self.figure3)
        layout.addWidget(self.canvas3, 1, 2, 1,1)

        toolbar1 = NavigationToolbar(self.canvas1, self)
        layout.addWidget(toolbar1, 0, 0, 1, 1)

        toolbar2 = NavigationToolbar(self.canvas2, self)
        layout.addWidget(toolbar2, 0, 1, 1, 1)

        toolbar3 = NavigationToolbar(self.canvas3, self)
        layout.addWidget(toolbar3, 0, 2, 1, 1)




        self.figure4 = Figure()
        self.canvas4 = FigureCanvas(self.figure4)
        layout.addWidget(self.canvas4, 3, 0, 1,1)

        self.figure5 = Figure()
        self.canvas5 = FigureCanvas(self.figure5)
        layout.addWidget(self.canvas5, 3, 1, 1,1)

        self.figure6 = Figure()
        self.canvas6 = FigureCanvas(self.figure6)
        layout.addWidget(self.canvas6, 3, 2, 1,1)

        toolbar4 = NavigationToolbar(self.canvas4, self)
        layout.addWidget(toolbar4, 2, 0, 1, 1)

        toolbar5 = NavigationToolbar(self.canvas5, self)
        layout.addWidget(toolbar5, 2, 1, 1, 1)

        toolbar6 = NavigationToolbar(self.canvas6, self)
        layout.addWidget(toolbar6, 2, 2, 1, 1)




        self.figure7 = Figure()
        self.canvas7 = FigureCanvas(self.figure7)
        layout.addWidget(self.canvas7, 5, 0, 1,1)

        self.figure8 = Figure()
        self.canvas8 = FigureCanvas(self.figure8)
        layout.addWidget(self.canvas8, 5, 1, 1,1)


        toolbar7 = NavigationToolbar(self.canvas7, self)
        layout.addWidget(toolbar7, 4, 0, 1, 1)

        toolbar8 = NavigationToolbar(self.canvas8, self)
        layout.addWidget(toolbar8, 4, 1, 1, 1)




        self.figure9 = Figure()
        self.canvas9 = FigureCanvas(self.figure9)
        layout.addWidget(self.canvas9, 7, 0, 1,1)

        self.figure10 = Figure()
        self.canvas10 = FigureCanvas(self.figure10)
        layout.addWidget(self.canvas10, 7, 1, 1,1)

        self.figure11 = Figure()
        self.canvas11 = FigureCanvas(self.figure11)
        layout.addWidget(self.canvas11, 7, 2, 1,1)

    

        toolbar9 = NavigationToolbar(self.canvas9, self)
        layout.addWidget(toolbar9, 6, 0, 1, 1)

        toolbar10 = NavigationToolbar(self.canvas10, self)
        layout.addWidget(toolbar10, 6, 1, 1, 1)

        toolbar11 = NavigationToolbar(self.canvas11, self)
        layout.addWidget(toolbar11, 6, 2, 1, 1)





        self.comboPort = self.findChild(QComboBox, "widgetPort")  # Replace "combobox_name" with the actual name of the combobox in the .ui file
        self.comboPort.addItems(["COM5", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9"])





        self.comboStandard = self.findChild(QComboBox, "widgetStandard")  # Replace "combobox_name" with the actual name of the combobox in the .ui file
        items = retrieve_standardss()
        # # Populate the combobox with the retrieved items
        if items is not None:
            self.comboStandard.addItems(items)
        
        self.comboStandard.setCurrentIndex(-1)

        #############or###############

        # items = retrieve_standards()
        # # # Populate the combobox with the retrieved items
        # for item in items:
        #     self.comboStandard.addItem(items[0])

        ### define what happend after selevting item in dropdown
        self.comboStandard.currentIndexChanged.connect(self.handle_dropdown_change)









        
        self.volt_list = []
        self.amptotal_list = []
        self.temperature1_list = []
        self.temperature2_list = []
        self.temperature3_list = []
        self.temperature4_list = []
        self.temperature5_list = []
        self.temperature6_list = []
        self.temperature7_list = []
        self.temperature8_list = []
        self.pressure_max_list = []
        self.pressure_min_list = []
    

        # Start a separate thread to fetch temperature data
        self.fetch_thread = None

        

        self.fetchButton.clicked.connect(self.start_fetching)
        self.stopButton.clicked.connect(self.stop_fetching)
        # self.saveButton.clicked.connect(self.insert_test)
        self.printButton.clicked.connect(self.print_label)


        # Add a flag to indicate whether the fetching should be stopped
        self.stop_flag  = False






    #### define what happend after selevting item in dropdown
    def handle_dropdown_change(self, index):
        selected_option = self.comboStandard.currentText()
        self.standard_list = retrieve_standardparam(selected_option)
        
        self.gasType.setText(str(self.standard_list[4]))

        self.durationTemp.setText(str(self.standard_list[5]))
        self.intervalTemp.setText(str(self.standard_list[6]))
        self.durationAmp.setText(str(self.standard_list[7]))
        self.intervalAmp.setText(str(self.standard_list[8]))

        
        
        self.checkTemp1.setChecked(bool(self.standard_list[20]))
        self.checkTemp2.setChecked(bool(self.standard_list[21]))
        self.checkTemp3.setChecked(bool(self.standard_list[22]))
        self.checkTemp4.setChecked(bool(self.standard_list[23]))
        self.checkTemp5.setChecked(bool(self.standard_list[24]))
        self.checkTemp6.setChecked(bool(self.standard_list[25]))
        self.checkTemp7.setChecked(bool(self.standard_list[26]))
        self.checkTemp8.setChecked(bool(self.standard_list[27]))
        self.checkAmpstart.setChecked(bool(self.standard_list[28]))
        self.checkAmptotal.setChecked(bool(self.standard_list[29]))
        self.checkVolt.setChecked(bool(self.standard_list[30]))
        print("Selected option:", self.standard_list)
        print(len(self.standard_list))
        self.calculate_tolerance()






    def calculate_tolerance(self):
        standard_tolerance = self.standard_list[9:20]
        self.max_value_list = []
        self.min_value_list = []
        for i, j in zip(range(31, 42), range(0, 11)):


            min_value = round(self.standard_list[i] - (self.standard_list[i] * standard_tolerance[j] / 100), 2)
            max_value = round(self.standard_list[i] + (self.standard_list[i] * standard_tolerance[j] / 100), 2)
            self.min_value_list.append(min_value)
            self.max_value_list.append(max_value)


        print(self.min_value_list)

        self.tableCompare.setItem(1, 0, QTableWidgetItem(f"{self.min_value_list[0]:.2f}-{self.max_value_list[0]:.2f}°C"))
        self.tableCompare.setItem(1, 1, QTableWidgetItem(f"{self.min_value_list[1]:.2f}-{self.max_value_list[1]:.2f}°C"))
        self.tableCompare.setItem(1, 2, QTableWidgetItem(f"{self.min_value_list[2]:.2f}-{self.max_value_list[2]:.2f}°C"))
        self.tableCompare.setItem(1, 3, QTableWidgetItem(f"{self.min_value_list[3]:.2f}-{self.max_value_list[3]:.2f}°C"))
        self.tableCompare.setItem(1, 4, QTableWidgetItem(f"{self.min_value_list[4]:.2f}-{self.max_value_list[4]:.2f}°C"))
        self.tableCompare.setItem(1, 5, QTableWidgetItem(f"{self.min_value_list[5]:.2f}-{self.max_value_list[5]:.2f}°C"))
        # self.tableCompare.setItem(0, 6, QTableWidgetItem(f"{self.min_value_list[]:.2f}-{self.max_value_list[]:.2f}°C"))
        # self.tableCompare.setItem(0, 7, QTableWidgetItem(f"{self.min_value_list[]:.2f}-{self.max_value_list[]:.2f}°C"))
        self.tableCompare.setItem(1, 6, QTableWidgetItem(f"{self.min_value_list[6]:.2f}-{self.max_value_list[6]:.2f}psi"))
        self.tableCompare.setItem(1, 7, QTableWidgetItem(f"{self.min_value_list[7]:.2f}-{self.max_value_list[7]:.2f}psi"))
        self.tableCompare.setItem(1, 8, QTableWidgetItem(f"{self.min_value_list[8]:.2f}-{self.max_value_list[8]:.2f}A"))
        self.tableCompare.setItem(1, 9, QTableWidgetItem(f"{self.min_value_list[9]:.2f}-{self.max_value_list[9]:.2f}A"))
        self.tableCompare.setItem(1, 10, QTableWidgetItem(f"{self.min_value_list[10]:.2f}-{self.max_value_list[10]:.2f}V"))
        
        




    def stop_fetching(self):
        self.stop_flag = True
    




    def start_fetching(self):

        self.stopButton.setEnabled(True)
        self.fetchButton.setEnabled(False)


        self.temperature1_list = []  # Reset the temperature1_list
        self.temperature2_list = []  # Reset the temperature1_list
        self.temperature3_list = []
        self.temperature4_list = []
        self.temperature5_list = []
        self.temperature6_list = []
        self.temperature7_list = []
        self.temperature8_list = []
        self.pressure_max_list = []
        self.pressure_min_list = []
        self.value_list = []
        self.amptotal_list = []
        self.volt_list = []

        if self.fetch_thread is None or not self.fetch_thread.is_alive():
            self.stop_flag = False
            self.fetch_thread = threading.Thread(target=self.fetchSensorData)
            self.fetch_thread.daemon = True
            self.fetch_thread.start()
            # self.start_animations()


    def fetchSensorData(self):
        # Get the COM port number from the user input
        #port = self.portInput.text()
        #port = self.findChild(QComboBox, "comboPort")  # Replace "combobox_name" with the actual name of the combobox in the .ui file
        #self.port.addItems(["Option 1", "Option 2", "Option 3"])
        port_input = str(self.comboPort.currentText())
        durationamperage_input = int(self.durationAmp.text())  # Uder-defined duration in seconds
        amperageiterations = int(self.intervalAmp.text())  # User-defined interval in seconds
        durationtemp_input = int(self.durationTemp.text())
        intervaltemp_input = int(self.intervalTemp.text())
        motorid = (self.motorId.text())
        

        start_timeTotal = datetime.datetime.now().strftime("%H:%M:%S")
        self.startTime.setText(str(start_timeTotal))

        # Convert the start time string to a datetime object
        start_time_datetime = datetime.datetime.strptime(start_timeTotal, "%H:%M:%S")


        # Convert the intervals to timedelta objects
        delta_amperage = datetime.timedelta(seconds=durationamperage_input)
        delta_temp = datetime.timedelta(seconds=durationtemp_input)

        # Calculate the end time
        end_time_datetime = start_time_datetime + delta_amperage + delta_temp

        # Convert the end time to a string in "HH:MM:SS" format
        end_timeTotal = end_time_datetime.strftime("%H:%M:%S")
        self.endTime.setText(end_timeTotal)


    
    
        # Create an instance of the Instrument class
        instrument = minimalmodbus.Instrument(port_input, slaveaddress=3)

        # Optionally, configure the serial communication parameters if needed
        instrument.serial.baudrate = 38400
        instrument.serial.bytesize = 8
        instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
        instrument.serial.stopbits = 1

        #Set the output value to True or False
        output_value = True

        # Write the digital output value to the RS485 sensor
        # instrument.slaveaddress = 3
        register_address = 192
        instrument.write_bit(register_address, output_value,functioncode=5)

        # Read the digital input value from the RS485 sensor
        # instrument.slaveaddress = 3
        register_address = 0
        input_value = instrument.read_bit(register_address, functioncode=1)

        #        Print the digital input value
        print("Digital Input Value:", input_value)

        # Calculate the number of iterations based on the duration and interval
        intervalamperage_input = float(durationamperage_input/amperageiterations)
        instrument = minimalmodbus.Instrument(port_input, slaveaddress=1)
       
        #number_of_registers = 1  # Replace with the appropriate number of registers for amperage

        self.ampstart_list = []
        self.volt_list = []


        end_timeAmp = time.perf_counter() + durationamperage_input


        # Fetch sensor amperage data for the specified duration and iterations
        while time.perf_counter() < end_timeAmp:
            # Fetch the amperage data from the RS485 device
            next_timeAmp = time.perf_counter() + intervalamperage_input

            # Fetch the amperage data from the RS485 device

            if self.stop_flag:
                break

            if self.checkAmpstart.isChecked():
                ampstart = instrument.read_float(registeraddress=32, functioncode=3)
                self.tableAverage.setItem(0, 9, QTableWidgetItem(f"{ampstart:.2f}A"))
                self.ampstart_list.append(ampstart)
                average_ampstart = sum(self.ampstart_list) / len(self.ampstart_list)
                self.tableAverage.setItem(1, 9, QTableWidgetItem(f"{average_ampstart:.2f}A"))
                print(f"ampstart at iteration : {ampstart:.2f}A")
            
            else:
                average_ampstart = 0
            

            
            if self.checkVolt.isChecked():
                volt = instrument.read_float(registeraddress=26, functioncode=3)
                self.tableAverage.setItem(0, 10, QTableWidgetItem(f"{volt:.2f}V"))
                self.volt_list.append(volt)
                average_volt = sum(self.volt_list) / len(self.volt_list)
                self.tableAverage.setItem(1, 10, QTableWidgetItem(f"{average_volt:.2f}V"))
                print(f"volt at iteration : {volt:.2f}V")
            
            else:
                average_volt = 0
                


            

            #plot only upfates 1 sec#################
            # self.update_plots()

            # Wait for the specified interval before the next data fetch
            
            while time.perf_counter() < next_timeAmp:
                pass

        self.tableAverage.viewport().update()

        self.update_plots()


                   
        def find_pressure_value(temppressure):
            x = [-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
            y = [47.7, 57.91, 69.62, 83.06, 98.38, 115.8, 135.3, 157.3, 181.9, 209.3, 239.6, 273.2, 310.1, 350.8, 395.4, 444.2, 497.7, 556.2, 620.2]
        
            # بررسی وجود عدد در ستون x
            if temppressure in x:
                index = x.index(temppressure)
                return y[index]
            
            # در صورتی که عدد در ستون x وجود نداشته باشد
            else:
                # پیدا کردن دو عدد نزدیک‌ترین به عدد ورودی
                closest_x = min(x, key=lambda num: abs(num - temppressure))
                closest_index = x.index(closest_x)
                
                # محاسبه مقدار تقریبی y با استفاده از دو عدد نزدیک‌ترین
                x1 = x[closest_index]
                y1 = y[closest_index]
                x2 = x[closest_index + 1]
                y2 = y[closest_index + 1]
                
                # محاسبه روش میانیابی مقدار y
                y_approx = y1 + ((temppressure - x1) / (x2 - x1)) * (y2 - y1)
                
                return y_approx






        # Calculate the number of iterations based on the duration and interval
        tempiterations = int(durationtemp_input / intervaltemp_input)
        instrument = minimalmodbus.Instrument(port_input, slaveaddress=2)
        instrumentamp = minimalmodbus.Instrument(port_input, slaveaddress=1)


        self.temperature1_list = []  # Reset the temperature1_list
        self.temperature2_list = []  # Reset the temperature1_list
        self.temperature3_list = []
        self.temperature4_list = []
        self.temperature5_list = []
        self.temperature6_list = []
        self.temperature7_list = []
        self.temperature8_list = []
        self.pressure_max_list = []
        self.pressure_min_list = []
        self.amptotal_list = []



        end_time = time.perf_counter() + durationtemp_input

        # for i in range(tempiterations):
        while time.perf_counter() <= end_time:
            next_time = time.perf_counter() + intervaltemp_input
            # Fetch the temperature data from the RS485 device
            
            if self.stop_flag:
                break            


            
            if self.checkTemp1.isChecked():
                temperature1 = instrument.read_float(registeraddress=30, functioncode=3)
                self.tableAverage.setItem(0, 0, QTableWidgetItem(f"{temperature1:.2f}°C"))
                self.temperature1_list.append(temperature1)
                average_temperature1 = sum(self.temperature1_list) / len(self.temperature1_list)
                self.tableAverage.setItem(1, 0, QTableWidgetItem(f"{average_temperature1:.2f}°C"))
                print(f"Temperature1 at iteration : {temperature1:.2f}°C")
            else:
                average_temperature1 = 0

            
            if self.checkTemp2.isChecked():
                temperature2 = instrument.read_float(registeraddress=32, functioncode=3)
                self.tableAverage.setItem(0, 1, QTableWidgetItem(f"{temperature2:.2f}°C"))
                self.temperature2_list.append(temperature2)
                average_temperature2 = sum(self.temperature2_list) / len(self.temperature2_list)
                self.tableAverage.setItem(1, 1, QTableWidgetItem(f"{average_temperature2:.2f}°C"))
                print(f"Temperature2 at iteration : {temperature2:.2f}°C")
            else:
                average_temperature2 = 0

            
            if self.checkTemp3.isChecked():
                temperature3 = instrument.read_float(registeraddress=34, functioncode=3)
                self.tableAverage.setItem(0, 2, QTableWidgetItem(f"{temperature3:.2f}°C"))
                self.temperature3_list.append(temperature3)
                average_temperature3 = sum(self.temperature3_list) / len(self.temperature3_list)
                self.tableAverage.setItem(1, 2, QTableWidgetItem(f"{average_temperature3:.2f}°C"))
                print(f"Temperature3 at iteration : {temperature3:.2f}°C")
            else:
                average_temperature3 = 0

            
            if self.checkTemp4.isChecked():
                temperature4 = instrument.read_float(registeraddress=36, functioncode=3)
                self.tableAverage.setItem(0, 3, QTableWidgetItem(f"{temperature4:.2f}°C"))
                self.temperature4_list.append(temperature4)
                average_temperature4 = sum(self.temperature4_list) / len(self.temperature4_list)
                self.tableAverage.setItem(1, 3, QTableWidgetItem(f"{average_temperature4:.2f}°C"))
                print(f"Temperature4 at iteration : {temperature4:.2f}°C")
            else:
                average_temperature4 = 0

            
            if self.checkTemp5.isChecked():
                temperature5 = instrument.read_float(registeraddress=38, functioncode=3)
                self.tableAverage.setItem(0, 4, QTableWidgetItem(f"{temperature5:.2f}°C"))
                self.temperature5_list.append(temperature5)
                average_temperature5 = sum(self.temperature5_list) / len(self.temperature5_list)
                self.tableAverage.setItem(1, 4, QTableWidgetItem(f"{average_temperature5:.2f}°C"))
                print(f"Temperature5 at iteration : {temperature5:.2f}°C")
            else:
                average_temperature5 = 0

            
            if self.checkTemp6.isChecked():
                temperature6 = instrument.read_float(registeraddress=40, functioncode=3)
                self.tableAverage.setItem(0, 5, QTableWidgetItem(f"{temperature6:.2f}°C"))
                self.temperature6_list.append(temperature6)
                average_temperature6 = sum(self.temperature6_list) / len(self.temperature6_list)
                self.tableAverage.setItem(1, 5, QTableWidgetItem(f"{average_temperature6:.2f}°C"))
                print(f"Temperature6 at iteration : {temperature6:.2f}°C")
            else:
                average_temperature6 = 0

            
            if self.checkTemp7.isChecked():
                temperature7 = instrument.read_float(registeraddress=42, functioncode=3)
                pressure_min = find_pressure_value(temperature7)
                self.tableAverage.setItem(0, 6, QTableWidgetItem(f"{pressure_min:.2f}PSI"))
                self.temperature7_list.append(temperature7)
                self.pressure_min_list.append(pressure_min)
                average_pressure_min = sum(self.pressure_min_list) / len(self.pressure_min_list)
                average_temperature7 = sum(self.temperature7_list) / len(self.temperature7_list)
                self.tableAverage.setItem(1, 6, QTableWidgetItem(f"{average_pressure_min:.2f}PSI"))
                print(f"Temperature7 at iteration : {temperature7:.2f}PSI")
            else:
                average_temperature7 = 0
                average_pressure_min = 0

            
            if self.checkTemp8.isChecked():
                temperature8 = instrument.read_float(registeraddress=44, functioncode=3)
                pressure_max = find_pressure_value(temperature8)
                self.tableAverage.setItem(0, 7, QTableWidgetItem(f"{pressure_max:.2f}PSI"))
                self.temperature8_list.append(temperature8)
                self.pressure_max_list.append(pressure_max)
                average_pressure_max = sum(self.pressure_max_list) / len(self.pressure_max_list)
                average_temperature8 = sum(self.temperature8_list) / len(self.temperature8_list)
                self.tableAverage.setItem(1, 7, QTableWidgetItem(f"{average_pressure_max:.2f}PSI"))
                print(f"Temperature8 at iteration : {temperature8:.2f}PSI")
            else:
                average_temperature8 = 0
                average_pressure_max = 0
            

            if self.checkAmptotal.isChecked():
                amptotal = instrumentamp.read_float(registeraddress=32, functioncode=3)
                self.tableAverage.setItem(0, 8, QTableWidgetItem(f"{amptotal:.2f}A"))
                self.amptotal_list.append(amptotal)
                average_amptotal = sum(self.amptotal_list) / len(self.amptotal_list)
                self.tableAverage.setItem(1, 8, QTableWidgetItem(f"{average_amptotal:.2f}A"))
                print(f"amptotal at iteration : {amptotal:.2f}A")
            else:
                average_amptotal = 0



            self.tableAverage.viewport().update()
            
            self.update_plots()

            # Wait for the specified interval before the next data fetch
            while time.perf_counter() < next_time:
                pass



        instrument = minimalmodbus.Instrument(port_input, slaveaddress=3)

        #Set the output value to True or False
        output_value = False

        # Write the digital output value to the RS485 sensor
        instrument.slaveaddress = 3
        register_address = 192
        instrument.write_bit(register_address, output_value,functioncode=5)

        # Read the digital input value from the RS485 sensor
        instrument.slaveaddress = 3
        register_address = 0
        input_value = instrument.read_bit(register_address, functioncode=1)

        print("Digital Input Value:", input_value)

        # print(f"Average Temperature1: {average_temperature1:.2f}°C")
        # print(f"Average Temperature2: {average_temperature2:.2f}°C")
        # print(f"Average Temperature3: {average_temperature3:.2f}°C")
        # print(f"Average Temperature4: {average_temperature4:.2f}°C")
        # print(f"Average Temperature5: {average_temperature5:.2f}°C")
        # print(f"Average Temperature6: {average_temperature6:.2f}°C")
        # print(f"Average Temperature7: {average_temperature7:.2f}°C")
        # print(f"Average Temperature8: {average_temperature8:.2f}°C")
        # print(f"Average pressure max: {average_pressure_max:.2f}psi")
        # print(f"Average pressure min: {average_pressure_min:.2f}psi")


        
        if self.stop_flag == False:
        


            self.value_list.append(average_temperature1)
            self.value_list.append(average_temperature2)
            self.value_list.append(average_temperature3)
            self.value_list.append(average_temperature4)
            self.value_list.append(average_temperature5)
            self.value_list.append(average_temperature6)
            # self.value_list.append(average_temperature7)
            # self.value_list.append(average_temperature8)
            self.value_list.append(average_pressure_min)
            self.value_list.append(average_pressure_max)
            self.value_list.append(average_amptotal)
            self.value_list.append(average_ampstart)
            self.value_list.append(average_volt)




            self.tableCompare.setItem(0, 0, QTableWidgetItem(f"{self.value_list[0]:.2f}°C"))
            self.tableCompare.setItem(0, 1, QTableWidgetItem(f"{self.value_list[1]:.2f}°C"))
            self.tableCompare.setItem(0, 2, QTableWidgetItem(f"{self.value_list[2]:.2f}°C"))
            self.tableCompare.setItem(0, 3, QTableWidgetItem(f"{self.value_list[3]:.2f}°C"))
            self.tableCompare.setItem(0, 4, QTableWidgetItem(f"{self.value_list[4]:.2f}°C"))
            self.tableCompare.setItem(0, 5, QTableWidgetItem(f"{self.value_list[5]:.2f}°C"))
            # self.tableCompare.setItem(0, 6, QTableWidgetItem(f"{self.value_list[11]:.2ff}°C"))
            # self.tableCompare.setItem(0, 7, QTableWidgetItem(f"{self.value_list[]:.2f}-"))
            self.tableCompare.setItem(0, 6, QTableWidgetItem(f"{self.value_list[6]:.2f}psi"))
            self.tableCompare.setItem(0, 7, QTableWidgetItem(f"{self.value_list[7]:.2f}psi"))
            self.tableCompare.setItem(0, 8, QTableWidgetItem(f"{self.value_list[8]:.2f}A"))
            self.tableCompare.setItem(0, 9, QTableWidgetItem(f"{self.value_list[9]:.2f}A"))
            self.tableCompare.setItem(0, 10, QTableWidgetItem(f"{self.value_list[10]:.2f}V"))


            #call the compare function
            self.compare()

            self.saveButton.setEnabled(True)

        self.stopButton.setEnabled(False)
        self.fetchButton.setEnabled(True)
           



    

    def update_plots(self):
        # Fetch real-time temperature data from sensors
        # Replace with your actual method of fetching temperature data

        # Update plottemp1 with temperature1 data
        self.figure1.clear()
        ax1 = self.figure1.add_subplot(111)
        ax1.plot(self.temperature1_list)  # Use appropriate plot method based on your data
        ax1.set_title("Temp 1")
        self.canvas1.draw()

        # Update plottemp2 with temperature2 data
        self.figure2.clear()
        ax2 = self.figure2.add_subplot(111)
        ax2.plot(self.temperature2_list)  # Use appropriate plot method based on your data
        ax2.set_title("Temp 2")
        self.canvas2.draw()

        # Update plottemp3 with temperature3 data
        self.figure3.clear()
        ax3 = self.figure3.add_subplot(111)
        ax3.plot(self.temperature3_list)  # Use appropriate plot method based on your data
        ax3.set_title("Temp 3")
        self.canvas3.draw()

        # Update plottemp4 with temperature4 data
        self.figure4.clear()
        ax4 = self.figure4.add_subplot(111)
        ax4.plot(self.temperature4_list)  # Use appropriate plot method based on your data
        ax4.set_title("Temp 4")
        self.canvas4.draw()

        # Update plottemp5 with temperature5 data
        self.figure5.clear()
        ax5 = self.figure5.add_subplot(111)
        ax5.plot(self.temperature5_list)  # Use appropriate plot method based on your data
        ax5.set_title("Temp 5")
        self.canvas5.draw()

        # Update plottemp6 with temperature6 data
        self.figure6.clear()
        ax6 = self.figure6.add_subplot(111)
        ax6.plot(self.temperature6_list)  # Use appropriate plot method based on your data
        ax6.set_title("Temp 6")
        self.canvas6.draw()

        # Update plottemp7 with temperature7 data
        self.figure7.clear()
        ax7 = self.figure7.add_subplot(111)
        ax7.plot(self.pressure_min_list)  # Use appropriate plot method based on your data
        ax7.set_title("PSI Min")
        self.canvas7.draw()

        # Update plottemp8 with temperature8 data
        self.figure8.clear()
        ax8 = self.figure8.add_subplot(111)
        ax8.plot(self.pressure_max_list)  # Use appropriate plot method based on your data
        ax8.set_title("PSI max")
        self.canvas8.draw()

        # Update plotamp with amp data
        self.figure9.clear()
        ax9 = self.figure9.add_subplot(111)
        ax9.plot(self.ampstart_list)  # Use appropriate plot method based on your data
        ax9.set_title("Amp start")
        self.canvas9.draw()

        # Update plotvolt with volt data
        self.figure10.clear()
        ax10 = self.figure10.add_subplot(111)
        ax10.plot(self.volt_list)  # Use appropriate plot method based on your data
        ax10.set_title("Voltage")
        self.canvas10.draw()

        # Update plotamp with amp data
        self.figure11.clear()
        ax11 = self.figure11.add_subplot(111)
        ax11.plot(self.amptotal_list)  # Use appropriate plot method based on your data
        ax11.set_title("Amp total")
        self.canvas11.draw()





    def compare(self):
        for i in range(0,11):
            if self.min_value_list[i] <= self.value_list[i] <= self.max_value_list[i] :
                self.tableCompare.setItem(2, i, QTableWidgetItem("پاس"))
                self.tableCompare.item(2, i).setBackground(QColor(0, 255, 0))

            else:
                self.tableCompare.setItem(2, i, QTableWidgetItem("مردود"))
                self.tableCompare.item(2, i).setBackground(QColor(255, 0, 0))
        

        self.tableCompare.viewport().update()

        all_correct = all(self.min_value_list[i] <= self.value_list[i] <= self.max_value_list[i] for i in range(11))
        if all_correct:

            self.printButton.setEnabled(True)



    def print_label(self):
        # def barcode_generate(self):
        # # Get the current Jalali date
        current_jdate = jdatetime.now()

        # Format the Jalali date as "yyyymmdd"
        jalali_date_str = current_jdate.strftime('%Y%m%d')

        # Generate a random 10-digit number
        random_number = random.randint(0, 55555)

        # Combine the Jalali date and random number to create a 13-digit number
        thirteen_digit_number = int(jalali_date_str + str(random_number).zfill(5))
        self.testResult.setText(str(thirteen_digit_number))
        # Generate EAN-13 barcode
        # ean = EAN13(thirteen_digit_number, writer=barcode.writer.ImageWriter())

        # # Convert barcode to PIL image
        # barcode_image = ean.render()
        # barcode_image.show("Samsung SCX-4x21 Series (USB001)")
        l = zpl.Label(25,60)
        height = 0
        l.origin(30,2)
        l.write_text("Hyundai AC", char_height=3, char_width=3, line_width=30, justification='C')
        l.endorigin()

        l.origin(30,10)
        l.write_text("1402/08/07 12:40", char_height=3, char_width=3, line_width=30, justification='C')
        l.endorigin()

        l.origin(30,20)
        l.write_text("QC PASSED", char_height=3, char_width=3, line_width=30, justification='C')
        l.endorigin()

        # height += 13
        # image_width = 5
        # l.origin((l.width-image_width)/2, height)
        # image_height = l.write_graphic(
        #     Image.open(os.path.join(os.path.dirname(zpl.__file__), 'trollface-large.png')),
        #     image_width)
        # l.endorigin()

        # height += image_height + 5
        l.origin(5, 2)
        l.barcode('2', thirteen_digit_number, height=150, check_digit='N')
        l.endorigin()
        print(str(self.tempbarcode))

        print(l.dumpZPL())
        l.preview()
        label = l.dumpZPL()


        printer_name = "Adobe PDF"

        # Create a Zebra object
        z = Zebra(printer_name)
        z.output(label)
        # print(z.getqueues())




        








