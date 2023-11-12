import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

import mysql.connector

from ui_main import Ui_MainWindow


from newtest import NewTestPage
from newstandard import NewStandardPage
from report import ReportPage
from warehouse import WarehousePage
from setting import SettingPage
from login import LoginDialog
from assembly import AssemblyPage
from classes.Auth import Auth


# from logout import LogoutPage






def create_tables():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="yekta",
        password="Yekta-5310",
        database="qc2"
        )
    cursor = connection.cursor()

    # Define your SQL statements to create the tables


    create_table_standard = '''
        CREATE TABLE IF NOT EXISTS standard (
            id INT AUTO_INCREMENT PRIMARY KEY,
            standardname VARCHAR(50),
            model VARCHAR(50),
            brand VARCHAR(50),
            gas VARCHAR(50),
            testtime INT,
            intervaltemp INT,
            durationamperage INT,
            intervalamperage INT,
            tolerancetemp1 INT,
            tolerancetemp2 INT,
            tolerancetemp3 INT,
            tolerancetemp4 INT,
            tolerancetemp5 INT,
            tolerancetemp6 INT,
            tolerancepressuremin INT,
            tolerancepressuremax INT,
            toleranceampstart INT,
            toleranceamptotal INT,
            tolerancevolt INT,
            sensorstat1 TINYINT(1),
            sensorstat2 TINYINT(1),
            sensorstat3 TINYINT(1),
            sensorstat4 TINYINT(1),
            sensorstat5 TINYINT(1),
            sensorstat6 TINYINT(1),
            sensorstat7 TINYINT(1),
            sensorstat8 TINYINT(1),
            ampstartstat TINYINT(1),
            amptotalstat TINYINT(1),
            voltstat TINYINT(1),
            averagetemperature1 FLOAT(10, 2),
            averagetemperature2 FLOAT(10, 2),
            averagetemperature3 FLOAT(10, 2),
            averagetemperature4 FLOAT(10, 2),
            averagetemperature5 FLOAT(10, 2),
            averagetemperature6 FLOAT(10, 2),
            averagepressure_min FLOAT(10, 2),
            averagepressure_max FLOAT(10, 2),
            averageampstart FLOAT(10, 2),
            averageamptotal FLOAT(10, 2),
            averagevolt FLOAT(10, 2),
            averagetemperature7 FLOAT(10, 2),
            averagetemperature8 FLOAT(10, 2)

        )
    '''



    # table1_sql = "CREATE TABLE IF NOT EXISTS table1 (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50))"
    # table2_sql = "CREATE TABLE IF NOT EXISTS table2 (id INT PRIMARY KEY AUTO_INCREMENT, age INT)"

    # Execute the SQL statements
    cursor.execute(create_table_standard)
    # cursor.execute(table2_sql)

    # Commit the changes and close the cursor and connection
    connection.commit()
    cursor.close()
    connection.close()






