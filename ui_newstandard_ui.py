# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_newstandard.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpinBox, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_NewStandardPage(object):
    def setupUi(self, NewStandardPage):
        if not NewStandardPage.objectName():
            NewStandardPage.setObjectName(u"NewStandardPage")
        NewStandardPage.resize(1229, 456)
        self.centralwidget = QWidget(NewStandardPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(Qt.RightToLeft)
        self.tabWidget.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.tabNewStandard = QWidget()
        self.tabNewStandard.setObjectName(u"tabNewStandard")
        self.verticalLayout_2 = QVBoxLayout(self.tabNewStandard)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.Test_Properties_2 = QFrame(self.tabNewStandard)
        self.Test_Properties_2.setObjectName(u"Test_Properties_2")
        self.Test_Properties_2.setFrameShape(QFrame.StyledPanel)
        self.Test_Properties_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.Test_Properties_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_21 = QLabel(self.Test_Properties_2)
        self.label_21.setObjectName(u"label_21")
        font1 = QFont()
        font1.setFamilies([u"IRANSansWeb(FaNum)"])
        font1.setPointSize(8)
        self.label_21.setFont(font1)
        self.label_21.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_4.addWidget(self.label_21, 1, 35, 1, 1)

        self.toleranceTemp3 = QSpinBox(self.Test_Properties_2)
        self.toleranceTemp3.setObjectName(u"toleranceTemp3")
        self.toleranceTemp3.setMinimum(1)
        self.toleranceTemp3.setValue(1)

        self.gridLayout_4.addWidget(self.toleranceTemp3, 4, 31, 1, 1)

        self.label_23 = QLabel(self.Test_Properties_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)
        self.label_23.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_4.addWidget(self.label_23, 0, 33, 1, 1)

        self.toleranceTemp4 = QSpinBox(self.Test_Properties_2)
        self.toleranceTemp4.setObjectName(u"toleranceTemp4")
        self.toleranceTemp4.setMinimum(1)
        self.toleranceTemp4.setValue(1)

        self.gridLayout_4.addWidget(self.toleranceTemp4, 4, 32, 1, 1)

        self.label_19 = QLabel(self.Test_Properties_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_4.addWidget(self.label_19, 2, 29, 1, 1)

        self.toleranceTemp6 = QSpinBox(self.Test_Properties_2)
        self.toleranceTemp6.setObjectName(u"toleranceTemp6")
        self.toleranceTemp6.setMinimum(1)
        self.toleranceTemp6.setValue(1)

        self.gridLayout_4.addWidget(self.toleranceTemp6, 4, 34, 1, 1)

        self.modelGas = QLineEdit(self.Test_Properties_2)
        self.modelGas.setObjectName(u"modelGas")

        self.gridLayout_4.addWidget(self.modelGas, 0, 36, 1, 1)

        self.checkTemp5 = QCheckBox(self.Test_Properties_2)
        self.checkTemp5.setObjectName(u"checkTemp5")
        self.checkTemp5.setEnabled(True)
        self.checkTemp5.setFont(font1)
        self.checkTemp5.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.checkTemp5, 3, 33, 1, 1)

        self.toleranceTemp8 = QSpinBox(self.Test_Properties_2)
        self.toleranceTemp8.setObjectName(u"toleranceTemp8")
        self.toleranceTemp8.setMinimum(1)
        self.toleranceTemp8.setValue(1)

        self.gridLayout_4.addWidget(self.toleranceTemp8, 4, 36, 1, 1)

        self.checkTemp1 = QCheckBox(self.Test_Properties_2)
        self.checkTemp1.setObjectName(u"checkTemp1")
        self.checkTemp1.setEnabled(True)
        self.checkTemp1.setFont(font1)
        self.checkTemp1.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.checkTemp1, 3, 29, 1, 1)

        self.checkVolt = QCheckBox(self.Test_Properties_2)
        self.checkVolt.setObjectName(u"checkVolt")
        self.checkVolt.setFont(font1)

        self.gridLayout_4.addWidget(self.checkVolt, 3, 39, 1, 1)

        self.toleranceVolt = QSpinBox(self.Test_Properties_2)
        self.toleranceVolt.setObjectName(u"toleranceVolt")
        self.toleranceVolt.setMinimum(1)
        self.toleranceVolt.setValue(1)

        self.gridLayout_4.addWidget(self.toleranceVolt, 4, 39, 1, 1)

        self.toleranceTemp5 = QSpinBox(self.Test_Properties_2)
        self.toleranceTemp5.setObjectName(u"toleranceTemp5")
        self.toleranceTemp5.setMinimum(1)
        self.toleranceTemp5.setValue(1)

        self.gridLayout_4.addWidget(self.toleranceTemp5, 4, 33, 1, 1)

        self.checkAmptotal = QCheckBox(self.Test_Properties_2)
        self.checkAmptotal.setObjectName(u"checkAmptotal")
        self.checkAmptotal.setFont(font1)

        self.gridLayout_4.addWidget(self.checkAmptotal, 3, 38, 1, 1)

        self.checkTemp2 = QCheckBox(self.Test_Properties_2)
        self.checkTemp2.setObjectName(u"checkTemp2")
        self.checkTemp2.setEnabled(True)
        self.checkTemp2.setFont(font1)
        self.checkTemp2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.checkTemp2, 3, 30, 1, 1)

        self.checkTemp7 = QCheckBox(self.Test_Properties_2)
        self.checkTemp7.setObjectName(u"checkTemp7")
        self.checkTemp7.setEnabled(True)
        self.checkTemp7.setFont(font1)
        self.checkTemp7.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.checkTemp7, 3, 35, 1, 1)

        self.intervalAmp = QLineEdit(self.Test_Properties_2)
        self.intervalAmp.setObjectName(u"intervalAmp")

        self.gridLayout_4.addWidget(self.intervalAmp, 1, 36, 1, 1)

        self.standardName = QLineEdit(self.Test_Properties_2)
        self.standardName.setObjectName(u"standardName")

        self.gridLayout_4.addWidget(self.standardName, 0, 30, 1, 1)

        self.checkTemp6 = QCheckBox(self.Test_Properties_2)
        self.checkTemp6.setObjectName(u"checkTemp6")
        self.checkTemp6.setEnabled(True)
        self.checkTemp6.setFont(font1)
        self.checkTemp6.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.checkTemp6, 3, 34, 1, 1)

        self.label_24 = QLabel(self.Test_Properties_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)
        self.label_24.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_4.addWidget(self.label_24, 1, 29, 1, 1)

        self.label_34 = QLabel(self.Test_Properties_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font1)
        self.label_34.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_4.addWidget(self.label_34, 0, 38, 1, 1)

        self.label_5 = QLabel(self.Test_Properties_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_4.addWidget(self.label_5, 0, 31, 1, 1)

        self.toleranceAmptotal = QSpinBox(self.Test_Properties_2)
        self.toleranceAmptotal.setObjectName(u"toleranceAmptotal")
        self.toleranceAmptotal.setMinimum(1)
        self.toleranceAmptotal.setValue(1)

        self.gridLayout_4.addWidget(self.toleranceAmptotal, 4, 38, 1, 1)

        self.intervalTemp = QLineEdit(self.Test_Properties_2)
        self.intervalTemp.setObjectName(u"intervalTemp")

        self.gridLayout_4.addWidget(self.intervalTemp, 1, 32, 1, 1)

        self.toleranceTemp1 = QSpinBox(self.Test_Properties_2)
        self.toleranceTemp1.setObjectName(u"toleranceTemp1")
        self.toleranceTemp1.setMinimum(1)
        self.toleranceTemp1.setValue(1)

        self.gridLayout_4.addWidget(self.toleranceTemp1, 4, 29, 1, 1)

        self.modelDevice = QLineEdit(self.Test_Properties_2)
        self.modelDevice.setObjectName(u"modelDevice")

        self.gridLayout_4.addWidget(self.modelDevice, 0, 32, 1, 1)

        self.label_25 = QLabel(self.Test_Properties_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)
        self.label_25.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_4.addWidget(self.label_25, 0, 29, 1, 1)

        self.label_22 = QLabel(self.Test_Properties_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_4.addWidget(self.label_22, 0, 37, 1, 1)

        self.label_15 = QLabel(self.Test_Properties_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_4.addWidget(self.label_15, 1, 31, 1, 1)

        self.durationTemp = QLineEdit(self.Test_Properties_2)
        self.durationTemp.setObjectName(u"durationTemp")

        self.gridLayout_4.addWidget(self.durationTemp, 1, 30, 1, 1)

        self.checkTemp4 = QCheckBox(self.Test_Properties_2)
        self.checkTemp4.setObjectName(u"checkTemp4")
        self.checkTemp4.setEnabled(True)
        self.checkTemp4.setFont(font1)
        self.checkTemp4.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.checkTemp4, 3, 32, 1, 1)

        self.label_6 = QLabel(self.Test_Properties_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_4.addWidget(self.label_6, 0, 35, 1, 1)

        self.saveButton = QPushButton(self.Test_Properties_2)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(False)
        self.saveButton.setFont(font1)

        self.gridLayout_4.addWidget(self.saveButton, 7, 35, 1, 1)

        self.toleranceTemp2 = QSpinBox(self.Test_Properties_2)
        self.toleranceTemp2.setObjectName(u"toleranceTemp2")
        self.toleranceTemp2.setMinimum(1)
        self.toleranceTemp2.setValue(1)

        self.gridLayout_4.addWidget(self.toleranceTemp2, 4, 30, 1, 1)

        self.fetchButton = QPushButton(self.Test_Properties_2)
        self.fetchButton.setObjectName(u"fetchButton")
        self.fetchButton.setFont(font1)

        self.gridLayout_4.addWidget(self.fetchButton, 7, 33, 1, 1)

        self.durationAmp = QLineEdit(self.Test_Properties_2)
        self.durationAmp.setObjectName(u"durationAmp")

        self.gridLayout_4.addWidget(self.durationAmp, 1, 34, 1, 1)

        self.checkTemp3 = QCheckBox(self.Test_Properties_2)
        self.checkTemp3.setObjectName(u"checkTemp3")
        self.checkTemp3.setEnabled(True)
        self.checkTemp3.setFont(font1)
        self.checkTemp3.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.checkTemp3, 3, 31, 1, 1)

        self.toleranceAmpstart = QSpinBox(self.Test_Properties_2)
        self.toleranceAmpstart.setObjectName(u"toleranceAmpstart")
        self.toleranceAmpstart.setMinimum(1)
        self.toleranceAmpstart.setValue(1)

        self.gridLayout_4.addWidget(self.toleranceAmpstart, 4, 37, 1, 1)

        self.stopButton = QPushButton(self.Test_Properties_2)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)
        self.stopButton.setFont(font1)

        self.gridLayout_4.addWidget(self.stopButton, 7, 34, 1, 1)

        self.checkAmpstart = QCheckBox(self.Test_Properties_2)
        self.checkAmpstart.setObjectName(u"checkAmpstart")
        self.checkAmpstart.setFont(font1)

        self.gridLayout_4.addWidget(self.checkAmpstart, 3, 37, 1, 1)

        self.companyName = QLineEdit(self.Test_Properties_2)
        self.companyName.setObjectName(u"companyName")
        self.companyName.setEnabled(True)
        self.companyName.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout_4.addWidget(self.companyName, 0, 34, 1, 1)

        self.toleranceTemp7 = QSpinBox(self.Test_Properties_2)
        self.toleranceTemp7.setObjectName(u"toleranceTemp7")
        self.toleranceTemp7.setMinimum(1)
        self.toleranceTemp7.setValue(1)

        self.gridLayout_4.addWidget(self.toleranceTemp7, 4, 35, 1, 1)

        self.checkTemp8 = QCheckBox(self.Test_Properties_2)
        self.checkTemp8.setObjectName(u"checkTemp8")
        self.checkTemp8.setEnabled(True)
        self.checkTemp8.setFont(font1)
        self.checkTemp8.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.checkTemp8, 3, 36, 1, 1)

        self.label_26 = QLabel(self.Test_Properties_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)
        self.label_26.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_4.addWidget(self.label_26, 1, 33, 1, 1)

        self.widgetPort = QComboBox(self.Test_Properties_2)
        self.widgetPort.setObjectName(u"widgetPort")

        self.gridLayout_4.addWidget(self.widgetPort, 1, 37, 1, 1)

        self.label_9 = QLabel(self.Test_Properties_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_4.addWidget(self.label_9, 1, 38, 1, 1)

        self.startTime = QLabel(self.Test_Properties_2)
        self.startTime.setObjectName(u"startTime")
        self.startTime.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout_4.addWidget(self.startTime, 0, 39, 1, 1)

        self.endTime = QLabel(self.Test_Properties_2)
        self.endTime.setObjectName(u"endTime")
        self.endTime.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout_4.addWidget(self.endTime, 1, 39, 1, 1)


        self.verticalLayout_2.addWidget(self.Test_Properties_2)

        self.tableAverage = QTableWidget(self.tabNewStandard)
        if (self.tableAverage.columnCount() < 11):
            self.tableAverage.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        if (self.tableAverage.rowCount() < 2):
            self.tableAverage.setRowCount(2)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableAverage.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableAverage.setVerticalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.tableAverage.setItem(0, 0, __qtablewidgetitem13)
        self.tableAverage.setObjectName(u"tableAverage")
        self.tableAverage.setEnabled(True)
        self.tableAverage.setFont(font1)
        self.tableAverage.setLayoutDirection(Qt.RightToLeft)
        self.tableAverage.setStyleSheet(u"")
        self.tableAverage.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.tableAverage.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableAverage.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableAverage.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableAverage.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableAverage.setCornerButtonEnabled(True)
        self.tableAverage.horizontalHeader().setDefaultSectionSize(100)
        self.tableAverage.horizontalHeader().setHighlightSections(True)
        self.tableAverage.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.tableAverage, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.Charts_Area = QScrollArea(self.tabNewStandard)
        self.Charts_Area.setObjectName(u"Charts_Area")
        self.Charts_Area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1168, 2000))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1000, 2000))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.Charts_Area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.Charts_Area)

        self.tabWidget.addTab(self.tabNewStandard, "")
        self.tabStandards = QWidget()
        self.tabStandards.setObjectName(u"tabStandards")
        self.verticalLayout_3 = QVBoxLayout(self.tabStandards)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.frame_2 = QFrame(self.tabStandards)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Test_Properties_3 = QFrame(self.frame_2)
        self.Test_Properties_3.setObjectName(u"Test_Properties_3")
        self.Test_Properties_3.setFrameShape(QFrame.StyledPanel)
        self.Test_Properties_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.Test_Properties_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.checkAmptotal_2 = QCheckBox(self.Test_Properties_3)
        self.checkAmptotal_2.setObjectName(u"checkAmptotal_2")
        self.checkAmptotal_2.setFont(font1)

        self.gridLayout_5.addWidget(self.checkAmptotal_2, 4, 38, 1, 1)

        self.checkAmpstart_2 = QCheckBox(self.Test_Properties_3)
        self.checkAmpstart_2.setObjectName(u"checkAmpstart_2")
        self.checkAmpstart_2.setFont(font1)

        self.gridLayout_5.addWidget(self.checkAmpstart_2, 4, 37, 1, 1)

        self.label_29 = QLabel(self.Test_Properties_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)
        self.label_29.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_5.addWidget(self.label_29, 2, 29, 1, 1)

        self.label_33 = QLabel(self.Test_Properties_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font1)
        self.label_33.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_5.addWidget(self.label_33, 1, 29, 1, 1)

        self.toleranceTemp1_2 = QSpinBox(self.Test_Properties_3)
        self.toleranceTemp1_2.setObjectName(u"toleranceTemp1_2")
        self.toleranceTemp1_2.setMinimum(1)
        self.toleranceTemp1_2.setValue(1)

        self.gridLayout_5.addWidget(self.toleranceTemp1_2, 5, 29, 1, 1)

        self.toleranceTemp5_2 = QSpinBox(self.Test_Properties_3)
        self.toleranceTemp5_2.setObjectName(u"toleranceTemp5_2")
        self.toleranceTemp5_2.setMinimum(1)
        self.toleranceTemp5_2.setValue(1)

        self.gridLayout_5.addWidget(self.toleranceTemp5_2, 5, 33, 1, 1)

        self.checkTemp1_2 = QCheckBox(self.Test_Properties_3)
        self.checkTemp1_2.setObjectName(u"checkTemp1_2")
        self.checkTemp1_2.setEnabled(True)
        self.checkTemp1_2.setFont(font1)
        self.checkTemp1_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_5.addWidget(self.checkTemp1_2, 4, 29, 1, 1)

        self.label_32 = QLabel(self.Test_Properties_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)
        self.label_32.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_5.addWidget(self.label_32, 2, 33, 1, 1)

        self.intervalAmp_2 = QLabel(self.Test_Properties_3)
        self.intervalAmp_2.setObjectName(u"intervalAmp_2")
        self.intervalAmp_2.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout_5.addWidget(self.intervalAmp_2, 2, 36, 1, 1)

        self.label_31 = QLabel(self.Test_Properties_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)
        self.label_31.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_5.addWidget(self.label_31, 1, 31, 1, 1)

        self.toleranceTemp7_2 = QSpinBox(self.Test_Properties_3)
        self.toleranceTemp7_2.setObjectName(u"toleranceTemp7_2")
        self.toleranceTemp7_2.setMinimum(1)
        self.toleranceTemp7_2.setValue(1)

        self.gridLayout_5.addWidget(self.toleranceTemp7_2, 5, 35, 1, 1)

        self.checkTemp3_2 = QCheckBox(self.Test_Properties_3)
        self.checkTemp3_2.setObjectName(u"checkTemp3_2")
        self.checkTemp3_2.setEnabled(True)
        self.checkTemp3_2.setFont(font1)
        self.checkTemp3_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_5.addWidget(self.checkTemp3_2, 4, 31, 1, 1)

        self.label_7 = QLabel(self.Test_Properties_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_5.addWidget(self.label_7, 1, 37, 1, 1)

        self.durationAmp_2 = QLabel(self.Test_Properties_3)
        self.durationAmp_2.setObjectName(u"durationAmp_2")
        self.durationAmp_2.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout_5.addWidget(self.durationAmp_2, 2, 34, 1, 1)

        self.durationTemp_2 = QLabel(self.Test_Properties_3)
        self.durationTemp_2.setObjectName(u"durationTemp_2")
        self.durationTemp_2.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout_5.addWidget(self.durationTemp_2, 2, 30, 1, 1)

        self.toleranceTemp6_2 = QSpinBox(self.Test_Properties_3)
        self.toleranceTemp6_2.setObjectName(u"toleranceTemp6_2")
        self.toleranceTemp6_2.setMinimum(1)
        self.toleranceTemp6_2.setValue(1)

        self.gridLayout_5.addWidget(self.toleranceTemp6_2, 5, 34, 1, 1)

        self.checkVolt_2 = QCheckBox(self.Test_Properties_3)
        self.checkVolt_2.setObjectName(u"checkVolt_2")
        self.checkVolt_2.setFont(font1)

        self.gridLayout_5.addWidget(self.checkVolt_2, 4, 39, 1, 1)

        self.checkTemp4_2 = QCheckBox(self.Test_Properties_3)
        self.checkTemp4_2.setObjectName(u"checkTemp4_2")
        self.checkTemp4_2.setEnabled(True)
        self.checkTemp4_2.setFont(font1)
        self.checkTemp4_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_5.addWidget(self.checkTemp4_2, 4, 32, 1, 1)

        self.toleranceTemp4_2 = QSpinBox(self.Test_Properties_3)
        self.toleranceTemp4_2.setObjectName(u"toleranceTemp4_2")
        self.toleranceTemp4_2.setMinimum(1)
        self.toleranceTemp4_2.setValue(1)

        self.gridLayout_5.addWidget(self.toleranceTemp4_2, 5, 32, 1, 1)

        self.checkTemp5_2 = QCheckBox(self.Test_Properties_3)
        self.checkTemp5_2.setObjectName(u"checkTemp5_2")
        self.checkTemp5_2.setEnabled(True)
        self.checkTemp5_2.setFont(font1)
        self.checkTemp5_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_5.addWidget(self.checkTemp5_2, 4, 33, 1, 1)

        self.label_20 = QLabel(self.Test_Properties_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_5.addWidget(self.label_20, 3, 29, 1, 1)

        self.label_17 = QLabel(self.Test_Properties_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_5.addWidget(self.label_17, 2, 31, 1, 1)

        self.widgetStandard_2 = QComboBox(self.Test_Properties_3)
        self.widgetStandard_2.setObjectName(u"widgetStandard_2")

        self.gridLayout_5.addWidget(self.widgetStandard_2, 1, 30, 1, 1)

        self.label_30 = QLabel(self.Test_Properties_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)
        self.label_30.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_5.addWidget(self.label_30, 6, 29, 1, 1)

        self.toleranceTemp3_2 = QSpinBox(self.Test_Properties_3)
        self.toleranceTemp3_2.setObjectName(u"toleranceTemp3_2")
        self.toleranceTemp3_2.setMinimum(1)
        self.toleranceTemp3_2.setValue(1)

        self.gridLayout_5.addWidget(self.toleranceTemp3_2, 5, 31, 1, 1)

        self.label_8 = QLabel(self.Test_Properties_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_5.addWidget(self.label_8, 1, 33, 1, 1)

        self.checkTemp8_2 = QCheckBox(self.Test_Properties_3)
        self.checkTemp8_2.setObjectName(u"checkTemp8_2")
        self.checkTemp8_2.setEnabled(True)
        self.checkTemp8_2.setFont(font1)
        self.checkTemp8_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_5.addWidget(self.checkTemp8_2, 4, 36, 1, 1)

        self.companyName_2 = QLabel(self.Test_Properties_3)
        self.companyName_2.setObjectName(u"companyName_2")
        self.companyName_2.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout_5.addWidget(self.companyName_2, 1, 36, 1, 1)

        self.toleranceAmpstart_2 = QSpinBox(self.Test_Properties_3)
        self.toleranceAmpstart_2.setObjectName(u"toleranceAmpstart_2")
        self.toleranceAmpstart_2.setMinimum(1)
        self.toleranceAmpstart_2.setValue(1)

        self.gridLayout_5.addWidget(self.toleranceAmpstart_2, 5, 37, 1, 1)

        self.label_28 = QLabel(self.Test_Properties_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)
        self.label_28.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_5.addWidget(self.label_28, 1, 35, 1, 1)

        self.standardName_2 = QLineEdit(self.Test_Properties_3)
        self.standardName_2.setObjectName(u"standardName_2")

        self.gridLayout_5.addWidget(self.standardName_2, 1, 32, 1, 1)

        self.toleranceVolt_2 = QSpinBox(self.Test_Properties_3)
        self.toleranceVolt_2.setObjectName(u"toleranceVolt_2")
        self.toleranceVolt_2.setMinimum(1)
        self.toleranceVolt_2.setValue(1)

        self.gridLayout_5.addWidget(self.toleranceVolt_2, 5, 39, 1, 1)

        self.checkTemp2_2 = QCheckBox(self.Test_Properties_3)
        self.checkTemp2_2.setObjectName(u"checkTemp2_2")
        self.checkTemp2_2.setEnabled(True)
        self.checkTemp2_2.setFont(font1)
        self.checkTemp2_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_5.addWidget(self.checkTemp2_2, 4, 30, 1, 1)

        self.checkTemp7_2 = QCheckBox(self.Test_Properties_3)
        self.checkTemp7_2.setObjectName(u"checkTemp7_2")
        self.checkTemp7_2.setEnabled(True)
        self.checkTemp7_2.setFont(font1)
        self.checkTemp7_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_5.addWidget(self.checkTemp7_2, 4, 35, 1, 1)

        self.toleranceTemp8_2 = QSpinBox(self.Test_Properties_3)
        self.toleranceTemp8_2.setObjectName(u"toleranceTemp8_2")
        self.toleranceTemp8_2.setMinimum(1)
        self.toleranceTemp8_2.setValue(1)

        self.gridLayout_5.addWidget(self.toleranceTemp8_2, 5, 36, 1, 1)

        self.modelDevice_2 = QLabel(self.Test_Properties_3)
        self.modelDevice_2.setObjectName(u"modelDevice_2")
        self.modelDevice_2.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout_5.addWidget(self.modelDevice_2, 1, 34, 1, 1)

        self.toleranceTemp2_2 = QSpinBox(self.Test_Properties_3)
        self.toleranceTemp2_2.setObjectName(u"toleranceTemp2_2")
        self.toleranceTemp2_2.setMinimum(1)
        self.toleranceTemp2_2.setValue(1)

        self.gridLayout_5.addWidget(self.toleranceTemp2_2, 5, 30, 1, 1)

        self.label_27 = QLabel(self.Test_Properties_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)
        self.label_27.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_5.addWidget(self.label_27, 2, 35, 1, 1)

        self.intervalTemp_2 = QLabel(self.Test_Properties_3)
        self.intervalTemp_2.setObjectName(u"intervalTemp_2")
        self.intervalTemp_2.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout_5.addWidget(self.intervalTemp_2, 2, 32, 1, 1)

        self.toleranceAmptotal_2 = QSpinBox(self.Test_Properties_3)
        self.toleranceAmptotal_2.setObjectName(u"toleranceAmptotal_2")
        self.toleranceAmptotal_2.setMinimum(1)
        self.toleranceAmptotal_2.setValue(1)

        self.gridLayout_5.addWidget(self.toleranceAmptotal_2, 5, 38, 1, 1)

        self.checkTemp6_2 = QCheckBox(self.Test_Properties_3)
        self.checkTemp6_2.setObjectName(u"checkTemp6_2")
        self.checkTemp6_2.setEnabled(True)
        self.checkTemp6_2.setFont(font1)
        self.checkTemp6_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_5.addWidget(self.checkTemp6_2, 4, 34, 1, 1)

        self.avgTemp1 = QLineEdit(self.Test_Properties_3)
        self.avgTemp1.setObjectName(u"avgTemp1")

        self.gridLayout_5.addWidget(self.avgTemp1, 7, 29, 1, 1)

        self.avgTemp2 = QLineEdit(self.Test_Properties_3)
        self.avgTemp2.setObjectName(u"avgTemp2")

        self.gridLayout_5.addWidget(self.avgTemp2, 7, 30, 1, 1)

        self.avgTemp3 = QLineEdit(self.Test_Properties_3)
        self.avgTemp3.setObjectName(u"avgTemp3")

        self.gridLayout_5.addWidget(self.avgTemp3, 7, 31, 1, 1)

        self.avgTemp4 = QLineEdit(self.Test_Properties_3)
        self.avgTemp4.setObjectName(u"avgTemp4")

        self.gridLayout_5.addWidget(self.avgTemp4, 7, 32, 1, 1)

        self.avgTemp5 = QLineEdit(self.Test_Properties_3)
        self.avgTemp5.setObjectName(u"avgTemp5")

        self.gridLayout_5.addWidget(self.avgTemp5, 7, 33, 1, 1)

        self.avgTemp6 = QLineEdit(self.Test_Properties_3)
        self.avgTemp6.setObjectName(u"avgTemp6")

        self.gridLayout_5.addWidget(self.avgTemp6, 7, 34, 1, 1)

        self.avgTemp7 = QLineEdit(self.Test_Properties_3)
        self.avgTemp7.setObjectName(u"avgTemp7")

        self.gridLayout_5.addWidget(self.avgTemp7, 7, 35, 1, 1)

        self.avgTemp8 = QLineEdit(self.Test_Properties_3)
        self.avgTemp8.setObjectName(u"avgTemp8")

        self.gridLayout_5.addWidget(self.avgTemp8, 7, 36, 1, 1)

        self.avgAmpstart = QLineEdit(self.Test_Properties_3)
        self.avgAmpstart.setObjectName(u"avgAmpstart")

        self.gridLayout_5.addWidget(self.avgAmpstart, 7, 37, 1, 1)

        self.avgAmptotal = QLineEdit(self.Test_Properties_3)
        self.avgAmptotal.setObjectName(u"avgAmptotal")

        self.gridLayout_5.addWidget(self.avgAmptotal, 7, 38, 1, 1)

        self.avgVolt = QLineEdit(self.Test_Properties_3)
        self.avgVolt.setObjectName(u"avgVolt")

        self.gridLayout_5.addWidget(self.avgVolt, 7, 39, 1, 1)

        self.deleteBtn = QPushButton(self.Test_Properties_3)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setEnabled(False)
        self.deleteBtn.setFont(font1)

        self.gridLayout_5.addWidget(self.deleteBtn, 8, 35, 1, 1)

        self.editBtn = QPushButton(self.Test_Properties_3)
        self.editBtn.setObjectName(u"editBtn")
        self.editBtn.setEnabled(False)
        self.editBtn.setFont(font1)

        self.gridLayout_5.addWidget(self.editBtn, 8, 34, 1, 1)

        self.gasType_2 = QLabel(self.Test_Properties_3)
        self.gasType_2.setObjectName(u"gasType_2")
        self.gasType_2.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout_5.addWidget(self.gasType_2, 1, 38, 1, 1)


        self.verticalLayout_4.addWidget(self.Test_Properties_3, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tabStandards, "")

        self.verticalLayout.addWidget(self.tabWidget)

        NewStandardPage.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.standardName, self.modelDevice)
        QWidget.setTabOrder(self.modelDevice, self.companyName)
        QWidget.setTabOrder(self.companyName, self.modelGas)
        QWidget.setTabOrder(self.modelGas, self.durationTemp)
        QWidget.setTabOrder(self.durationTemp, self.intervalTemp)
        QWidget.setTabOrder(self.intervalTemp, self.durationAmp)
        QWidget.setTabOrder(self.durationAmp, self.intervalAmp)
        QWidget.setTabOrder(self.intervalAmp, self.widgetPort)
        QWidget.setTabOrder(self.widgetPort, self.checkTemp1)
        QWidget.setTabOrder(self.checkTemp1, self.toleranceTemp1)
        QWidget.setTabOrder(self.toleranceTemp1, self.checkTemp2)
        QWidget.setTabOrder(self.checkTemp2, self.toleranceTemp2)
        QWidget.setTabOrder(self.toleranceTemp2, self.checkTemp3)
        QWidget.setTabOrder(self.checkTemp3, self.toleranceTemp3)
        QWidget.setTabOrder(self.toleranceTemp3, self.checkTemp4)
        QWidget.setTabOrder(self.checkTemp4, self.toleranceTemp4)
        QWidget.setTabOrder(self.toleranceTemp4, self.checkTemp5)
        QWidget.setTabOrder(self.checkTemp5, self.toleranceTemp5)
        QWidget.setTabOrder(self.toleranceTemp5, self.checkTemp6)
        QWidget.setTabOrder(self.checkTemp6, self.toleranceTemp6)
        QWidget.setTabOrder(self.toleranceTemp6, self.checkTemp7)
        QWidget.setTabOrder(self.checkTemp7, self.toleranceTemp7)
        QWidget.setTabOrder(self.toleranceTemp7, self.checkTemp8)
        QWidget.setTabOrder(self.checkTemp8, self.toleranceTemp8)
        QWidget.setTabOrder(self.toleranceTemp8, self.checkAmpstart)
        QWidget.setTabOrder(self.checkAmpstart, self.toleranceAmpstart)
        QWidget.setTabOrder(self.toleranceAmpstart, self.checkAmptotal)
        QWidget.setTabOrder(self.checkAmptotal, self.toleranceAmptotal)
        QWidget.setTabOrder(self.toleranceAmptotal, self.checkVolt)
        QWidget.setTabOrder(self.checkVolt, self.toleranceVolt)
        QWidget.setTabOrder(self.toleranceVolt, self.fetchButton)
        QWidget.setTabOrder(self.fetchButton, self.stopButton)
        QWidget.setTabOrder(self.stopButton, self.saveButton)
        QWidget.setTabOrder(self.saveButton, self.tableAverage)
        QWidget.setTabOrder(self.tableAverage, self.Charts_Area)
        QWidget.setTabOrder(self.Charts_Area, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.widgetStandard_2)
        QWidget.setTabOrder(self.widgetStandard_2, self.standardName_2)
        QWidget.setTabOrder(self.standardName_2, self.checkTemp1_2)
        QWidget.setTabOrder(self.checkTemp1_2, self.toleranceTemp1_2)
        QWidget.setTabOrder(self.toleranceTemp1_2, self.avgTemp1)
        QWidget.setTabOrder(self.avgTemp1, self.checkTemp2_2)
        QWidget.setTabOrder(self.checkTemp2_2, self.toleranceTemp2_2)
        QWidget.setTabOrder(self.toleranceTemp2_2, self.avgTemp2)
        QWidget.setTabOrder(self.avgTemp2, self.checkTemp3_2)
        QWidget.setTabOrder(self.checkTemp3_2, self.toleranceTemp3_2)
        QWidget.setTabOrder(self.toleranceTemp3_2, self.avgTemp3)
        QWidget.setTabOrder(self.avgTemp3, self.checkTemp4_2)
        QWidget.setTabOrder(self.checkTemp4_2, self.toleranceTemp4_2)
        QWidget.setTabOrder(self.toleranceTemp4_2, self.avgTemp4)
        QWidget.setTabOrder(self.avgTemp4, self.checkTemp5_2)
        QWidget.setTabOrder(self.checkTemp5_2, self.toleranceTemp5_2)
        QWidget.setTabOrder(self.toleranceTemp5_2, self.avgTemp5)
        QWidget.setTabOrder(self.avgTemp5, self.checkTemp6_2)
        QWidget.setTabOrder(self.checkTemp6_2, self.toleranceTemp6_2)
        QWidget.setTabOrder(self.toleranceTemp6_2, self.avgTemp6)
        QWidget.setTabOrder(self.avgTemp6, self.checkTemp7_2)
        QWidget.setTabOrder(self.checkTemp7_2, self.toleranceTemp7_2)
        QWidget.setTabOrder(self.toleranceTemp7_2, self.avgTemp7)
        QWidget.setTabOrder(self.avgTemp7, self.checkTemp8_2)
        QWidget.setTabOrder(self.checkTemp8_2, self.toleranceTemp8_2)
        QWidget.setTabOrder(self.toleranceTemp8_2, self.avgTemp8)
        QWidget.setTabOrder(self.avgTemp8, self.checkAmpstart_2)
        QWidget.setTabOrder(self.checkAmpstart_2, self.toleranceAmpstart_2)
        QWidget.setTabOrder(self.toleranceAmpstart_2, self.avgAmpstart)
        QWidget.setTabOrder(self.avgAmpstart, self.checkAmptotal_2)
        QWidget.setTabOrder(self.checkAmptotal_2, self.toleranceAmptotal_2)
        QWidget.setTabOrder(self.toleranceAmptotal_2, self.avgAmptotal)
        QWidget.setTabOrder(self.avgAmptotal, self.checkVolt_2)
        QWidget.setTabOrder(self.checkVolt_2, self.toleranceVolt_2)
        QWidget.setTabOrder(self.toleranceVolt_2, self.avgVolt)
        QWidget.setTabOrder(self.avgVolt, self.editBtn)
        QWidget.setTabOrder(self.editBtn, self.deleteBtn)

        self.retranslateUi(NewStandardPage)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(NewStandardPage)
    # setupUi

    def retranslateUi(self, NewStandardPage):
        NewStandardPage.setWindowTitle(QCoreApplication.translate("NewStandardPage", u"MainWindow", None))
        self.label_21.setText(QCoreApplication.translate("NewStandardPage", u"\u062a\u0639\u062f\u0627\u062f \u062c\u0631\u06cc\u0627\u0646", None))
        self.label_23.setText(QCoreApplication.translate("NewStandardPage", u"\u06a9\u0645\u067e\u0627\u0646\u06cc \u0633\u0627\u0632\u0646\u062f\u0647:", None))
        self.label_19.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631\u0647\u0627 \u0648 \u062a\u0644\u0648\u0631\u0627\u0646\u0633:", None))
        self.checkTemp5.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 5", None))
        self.checkTemp1.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 1", None))
        self.checkVolt.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631 \u0648\u0644\u062a\u0627\u0698", None))
        self.checkAmptotal.setText(QCoreApplication.translate("NewStandardPage", u"\u062c\u0631\u06cc\u0627\u0646 \u06a9\u0644", None))
        self.checkTemp2.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 2", None))
        self.checkTemp7.setText(QCoreApplication.translate("NewStandardPage", u"min \u0633\u0646\u0633\u0648\u0631 \u0641\u0634\u0627\u0631", None))
        self.checkTemp6.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 6", None))
        self.label_24.setText(QCoreApplication.translate("NewStandardPage", u"\u0632\u0645\u0627\u0646 \u062a\u0633\u062a(\u062b\u0627\u0646\u06cc\u0647):", None))
        self.label_34.setText(QCoreApplication.translate("NewStandardPage", u"\u0632\u0645\u0627\u0646 \u0634\u0631\u0648\u0639 \u062a\u0633\u062a", None))
        self.label_5.setText(QCoreApplication.translate("NewStandardPage", u"\u0645\u062f\u0644 \u062f\u0633\u062a\u06af\u0627\u0647", None))
        self.label_25.setText(QCoreApplication.translate("NewStandardPage", u"\u0639\u0646\u0648\u0627\u0646 \u0627\u0633\u062a\u0627\u0646\u062f\u0627\u0631\u062f:", None))
        self.label_22.setText(QCoreApplication.translate("NewStandardPage", u"\u067e\u0648\u0631\u062a:", None))
        self.label_15.setText(QCoreApplication.translate("NewStandardPage", u"\u062a\u0646\u0627\u0648\u0628 \u0633\u0646\u0633\u0648\u0631(\u062b\u0627\u0646\u06cc\u0647):", None))
        self.checkTemp4.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 4", None))
        self.label_6.setText(QCoreApplication.translate("NewStandardPage", u"\u0646\u0648\u0639 \u06af\u0627\u0632", None))
        self.saveButton.setText(QCoreApplication.translate("NewStandardPage", u"\u062b\u0628\u062a \u062a\u0633\u062a", None))
        self.fetchButton.setText(QCoreApplication.translate("NewStandardPage", u"\u0634\u0631\u0648\u0639 \u062a\u0633\u062a", None))
        self.checkTemp3.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 3", None))
        self.stopButton.setText(QCoreApplication.translate("NewStandardPage", u"\u062a\u0648\u0642\u0641 \u062a\u0633\u062a", None))
        self.checkAmpstart.setText(QCoreApplication.translate("NewStandardPage", u"\u062c\u0631\u06cc\u0627\u0646 \u0634\u0631\u0648\u0639", None))
        self.checkTemp8.setText(QCoreApplication.translate("NewStandardPage", u"max \u0633\u0646\u0633\u0648\u0631 \u0641\u0634\u0627\u0631", None))
        self.label_26.setText(QCoreApplication.translate("NewStandardPage", u"\u0632\u0645\u0627\u0646 \u062c\u0631\u06cc\u0627\u0646(\u062b\u0627\u0646\u06cc\u0647):", None))
        self.label_9.setText(QCoreApplication.translate("NewStandardPage", u"\u0632\u0645\u0627\u0646 \u067e\u0627\u06cc\u0627\u0646 \u062a\u0633\u062a", None))
        self.startTime.setText("")
        self.endTime.setText("")
        ___qtablewidgetitem = self.tableAverage.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("NewStandardPage", u"\u062f\u0645\u0627 1", None));
        ___qtablewidgetitem1 = self.tableAverage.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("NewStandardPage", u"\u062f\u0645\u0627 2", None));
        ___qtablewidgetitem2 = self.tableAverage.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("NewStandardPage", u"\u062f\u0645\u0627 3", None));
        ___qtablewidgetitem3 = self.tableAverage.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("NewStandardPage", u"\u062f\u0645\u0627 4", None));
        ___qtablewidgetitem4 = self.tableAverage.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("NewStandardPage", u"\u062f\u0645\u0627 5", None));
        ___qtablewidgetitem5 = self.tableAverage.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("NewStandardPage", u"\u062f\u0645\u0627 6", None));
        ___qtablewidgetitem6 = self.tableAverage.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("NewStandardPage", u"min \u0641\u0634\u0627\u0631", None));
        ___qtablewidgetitem7 = self.tableAverage.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("NewStandardPage", u"max \u0641\u0634\u0627\u0631", None));
        ___qtablewidgetitem8 = self.tableAverage.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("NewStandardPage", u"\u062c\u0631\u06cc\u0627\u0646 \u06a9\u0644", None));
        ___qtablewidgetitem9 = self.tableAverage.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("NewStandardPage", u"\u062c\u0631\u06cc\u0627\u0646 \u0634\u0631\u0648\u0639", None));
        ___qtablewidgetitem10 = self.tableAverage.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("NewStandardPage", u"\u0648\u0644\u062a\u0627\u0698", None));
        ___qtablewidgetitem11 = self.tableAverage.verticalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("NewStandardPage", u"\u0644\u062d\u0638\u0647 \u0627\u06cc", None));
        ___qtablewidgetitem12 = self.tableAverage.verticalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("NewStandardPage", u"\u0645\u062a\u0648\u0633\u0637", None));

        __sortingEnabled = self.tableAverage.isSortingEnabled()
        self.tableAverage.setSortingEnabled(False)
        self.tableAverage.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNewStandard), QCoreApplication.translate("NewStandardPage", u"\u062b\u0628\u062a \u0627\u0633\u062a\u0627\u0646\u062f\u0627\u0631\u062f \u062c\u062f\u06cc\u062f", None))
        self.checkAmptotal_2.setText(QCoreApplication.translate("NewStandardPage", u"\u062c\u0631\u06cc\u0627\u0646 \u06a9\u0644", None))
        self.checkAmpstart_2.setText(QCoreApplication.translate("NewStandardPage", u"\u062c\u0631\u06cc\u0627\u0646 \u0634\u0631\u0648\u0639", None))
        self.label_29.setText(QCoreApplication.translate("NewStandardPage", u"\u0632\u0645\u0627\u0646 \u062a\u0633\u062a(\u062b\u0627\u0646\u06cc\u0647):", None))
        self.label_33.setText(QCoreApplication.translate("NewStandardPage", u"\u0639\u0646\u0648\u0627\u0646 \u0627\u0633\u062a\u0627\u0646\u062f\u0627\u0631\u062f:", None))
        self.checkTemp1_2.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 1", None))
        self.label_32.setText(QCoreApplication.translate("NewStandardPage", u"\u0632\u0645\u0627\u0646 \u062c\u0631\u06cc\u0627\u0646(\u062b\u0627\u0646\u06cc\u0647):", None))
        self.intervalAmp_2.setText("")
        self.label_31.setText(QCoreApplication.translate("NewStandardPage", u"\u0639\u0646\u0648\u0627\u0646 \u0627\u0633\u062a\u0627\u0646\u062f\u0627\u0631\u062f:", None))
        self.checkTemp3_2.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 3", None))
        self.label_7.setText(QCoreApplication.translate("NewStandardPage", u"\u0646\u0648\u0639 \u06af\u0627\u0632", None))
        self.durationAmp_2.setText("")
        self.durationTemp_2.setText("")
        self.checkVolt_2.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631 \u0648\u0644\u062a\u0627\u0698", None))
        self.checkTemp4_2.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 4", None))
        self.checkTemp5_2.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 5", None))
        self.label_20.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631\u0647\u0627 \u0648 \u062a\u0644\u0648\u0631\u0627\u0646\u0633:", None))
        self.label_17.setText(QCoreApplication.translate("NewStandardPage", u"\u062a\u0646\u0627\u0648\u0628 \u0633\u0646\u0633\u0648\u0631(\u062b\u0627\u0646\u06cc\u0647):", None))
        self.label_30.setText(QCoreApplication.translate("NewStandardPage", u"\u0645\u06cc\u0627\u0646\u06af\u06cc\u0646 \u0647\u0627:", None))
        self.label_8.setText(QCoreApplication.translate("NewStandardPage", u"\u0645\u062f\u0644 \u062f\u0633\u062a\u06af\u0627\u0647", None))
        self.checkTemp8_2.setText(QCoreApplication.translate("NewStandardPage", u"max \u0633\u0646\u0633\u0648\u0631 \u0641\u0634\u0627\u0631", None))
        self.companyName_2.setText("")
        self.label_28.setText(QCoreApplication.translate("NewStandardPage", u"\u06a9\u0645\u067e\u0627\u0646\u06cc \u0633\u0627\u0632\u0646\u062f\u0647:", None))
        self.checkTemp2_2.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 2", None))
        self.checkTemp7_2.setText(QCoreApplication.translate("NewStandardPage", u"min \u0633\u0646\u0633\u0648\u0631 \u0641\u0634\u0627\u0631", None))
        self.modelDevice_2.setText("")
        self.label_27.setText(QCoreApplication.translate("NewStandardPage", u"\u062a\u0639\u062f\u0627\u062f \u062c\u0631\u06cc\u0627\u0646", None))
        self.intervalTemp_2.setText("")
        self.checkTemp6_2.setText(QCoreApplication.translate("NewStandardPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 6", None))
        self.deleteBtn.setText(QCoreApplication.translate("NewStandardPage", u"\u062d\u0630\u0641 \u0627\u0633\u062a\u0627\u0646\u062f\u0627\u0631\u062f", None))
        self.editBtn.setText(QCoreApplication.translate("NewStandardPage", u"\u0630\u062e\u06cc\u0631\u0647 \u062a\u063a\u06cc\u06cc\u0631\u0627\u062a", None))
        self.gasType_2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStandards), QCoreApplication.translate("NewStandardPage", u"\u0627\u0633\u062a\u0627\u0646\u062f\u0627\u0631\u062f\u0647\u0627\u06cc \u062b\u0628\u062a \u0634\u062f\u0647", None))
    # retranslateUi

