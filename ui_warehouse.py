# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_warehouse.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WarehousePage(object):
    def setupUi(self, WarehousePage):
        WarehousePage.setObjectName("WarehousePage")
        WarehousePage.resize(1196, 854)
        self.centralwidget = QtWidgets.QWidget(WarehousePage)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Test_Properties = QtWidgets.QFrame(self.centralwidget)
        self.Test_Properties.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Test_Properties.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Test_Properties.setObjectName("Test_Properties")
        self.gridLayout = QtWidgets.QGridLayout(self.Test_Properties)
        self.gridLayout.setObjectName("gridLayout")
        self.label_18 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_18.setFont(font)
        self.label_18.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_18.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 1, 39, 1, 1)
        self.partSupplier = QtWidgets.QLineEdit(self.Test_Properties)
        self.partSupplier.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partSupplier.sizePolicy().hasHeightForWidth())
        self.partSupplier.setSizePolicy(sizePolicy)
        self.partSupplier.setMinimumSize(QtCore.QSize(0, 20))
        self.partSupplier.setMaximumSize(QtCore.QSize(16777215, 20))
        self.partSupplier.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.partSupplier.setObjectName("partSupplier")
        self.gridLayout.addWidget(self.partSupplier, 0, 36, 1, 1)
        self.partSerial = QtWidgets.QLineEdit(self.Test_Properties)
        self.partSerial.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partSerial.sizePolicy().hasHeightForWidth())
        self.partSerial.setSizePolicy(sizePolicy)
        self.partSerial.setMinimumSize(QtCore.QSize(0, 20))
        self.partSerial.setMaximumSize(QtCore.QSize(16777215, 20))
        self.partSerial.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.partSerial.setObjectName("partSerial")
        self.gridLayout.addWidget(self.partSerial, 0, 40, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_19.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 41, 1, 1)
        self.addPartBtn = QtWidgets.QPushButton(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.addPartBtn.setFont(font)
        self.addPartBtn.setObjectName("addPartBtn")
        self.gridLayout.addWidget(self.addPartBtn, 1, 36, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 43, 1, 1)
        self.orderId = QtWidgets.QLineEdit(self.Test_Properties)
        self.orderId.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orderId.sizePolicy().hasHeightForWidth())
        self.orderId.setSizePolicy(sizePolicy)
        self.orderId.setMinimumSize(QtCore.QSize(0, 20))
        self.orderId.setMaximumSize(QtCore.QSize(16777215, 20))
        self.orderId.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.orderId.setObjectName("orderId")
        self.gridLayout.addWidget(self.orderId, 0, 38, 1, 1)
        self.date = QtWidgets.QLineEdit(self.Test_Properties)
        self.date.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date.sizePolicy().hasHeightForWidth())
        self.date.setSizePolicy(sizePolicy)
        self.date.setMinimumSize(QtCore.QSize(0, 20))
        self.date.setMaximumSize(QtCore.QSize(16777215, 20))
        self.date.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.date.setObjectName("date")
        self.gridLayout.addWidget(self.date, 1, 38, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_17.setFont(font)
        self.label_17.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_17.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 43, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_14.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 37, 1, 1)
        self.partCountry = QtWidgets.QLineEdit(self.Test_Properties)
        self.partCountry.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partCountry.sizePolicy().hasHeightForWidth())
        self.partCountry.setSizePolicy(sizePolicy)
        self.partCountry.setMinimumSize(QtCore.QSize(0, 20))
        self.partCountry.setMaximumSize(QtCore.QSize(16777215, 20))
        self.partCountry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.partCountry.setObjectName("partCountry")
        self.gridLayout.addWidget(self.partCountry, 1, 40, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_15.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 39, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 41, 1, 1)
        self.parCategory = QtWidgets.QLineEdit(self.Test_Properties)
        self.parCategory.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parCategory.sizePolicy().hasHeightForWidth())
        self.parCategory.setSizePolicy(sizePolicy)
        self.parCategory.setMinimumSize(QtCore.QSize(0, 20))
        self.parCategory.setMaximumSize(QtCore.QSize(16777215, 20))
        self.parCategory.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.parCategory.setObjectName("parCategory")
        self.gridLayout.addWidget(self.parCategory, 0, 42, 1, 1)
        self.partCompany = QtWidgets.QLineEdit(self.Test_Properties)
        self.partCompany.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partCompany.sizePolicy().hasHeightForWidth())
        self.partCompany.setSizePolicy(sizePolicy)
        self.partCompany.setMinimumSize(QtCore.QSize(0, 20))
        self.partCompany.setMaximumSize(QtCore.QSize(16777215, 20))
        self.partCompany.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.partCompany.setObjectName("partCompany")
        self.gridLayout.addWidget(self.partCompany, 1, 42, 1, 1)
        self.verticalLayout.addWidget(self.Test_Properties, 0, QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(450, 180, 321, 81))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.frame)
        WarehousePage.setCentralWidget(self.centralwidget)

        self.retranslateUi(WarehousePage)
        QtCore.QMetaObject.connectSlotsByName(WarehousePage)

    def retranslateUi(self, WarehousePage):
        _translate = QtCore.QCoreApplication.translate
        WarehousePage.setWindowTitle(_translate("WarehousePage", "MainWindow"))
        self.label_18.setText(_translate("WarehousePage", "تاریخ ثبت"))
        self.label_19.setText(_translate("WarehousePage", "سریال"))
        self.addPartBtn.setText(_translate("WarehousePage", "ثبت قطعه"))
        self.label_7.setText(_translate("WarehousePage", "شرکت سازنده"))
        self.label_17.setText(_translate("WarehousePage", "دسته بندی قطعه"))
        self.label_14.setText(_translate("WarehousePage", "سوپلایر"))
        self.label_15.setText(_translate("WarehousePage", "شماره سفارش"))
        self.label_6.setText(_translate("WarehousePage", "کشور سازنده"))
        self.label.setText(_translate("WarehousePage", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">لیست موجودی قطعات</span></p></body></html>"))