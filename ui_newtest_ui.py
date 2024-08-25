# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\armin\Desktop\PLC-QMS-Warehouse\ui_newtest.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewTestPage(object):
    def setupUi(self, NewTestPage):
        NewTestPage.setObjectName("NewTestPage")
        NewTestPage.resize(1394, 859)
        self.centralwidget = QtWidgets.QWidget(NewTestPage)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Test_Properties = QtWidgets.QFrame(self.centralwidget)
        self.Test_Properties.setFrameShape(QtCore.Qt.QFrame::Shape::StyledPanel)
        self.Test_Properties.setFrameShadow(QtCore.Qt.QFrame::Shadow::Raised)
        self.Test_Properties.setObjectName("Test_Properties")
        self.gridLayout = QtWidgets.QGridLayout(self.Test_Properties)
        self.gridLayout.setObjectName("gridLayout")
        self.motorId = QtWidgets.QLineEdit(self.Test_Properties)
        self.motorId.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motorId.sizePolicy().hasHeightForWidth())
        self.motorId.setSizePolicy(sizePolicy)
        self.motorId.setMinimumSize(QtCore.QSize(0, 20))
        self.motorId.setMaximumSize(QtCore.QSize(16777215, 30))
        self.motorId.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.motorId.setObjectName("motorId")
        self.gridLayout.addWidget(self.motorId, 0, 43, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignRight|QtCore.Qt.Qt::AlignmentFlag::AlignTrailing|QtCore.Qt.Qt::AlignmentFlag::AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 40, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.Test_Properties)
        self.saveButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        font.setBold(True)
        self.saveButton.setFont(font)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentSave")
        self.saveButton.setIcon(icon)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 35, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignRight|QtCore.Qt.Qt::AlignmentFlag::AlignTrailing|QtCore.Qt.Qt::AlignmentFlag::AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 44, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_19.setFont(font)
        self.label_19.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_19.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignRight|QtCore.Qt.Qt::AlignmentFlag::AlignTrailing|QtCore.Qt.Qt::AlignmentFlag::AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 44, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_12.setFont(font)
        self.label_12.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_12.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignRight|QtCore.Qt.Qt::AlignmentFlag::AlignTrailing|QtCore.Qt.Qt::AlignmentFlag::AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 36, 1, 1)
        self.widgetPort = QtWidgets.QComboBox(self.Test_Properties)
        self.widgetPort.setObjectName("widgetPort")
        self.gridLayout.addWidget(self.widgetPort, 0, 45, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_17.setFont(font)
        self.label_17.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_17.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignRight|QtCore.Qt.Qt::AlignmentFlag::AlignTrailing|QtCore.Qt.Qt::AlignmentFlag::AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 47, 1, 1)
        self.startTime = QtWidgets.QLabel(self.Test_Properties)
        self.startTime.setMaximumSize(QtCore.QSize(16777215, 30))
        self.startTime.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")
        self.startTime.setText("")
        self.startTime.setObjectName("startTime")
        self.gridLayout.addWidget(self.startTime, 1, 45, 1, 1)
        self.gasType = QtWidgets.QLabel(self.Test_Properties)
        self.gasType.setMinimumSize(QtCore.QSize(0, 20))
        self.gasType.setMaximumSize(QtCore.QSize(16777215, 30))
        self.gasType.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")
        self.gasType.setObjectName("gasType")
        self.gridLayout.addWidget(self.gasType, 0, 39, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignRight|QtCore.Qt.Qt::AlignmentFlag::AlignTrailing|QtCore.Qt.Qt::AlignmentFlag::AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 38, 1, 1)
        self.endTime = QtWidgets.QLabel(self.Test_Properties)
        self.endTime.setMaximumSize(QtCore.QSize(16777215, 30))
        self.endTime.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")
        self.endTime.setText("")
        self.endTime.setObjectName("endTime")
        self.gridLayout.addWidget(self.endTime, 1, 43, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        font.setBold(False)
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(QtCore.Qt.Qt::LayoutDirection::RightToLeft)
        self.label_20.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_20.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignLeading|QtCore.Qt.Qt::AlignmentFlag::AlignLeft|QtCore.Qt.Qt::AlignmentFlag::AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 1, 42, 1, 1)
        self.widgetModel = QtWidgets.QComboBox(self.Test_Properties)
        self.widgetModel.setObjectName("widgetModel")
        self.gridLayout.addWidget(self.widgetModel, 0, 41, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_14.setFont(font)
        self.label_14.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_14.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignRight|QtCore.Qt.Qt::AlignmentFlag::AlignTrailing|QtCore.Qt.Qt::AlignmentFlag::AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 42, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.Test_Properties)
        self.stopButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        font.setBold(True)
        self.stopButton.setFont(font)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::ApplicationExit")
        self.stopButton.setIcon(icon)
        self.stopButton.setIconSize(QtCore.QSize(15, 15))
        self.stopButton.setObjectName("stopButton")
        self.gridLayout.addWidget(self.stopButton, 1, 36, 1, 1)
        self.durationTemp = QtWidgets.QLabel(self.Test_Properties)
        self.durationTemp.setMinimumSize(QtCore.QSize(0, 20))
        self.durationTemp.setMaximumSize(QtCore.QSize(16777215, 30))
        self.durationTemp.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")
        self.durationTemp.setObjectName("durationTemp")
        self.gridLayout.addWidget(self.durationTemp, 0, 35, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        self.label_21.setFont(font)
        self.label_21.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label_21.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignRight|QtCore.Qt.Qt::AlignmentFlag::AlignTrailing|QtCore.Qt.Qt::AlignmentFlag::AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 1, 47, 1, 1)
        self.widgetTestType = QtWidgets.QComboBox(self.Test_Properties)
        self.widgetTestType.setObjectName("widgetTestType")
        self.gridLayout.addWidget(self.widgetTestType, 0, 37, 1, 1)
        self.fetchButton = QtWidgets.QPushButton(self.Test_Properties)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        font.setBold(True)
        self.fetchButton.setFont(font)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::MediaPlaybackStart")
        self.fetchButton.setIcon(icon)
        self.fetchButton.setObjectName("fetchButton")
        self.gridLayout.addWidget(self.fetchButton, 1, 37, 1, 1)
        self.testResult = QtWidgets.QLabel(self.Test_Properties)
        self.testResult.setMaximumSize(QtCore.QSize(16777215, 30))
        self.testResult.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")
        self.testResult.setObjectName("testResult")
        self.gridLayout.addWidget(self.testResult, 1, 38, 1, 4)
        self.verticalLayout.addWidget(self.Test_Properties)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.Qt::LayoutDirection::RightToLeft)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.tabWidget.setObjectName("tabWidget")
        self.tabTablePlot = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        font.setPointSize(8)
        self.tabTablePlot.setFont(font)
        self.tabTablePlot.setObjectName("tabTablePlot")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabTablePlot)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Charts_Area = QtWidgets.QScrollArea(self.tabTablePlot)
        self.Charts_Area.setWidgetResizable(True)
        self.Charts_Area.setObjectName("Charts_Area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1325, 2000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(1000, 2000))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtCore.Qt.QFrame::Shape::StyledPanel)
        self.frame.setFrameShadow(QtCore.Qt.QFrame::Shadow::Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.Charts_Area.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.Charts_Area)
        self.tabWidget.addTab(self.tabTablePlot, "")
        self.tabTable = QtWidgets.QWidget()
        self.tabTable.setObjectName("tabTable")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabTable)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableAverage = QtWidgets.QTableWidget(self.tabTable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableAverage.sizePolicy().hasHeightForWidth())
        self.tableAverage.setSizePolicy(sizePolicy)
        self.tableAverage.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum)")
        font.setPointSize(8)
        self.tableAverage.setFont(font)
        self.tableAverage.setLayoutDirection(QtCore.Qt.Qt::LayoutDirection::RightToLeft)
        self.tableAverage.setStyleSheet("")
        self.tableAverage.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.tableAverage.setVerticalScrollBarPolicy(QtCore.Qt.Qt::ScrollBarPolicy::ScrollBarAlwaysOff)
        self.tableAverage.setHorizontalScrollBarPolicy(QtCore.Qt.Qt::ScrollBarPolicy::ScrollBarAlwaysOff)
        self.tableAverage.setSizeAdjustPolicy(QtCore.Qt.QAbstractScrollArea::SizeAdjustPolicy::AdjustToContentsOnFirstShow)
        self.tableAverage.setEditTriggers(QtCore.Qt.QAbstractItemView::EditTrigger::NoEditTriggers)
        self.tableAverage.setObjectName("tableAverage")
        self.tableAverage.setColumnCount(11)
        self.tableAverage.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableAverage.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAverage.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAverage.setHorizontalHeaderItem(10, item)
        self.tableAverage.horizontalHeader().setCascadingSectionResizes(True)
        self.tableAverage.horizontalHeader().setDefaultSectionSize(100)
        self.tableAverage.horizontalHeader().setSortIndicatorShown(False)
        self.tableAverage.horizontalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.tableAverage, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.tabTable)
        self.widget.setObjectName("widget")
        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabTable, "")
        self.verticalLayout.addWidget(self.tabWidget)
        NewTestPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewTestPage)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NewTestPage)
        NewTestPage.setTabOrder(self.widgetPort, self.motorId)
        NewTestPage.setTabOrder(self.motorId, self.widgetModel)
        NewTestPage.setTabOrder(self.widgetModel, self.widgetTestType)
        NewTestPage.setTabOrder(self.widgetTestType, self.fetchButton)
        NewTestPage.setTabOrder(self.fetchButton, self.stopButton)
        NewTestPage.setTabOrder(self.stopButton, self.saveButton)
        NewTestPage.setTabOrder(self.saveButton, self.tabWidget)
        NewTestPage.setTabOrder(self.tabWidget, self.tableAverage)
        NewTestPage.setTabOrder(self.tableAverage, self.Charts_Area)

    def retranslateUi(self, NewTestPage):
        _translate = QtCore.QCoreApplication.translate
        NewTestPage.setWindowTitle(_translate("NewTestPage", "MainWindow"))
        self.label_6.setText(_translate("NewTestPage", "نوع گاز:"))
        self.saveButton.setText(_translate("NewTestPage", "ثبت"))
        self.label_7.setText(_translate("NewTestPage", "زمان پایان تست:"))
        self.label_19.setText(_translate("NewTestPage", "سریال دستگاه:"))
        self.label_12.setText(_translate("NewTestPage", "زمان تست (دقیقه):"))
        self.label_17.setText(_translate("NewTestPage", "پورت:"))
        self.gasType.setText(_translate("NewTestPage", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("NewTestPage", "نوع تست:"))
        self.label_20.setText(_translate("NewTestPage", "<html><head/><body><p>:وضعیت تست</p></body></html>"))
        self.label_14.setText(_translate("NewTestPage", "نوع دستگاه:"))
        self.stopButton.setText(_translate("NewTestPage", "توقف"))
        self.durationTemp.setText(_translate("NewTestPage", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_21.setText(_translate("NewTestPage", "زمان شروع تست:"))
        self.fetchButton.setText(_translate("NewTestPage", "شروع"))
        self.testResult.setText(_translate("NewTestPage", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.tabTablePlot.setToolTip(_translate("NewTestPage", "<html><head/><body><p><br/></p></body></html>"))
        self.tabTablePlot.setWhatsThis(_translate("NewTestPage", "<html><head/><body><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTablePlot), _translate("NewTestPage", "نمای نمودار"))
        self.tableAverage.setSortingEnabled(True)
        item = self.tableAverage.verticalHeaderItem(0)
        item.setText(_translate("NewTestPage", "لحظه ای"))
        item = self.tableAverage.verticalHeaderItem(1)
        item.setText(_translate("NewTestPage", "متوسط"))
        item = self.tableAverage.horizontalHeaderItem(0)
        item.setText(_translate("NewTestPage", "دمای محیط 1"))
        item = self.tableAverage.horizontalHeaderItem(1)
        item.setText(_translate("NewTestPage", "دمای محیط 2"))
        item = self.tableAverage.horizontalHeaderItem(2)
        item.setText(_translate("NewTestPage", "دمای خروجی 1"))
        item = self.tableAverage.horizontalHeaderItem(3)
        item.setText(_translate("NewTestPage", "دمای خروجی 2"))
        item = self.tableAverage.horizontalHeaderItem(4)
        item.setText(_translate("NewTestPage", "دمای لوله ورودی"))
        item = self.tableAverage.horizontalHeaderItem(5)
        item.setText(_translate("NewTestPage", "دمای لوله خروجی"))
        item = self.tableAverage.horizontalHeaderItem(6)
        item.setText(_translate("NewTestPage", "فشار لوله ورودی"))
        item = self.tableAverage.horizontalHeaderItem(7)
        item.setText(_translate("NewTestPage", "فشار لوله خروجی"))
        item = self.tableAverage.horizontalHeaderItem(8)
        item.setText(_translate("NewTestPage", "جریان"))
        item = self.tableAverage.horizontalHeaderItem(9)
        item.setText(_translate("NewTestPage", "وات مصرفی"))
        item = self.tableAverage.horizontalHeaderItem(10)
        item.setText(_translate("NewTestPage", "ولتاژ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTable), _translate("NewTestPage", "نمای جدول"))
