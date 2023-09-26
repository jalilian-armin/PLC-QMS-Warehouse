from PyQt5.QtWidgets import *
from ui_packegeassembly import Ui_AssemblyPage
from PyQt5.QtCore import QMetaObject, Qt, QModelIndex
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import mysql.connector

import random
from jdatetime import datetime as jdatetime




class AssemblyPage(QMainWindow, Ui_AssemblyPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


     
        # Connect the editingFinished signals to the common function for all inputs
        self.packageSerial1.editingFinished.connect(self.on_text_changed)
        self.packageSerial2.editingFinished.connect(self.on_text_changed)
        self.packageSerial3.editingFinished.connect(self.on_text_changed)
        self.packageSerial4.editingFinished.connect(self.on_text_changed)
        self.packageSerial5.editingFinished.connect(self.on_text_changed)
        self.packageSerial6.editingFinished.connect(self.on_text_changed)
        self.packageSerial7.editingFinished.connect(self.on_text_changed)
        self.packageSerial8.editingFinished.connect(self.on_text_changed)
        self.packageSerial9.editingFinished.connect(self.on_text_changed)
        self.packageSerial10.editingFinished.connect(self.on_text_changed)
        # Connect more serial number inputs as needed
        
        self.assembleBtn.setEnabled(False)
        self.assembleBtn.clicked.connect(self.assemble_package)
        self.refreshPackageDB.clicked.connect(self.load_data)

    def on_text_changed(self):
        # Get the sender object that triggered the signal
        sender = self.sender()

        # Extract the serial number from the sender's text
        serial = sender.text().strip()

        # Establish the database connection
        db_connection = mysql.connector.connect(
            host="85.185.84.197",
            user="yekta",
            password="Yekta-5310",
            database="qc2"
        )

        # Prepare and execute the database query
        cursor = db_connection.cursor()
        query = "SELECT category FROM dailywarehouse WHERE serial = %s"
        cursor.execute(query, (serial,))
        result = cursor.fetchone()



        # Update the corresponding part category widget
        if sender == self.packageSerial1:
            self.partCategory1.setText(str(result))
        elif sender == self.packageSerial2:
            self.partCategory2.setText(str(result))
        elif sender == self.packageSerial3:
            self.partCategory3.setText(str(result))
        elif sender == self.packageSerial4:
            self.partCategory4.setText(str(result))
        elif sender == self.packageSerial5:
            self.partCategory5.setText(str(result))
        elif sender == self.packageSerial6:
            self.partCategory6.setText(str(result))
        elif sender == self.packageSerial7:
            self.partCategory7.setText(str(result))
        elif sender == self.packageSerial8:
            self.partCategory8.setText(str(result))
        elif sender == self.packageSerial9:
            self.partCategory9.setText(str(result))
        elif sender == self.packageSerial10:
            self.partCategory10.setText(str(result))
        # Add more conditions for additional serial number inputs

        all_results_none = any(res == "None" for res in [self.partCategory1.text(), self.partCategory2.text(), self.partCategory3.text(), self.partCategory4.text(), self.partCategory5.text(), self.partCategory6.text(), self.partCategory7.text(), self.partCategory8.text(), self.partCategory9.text(), self.partCategory10.text()])

        if all_results_none:
        # Execute function when all results are not None
           self.assembleBtn.setEnabled(False)
        else:
            self.assembleBtn.setEnabled(True)

        # Clean up
        cursor.close()
        db_connection.close()
        print(all_results_none)
        print("Text changed:", serial)
        print("Text changed:", self.partCategory1.text())
        # Your custom code here



    def load_data(self):
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="85.185.84.197",
            user="yekta",
            password="Yekta-5310",
            database="qc2"
        )
        cursor = connection.cursor()

        # Fetch data from the database
        cursor.execute("SELECT * FROM package")
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
        connection = mysql.connector.connect(
            host="85.185.84.197",
            user="yekta",
            password="Yekta-5310",
            database="qc2"
        )
        cursor = connection.cursor()

        # Delete the record with the specified ID
        cursor.execute("DELETE FROM package WHERE id=%s", (record_id,))
        connection.commit()

        # Reload data after deletion
        self.load_data()

        # Close the cursor (not the connection)
        cursor.close()

    def barcode_generate(self):
                # Get the current Jalali date
        current_jdate = jdatetime.now()

        # Format the Jalali date as "yyyymmdd"
        jalali_date_str = current_jdate.strftime('%Y%m%d')

        # Generate a random 10-digit number
        random_number = random.randint(0, 55555)

        # Combine the Jalali date and random number to create a 13-digit number
        thirteen_digit_number = int(jalali_date_str + str(random_number).zfill(5))

        self.tempBarcode.setText(str(thirteen_digit_number))
        return thirteen_digit_number


    def assemble_package(self):
        tempbarcode = self.barcode_generate()
        operator = "101"
        name = self.packageName.text()
        currentdate = str(jdatetime.now())
        part1=self.packageSerial1.text()
        part2=self.packageSerial2.text()
        part3=self.packageSerial3.text()
        part4=self.packageSerial4.text()
        part5=self.packageSerial5.text()
        part6=self.packageSerial6.text()
        part7=self.packageSerial7.text()
        part8=self.packageSerial8.text()
        part9=self.packageSerial9.text()
        part10=self.packageSerial10.text()

        data =[(name, tempbarcode, part1,part2,part3,part4,part5,part6,part7,part8,part9,part10,operator,currentdate)]


        #Establish a connection to the MySQL database
        
        db_connection = mysql.connector.connect(
            host="85.185.84.197",
            user="yekta",
            password="Yekta-5310",
            database="qc2"
            
        )




        # Create a cursor object to execute SQL queries
        cursor = db_connection.cursor()


        # Define the SQL query to insert data into the table
        insert_package = "INSERT INTO package (name, tempbarcode, part1, part2, part3, part4, part5, part6, part7, part8, part9, part10, operator, currentdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    
        

        # Execute the SQL query to insert the data into the table
        cursor.executemany(insert_package, data)

        # Commit the changes to the database
        db_connection.commit()

        # Close the cursor and database connection
        cursor.close()
        db_connection.close()
        self.load_data()
        self.move_record()



    def move_record(self):
        try:
            # Connect to the MySQL database
            db_connection = mysql.connector.connect(
            host="85.185.84.197",
            user="yekta",
            password="Yekta-5310",
            database="qc2"
        )

            # Create a cursor
            cursor = db_connection.cursor()

            # Specify the list of package serials to move
            serials_to_move = [
                self.packageSerial1.text().strip(),
                self.packageSerial2.text().strip(),
                self.packageSerial3.text().strip(),
                self.packageSerial4.text().strip(),
                self.packageSerial5.text().strip(),
                self.packageSerial6.text().strip(),
                self.packageSerial7.text().strip(),
                self.packageSerial8.text().strip(),
                self.packageSerial9.text().strip(),
                self.packageSerial10.text().strip(),
                # Add more self.packageserial variables here
            ]

            for serial in serials_to_move:
                # Move the row from table1 to table2
                query_move = f"INSERT INTO usedparts SELECT * FROM dailywarehouse WHERE serial = '{serial}'"
                cursor.execute(query_move)
                db_connection.commit()

                # Delete the row from table1
                query_delete = f"DELETE FROM dailywarehouse WHERE serial = '{serial}'"
                cursor.execute(query_delete)
                db_connection.commit()

            # Close the cursor and connection
            cursor.close()
            db_connection.close()
            self.assembleBtn.setEnabled(False)
        

        except mysql.connector.Error as err:
            print("Error:", err)










        
