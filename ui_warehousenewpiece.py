# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_warehousenewpiece.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WarehousePage(object):
    def setupUi(self, WarehousePage):
        WarehousePage.setObjectName("WarehousePage")
        WarehousePage.resize(1322, 854)
        self.centralwidget = QtWidgets.QWidget(WarehousePage)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setObjectName("tabWidget")
        self.warehouseIn = QtWidgets.QWidget()
        self.warehouseIn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.warehouseIn.setObjectName("warehouseIn")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.warehouseIn)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.warehouseIn)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_Properties = QtWidgets.QFrame(self.frame)
        self.input_Properties.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_Properties.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_Properties.setObjectName("input_Properties")
        self.gridLayout = QtWidgets.QGridLayout(self.input_Properties)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.addPartBtn = QtWidgets.QPushButton(self.input_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.addPartBtn.setFont(font)
        self.addPartBtn.setObjectName("addPartBtn")
        self.gridLayout.addWidget(self.addPartBtn, 2, 45, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.input_Properties)
        self.label_14.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_14.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 45, 1, 1)
        self.partCompany = QtWidgets.QLineEdit(self.input_Properties)
        self.partCompany.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partCompany.sizePolicy().hasHeightForWidth())
        self.partCompany.setSizePolicy(sizePolicy)
        self.partCompany.setMinimumSize(QtCore.QSize(150, 28))
        self.partCompany.setMaximumSize(QtCore.QSize(16777215, 28))
        self.partCompany.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.partCompany.setObjectName("partCompany")
        self.gridLayout.addWidget(self.partCompany, 2, 37, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.input_Properties)
        self.label_17.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_17.setFont(font)
        self.label_17.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_17.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 36, 1, 1)
        self.date = QtWidgets.QLineEdit(self.input_Properties)
        self.date.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date.sizePolicy().hasHeightForWidth())
        self.date.setSizePolicy(sizePolicy)
        self.date.setMinimumSize(QtCore.QSize(150, 28))
        self.date.setMaximumSize(QtCore.QSize(16777215, 28))
        self.date.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.date.setObjectName("date")
        self.gridLayout.addWidget(self.date, 2, 42, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.input_Properties)
        self.label_18.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_18.setFont(font)
        self.label_18.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_18.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 41, 1, 1)
        self.partCategory = QtWidgets.QLineEdit(self.input_Properties)
        self.partCategory.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partCategory.sizePolicy().hasHeightForWidth())
        self.partCategory.setSizePolicy(sizePolicy)
        self.partCategory.setMinimumSize(QtCore.QSize(150, 28))
        self.partCategory.setMaximumSize(QtCore.QSize(16777215, 28))
        self.partCategory.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.partCategory.setObjectName("partCategory")
        self.gridLayout.addWidget(self.partCategory, 0, 37, 1, 1)
        self.partSupplier = QtWidgets.QLineEdit(self.input_Properties)
        self.partSupplier.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partSupplier.sizePolicy().hasHeightForWidth())
        self.partSupplier.setSizePolicy(sizePolicy)
        self.partSupplier.setMinimumSize(QtCore.QSize(150, 28))
        self.partSupplier.setMaximumSize(QtCore.QSize(16777215, 28))
        self.partSupplier.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.partSupplier.setObjectName("partSupplier")
        self.gridLayout.addWidget(self.partSupplier, 0, 46, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.input_Properties)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 38, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.input_Properties)
        self.label_7.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 36, 1, 1)
        self.refreshWarehouse = QtWidgets.QPushButton(self.input_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.refreshWarehouse.setFont(font)
        self.refreshWarehouse.setObjectName("refreshWarehouse")
        self.gridLayout.addWidget(self.refreshWarehouse, 2, 46, 1, 1)
        self.partCountry = QtWidgets.QLineEdit(self.input_Properties)
        self.partCountry.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partCountry.sizePolicy().hasHeightForWidth())
        self.partCountry.setSizePolicy(sizePolicy)
        self.partCountry.setMinimumSize(QtCore.QSize(150, 28))
        self.partCountry.setMaximumSize(QtCore.QSize(16777215, 28))
        self.partCountry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.partCountry.setObjectName("partCountry")
        self.gridLayout.addWidget(self.partCountry, 2, 39, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.input_Properties)
        self.label_19.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_19.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 38, 1, 1)
        self.partSerial = QtWidgets.QLineEdit(self.input_Properties)
        self.partSerial.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partSerial.sizePolicy().hasHeightForWidth())
        self.partSerial.setSizePolicy(sizePolicy)
        self.partSerial.setMinimumSize(QtCore.QSize(150, 28))
        self.partSerial.setMaximumSize(QtCore.QSize(16777215, 28))
        self.partSerial.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.partSerial.setObjectName("partSerial")
        self.gridLayout.addWidget(self.partSerial, 0, 39, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.input_Properties)
        self.label_15.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_15.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 41, 1, 1)
        self.orderId = QtWidgets.QLineEdit(self.input_Properties)
        self.orderId.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orderId.sizePolicy().hasHeightForWidth())
        self.orderId.setSizePolicy(sizePolicy)
        self.orderId.setMinimumSize(QtCore.QSize(150, 28))
        self.orderId.setMaximumSize(QtCore.QSize(16777215, 28))
        self.orderId.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.orderId.setObjectName("orderId")
        self.gridLayout.addWidget(self.orderId, 0, 42, 1, 1)
        self.verticalLayout_2.addWidget(self.input_Properties, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.inputPartTable = QtWidgets.QFrame(self.frame)
        self.inputPartTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inputPartTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputPartTable.setObjectName("inputPartTable")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.inputPartTable)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.inputPartTable)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_2.addWidget(self.inputPartTable)
        self.horizontalLayout.addWidget(self.frame)
        self.tabWidget.addTab(self.warehouseIn, "")
        self.warehouseOut = QtWidgets.QWidget()
        self.warehouseOut.setObjectName("warehouseOut")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.warehouseOut)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.warehouseOut)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.output_Properties = QtWidgets.QFrame(self.frame_3)
        self.output_Properties.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output_Properties.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_Properties.setObjectName("output_Properties")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.output_Properties)
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_20 = QtWidgets.QLabel(self.output_Properties)
        self.label_20.setMinimumSize(QtCore.QSize(0, 0))
        self.label_20.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_20.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_4.addWidget(self.label_20)
        self.exitPartSerial = QtWidgets.QLineEdit(self.output_Properties)
        self.exitPartSerial.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitPartSerial.sizePolicy().hasHeightForWidth())
        self.exitPartSerial.setSizePolicy(sizePolicy)
        self.exitPartSerial.setMinimumSize(QtCore.QSize(200, 28))
        self.exitPartSerial.setMaximumSize(QtCore.QSize(16777215, 28))
        self.exitPartSerial.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.exitPartSerial.setObjectName("exitPartSerial")
        self.horizontalLayout_4.addWidget(self.exitPartSerial)
        self.label = QtWidgets.QLabel(self.output_Properties)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.exitPartName = QtWidgets.QLabel(self.output_Properties)
        self.exitPartName.setMinimumSize(QtCore.QSize(200, 28))
        self.exitPartName.setMaximumSize(QtCore.QSize(200, 28))
        self.exitPartName.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")
        self.exitPartName.setText("")
        self.exitPartName.setObjectName("exitPartName")
        self.horizontalLayout_4.addWidget(self.exitPartName)
        self.exitPartBtn = QtWidgets.QPushButton(self.output_Properties)
        self.exitPartBtn.setMinimumSize(QtCore.QSize(150, 0))
        self.exitPartBtn.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.exitPartBtn.setFont(font)
        self.exitPartBtn.setObjectName("exitPartBtn")
        self.horizontalLayout_4.addWidget(self.exitPartBtn)
        self.refreshDailyWarehouse = QtWidgets.QPushButton(self.output_Properties)
        self.refreshDailyWarehouse.setObjectName("refreshDailyWarehouse")
        self.horizontalLayout_4.addWidget(self.refreshDailyWarehouse)
        self.verticalLayout_3.addWidget(self.output_Properties, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.outputPartTable = QtWidgets.QFrame(self.frame_3)
        self.outputPartTable.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.outputPartTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outputPartTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputPartTable.setObjectName("outputPartTable")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.outputPartTable)
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.outputPartTable)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(10)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        self.horizontalLayout_5.addWidget(self.tableWidget_2)
        self.verticalLayout_3.addWidget(self.outputPartTable)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.tabWidget.addTab(self.warehouseOut, "")
        self.verticalLayout.addWidget(self.tabWidget)
        WarehousePage.setCentralWidget(self.centralwidget)

        self.retranslateUi(WarehousePage)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WarehousePage)
        WarehousePage.setTabOrder(self.partCategory, self.partSerial)
        WarehousePage.setTabOrder(self.partSerial, self.orderId)
        WarehousePage.setTabOrder(self.orderId, self.partSupplier)
        WarehousePage.setTabOrder(self.partSupplier, self.partCompany)
        WarehousePage.setTabOrder(self.partCompany, self.partCountry)
        WarehousePage.setTabOrder(self.partCountry, self.date)
        WarehousePage.setTabOrder(self.date, self.addPartBtn)
        WarehousePage.setTabOrder(self.addPartBtn, self.refreshWarehouse)
        WarehousePage.setTabOrder(self.refreshWarehouse, self.tableWidget)
        WarehousePage.setTabOrder(self.tableWidget, self.tabWidget)
        WarehousePage.setTabOrder(self.tabWidget, self.exitPartSerial)
        WarehousePage.setTabOrder(self.exitPartSerial, self.exitPartBtn)
        WarehousePage.setTabOrder(self.exitPartBtn, self.refreshDailyWarehouse)
        WarehousePage.setTabOrder(self.refreshDailyWarehouse, self.tableWidget_2)

    def retranslateUi(self, WarehousePage):
        _translate = QtCore.QCoreApplication.translate
        WarehousePage.setWindowTitle(_translate("WarehousePage", "MainWindow"))
        self.addPartBtn.setText(_translate("WarehousePage", "ثبت قطعه"))
        self.label_14.setText(_translate("WarehousePage", "سوپلایر"))
        self.label_17.setText(_translate("WarehousePage", "دسته بندی قطعه"))
        self.label_18.setText(_translate("WarehousePage", "تاریخ سفارش"))
        self.label_6.setText(_translate("WarehousePage", "کشور سازنده"))
        self.label_7.setText(_translate("WarehousePage", "شرکت سازنده"))
        self.refreshWarehouse.setText(_translate("WarehousePage", "بروز رسانی لیست"))
        self.label_19.setText(_translate("WarehousePage", "سریال"))
        self.label_15.setText(_translate("WarehousePage", "شماره سفارش"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("WarehousePage", "حذف قطعه"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("WarehousePage", "تاریخ سفارش"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("WarehousePage", "دسته بندی"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("WarehousePage", "سریال"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("WarehousePage", "شماره سفارش"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("WarehousePage", "سوپلایر"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("WarehousePage", "شرکت سازنده"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("WarehousePage", "کشور سازنده"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("WarehousePage", "اپراتور ثبت کننده"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("WarehousePage", "تاریخ ثبت"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.warehouseIn), _translate("WarehousePage", "ورود به انبار"))
        self.label_20.setText(_translate("WarehousePage", "سریال"))
        self.label.setText(_translate("WarehousePage", "نوع قطعه"))
        self.exitPartBtn.setText(_translate("WarehousePage", "خروج از انبار"))
        self.refreshDailyWarehouse.setText(_translate("WarehousePage", "بروز رسانی لیست"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("WarehousePage", "حذف قطعه"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("WarehousePage", "تاریخ سفارش"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("WarehousePage", "دسته بندی"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("WarehousePage", "سریال"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("WarehousePage", "شماره سفارش"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("WarehousePage", "سوپلایر"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("WarehousePage", "شرکت سازنده"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("WarehousePage", "کشور سازنده"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("WarehousePage", "اپراتور ثبت کننده"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("WarehousePage", "تاریخ ثبت"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.warehouseOut), _translate("WarehousePage", "خروج از انبار"))
