# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_warehousenewpiece.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_WarehousePage(object):
    def setupUi(self, WarehousePage):
        if not WarehousePage.objectName():
            WarehousePage.setObjectName(u"WarehousePage")
        WarehousePage.resize(1322, 854)
        self.centralwidget = QWidget(WarehousePage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"IRANSansWeb(FaNum)"])
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(Qt.RightToLeft)
        self.warehouseIn = QWidget()
        self.warehouseIn.setObjectName(u"warehouseIn")
        self.warehouseIn.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout = QHBoxLayout(self.warehouseIn)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.warehouseIn)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.input_Properties = QFrame(self.frame)
        self.input_Properties.setObjectName(u"input_Properties")
        self.input_Properties.setFrameShape(QFrame.StyledPanel)
        self.input_Properties.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.input_Properties)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.addPartBtn = QPushButton(self.input_Properties)
        self.addPartBtn.setObjectName(u"addPartBtn")
        self.addPartBtn.setFont(font)

        self.gridLayout.addWidget(self.addPartBtn, 2, 45, 1, 1)

        self.label_14 = QLabel(self.input_Properties)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(100, 0))
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(Qt.RightToLeft)
        self.label_14.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_14, 0, 45, 1, 1)

        self.partCompany = QLineEdit(self.input_Properties)
        self.partCompany.setObjectName(u"partCompany")
        self.partCompany.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partCompany.sizePolicy().hasHeightForWidth())
        self.partCompany.setSizePolicy(sizePolicy)
        self.partCompany.setMinimumSize(QSize(150, 28))
        self.partCompany.setMaximumSize(QSize(16777215, 28))
        self.partCompany.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partCompany, 2, 37, 1, 1)

        self.label_17 = QLabel(self.input_Properties)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(100, 0))
        self.label_17.setFont(font)
        self.label_17.setLayoutDirection(Qt.RightToLeft)
        self.label_17.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_17, 0, 36, 1, 1)

        self.date = QLineEdit(self.input_Properties)
        self.date.setObjectName(u"date")
        self.date.setEnabled(True)
        sizePolicy.setHeightForWidth(self.date.sizePolicy().hasHeightForWidth())
        self.date.setSizePolicy(sizePolicy)
        self.date.setMinimumSize(QSize(150, 28))
        self.date.setMaximumSize(QSize(16777215, 28))
        self.date.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.date, 2, 42, 1, 1)

        self.label_18 = QLabel(self.input_Properties)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(100, 0))
        self.label_18.setFont(font)
        self.label_18.setLayoutDirection(Qt.RightToLeft)
        self.label_18.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_18, 2, 41, 1, 1)

        self.partCategory = QLineEdit(self.input_Properties)
        self.partCategory.setObjectName(u"partCategory")
        self.partCategory.setEnabled(True)
        sizePolicy.setHeightForWidth(self.partCategory.sizePolicy().hasHeightForWidth())
        self.partCategory.setSizePolicy(sizePolicy)
        self.partCategory.setMinimumSize(QSize(150, 28))
        self.partCategory.setMaximumSize(QSize(16777215, 28))
        self.partCategory.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partCategory, 0, 37, 1, 1)

        self.partSupplier = QLineEdit(self.input_Properties)
        self.partSupplier.setObjectName(u"partSupplier")
        self.partSupplier.setEnabled(True)
        sizePolicy.setHeightForWidth(self.partSupplier.sizePolicy().hasHeightForWidth())
        self.partSupplier.setSizePolicy(sizePolicy)
        self.partSupplier.setMinimumSize(QSize(150, 28))
        self.partSupplier.setMaximumSize(QSize(16777215, 28))
        self.partSupplier.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partSupplier, 0, 46, 1, 1)

        self.label_6 = QLabel(self.input_Properties)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.RightToLeft)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 2, 38, 1, 1)

        self.label_7 = QLabel(self.input_Properties)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 0))
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(Qt.RightToLeft)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 2, 36, 1, 1)

        self.refreshWarehouse = QPushButton(self.input_Properties)
        self.refreshWarehouse.setObjectName(u"refreshWarehouse")
        self.refreshWarehouse.setFont(font)

        self.gridLayout.addWidget(self.refreshWarehouse, 2, 46, 1, 1)

        self.partCountry = QLineEdit(self.input_Properties)
        self.partCountry.setObjectName(u"partCountry")
        self.partCountry.setEnabled(True)
        sizePolicy.setHeightForWidth(self.partCountry.sizePolicy().hasHeightForWidth())
        self.partCountry.setSizePolicy(sizePolicy)
        self.partCountry.setMinimumSize(QSize(150, 28))
        self.partCountry.setMaximumSize(QSize(16777215, 28))
        self.partCountry.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partCountry, 2, 39, 1, 1)

        self.label_19 = QLabel(self.input_Properties)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(100, 0))
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(Qt.RightToLeft)
        self.label_19.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_19, 0, 38, 1, 1)

        self.partSerial = QLineEdit(self.input_Properties)
        self.partSerial.setObjectName(u"partSerial")
        self.partSerial.setEnabled(True)
        sizePolicy.setHeightForWidth(self.partSerial.sizePolicy().hasHeightForWidth())
        self.partSerial.setSizePolicy(sizePolicy)
        self.partSerial.setMinimumSize(QSize(150, 28))
        self.partSerial.setMaximumSize(QSize(16777215, 28))
        self.partSerial.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partSerial, 0, 39, 1, 1)

        self.label_15 = QLabel(self.input_Properties)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(100, 0))
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(Qt.RightToLeft)
        self.label_15.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_15, 0, 41, 1, 1)

        self.orderId = QLineEdit(self.input_Properties)
        self.orderId.setObjectName(u"orderId")
        self.orderId.setEnabled(True)
        sizePolicy.setHeightForWidth(self.orderId.sizePolicy().hasHeightForWidth())
        self.orderId.setSizePolicy(sizePolicy)
        self.orderId.setMinimumSize(QSize(150, 28))
        self.orderId.setMaximumSize(QSize(16777215, 28))
        self.orderId.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.orderId, 0, 42, 1, 1)


        self.verticalLayout_2.addWidget(self.input_Properties, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.inputPartTable = QFrame(self.frame)
        self.inputPartTable.setObjectName(u"inputPartTable")
        self.inputPartTable.setFrameShape(QFrame.StyledPanel)
        self.inputPartTable.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.inputPartTable)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.tableWidget = QTableWidget(self.inputPartTable)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_2.addWidget(self.tableWidget)


        self.verticalLayout_2.addWidget(self.inputPartTable)


        self.horizontalLayout.addWidget(self.frame)

        self.tabWidget.addTab(self.warehouseIn, "")
        self.warehouseOut = QWidget()
        self.warehouseOut.setObjectName(u"warehouseOut")
        self.horizontalLayout_3 = QHBoxLayout(self.warehouseOut)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.frame_3 = QFrame(self.warehouseOut)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.output_Properties = QFrame(self.frame_3)
        self.output_Properties.setObjectName(u"output_Properties")
        self.output_Properties.setFrameShape(QFrame.StyledPanel)
        self.output_Properties.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.output_Properties)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_20 = QLabel(self.output_Properties)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setMaximumSize(QSize(50, 16777215))
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(Qt.RightToLeft)
        self.label_20.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_20)

        self.exitPartSerial = QLineEdit(self.output_Properties)
        self.exitPartSerial.setObjectName(u"exitPartSerial")
        self.exitPartSerial.setEnabled(True)
        sizePolicy.setHeightForWidth(self.exitPartSerial.sizePolicy().hasHeightForWidth())
        self.exitPartSerial.setSizePolicy(sizePolicy)
        self.exitPartSerial.setMinimumSize(QSize(200, 28))
        self.exitPartSerial.setMaximumSize(QSize(16777215, 28))
        self.exitPartSerial.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.horizontalLayout_4.addWidget(self.exitPartSerial)

        self.label = QLabel(self.output_Properties)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setMaximumSize(QSize(100, 16777215))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.exitPartName = QLabel(self.output_Properties)
        self.exitPartName.setObjectName(u"exitPartName")
        self.exitPartName.setMinimumSize(QSize(200, 28))
        self.exitPartName.setMaximumSize(QSize(200, 28))
        self.exitPartName.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.horizontalLayout_4.addWidget(self.exitPartName)

        self.exitPartBtn = QPushButton(self.output_Properties)
        self.exitPartBtn.setObjectName(u"exitPartBtn")
        self.exitPartBtn.setMinimumSize(QSize(150, 0))
        self.exitPartBtn.setMaximumSize(QSize(150, 16777215))
        self.exitPartBtn.setFont(font)

        self.horizontalLayout_4.addWidget(self.exitPartBtn)

        self.refreshDailyWarehouse = QPushButton(self.output_Properties)
        self.refreshDailyWarehouse.setObjectName(u"refreshDailyWarehouse")

        self.horizontalLayout_4.addWidget(self.refreshDailyWarehouse)


        self.verticalLayout_3.addWidget(self.output_Properties, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.outputPartTable = QFrame(self.frame_3)
        self.outputPartTable.setObjectName(u"outputPartTable")
        self.outputPartTable.setMaximumSize(QSize(16777215, 16777215))
        self.outputPartTable.setFrameShape(QFrame.StyledPanel)
        self.outputPartTable.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.outputPartTable)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.tableWidget_2 = QTableWidget(self.outputPartTable)
        if (self.tableWidget_2.columnCount() < 10):
            self.tableWidget_2.setColumnCount(10)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, __qtablewidgetitem19)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.horizontalLayout_5.addWidget(self.tableWidget_2)


        self.verticalLayout_3.addWidget(self.outputPartTable)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.tabWidget.addTab(self.warehouseOut, "")

        self.verticalLayout.addWidget(self.tabWidget)

        WarehousePage.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.partCategory, self.partSerial)
        QWidget.setTabOrder(self.partSerial, self.orderId)
        QWidget.setTabOrder(self.orderId, self.partSupplier)
        QWidget.setTabOrder(self.partSupplier, self.partCompany)
        QWidget.setTabOrder(self.partCompany, self.partCountry)
        QWidget.setTabOrder(self.partCountry, self.date)
        QWidget.setTabOrder(self.date, self.addPartBtn)
        QWidget.setTabOrder(self.addPartBtn, self.refreshWarehouse)
        QWidget.setTabOrder(self.refreshWarehouse, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.exitPartSerial)
        QWidget.setTabOrder(self.exitPartSerial, self.exitPartBtn)
        QWidget.setTabOrder(self.exitPartBtn, self.refreshDailyWarehouse)
        QWidget.setTabOrder(self.refreshDailyWarehouse, self.tableWidget_2)

        self.retranslateUi(WarehousePage)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WarehousePage)
    # setupUi

    def retranslateUi(self, WarehousePage):
        WarehousePage.setWindowTitle(QCoreApplication.translate("WarehousePage", u"MainWindow", None))
        self.addPartBtn.setText(QCoreApplication.translate("WarehousePage", u"\u062b\u0628\u062a \u0642\u0637\u0639\u0647", None))
        self.label_14.setText(QCoreApplication.translate("WarehousePage", u"\u0633\u0648\u067e\u0644\u0627\u06cc\u0631", None))
        self.label_17.setText(QCoreApplication.translate("WarehousePage", u"\u062f\u0633\u062a\u0647 \u0628\u0646\u062f\u06cc \u0642\u0637\u0639\u0647", None))
        self.label_18.setText(QCoreApplication.translate("WarehousePage", u"\u062a\u0627\u0631\u06cc\u062e \u0633\u0641\u0627\u0631\u0634", None))
        self.label_6.setText(QCoreApplication.translate("WarehousePage", u"\u06a9\u0634\u0648\u0631 \u0633\u0627\u0632\u0646\u062f\u0647", None))
        self.label_7.setText(QCoreApplication.translate("WarehousePage", u"\u0634\u0631\u06a9\u062a \u0633\u0627\u0632\u0646\u062f\u0647", None))
        self.refreshWarehouse.setText(QCoreApplication.translate("WarehousePage", u"\u0628\u0631\u0648\u0632 \u0631\u0633\u0627\u0646\u06cc \u0644\u06cc\u0633\u062a", None))
        self.label_19.setText(QCoreApplication.translate("WarehousePage", u"\u0633\u0631\u06cc\u0627\u0644", None))
        self.label_15.setText(QCoreApplication.translate("WarehousePage", u"\u0634\u0645\u0627\u0631\u0647 \u0633\u0641\u0627\u0631\u0634", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WarehousePage", u"\u062d\u0630\u0641 \u0642\u0637\u0639\u0647", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WarehousePage", u"\u062a\u0627\u0631\u06cc\u062e \u0633\u0641\u0627\u0631\u0634", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WarehousePage", u"\u062f\u0633\u062a\u0647 \u0628\u0646\u062f\u06cc", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WarehousePage", u"\u0633\u0631\u06cc\u0627\u0644", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WarehousePage", u"\u0634\u0645\u0627\u0631\u0647 \u0633\u0641\u0627\u0631\u0634", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WarehousePage", u"\u0633\u0648\u067e\u0644\u0627\u06cc\u0631", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("WarehousePage", u"\u0634\u0631\u06a9\u062a \u0633\u0627\u0632\u0646\u062f\u0647", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("WarehousePage", u"\u06a9\u0634\u0648\u0631 \u0633\u0627\u0632\u0646\u062f\u0647", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("WarehousePage", u"\u0627\u067e\u0631\u0627\u062a\u0648\u0631 \u062b\u0628\u062a \u06a9\u0646\u0646\u062f\u0647", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("WarehousePage", u"\u062a\u0627\u0631\u06cc\u062e \u062b\u0628\u062a", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.warehouseIn), QCoreApplication.translate("WarehousePage", u"\u0648\u0631\u0648\u062f \u0628\u0647 \u0627\u0646\u0628\u0627\u0631", None))
        self.label_20.setText(QCoreApplication.translate("WarehousePage", u"\u0633\u0631\u06cc\u0627\u0644", None))
        self.label.setText(QCoreApplication.translate("WarehousePage", u"\u0646\u0648\u0639 \u0642\u0637\u0639\u0647", None))
        self.exitPartName.setText("")
        self.exitPartBtn.setText(QCoreApplication.translate("WarehousePage", u"\u062e\u0631\u0648\u062c \u0627\u0632 \u0627\u0646\u0628\u0627\u0631", None))
        self.refreshDailyWarehouse.setText(QCoreApplication.translate("WarehousePage", u"\u0628\u0631\u0648\u0632 \u0631\u0633\u0627\u0646\u06cc \u0644\u06cc\u0633\u062a", None))
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("WarehousePage", u"\u062d\u0630\u0641 \u0642\u0637\u0639\u0647", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("WarehousePage", u"\u062a\u0627\u0631\u06cc\u062e \u0633\u0641\u0627\u0631\u0634", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("WarehousePage", u"\u062f\u0633\u062a\u0647 \u0628\u0646\u062f\u06cc", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("WarehousePage", u"\u0633\u0631\u06cc\u0627\u0644", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("WarehousePage", u"\u0634\u0645\u0627\u0631\u0647 \u0633\u0641\u0627\u0631\u0634", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("WarehousePage", u"\u0633\u0648\u067e\u0644\u0627\u06cc\u0631", None));
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("WarehousePage", u"\u0634\u0631\u06a9\u062a \u0633\u0627\u0632\u0646\u062f\u0647", None));
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("WarehousePage", u"\u06a9\u0634\u0648\u0631 \u0633\u0627\u0632\u0646\u062f\u0647", None));
        ___qtablewidgetitem18 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("WarehousePage", u"\u0627\u067e\u0631\u0627\u062a\u0648\u0631 \u062b\u0628\u062a \u06a9\u0646\u0646\u062f\u0647", None));
        ___qtablewidgetitem19 = self.tableWidget_2.horizontalHeaderItem(9)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("WarehousePage", u"\u062a\u0627\u0631\u06cc\u062e \u062b\u0628\u062a", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.warehouseOut), QCoreApplication.translate("WarehousePage", u"\u062e\u0631\u0648\u062c \u0627\u0632 \u0627\u0646\u0628\u0627\u0631", None))
    # retranslateUi