class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.test = NewTestPage()
        self.report = ReportPage()
        self.newstandard = NewStandardPage()
        self.warehouse = WarehousePage()
        self.setting = SettingPage()
        self.assembly = AssemblyPage()
        
        self.ui.Stacked_Pages.addWidget(self.test)
        self.ui.Stacked_Pages.addWidget(self.report)
        self.ui.Stacked_Pages.addWidget(self.newstandard)
        self.ui.Stacked_Pages.addWidget(self.warehouse)
        self.ui.Stacked_Pages.addWidget(self.setting)
        self.ui.Stacked_Pages.addWidget(self.assembly)

        # newTestIcon = QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons/newTest.svg"))
        # standardsIcon = QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons/standards.svg"))
        # reportsIcon = QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons/reports.svg"))
        # warehouseIcon = QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons/warehouse.svg"))
        # settingsIcon = QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons/settings.svg"))
        # helpIcon = QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons/help.svg"))
        # logoutIcon = QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons/logout.svg"))
        # menuOpenIcon = QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons/menuOpen.svg"))
        # menuCloseIcon = QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons/menuClose.svg"))
        LogoIcon = QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons/logo.png"))


        self.ui.Logo.setIcon(LogoIcon)



        self.login_dialog = LoginDialog()
        if self.login_dialog.exec_() == LoginDialog.Accepted:
            self.show()
        else:
            sys.exit(0)


        # #self.ui.Menu_btn.setIcon(menuOpenIcon)
        # self.ui.Menu_Btn_Text.setIcon(menuOpenIcon)

        # self.ui.Test_Btn.setIcon(newTestIcon)
        # self.ui.Test_Btn_Text.setIcon(newTestIcon)
        
        # self.ui.Standards_Btn.setIcon(standardsIcon)
        # self.ui.Standards_Btn_Text.setIcon(standardsIcon)
        
        # self.ui.Reports_Btn.setIcon(reportsIcon)
        # self.ui.Reporst_Btn_Text.setIcon(reportsIcon)
        
        # self.ui.Warehouse_Btn.setIcon(warehouseIcon)
        # self.ui.Warehouse_Btn_Text.setIcon(warehouseIcon)
        
        # self.ui.Settings_Btn.setIcon(settingsIcon)
        # self.ui.Settings_Btn_Text.setIcon(settingsIcon)
        
        # self.ui.Help_Btn.setIcon(helpIcon)
        # self.ui.Help_Btn_Text.setIcon(helpIcon)
        
        # self.ui.Logout_Btn.setIcon(logoutIcon)
        # self.ui.Logout_Btn_Text.setIcon(logoutIcon)
        



        # self.ui.Test_Btn.clicked.connect(self.show_test)
        self.ui.Test_Btn_Text.clicked.connect(self.show_test)

        # self.ui.Standards_Btn.clicked.connect(self.show_standard)
        self.ui.Standards_Btn_Text.clicked.connect(self.show_standard)
        
        # self.ui.Reports_Btn.clicked.connect(self.show_test)
        self.ui.Reporst_Btn_Text.clicked.connect(self.show_report)

        # self.ui.Warehouse_Btn.clicked.connect(self.show_report)
        self.ui.Warehouse_Btn_Text.clicked.connect(self.show_warehouse)
        
        # self.ui.Settings_Btn.clicked.connect(self.show_test)
        self.ui.Settings_Btn_Text.clicked.connect(self.show_setting)



        # self.ui.Pack_Btn.clicked.connect(self.show_report)
        self.ui.Pack_Btn_Text.clicked.connect(self.show_assembly)

        # self.ui.Logout_Btn.clicked.connect(sys.exit)
        self.ui.Logout_Btn_Text.clicked.connect(sys.exit)



        
    def show_test(self):
        if Auth().has_permission('ثبت دستگاه'):
            self.ui.Stacked_Pages.setCurrentWidget(self.test)
            self.ui.menuTitle.setText("تست دستگاه")
        
    def show_report(self):
        if Auth().has_permission('گزارش ها'):
        
            self.ui.Stacked_Pages.setCurrentWidget(self.report)
            self.ui.menuTitle.setText("گزارش ها")

    def show_warehouse(self):
        if Auth().has_permission('انبار اصلی'):
            
            self.ui.Stacked_Pages.setCurrentWidget(self.warehouse)
            self.ui.menuTitle.setText("انبار اصلی")

    def show_standard(self):
        if Auth().has_permission('استاندارد'):
            
            self.ui.Stacked_Pages.setCurrentWidget(self.newstandard)
            self.ui.menuTitle.setText(" استاندارد ")
        

    def show_setting(self):
        if Auth().has_permission('تنظیمات'):
            
            self.ui.Stacked_Pages.setCurrentWidget(self.setting)
            self.ui.menuTitle.setText(" تنظیمات ")


    def show_assembly(self):
        if Auth().has_permission('ایجاد بسته'):
            
            self.ui.Stacked_Pages.setCurrentWidget(self.assembly)
            self.ui.menuTitle.setText(" ایجاد بسته ")
        





if __name__ == '__main__':
    create_tables()
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
