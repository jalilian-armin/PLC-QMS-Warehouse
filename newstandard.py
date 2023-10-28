
import os
import sys
from PyQt5.QtCore import QMetaObject, Qt, QModelIndex
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import minimalmodbus
import time
import mysql.connector
from ui_newstandard import Ui_NewStandardPage

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import threading

from databasefile import *

import datetime









class NewStandardPage(QMainWindow, Ui_NewStandardPage):
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
       




        ############tab2#########################################################################################################################################################################################
        self.comboStandard = self.findChild(QComboBox, "widgetStandard_2")  # Replace "combobox_name" with the actual name of the combobox in the .ui file
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

        self.editBtn.clicked.connect(self.edit_standard)
        self.deleteBtn.clicked.connect(self.delete_standard)



        #################tab2##################################

        # self.toleranceSpin.valueChanged.connect(self.tolerance)
        self.toleranceTemp1.clear()
        self.toleranceTemp2.clear()
        self.toleranceTemp3.clear()
        self.toleranceTemp4.clear()
        self.toleranceTemp5.clear()
        self.toleranceTemp6.clear()
        self.toleranceTemp7.clear()
        self.toleranceTemp8.clear()
        self.toleranceAmpstart.clear()
        self.toleranceAmptotal.clear()
        self.toleranceVolt.clear()


        

        self.amptotal_list = []
        self.volt_list = []

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
    


        # # Enable the button if all line edits have non-empty and different text, otherwise disable it
        # if (self.standardName.text()) != "" :
        #     self.fetchButton.setEnabled(True)
        # else:
        #    self.fetchButton.setEnabled(False)



        # Start a separate thread to fetch temperature data
        self.fetch_thread = None


        self.fetchButton.clicked.connect(self.start_fetching)
        self.stopButton.clicked.connect(self.stop_fetching)
        self.saveButton.clicked.connect(self.insert_standard)


        # Add a flag to indicate whether the fetching should be stopped
        self.stop_flag  = False














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
        standardname = str(self.standardName.text())
        port_input = str(self.comboPort.currentText())
        
        durationamperage_input = int(self.durationAmp.text())  # Uder-defined duration in seconds
        # intervalamperage_input = float(self.intervalAmp.text())  # User-defined interval in seconds
        amperageiterations = int(self.intervalAmp.text())  # User-defined interval in seconds
        durationtemp_input = int(self.durationTemp.text())
        intervaltemp_input = int(self.intervalTemp.text())
        model_input = str(self.modelDevice.text())
        brand_input = str(self.companyName.text())
        gas_input = str(self.modelGas.text())
        tolerance_temp1 = int(self.toleranceTemp1.value())
        tolerance_temp2 = int(self.toleranceTemp2.value())
        tolerance_temp3 = int(self.toleranceTemp3.value())
        tolerance_temp4 = int(self.toleranceTemp4.value())
        tolerance_temp5 = int(self.toleranceTemp5.value())
        tolerance_temp6 = int(self.toleranceTemp6.value())
        tolerance_temp7 = int(self.toleranceTemp7.value())
        tolerance_temp8 = int(self.toleranceTemp8.value())
        tolerance_amptotal = int(self.toleranceAmptotal.value())
        tolerance_ampstart = int(self.toleranceAmpstart.value())
        tolerance_volt = int(self.toleranceVolt.value())

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
        # try:
    
        
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

    

        # except Exception as e:
        #     # QMessageBox.critical(self.reusltLabel, "Error", f"An error occurred: {str(e)}")
        #     self.resultLabel.setText("Hello, World!")


        # Read the digital input value from the RS485 sensor
        # instrument.slaveaddress = 3
        register_address = 0
        input_value = instrument.read_bit(register_address, functioncode=1)

        #        Print the digital input value
        print("Digital Input Value:", input_value)

        
        # Calculate the number of iterations based on the duration and interval
        # amperageiterations = int(durationamperage_input / intervalamperage_input)
        intervalamperage_input = float(durationamperage_input/amperageiterations)
        
        instrumentamp = minimalmodbus.Instrument(port_input, slaveaddress=1)

        # Optionally, configure the serial communication parameters if needed


        

        self.ampstart_list = []
        self.volt_list = []


        end_timeAmp = time.perf_counter() + durationamperage_input


        # Fetch sensor amperage data for the specified duration and iterations
        while time.perf_counter() < end_timeAmp:
            # Fetch the amperage data from the RS485 device
            next_timeAmp = time.perf_counter() + intervalamperage_input
            if self.stop_flag:
                break




            if self.checkAmpstart.isChecked():
                ampstart = instrumentamp.read_float(registeraddress=32, functioncode=3)
                self.tableAverage.setItem(0, 9, QTableWidgetItem(f"{ampstart:.2f}A"))
                self.ampstart_list.append(ampstart)
                average_ampstart = sum(self.ampstart_list) / len(self.ampstart_list)
                self.tableAverage.setItem(1, 9, QTableWidgetItem(f"{average_ampstart:.2f}A"))
                print(f"ampstart at iteration {+1}: {ampstart:.2f}A")
                ampstart_stat = 1
            else:
                average_ampstart = 0
                ampstart_stat = 0

            
            if self.checkVolt.isChecked():
                volt = instrumentamp.read_float(registeraddress=26, functioncode=3)
                self.tableAverage.setItem(0, 10, QTableWidgetItem(f"{volt:.2f}V"))
                self.volt_list.append(volt)
                average_volt = sum(self.volt_list) / len(self.volt_list)
                self.tableAverage.setItem(1, 10, QTableWidgetItem(f"{average_volt:.2f}V"))
                print(f"volt at iteration {+1}: {volt:.2f}V")
                volt_stat = 1
            else:
                average_volt = 0
                volt_stat = 0

            
            

            

            # Wait for the specified interval before the next data fetch
            # time.sleep(intervalamperage_input)
            
            while time.perf_counter() < next_timeAmp:
                pass
        print(len(self.ampstart_list))
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
                sensor_stat1 = 1
            else:
                average_temperature1 = 0
                sensor_stat1 = 0

            
            if self.checkTemp2.isChecked():
                temperature2 = instrument.read_float(registeraddress=32, functioncode=3)
                self.tableAverage.setItem(0, 1, QTableWidgetItem(f"{temperature2:.2f}°C"))
                self.temperature2_list.append(temperature2)
                average_temperature2 = sum(self.temperature2_list) / len(self.temperature2_list)
                self.tableAverage.setItem(1, 1, QTableWidgetItem(f"{average_temperature2:.2f}°C"))
                print(f"Temperature2 at iteration : {temperature2:.2f}°C")
                sensor_stat2 = 1
            else:
                average_temperature2 = 0
                sensor_stat2 = 0

            
            if self.checkTemp3.isChecked():
                temperature3 = instrument.read_float(registeraddress=34, functioncode=3)
                self.tableAverage.setItem(0, 2, QTableWidgetItem(f"{temperature3:.2f}°C"))
                self.temperature3_list.append(temperature3)
                average_temperature3 = sum(self.temperature3_list) / len(self.temperature3_list)
                self.tableAverage.setItem(1, 2, QTableWidgetItem(f"{average_temperature3:.2f}°C"))
                print(f"Temperature3 at iteration : {temperature3:.2f}°C")
                sensor_stat3 = 1
            else:
                average_temperature3 = 0
                sensor_stat3 = 0

            
            if self.checkTemp4.isChecked():
                temperature4 = instrument.read_float(registeraddress=36, functioncode=3)
                self.tableAverage.setItem(0, 3, QTableWidgetItem(f"{temperature4:.2f}°C"))
                self.temperature4_list.append(temperature4)
                average_temperature4 = sum(self.temperature4_list) / len(self.temperature4_list)
                self.tableAverage.setItem(1, 3, QTableWidgetItem(f"{average_temperature4:.2f}°C"))
                print(f"Temperature4 at iteration : {temperature4:.2f}°C")
                sensor_stat4 = 1
            else:
                average_temperature4 = 0
                sensor_stat4 = 0

            
            if self.checkTemp5.isChecked():
                temperature5 = instrument.read_float(registeraddress=38, functioncode=3)
                self.tableAverage.setItem(0, 4, QTableWidgetItem(f"{temperature5:.2f}°C"))
                self.temperature5_list.append(temperature5)
                average_temperature5 = sum(self.temperature5_list) / len(self.temperature5_list)
                self.tableAverage.setItem(1, 4, QTableWidgetItem(f"{average_temperature5:.2f}°C"))
                print(f"Temperature5 at iteration : {temperature5:.2f}°C")
                sensor_stat5 = 1
            else:
                average_temperature5 = 0
                sensor_stat5 = 0

            
            if self.checkTemp6.isChecked():
                temperature6 = instrument.read_float(registeraddress=40, functioncode=3)
                self.tableAverage.setItem(0, 5, QTableWidgetItem(f"{temperature6:.2f}°C"))
                self.temperature6_list.append(temperature6)
                average_temperature6 = sum(self.temperature6_list) / len(self.temperature6_list)
                self.tableAverage.setItem(1, 5, QTableWidgetItem(f"{average_temperature6:.2f}°C"))
                print(f"Temperature6 at iteration : {temperature6:.2f}°C")
                sensor_stat6 = 1
            else:
                average_temperature6 = 0
                sensor_stat6 = 0

            
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
                sensor_stat7 = 1
            else:
                average_temperature7 = 0
                average_pressure_min = 0
                sensor_stat7 = 0

            
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
                sensor_stat8 = 1
            else:
                average_temperature8 = 0
                average_pressure_max = 0
                sensor_stat8 = 0


            if self.checkAmptotal.isChecked():
                amptotal = instrumentamp.read_float(registeraddress=32, functioncode=3)
                self.tableAverage.setItem(0, 8, QTableWidgetItem(f"{amptotal:.2f}A"))
                self.amptotal_list.append(amptotal)
                average_amptotal = sum(self.amptotal_list) / len(self.amptotal_list)
                self.tableAverage.setItem(1, 8, QTableWidgetItem(f"{average_amptotal:.2f}A"))
                print(f"amptotal at iteration : {amptotal:.2f}A")
                amptotal_stat = 1
            else:
                average_amptotal = 0
                amptotal_stat = 0

            self.tableAverage.viewport().update()

            

            # Wait for the specified interval before the next data fetch
            
            self.update_plots() 

            #Wait until the next interval
            
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


        # Prepare the data as a list of tuples
            self.data = [
                (standardname, model_input, brand_input, gas_input, durationtemp_input, intervaltemp_input, durationamperage_input, amperageiterations, tolerance_temp1, tolerance_temp2, tolerance_temp3, tolerance_temp4, tolerance_temp5, tolerance_temp6, tolerance_temp7, tolerance_temp8, tolerance_amptotal, tolerance_ampstart, tolerance_volt, sensor_stat1, sensor_stat2, sensor_stat3, sensor_stat4, sensor_stat5, sensor_stat6, sensor_stat7, sensor_stat8, ampstart_stat, amptotal_stat, volt_stat, average_temperature1, average_temperature2, average_temperature3, average_temperature4, average_temperature5,
                average_temperature6, average_pressure_min, average_pressure_max, average_ampstart, average_amptotal, average_volt, average_temperature7, average_temperature8)
                #for i in range(len(average_temperature1))
            ]



            

        self.stopButton.setEnabled(False)
        self.fetchButton.setEnabled(True)



        if self.stop_flag == False:
            self.saveButton.setEnabled(True)
    

        

        


        


        


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

        # Update plotvolt with volt data
        self.figure11.clear()
        ax11 = self.figure11.add_subplot(111)
        ax11.plot(self.amptotal_list)  # Use appropriate plot method based on your data
        ax11.set_title("Amp total")
        self.canvas11.draw()


    def database_info(self):
        return mysql.connector.connect(
            host="85.185.84.197",
            user="yekta",
            password="Yekta-5310",
            database="qc2"
        )



    def insert_standard(self):

        #Establish a connection to the MySQL database
        
        db_connection = self.database_info()




        # Create a cursor object to execute SQL queries
        cursor = db_connection.cursor()


        # Define the SQL query to insert data into the table
        insert_query = "INSERT INTO standard (standardname, model, brand, gas, testtime, intervaltemp, durationamperage, intervalamperage, tolerancetemp1, tolerancetemp2, tolerancetemp3, tolerancetemp4, tolerancetemp5, tolerancetemp6, tolerancepressuremin, tolerancepressuremax, toleranceampstart, toleranceamptotal, tolerancevolt, sensorstat1, sensorstat2, sensorstat3, sensorstat4, sensorstat5, sensorstat6, sensorstat7, sensorstat8, ampstartstat, amptotalstat, voltstat, averagetemperature1, averagetemperature2, averagetemperature3, averagetemperature4, averagetemperature5, averagetemperature6, averagepressure_min, averagepressure_max, averageampstart, averageamptotal, averagevolt, averagetemperature7, averagetemperature8) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # # Prepare the data as a list of tuples
        # self.data = [
        #     (standardname, durationtemp_input, intervaltemp_input, durationamperage_input, intervalamperage_input, tolerance_input, sensor_stat1, sensor_stat2, sensor_stat3, sensor_stat4, sensor_stat5, sensor_stat6, sensor_stat7, sensor_stat8, amp_stat, volt_stat, average_temperature1, average_temperature2, average_temperature3, average_temperature4, average_temperature5,
        #     average_temperature6, average_temperature7, average_temperature8, average_pressure_max, average_pressure_min)
        #     #for i in range(len(average_temperature1))
        # ]

        # Execute the SQL query to insert the data into the table
        cursor.executemany(insert_query, self.data)

        # Commit the changes to the database
        db_connection.commit()

        # Close the cursor and database connection
        cursor.close()
        db_connection.close()
        self.saveButton.setEnabled(False)





    # def showErrorMessage(self):
    #     print("dsdsad")




    ###################tab2###############################################################################################################################################################################################################
    #### define what happend after selevting item in dropdown
    def handle_dropdown_change(self, index):
        selected_option = self.comboStandard.currentText()
        self.standard_list = retrieve_standardparam(selected_option)
        
        self.standardName_2.setText(str(selected_option))
        self.modelDevice_2.setText(str(self.standard_list[2]))
        self.companyName_2.setText(str(self.standard_list[3]))
        self.gasType_2.setText(str(self.standard_list[4]))

        self.durationTemp_2.setText(str(self.standard_list[5]))
        self.intervalTemp_2.setText(str(self.standard_list[6]))
        self.durationAmp_2.setText(str(self.standard_list[7]))
        self.intervalAmp_2.setText(str(self.standard_list[8]))

        self.toleranceTemp1_2.setValue(int(self.standard_list[9]))
        self.toleranceTemp2_2.setValue(int(self.standard_list[10]))
        self.toleranceTemp3_2.setValue(int(self.standard_list[11]))
        self.toleranceTemp4_2.setValue(int(self.standard_list[12]))
        self.toleranceTemp5_2.setValue(int(self.standard_list[13]))
        self.toleranceTemp6_2.setValue(int(self.standard_list[14]))
        self.toleranceTemp7_2.setValue(int(self.standard_list[15]))
        self.toleranceTemp8_2.setValue(int(self.standard_list[16]))
        self.toleranceAmpstart_2.setValue(int(self.standard_list[17]))
        self.toleranceAmptotal_2.setValue(int(self.standard_list[18]))
        self.toleranceVolt_2.setValue(int(self.standard_list[19]))

        self.checkTemp1_2.setChecked(bool(self.standard_list[20]))
        self.checkTemp2_2.setChecked(bool(self.standard_list[21]))
        self.checkTemp3_2.setChecked(bool(self.standard_list[22]))
        self.checkTemp4_2.setChecked(bool(self.standard_list[23]))
        self.checkTemp5_2.setChecked(bool(self.standard_list[24]))
        self.checkTemp6_2.setChecked(bool(self.standard_list[25]))
        self.checkTemp7_2.setChecked(bool(self.standard_list[26]))
        self.checkTemp8_2.setChecked(bool(self.standard_list[27]))
        self.checkAmpstart_2.setChecked(bool(self.standard_list[28]))
        self.checkAmptotal_2.setChecked(bool(self.standard_list[29]))
        self.checkVolt_2.setChecked(bool(self.standard_list[30]))

        self.avgTemp1.setText(str(self.standard_list[31]))
        self.avgTemp2.setText(str(self.standard_list[32]))
        self.avgTemp3.setText(str(self.standard_list[33]))
        self.avgTemp4.setText(str(self.standard_list[34]))
        self.avgTemp5.setText(str(self.standard_list[35]))
        self.avgTemp6.setText(str(self.standard_list[36]))
        self.avgTemp7.setText(str(self.standard_list[37]))
        self.avgTemp8.setText(str(self.standard_list[38]))
        self.avgAmpstart.setText(str(self.standard_list[39]))
        self.avgAmptotal.setText(str(self.standard_list[40]))
        self.avgVolt.setText(str(self.standard_list[41]))


        print("Selected option:", self.standard_list)
        print(len(self.standard_list))
        self.deleteBtn.setEnabled(True)
        self.editBtn.setEnabled(True)



    def edit_standard(self):



        standard_name = self.comboStandard.currentText()

        newstandardname = str(self.standardName_2.text())
        newtolerancetemp1 = int(self.toleranceTemp1_2.value()) 
        newtolerancetemp2 = int(self.toleranceTemp2_2.value()) 
        newtolerancetemp3 = int(self.toleranceTemp3_2.value()) 
        newtolerancetemp4 = int(self.toleranceTemp4_2.value()) 
        newtolerancetemp5 = int(self.toleranceTemp5_2.value())
        newtolerancetemp6 = int(self.toleranceTemp6_2.value()) 
        newtolerancepressuremin = int(self.toleranceTemp7_2.value()) 
        newtolerancepressuremax = int(self.toleranceTemp8_2.value()) 
        newtoleranceampstart = int(self.toleranceAmpstart_2.value()) 
        newtoleranceamptotal = int(self.toleranceAmptotal_2.value()) 
        newtolerancevolt = int(self.toleranceVolt_2.value())
        avgtemp1 = float(self.avgTemp1.text()) 
        avgtemp2 = float(self.avgTemp2.text()) 
        avgtemp3 = float(self.avgTemp3.text()) 
        avgtemp4 = float(self.avgTemp4.text()) 
        avgtemp5 = float(self.avgTemp5.text()) 
        avgtemp6 = float(self.avgTemp6.text()) 
        avgtemp7 = float(self.avgTemp7.text()) 
        avgtemp8 = float(self.avgTemp8.text()) 
        avgampstart = float(self.avgAmpstart.text()) 
        avgamptotal = float(self.avgAmptotal.text()) 
        avgvolt = float(self.avgVolt.text())
        newdurationamperage = int(self.durationAmp_2.text())  # Uder-defined duration in seconds
        newamperageiterations = int(self.intervalAmp_2.text())  # User-defined interval in seconds
        newdurationtemp = int(self.durationTemp_2.text())
        newintervaltemp = int(self.intervalTemp_2.text())
        



        if self.checkTemp1_2.isChecked():
            newsensor_stat1 = 1
        else:
            newsensor_stat1 = 0

        if self.checkTemp2_2.isChecked():
            newsensor_stat2 = 1
        else:
            newsensor_stat2 = 0

        if self.checkTemp3_2.isChecked():
            newsensor_stat3 = 1
        else:
            newsensor_stat3 = 0

        if self.checkTemp4_2.isChecked():
            newsensor_stat4 = 1
        else:
            newsensor_stat4 = 0

        if self.checkTemp5_2.isChecked():
            newsensor_stat5 = 1
        else:
            newsensor_stat5 = 0

        if self.checkTemp6_2.isChecked():
            newsensor_stat6 = 1
        else:
            newsensor_stat6 = 0

        if self.checkTemp7_2.isChecked():
            newsensor_stat7 = 1
        else:
            newsensor_stat7 = 0

        if self.checkTemp8_2.isChecked():
            newsensor_stat8 = 1
        else:
            newsensor_stat8 = 0

        if self.checkAmpstart_2.isChecked():
            newampstart_stat = 1
        else:
            newampstart_stat = 0

        if self.checkAmptotal_2.isChecked():
            newamptotal_stat = 1
        else:
            newamptotal_stat = 0

        if self.checkVolt_2.isChecked():
            newvolt_stat = 1
        else:
            newvolt_stat = 0


        #Establish a connection to the MySQL database
        
        db_connection = self.database_info()




        # Create a cursor object to execute SQL queries
        cursor = db_connection.cursor()

        

        # Define the SQL query to insert data into the table
        edit_query = "INSERT INTO standard (standardname, testtime, intervaltemp, durationamperage, intervalamperage, sensorstat1, sensorstat2, sensorstat3, sensorstat4, sensorstat5, sensorstat6, sensorstat7, sensorstat8, ampstartstat, amptotalstat, voltstat, tolerancetemp1, tolerancetemp2, tolerancetemp3, tolerancetemp4, tolerancetemp5, tolerancetemp6, tolerancepressuremin, tolerancepressuremax, toleranceampstart, toleranceamptotal, tolerancevolt, averagetemperature1, averagetemperature2, averagetemperature3, averagetemperature4, averagetemperature5, averagetemperature6, averagepressure_min, averagepressure_max, averageampstart, averageamptotal, averagevolt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"



        # Execute the SQL query to insert the data into the table
        cursor.execute(edit_query, (newstandardname, newdurationtemp, newintervaltemp, newdurationamperage, newamperageiterations, newsensor_stat1, newsensor_stat2, newsensor_stat3, newsensor_stat4, newsensor_stat5, newsensor_stat6, newsensor_stat7, newsensor_stat8, newampstart_stat, newamptotal_stat, newvolt_stat, newtolerancetemp1, newtolerancetemp2, newtolerancetemp3, newtolerancetemp4, newtolerancetemp5, newtolerancetemp6, newtolerancepressuremin, newtolerancepressuremax, newtoleranceampstart, newtoleranceamptotal, newtolerancevolt, avgtemp1, avgtemp2, avgtemp3, avgtemp4,avgtemp5,avgtemp6,avgtemp7,avgtemp8, avgampstart, avgamptotal, avgvolt))

        # Commit the changes to the database
        db_connection.commit()

        # Close the cursor and database connection
        cursor.close()
        db_connection.close()

        self.editBtn.setEnabled(False)


    # def edit_standard(self):



    #     standard_name = self.comboStandard.currentText()

    #     newstandardname = str(self.standardName_2.text())
    #     # newtolerancepercent = int(self.tolerancePercent_2.value()) 



    #     if self.checkTemp1_2.isChecked():
    #         newsensor_stat1 = 1
    #     else:
    #         newsensor_stat1 = 0

    #     if self.checkTemp2_2.isChecked():
    #         newsensor_stat2 = 1
    #     else:
    #         newsensor_stat2 = 0

    #     if self.checkTemp3_2.isChecked():
    #         newsensor_stat3 = 1
    #     else:
    #         newsensor_stat3 = 0

    #     if self.checkTemp4_2.isChecked():
    #         newsensor_stat4 = 1
    #     else:
    #         newsensor_stat4 = 0

    #     if self.checkTemp5_2.isChecked():
    #         newsensor_stat5 = 1
    #     else:
    #         newsensor_stat5 = 0

    #     if self.checkTemp6_2.isChecked():
    #         newsensor_stat6 = 1
    #     else:
    #         newsensor_stat6 = 0

    #     if self.checkTemp7_2.isChecked():
    #         newsensor_stat7 = 1
    #     else:
    #         newsensor_stat7 = 0

    #     if self.checkTemp8_2.isChecked():
    #         newsensor_stat8 = 1
    #     else:
    #         newsensor_stat8 = 0

    #     if self.checkAmpstart_2.isChecked():
    #         newampstart_stat = 1
    #     else:
    #         newampstart_stat = 0

    #     if self.checkAmptotal_2.isChecked():
    #         newamptotal_stat = 1
    #     else:
    #         newamptotal_stat = 0

    #     if self.checkVolt_2.isChecked():
    #         newvolt_stat = 1
    #     else:
    #         newvolt_stat = 0


    #     #Establish a connection to the MySQL database
        
    #     db_connection = self.database_info()




    #     # Create a cursor object to execute SQL queries
    #     cursor = db_connection.cursor()

        

    #     # Define the SQL query to insert data into the table
    #     edit_query = "UPDATE standard SET standardname = %s, sensorstat1 = %s, sensorstat2 = %s, sensorstat3 = %s, sensorstat4 = %s, sensorstat5 = %s, sensorstat6 = %s, sensorstat7 = %s, sensorstat8 = %s, ampstartstat = %s, amptotalstat = %s, voltstat = %s WHERE standardname = %s"

    #     # # Prepare the data as a list of tuples
    #     # self.data = [
    #     #     (standardname, durationtemp_input, intervaltemp_input, durationamperage_input, intervalamperage_input, tolerance_input, sensor_stat1, sensor_stat2, sensor_stat3, sensor_stat4, sensor_stat5, sensor_stat6, sensor_stat7, sensor_stat8, amp_stat, volt_stat, average_temperature1, average_temperature2, average_temperature3, average_temperature4, average_temperature5,
    #     #     average_temperature6, average_temperature7, average_temperature8, average_pressure_max, average_pressure_min)
    #     #     #for i in range(len(average_temperature1))
    #     # ]

    #     # Execute the SQL query to insert the data into the table
    #     cursor.execute(edit_query, (newstandardname, newsensor_stat1, newsensor_stat2, newsensor_stat3, newsensor_stat4, newsensor_stat5, newsensor_stat6, newsensor_stat7, newsensor_stat8, newampstart_stat, newamptotal_stat, newvolt_stat, standard_name ))

    #     # Commit the changes to the database
    #     db_connection.commit()

    #     # Close the cursor and database connection
    #     cursor.close()
    #     db_connection.close()

    #     self.editBtn.setEnabled(False)






    def delete_standard(self):
        # Establish a connection to the MySQL server
        connection = self.database_info()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Define the value to match for deletion
        standard_name = self.comboStandard.currentText()

        # Prepare the SQL query with placeholders
        delete_query = "DELETE FROM standard WHERE standardname = %s"

        # Execute the query
        cursor.execute(delete_query, (standard_name,))

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()


        self.standardName_2.clear()
        self.durationTemp_2.clear()
        self.intervalTemp_2.clear()
        self.durationAmp_2.clear()
        self.intervalAmp_2.clear()
        self.modelDevice_2.clear()
        self.companyName_2.clear()
        self.gasType_2.clear()
        self.toleranceTemp1_2.clear()
        self.toleranceTemp2_2.clear()
        self.toleranceTemp3_2.clear()
        self.toleranceTemp4_2.clear()
        self.toleranceTemp5_2.clear()
        self.toleranceTemp6_2.clear()
        self.toleranceTemp7_2.clear()
        self.toleranceTemp8_2.clear()
        self.toleranceAmpstart_2.clear()
        self.toleranceAmptotal_2.clear()
        self.toleranceVolt_2.clear()
        self.checkTemp1_2.setChecked(False)
        self.checkTemp2_2.setChecked(False)
        self.checkTemp3_2.setChecked(False)
        self.checkTemp4_2.setChecked(False)
        self.checkTemp5_2.setChecked(False)
        self.checkTemp6_2.setChecked(False)
        self.checkTemp7_2.setChecked(False)
        self.checkTemp8_2.setChecked(False)
        self.checkAmpstart_2.setChecked(False)
        self.checkAmptotal_2.setChecked(False)
        self.checkVolt_2.setChecked(False)
        self.avgTemp1.clear()
        self.avgTemp2.clear()
        self.avgTemp3.clear()
        self.avgTemp4.clear()
        self.avgTemp5.clear()
        self.avgTemp6.clear()
        self.avgTemp7.clear()
        self.avgTemp8.clear()
        self.avgAmpstart.clear()
        self.avgAmptotal.clear()
        self.avgVolt.clear()

        self.deleteBtn.setEnabled(False)
        self.editBtn.setEnabled(False)

    

    



