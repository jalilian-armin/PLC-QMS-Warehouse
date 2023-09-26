# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_newtest.ui'
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
    QScrollArea, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_NewTestPage(object):
    def setupUi(self, NewTestPage):
        if not NewTestPage.objectName():
            NewTestPage.setObjectName(u"NewTestPage")
        NewTestPage.resize(1212, 859)
        self.centralwidget = QWidget(NewTestPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Test_Properties = QFrame(self.centralwidget)
        self.Test_Properties.setObjectName(u"Test_Properties")
        self.Test_Properties.setFrameShape(QFrame.StyledPanel)
        self.Test_Properties.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.Test_Properties)
        self.gridLayout.setObjectName(u"gridLayout")
        self.durationAmp = QLabel(self.Test_Properties)
        self.durationAmp.setObjectName(u"durationAmp")
        self.durationAmp.setMinimumSize(QSize(0, 20))
        self.durationAmp.setMaximumSize(QSize(16777215, 20))
        self.durationAmp.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.durationAmp, 1, 38, 1, 1)

        self.checkTemp1 = QCheckBox(self.Test_Properties)
        self.checkTemp1.setObjectName(u"checkTemp1")
        self.checkTemp1.setEnabled(False)
        font = QFont()
        font.setFamilies([u"IRANSansWeb(FaNum)"])
        self.checkTemp1.setFont(font)
        self.checkTemp1.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.checkTemp1, 2, 43, 1, 1)

        self.intervalTemp = QLabel(self.Test_Properties)
        self.intervalTemp.setObjectName(u"intervalTemp")
        self.intervalTemp.setMinimumSize(QSize(0, 20))
        self.intervalTemp.setMaximumSize(QSize(16777215, 20))
        self.intervalTemp.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.intervalTemp, 1, 40, 1, 1)

        self.label_21 = QLabel(self.Test_Properties)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout.addWidget(self.label_21, 0, 34, 1, 1)

        self.label_12 = QLabel(self.Test_Properties)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout.addWidget(self.label_12, 1, 43, 1, 1)

        self.checkTemp4 = QCheckBox(self.Test_Properties)
        self.checkTemp4.setObjectName(u"checkTemp4")
        self.checkTemp4.setEnabled(False)
        self.checkTemp4.setFont(font)
        self.checkTemp4.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.checkTemp4, 2, 40, 1, 1)

        self.durationTemp = QLabel(self.Test_Properties)
        self.durationTemp.setObjectName(u"durationTemp")
        self.durationTemp.setMinimumSize(QSize(0, 20))
        self.durationTemp.setMaximumSize(QSize(16777215, 20))
        self.durationTemp.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.durationTemp, 1, 42, 1, 1)

        self.label_6 = QLabel(self.Test_Properties)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 0, 37, 1, 1)

        self.checkTemp8 = QCheckBox(self.Test_Properties)
        self.checkTemp8.setObjectName(u"checkTemp8")
        self.checkTemp8.setEnabled(False)
        self.checkTemp8.setFont(font)
        self.checkTemp8.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.checkTemp8, 2, 36, 1, 1)

        self.checkVolt = QCheckBox(self.Test_Properties)
        self.checkVolt.setObjectName(u"checkVolt")
        self.checkVolt.setEnabled(False)
        self.checkVolt.setFont(font)
        self.checkVolt.setLayoutDirection(Qt.RightToLeft)
        self.checkVolt.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout.addWidget(self.checkVolt, 2, 0, 1, 1)

        self.label_14 = QLabel(self.Test_Properties)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout.addWidget(self.label_14, 0, 39, 1, 1)

        self.intervalAmp = QLabel(self.Test_Properties)
        self.intervalAmp.setObjectName(u"intervalAmp")
        self.intervalAmp.setMinimumSize(QSize(0, 20))
        self.intervalAmp.setMaximumSize(QSize(16777215, 20))
        self.intervalAmp.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.intervalAmp, 1, 36, 1, 1)

        self.widgetPort = QComboBox(self.Test_Properties)
        self.widgetPort.setObjectName(u"widgetPort")

        self.gridLayout.addWidget(self.widgetPort, 0, 42, 1, 1)

        self.label_7 = QLabel(self.Test_Properties)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 1, 34, 1, 1)

        self.startTime = QLabel(self.Test_Properties)
        self.startTime.setObjectName(u"startTime")
        self.startTime.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.startTime, 0, 0, 1, 1)

        self.label_16 = QLabel(self.Test_Properties)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout.addWidget(self.label_16, 1, 37, 1, 1)

        self.gasType = QLabel(self.Test_Properties)
        self.gasType.setObjectName(u"gasType")
        self.gasType.setMinimumSize(QSize(0, 20))
        self.gasType.setMaximumSize(QSize(16777215, 20))
        self.gasType.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.gasType, 0, 36, 1, 1)

        self.label_17 = QLabel(self.Test_Properties)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout.addWidget(self.label_17, 0, 43, 1, 1)

        self.checkTemp7 = QCheckBox(self.Test_Properties)
        self.checkTemp7.setObjectName(u"checkTemp7")
        self.checkTemp7.setEnabled(False)
        self.checkTemp7.setFont(font)
        self.checkTemp7.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.checkTemp7, 2, 37, 1, 1)

        self.motorId = QLineEdit(self.Test_Properties)
        self.motorId.setObjectName(u"motorId")
        self.motorId.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motorId.sizePolicy().hasHeightForWidth())
        self.motorId.setSizePolicy(sizePolicy)
        self.motorId.setMinimumSize(QSize(0, 20))
        self.motorId.setMaximumSize(QSize(16777215, 20))
        self.motorId.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.motorId, 0, 40, 1, 1)

        self.checkTemp5 = QCheckBox(self.Test_Properties)
        self.checkTemp5.setObjectName(u"checkTemp5")
        self.checkTemp5.setEnabled(False)
        self.checkTemp5.setFont(font)
        self.checkTemp5.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.checkTemp5, 2, 39, 1, 1)

        self.widgetStandard = QComboBox(self.Test_Properties)
        self.widgetStandard.setObjectName(u"widgetStandard")

        self.gridLayout.addWidget(self.widgetStandard, 0, 38, 1, 1)

        self.checkTemp3 = QCheckBox(self.Test_Properties)
        self.checkTemp3.setObjectName(u"checkTemp3")
        self.checkTemp3.setEnabled(False)
        self.checkTemp3.setFont(font)
        self.checkTemp3.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.checkTemp3, 2, 41, 1, 1)

        self.checkAmptotal = QCheckBox(self.Test_Properties)
        self.checkAmptotal.setObjectName(u"checkAmptotal")
        self.checkAmptotal.setEnabled(False)
        self.checkAmptotal.setFont(font)
        self.checkAmptotal.setLayoutDirection(Qt.RightToLeft)
        self.checkAmptotal.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout.addWidget(self.checkAmptotal, 2, 34, 1, 1)

        self.label_20 = QLabel(self.Test_Properties)
        self.label_20.setObjectName(u"label_20")
        font1 = QFont()
        font1.setFamilies([u"IRANSansWeb(FaNum)"])
        font1.setBold(False)
        self.label_20.setFont(font1)
        self.label_20.setLayoutDirection(Qt.RightToLeft)
        self.label_20.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout.addWidget(self.label_20, 3, 43, 1, 1)

        self.endTime = QLabel(self.Test_Properties)
        self.endTime.setObjectName(u"endTime")
        self.endTime.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.endTime, 1, 0, 1, 1)

        self.label_13 = QLabel(self.Test_Properties)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout.addWidget(self.label_13, 1, 41, 1, 1)

        self.label_18 = QLabel(self.Test_Properties)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout.addWidget(self.label_18, 1, 39, 1, 1)

        self.checkTemp2 = QCheckBox(self.Test_Properties)
        self.checkTemp2.setObjectName(u"checkTemp2")
        self.checkTemp2.setEnabled(False)
        self.checkTemp2.setFont(font)
        self.checkTemp2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.checkTemp2, 2, 42, 1, 1)

        self.testResult = QLabel(self.Test_Properties)
        self.testResult.setObjectName(u"testResult")
        self.testResult.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.testResult, 3, 37, 1, 6)

        self.checkTemp6 = QCheckBox(self.Test_Properties)
        self.checkTemp6.setObjectName(u"checkTemp6")
        self.checkTemp6.setEnabled(False)
        self.checkTemp6.setFont(font)
        self.checkTemp6.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.checkTemp6, 2, 38, 1, 1)

        self.label_19 = QLabel(self.Test_Properties)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout.addWidget(self.label_19, 0, 41, 1, 1)

        self.checkAmpstart = QCheckBox(self.Test_Properties)
        self.checkAmpstart.setObjectName(u"checkAmpstart")
        self.checkAmpstart.setEnabled(False)
        self.checkAmpstart.setFont(font)
        self.checkAmpstart.setLayoutDirection(Qt.RightToLeft)
        self.checkAmpstart.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout.addWidget(self.checkAmpstart, 2, 35, 1, 1)

        self.fetchButton = QPushButton(self.Test_Properties)
        self.fetchButton.setObjectName(u"fetchButton")
        self.fetchButton.setFont(font)

        self.gridLayout.addWidget(self.fetchButton, 3, 36, 1, 1)

        self.stopButton = QPushButton(self.Test_Properties)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)
        self.stopButton.setFont(font)

        self.gridLayout.addWidget(self.stopButton, 3, 35, 1, 1)

        self.saveButton = QPushButton(self.Test_Properties)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(False)
        self.saveButton.setFont(font)

        self.gridLayout.addWidget(self.saveButton, 3, 34, 1, 1)

        self.printButton = QPushButton(self.Test_Properties)
        self.printButton.setObjectName(u"printButton")
        self.printButton.setEnabled(False)
        self.printButton.setFont(font)

        self.gridLayout.addWidget(self.printButton, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.Test_Properties)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font2 = QFont()
        font2.setPointSize(8)
        self.tabWidget.setFont(font2)
        self.tabWidget.setLayoutDirection(Qt.RightToLeft)
        self.tabWidget.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.tabTablePlot = QWidget()
        self.tabTablePlot.setObjectName(u"tabTablePlot")
        self.tabTablePlot.setFont(font2)
        self.verticalLayout_2 = QVBoxLayout(self.tabTablePlot)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableAverage = QTableWidget(self.tabTablePlot)
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
        self.tableAverage.setObjectName(u"tableAverage")
        self.tableAverage.setMinimumSize(QSize(0, 100))
        font3 = QFont()
        font3.setFamilies([u"IRANSansWeb(FaNum)"])
        font3.setPointSize(8)
        self.tableAverage.setFont(font3)
        self.tableAverage.setLayoutDirection(Qt.RightToLeft)
        self.tableAverage.setStyleSheet(u"")
        self.tableAverage.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.tableAverage.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableAverage.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableAverage.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableAverage.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableAverage.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout_2.addWidget(self.tableAverage, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.tableCompare = QTableWidget(self.tabTablePlot)
        if (self.tableCompare.columnCount() < 11):
            self.tableCompare.setColumnCount(11)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableCompare.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableCompare.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableCompare.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableCompare.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableCompare.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableCompare.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableCompare.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableCompare.setHorizontalHeaderItem(7, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableCompare.setHorizontalHeaderItem(8, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableCompare.setHorizontalHeaderItem(9, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableCompare.setHorizontalHeaderItem(10, __qtablewidgetitem23)
        if (self.tableCompare.rowCount() < 3):
            self.tableCompare.setRowCount(3)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableCompare.setVerticalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableCompare.setVerticalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableCompare.setVerticalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.tableCompare.setItem(0, 0, __qtablewidgetitem27)
        self.tableCompare.setObjectName(u"tableCompare")
        self.tableCompare.setEnabled(True)
        self.tableCompare.setMinimumSize(QSize(0, 130))
        self.tableCompare.setFont(font3)
        self.tableCompare.setLayoutDirection(Qt.RightToLeft)
        self.tableCompare.setStyleSheet(u"")
        self.tableCompare.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.tableCompare.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableCompare.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableCompare.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableCompare.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCompare.setCornerButtonEnabled(True)
        self.tableCompare.horizontalHeader().setDefaultSectionSize(98)
        self.tableCompare.horizontalHeader().setHighlightSections(True)
        self.tableCompare.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.tableCompare, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.Charts_Area = QScrollArea(self.tabTablePlot)
        self.Charts_Area.setObjectName(u"Charts_Area")
        self.Charts_Area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-902, 0, 1000, 2000))
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

        self.tabWidget.addTab(self.tabTablePlot, "")
        self.tabTable = QWidget()
        self.tabTable.setObjectName(u"tabTable")
        self.gridLayout_7 = QGridLayout(self.tabTable)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tableAverage_2 = QTableWidget(self.tabTable)
        if (self.tableAverage_2.columnCount() < 10):
            self.tableAverage_2.setColumnCount(10)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableAverage_2.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableAverage_2.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableAverage_2.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableAverage_2.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableAverage_2.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableAverage_2.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableAverage_2.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableAverage_2.setHorizontalHeaderItem(7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableAverage_2.setHorizontalHeaderItem(8, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableAverage_2.setHorizontalHeaderItem(9, __qtablewidgetitem37)
        if (self.tableAverage_2.rowCount() < 2):
            self.tableAverage_2.setRowCount(2)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableAverage_2.setVerticalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableAverage_2.setVerticalHeaderItem(1, __qtablewidgetitem39)
        self.tableAverage_2.setObjectName(u"tableAverage_2")
        self.tableAverage_2.setFont(font3)
        self.tableAverage_2.setLayoutDirection(Qt.RightToLeft)
        self.tableAverage_2.setStyleSheet(u"")
        self.tableAverage_2.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.tableAverage_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableAverage_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableAverage_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableAverage_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableAverage_2.horizontalHeader().setDefaultSectionSize(100)

        self.gridLayout_7.addWidget(self.tableAverage_2, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.tableCompare_2 = QTableWidget(self.tabTable)
        if (self.tableCompare_2.columnCount() < 10):
            self.tableCompare_2.setColumnCount(10)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableCompare_2.setHorizontalHeaderItem(0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableCompare_2.setHorizontalHeaderItem(1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableCompare_2.setHorizontalHeaderItem(2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableCompare_2.setHorizontalHeaderItem(3, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableCompare_2.setHorizontalHeaderItem(4, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableCompare_2.setHorizontalHeaderItem(5, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableCompare_2.setHorizontalHeaderItem(6, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableCompare_2.setHorizontalHeaderItem(7, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableCompare_2.setHorizontalHeaderItem(8, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableCompare_2.setHorizontalHeaderItem(9, __qtablewidgetitem49)
        if (self.tableCompare_2.rowCount() < 3):
            self.tableCompare_2.setRowCount(3)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableCompare_2.setVerticalHeaderItem(0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableCompare_2.setVerticalHeaderItem(1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableCompare_2.setVerticalHeaderItem(2, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.tableCompare_2.setItem(0, 0, __qtablewidgetitem53)
        self.tableCompare_2.setObjectName(u"tableCompare_2")
        self.tableCompare_2.setEnabled(True)
        self.tableCompare_2.setFont(font3)
        self.tableCompare_2.setLayoutDirection(Qt.RightToLeft)
        self.tableCompare_2.setStyleSheet(u"")
        self.tableCompare_2.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.tableCompare_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableCompare_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableCompare_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableCompare_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCompare_2.setCornerButtonEnabled(True)
        self.tableCompare_2.horizontalHeader().setDefaultSectionSize(100)
        self.tableCompare_2.horizontalHeader().setHighlightSections(True)
        self.tableCompare_2.horizontalHeader().setStretchLastSection(False)

        self.gridLayout_7.addWidget(self.tableCompare_2, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.tabWidget.addTab(self.tabTable, "")
        self.tabGraph = QWidget()
        self.tabGraph.setObjectName(u"tabGraph")
        self.verticalLayout_4 = QVBoxLayout(self.tabGraph)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Charts_Area_2 = QScrollArea(self.tabGraph)
        self.Charts_Area_2.setObjectName(u"Charts_Area_2")
        self.Charts_Area_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1139, 2000))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(1000, 2000))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.plotTemp8_3 = QWidget(self.frame_2)
        self.plotTemp8_3.setObjectName(u"plotTemp8_3")
        self.plotTemp8_3.setMinimumSize(QSize(500, 500))

        self.gridLayout_6.addWidget(self.plotTemp8_3, 3, 1, 1, 1)

        self.plotTemp6_3 = QWidget(self.frame_2)
        self.plotTemp6_3.setObjectName(u"plotTemp6_3")
        self.plotTemp6_3.setMinimumSize(QSize(500, 500))

        self.gridLayout_6.addWidget(self.plotTemp6_3, 2, 1, 1, 1)

        self.plotTemp7_3 = QWidget(self.frame_2)
        self.plotTemp7_3.setObjectName(u"plotTemp7_3")
        self.plotTemp7_3.setMinimumSize(QSize(500, 500))

        self.gridLayout_6.addWidget(self.plotTemp7_3, 3, 0, 1, 1)

        self.plotTemp5_3 = QWidget(self.frame_2)
        self.plotTemp5_3.setObjectName(u"plotTemp5_3")
        self.plotTemp5_3.setMinimumSize(QSize(500, 500))

        self.gridLayout_6.addWidget(self.plotTemp5_3, 2, 0, 1, 1)

        self.plotTemp2_3 = QWidget(self.frame_2)
        self.plotTemp2_3.setObjectName(u"plotTemp2_3")
        self.plotTemp2_3.setMinimumSize(QSize(500, 500))

        self.gridLayout_6.addWidget(self.plotTemp2_3, 0, 1, 1, 1)

        self.plotTemp1_3 = QWidget(self.frame_2)
        self.plotTemp1_3.setObjectName(u"plotTemp1_3")
        self.plotTemp1_3.setMinimumSize(QSize(500, 500))

        self.gridLayout_6.addWidget(self.plotTemp1_3, 0, 0, 1, 1)

        self.plotTemp3_3 = QWidget(self.frame_2)
        self.plotTemp3_3.setObjectName(u"plotTemp3_3")
        self.plotTemp3_3.setMinimumSize(QSize(500, 500))

        self.gridLayout_6.addWidget(self.plotTemp3_3, 1, 0, 1, 1)

        self.plotTemp4_3 = QWidget(self.frame_2)
        self.plotTemp4_3.setObjectName(u"plotTemp4_3")
        self.plotTemp4_3.setMinimumSize(QSize(500, 500))

        self.gridLayout_6.addWidget(self.plotTemp4_3, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 1)

        self.Charts_Area_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.Charts_Area_2)

        self.tabWidget.addTab(self.tabGraph, "")

        self.verticalLayout.addWidget(self.tabWidget)

        NewTestPage.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.widgetPort, self.motorId)
        QWidget.setTabOrder(self.motorId, self.widgetStandard)
        QWidget.setTabOrder(self.widgetStandard, self.checkTemp1)
        QWidget.setTabOrder(self.checkTemp1, self.checkTemp2)
        QWidget.setTabOrder(self.checkTemp2, self.checkTemp3)
        QWidget.setTabOrder(self.checkTemp3, self.checkTemp4)
        QWidget.setTabOrder(self.checkTemp4, self.checkTemp5)
        QWidget.setTabOrder(self.checkTemp5, self.checkTemp6)
        QWidget.setTabOrder(self.checkTemp6, self.checkTemp7)
        QWidget.setTabOrder(self.checkTemp7, self.checkTemp8)
        QWidget.setTabOrder(self.checkTemp8, self.checkAmpstart)
        QWidget.setTabOrder(self.checkAmpstart, self.checkAmptotal)
        QWidget.setTabOrder(self.checkAmptotal, self.checkVolt)
        QWidget.setTabOrder(self.checkVolt, self.fetchButton)
        QWidget.setTabOrder(self.fetchButton, self.stopButton)
        QWidget.setTabOrder(self.stopButton, self.saveButton)
        QWidget.setTabOrder(self.saveButton, self.printButton)
        QWidget.setTabOrder(self.printButton, self.tableAverage)
        QWidget.setTabOrder(self.tableAverage, self.tableCompare)
        QWidget.setTabOrder(self.tableCompare, self.Charts_Area)
        QWidget.setTabOrder(self.Charts_Area, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.tableAverage_2)
        QWidget.setTabOrder(self.tableAverage_2, self.tableCompare_2)
        QWidget.setTabOrder(self.tableCompare_2, self.Charts_Area_2)

        self.retranslateUi(NewTestPage)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(NewTestPage)
    # setupUi

    def retranslateUi(self, NewTestPage):
        NewTestPage.setWindowTitle(QCoreApplication.translate("NewTestPage", u"MainWindow", None))
        self.durationAmp.setText(QCoreApplication.translate("NewTestPage", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.checkTemp1.setText(QCoreApplication.translate("NewTestPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 1", None))
        self.intervalTemp.setText(QCoreApplication.translate("NewTestPage", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("NewTestPage", u"\u0632\u0645\u0627\u0646 \u0634\u0631\u0648\u0639 \u062a\u0633\u062a", None))
        self.label_12.setText(QCoreApplication.translate("NewTestPage", u"\u0632\u0645\u0627\u0646 \u062a\u0633\u062a(\u062b\u0627\u0646\u06cc\u0647):", None))
        self.checkTemp4.setText(QCoreApplication.translate("NewTestPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 4", None))
        self.durationTemp.setText(QCoreApplication.translate("NewTestPage", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("NewTestPage", u"\u0646\u0648\u0639 \u06af\u0627\u0632", None))
        self.checkTemp8.setText(QCoreApplication.translate("NewTestPage", u"max \u0633\u0646\u0633\u0648\u0631 \u0641\u0634\u0627\u0631", None))
        self.checkVolt.setText(QCoreApplication.translate("NewTestPage", u"\u0633\u0646\u0633\u0648\u0631 \u0648\u0644\u062a\u0627\u0698", None))
        self.label_14.setText(QCoreApplication.translate("NewTestPage", u"\u0627\u0633\u062a\u0627\u0646\u062f\u0627\u0631\u062f:", None))
        self.intervalAmp.setText(QCoreApplication.translate("NewTestPage", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("NewTestPage", u"\u0632\u0645\u0627\u0646 \u067e\u0627\u06cc\u0627\u0646 \u062a\u0633\u062a", None))
        self.startTime.setText("")
        self.label_16.setText(QCoreApplication.translate("NewTestPage", u"\u062a\u0639\u062f\u0627\u062f \u062c\u0631\u06cc\u0627\u0646", None))
        self.gasType.setText(QCoreApplication.translate("NewTestPage", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("NewTestPage", u"\u067e\u0648\u0631\u062a:", None))
        self.checkTemp7.setText(QCoreApplication.translate("NewTestPage", u"min \u0633\u0646\u0633\u0648\u0631 \u0641\u0634\u0627\u0631", None))
        self.checkTemp5.setText(QCoreApplication.translate("NewTestPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 5", None))
        self.checkTemp3.setText(QCoreApplication.translate("NewTestPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 3", None))
        self.checkAmptotal.setText(QCoreApplication.translate("NewTestPage", u"\u062c\u0631\u06cc\u0627\u0646 \u06a9\u0644", None))
        self.label_20.setText(QCoreApplication.translate("NewTestPage", u"<html><head/><body><p align=\"right\">\u0648\u0636\u0639\u06cc\u062a \u062a\u0633\u062a</p></body></html>", None))
        self.endTime.setText("")
        self.label_13.setText(QCoreApplication.translate("NewTestPage", u"\u062a\u0646\u0627\u0648\u0628 \u0633\u0646\u0633\u0648\u0631(\u062b\u0627\u0646\u06cc\u0647):", None))
        self.label_18.setText(QCoreApplication.translate("NewTestPage", u"\u0632\u0645\u0627\u0646 \u062c\u0631\u06cc\u0627\u0646(\u062b\u0627\u0646\u06cc\u0647):", None))
        self.checkTemp2.setText(QCoreApplication.translate("NewTestPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 2", None))
        self.testResult.setText(QCoreApplication.translate("NewTestPage", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.checkTemp6.setText(QCoreApplication.translate("NewTestPage", u"\u0633\u0646\u0633\u0648\u0631 \u062f\u0645\u0627 6", None))
        self.label_19.setText(QCoreApplication.translate("NewTestPage", u"\u0633\u0631\u06cc\u0627\u0644 \u062f\u0633\u062a\u06af\u0627\u0647:", None))
        self.checkAmpstart.setText(QCoreApplication.translate("NewTestPage", u"\u062c\u0631\u06cc\u0627\u0646 \u0634\u0631\u0648\u0639", None))
        self.fetchButton.setText(QCoreApplication.translate("NewTestPage", u"\u0634\u0631\u0648\u0639 \u062a\u0633\u062a", None))
        self.stopButton.setText(QCoreApplication.translate("NewTestPage", u"\u062a\u0648\u0642\u0641 \u062a\u0633\u062a", None))
        self.saveButton.setText(QCoreApplication.translate("NewTestPage", u"\u062b\u0628\u062a \u062a\u0633\u062a", None))
        self.printButton.setText(QCoreApplication.translate("NewTestPage", u"\u0686\u0627\u067e \u0628\u0627\u0631\u06a9\u062f", None))
#if QT_CONFIG(tooltip)
        self.tabTablePlot.setToolTip(QCoreApplication.translate("NewTestPage", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tabTablePlot.setWhatsThis(QCoreApplication.translate("NewTestPage", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem = self.tableAverage.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("NewTestPage", u"\u062f\u0645\u0627 1", None));
        ___qtablewidgetitem1 = self.tableAverage.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("NewTestPage", u"\u062f\u0645\u0627 2", None));
        ___qtablewidgetitem2 = self.tableAverage.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("NewTestPage", u"\u062f\u0645\u0627 3", None));
        ___qtablewidgetitem3 = self.tableAverage.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("NewTestPage", u"\u062f\u0645\u0627 4", None));
        ___qtablewidgetitem4 = self.tableAverage.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("NewTestPage", u"\u062f\u0645\u0627 5", None));
        ___qtablewidgetitem5 = self.tableAverage.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("NewTestPage", u"\u062f\u0645\u0627 6", None));
        ___qtablewidgetitem6 = self.tableAverage.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("NewTestPage", u"min \u0641\u0634\u0627\u0631", None));
        ___qtablewidgetitem7 = self.tableAverage.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("NewTestPage", u"max \u0641\u0634\u0627\u0631", None));
        ___qtablewidgetitem8 = self.tableAverage.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("NewTestPage", u"\u062c\u0631\u06cc\u0627\u0646 \u06a9\u0644", None));
        ___qtablewidgetitem9 = self.tableAverage.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("NewTestPage", u"\u062c\u0631\u06cc\u0627\u0646 \u0634\u0631\u0648\u0639", None));
        ___qtablewidgetitem10 = self.tableAverage.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("NewTestPage", u"\u0648\u0644\u062a\u0627\u0698", None));
        ___qtablewidgetitem11 = self.tableAverage.verticalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("NewTestPage", u"\u0644\u062d\u0638\u0647 \u0627\u06cc", None));
        ___qtablewidgetitem12 = self.tableAverage.verticalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637", None));
        ___qtablewidgetitem13 = self.tableCompare.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u062f\u0645\u0627 1", None));
        ___qtablewidgetitem14 = self.tableCompare.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u062f\u0645\u0627 2", None));
        ___qtablewidgetitem15 = self.tableCompare.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u062f\u0645\u0627 3", None));
        ___qtablewidgetitem16 = self.tableCompare.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u062f\u0645\u0627 4", None));
        ___qtablewidgetitem17 = self.tableCompare.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u062f\u0645\u0627 5", None));
        ___qtablewidgetitem18 = self.tableCompare.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u062f\u0645\u0627 6", None));
        ___qtablewidgetitem19 = self.tableCompare.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("NewTestPage", u"min \u0645\u062a\u0648\u0633\u0637 \u0641\u0634\u0627\u0631", None));
        ___qtablewidgetitem20 = self.tableCompare.horizontalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("NewTestPage", u"max \u0645\u062a\u0648\u0633\u0637 \u0641\u0634\u0627\u0631", None));
        ___qtablewidgetitem21 = self.tableCompare.horizontalHeaderItem(8)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u062c\u0631\u06cc\u0627\u0646 \u06a9\u0644", None));
        ___qtablewidgetitem22 = self.tableCompare.horizontalHeaderItem(9)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u062c\u0631\u06cc\u0627\u0646 \u0634\u0631\u0648\u0639", None));
        ___qtablewidgetitem23 = self.tableCompare.horizontalHeaderItem(10)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u0648\u0644\u062a\u0627\u0698", None));
        ___qtablewidgetitem24 = self.tableCompare.verticalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("NewTestPage", u"\u062f\u0633\u062a\u06af\u0627\u0647 \u062a\u0633\u062a", None));
        ___qtablewidgetitem25 = self.tableCompare.verticalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("NewTestPage", u"\u0627\u0633\u062a\u0627\u0646\u062f\u0627\u0631\u062f", None));
        ___qtablewidgetitem26 = self.tableCompare.verticalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("NewTestPage", u"\u0646\u062a\u06cc\u062c\u0647", None));

        __sortingEnabled = self.tableCompare.isSortingEnabled()
        self.tableCompare.setSortingEnabled(False)
        self.tableCompare.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTablePlot), QCoreApplication.translate("NewTestPage", u"\u0646\u0645\u0627\u06cc \u062c\u062f\u0648\u0644 \u0648 \u0646\u0645\u0648\u062f\u0627\u0631", None))
        ___qtablewidgetitem27 = self.tableAverage_2.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("NewTestPage", u"\u062f\u0645\u0627 1", None));
        ___qtablewidgetitem28 = self.tableAverage_2.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("NewTestPage", u"\u062f\u0645\u0627 2", None));
        ___qtablewidgetitem29 = self.tableAverage_2.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("NewTestPage", u"\u062f\u0645\u0627 3", None));
        ___qtablewidgetitem30 = self.tableAverage_2.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("NewTestPage", u"\u062f\u0645\u0627 4", None));
        ___qtablewidgetitem31 = self.tableAverage_2.horizontalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("NewTestPage", u"\u062f\u0645\u0627 5", None));
        ___qtablewidgetitem32 = self.tableAverage_2.horizontalHeaderItem(5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("NewTestPage", u"\u062f\u0645\u0627 6", None));
        ___qtablewidgetitem33 = self.tableAverage_2.horizontalHeaderItem(6)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("NewTestPage", u"min \u0641\u0634\u0627\u0631", None));
        ___qtablewidgetitem34 = self.tableAverage_2.horizontalHeaderItem(7)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("NewTestPage", u"max \u0641\u0634\u0627\u0631", None));
        ___qtablewidgetitem35 = self.tableAverage_2.horizontalHeaderItem(8)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("NewTestPage", u"\u062c\u0631\u06cc\u0627\u0646", None));
        ___qtablewidgetitem36 = self.tableAverage_2.horizontalHeaderItem(9)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("NewTestPage", u"\u0648\u0644\u062a\u0627\u0698", None));
        ___qtablewidgetitem37 = self.tableAverage_2.verticalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("NewTestPage", u"\u0644\u062d\u0638\u0647 \u0627\u06cc", None));
        ___qtablewidgetitem38 = self.tableAverage_2.verticalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637", None));
        ___qtablewidgetitem39 = self.tableCompare_2.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u062f\u0645\u0627 1", None));
        ___qtablewidgetitem40 = self.tableCompare_2.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u062f\u0645\u0627 2", None));
        ___qtablewidgetitem41 = self.tableCompare_2.horizontalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u062f\u0645\u0627 3", None));
        ___qtablewidgetitem42 = self.tableCompare_2.horizontalHeaderItem(3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u062f\u0645\u0627 4", None));
        ___qtablewidgetitem43 = self.tableCompare_2.horizontalHeaderItem(4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u062f\u0645\u0627 5", None));
        ___qtablewidgetitem44 = self.tableCompare_2.horizontalHeaderItem(5)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("NewTestPage", u"\u0645\u062a\u0648\u0633\u0637 \u062f\u0645\u0627 6", None));
        ___qtablewidgetitem45 = self.tableCompare_2.horizontalHeaderItem(6)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("NewTestPage", u"min \u0641\u0634\u0627\u0631", None));
        ___qtablewidgetitem46 = self.tableCompare_2.horizontalHeaderItem(7)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("NewTestPage", u"max \u0641\u0634\u0627\u0631", None));
        ___qtablewidgetitem47 = self.tableCompare_2.horizontalHeaderItem(8)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("NewTestPage", u"\u062c\u0631\u06cc\u0627\u0646", None));
        ___qtablewidgetitem48 = self.tableCompare_2.horizontalHeaderItem(9)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("NewTestPage", u"\u0648\u0644\u062a\u0627\u0698", None));
        ___qtablewidgetitem49 = self.tableCompare_2.verticalHeaderItem(0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("NewTestPage", u"\u062f\u0633\u062a\u06af\u0627\u0647 \u062a\u0633\u062a", None));
        ___qtablewidgetitem50 = self.tableCompare_2.verticalHeaderItem(1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("NewTestPage", u"\u0627\u0633\u062a\u0627\u0646\u062f\u0627\u0631\u062f", None));
        ___qtablewidgetitem51 = self.tableCompare_2.verticalHeaderItem(2)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("NewTestPage", u"\u0646\u062a\u06cc\u062c\u0647", None));

        __sortingEnabled1 = self.tableCompare_2.isSortingEnabled()
        self.tableCompare_2.setSortingEnabled(False)
        self.tableCompare_2.setSortingEnabled(__sortingEnabled1)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTable), QCoreApplication.translate("NewTestPage", u"\u0646\u0645\u0627\u06cc \u062c\u062f\u0648\u0644", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGraph), QCoreApplication.translate("NewTestPage", u"\u0646\u0645\u0627\u06cc \u0646\u0645\u0648\u062f\u0627\u0631", None))
    # retranslateUi

