from PyQt5.QtWidgets import *
from ui_warehousenewpiece import Ui_WarehousePage
from PyQt5.QtCore import QMetaObject, Qt, QModelIndex
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import mysql.connector

import jdatetime

# Get the current Jalali date and time
current_jdatetime = jdatetime.datetime.now()



class WarehousePage(QMainWindow, Ui_WarehousePage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Add your compute logic for the report page here
        
        self.addPartBtn.clicked.connect(self.savetoDB)
        # self.exitPartBtn.clicked.connect(self.move_record)
        # self.exitPartSerial.editingFinished.connect(self.on_text_changed)
        self.refreshWarehouse.clicked.connect(self.load_data)
        # self.refreshDailyWarehouse.clicked.connect(self.load_datadaily)


    def savetoDB(self):
        partcategory = str(self.partCategory.text())
        partserial = str(self.partSerial.text())
        partorderId = str(self.orderId.text())
        partsupplier = str(self.partSupplier.text())
        partcompany = str(self.partCompany.text())
        partcountry = str(self.partCountry.text())
        orderdate = str(self.date.text())
        operator = "101"
        currentdate = str(jdatetime.datetime.now())

        self.warehousedata = [
            (orderdate, partcategory, partserial, partorderId, partsupplier, partcompany, partcountry, operator, currentdate)
            ]
        self.addWarehouse()
        self.load_data()




    def database_info(self):
        return mysql.connector.connect(
            host="192.168.100.201",
            user="yekta",
            password="Yekta-5310",
            database="qc2"
        )




    def addWarehouse(self):

        #Establish a connection to the MySQL database
        
        db_connection = self.database_info()




        # Create a cursor object to execute SQL queries
        cursor = db_connection.cursor()


        # Define the SQL query to insert data into the table
        insert_part = "INSERT INTO dailywarehouse (orderdate, category, serial, ordernum, supplier, company, country, operator, currentdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    
        

        # Execute the SQL query to insert the data into the table
        cursor.executemany(insert_part, self.warehousedata)

        # Commit the changes to the database
        db_connection.commit()

        # Close the cursor and database connection
        cursor.close()
        db_connection.close()



    def load_data(self):
        # Connect to the MySQL database
        connection = self.database_info()

        cursor = connection.cursor()

        # Fetch data from the database
        cursor.execute("SELECT * FROM dailywarehouse")
        data = cursor.fetchall()

        # Populate the QTableWidget
        self.tableWidget.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, cell_data in enumerate(row_data):
                if col_index == 0:  # Create delete button in the last column
                    delete_button = QPushButton("Delete")
                    delete_button.clicked.connect(lambda _, r=row_data[0]: self.delete_record(connection, r))
                    self.tableWidget.setCellWidget(row_index, col_index, delete_button)
                else:
                    item = QTableWidgetItem(str(cell_data))
                    self.tableWidget.setItem(row_index, col_index, item)

        # Close the database connection
        cursor.close()
        connection.close()

    def delete_record(self, connection, record_id):
        connection = self.database_info()

        cursor = connection.cursor()

        # Delete the record with the specified ID
        cursor.execute("DELETE FROM dailywarehouse WHERE id=%s", (record_id,))
        connection.commit()

        # Reload data after deletion
        self.load_data()

        # Close the cursor (not the connection)
        cursor.close()




######################################tab exit################################

    # def load_datadaily(self):
    #     # Connect to the MySQL database
    #     connection =self.database_info()

    #     cursor = connection.cursor()

    #     # Fetch data from the database
    #     cursor.execute("SELECT * FROM dailywarehouse")
    #     data = cursor.fetchall()

    #     # Populate the QTableWidget
    #     self.tableWidget_2.setRowCount(len(data))
    #     for row_index, row_data in enumerate(data):
    #         for col_index, cell_data in enumerate(row_data):
    #             if col_index == 0:  # Create delete button in the last column
    #                 delete_button = QPushButton("Delete")
    #                 delete_button.clicked.connect(lambda _, r=row_data[0]: self.delete_recorddaily(connection, r))
    #                 self.tableWidget_2.setCellWidget(row_index, col_index, delete_button)
    #             else:
    #                 item = QTableWidgetItem(str(cell_data))
    #                 self.tableWidget_2.setItem(row_index, col_index, item)

    #     # Close the database connection
    #     cursor.close()
    #     connection.close()

    # def delete_recorddaily(self, connection, record_id):
    #     connection = self.database_info()

    #     cursor = connection.cursor()

    #     # Delete the record with the specified ID
    #     cursor.execute("DELETE FROM dailywarehouse WHERE id=%s", (record_id,))
    #     connection.commit()

    #     # Reload data after deletion
    #     self.load_datadaily()

    #     # Close the cursor (not the connection)
    #     cursor.close()






             
    # def on_text_changed(self):
    #     serial = self.exitPartSerial.text().strip()  # Get rid of any leading/trailing spaces
    #     db_connection = self.database_info()

    #     cursor = db_connection.cursor()
    #     query = "SELECT category FROM warehouse WHERE serial = %s"
        
    #     cursor.execute(query, (serial,))
    #     result = cursor.fetchone()
    #     self.exitPartName.setText(str(result))
    #     print("Text changed:", serial)
    #     # Your custom code here




    # def move_record(self):
    #     try:
    #         # Connect to the MySQL database
    #         db_connection = self.database_info()

    #         # Create a cursor
    #         cursor = db_connection.cursor()

    #         # Specify the row number to move
    #         serial = self.exitPartSerial.text().strip()

    #         # Move the row from table1 to table2
    #         query_move = f"INSERT INTO dailywarehouse SELECT * FROM warehouse WHERE serial = '{serial}'"
    #         cursor.execute(query_move)
    #         db_connection.commit()

    #         # Delete the row from table1
    #         query_delete = f"DELETE FROM warehouse WHERE serial = '{serial}'"
    #         cursor.execute(query_delete)
    #         db_connection.commit()

    #         # Close the cursor and connection
    #         cursor.close()
    #         db_connection.close()
    #         self.load_datadaily()

    #     except mysql.connector.Error as err:
    #         print("Error:", err)









