# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_SettingPage(object):
    def setupUi(self, SettingPage):
        if not SettingPage.objectName():
            SettingPage.setObjectName(u"SettingPage")
        SettingPage.resize(1123, 856)
        font = QFont()
        font.setFamilies([u"IRANSansWeb(FaNum)"])
        SettingPage.setFont(font)
        SettingPage.setLayoutDirection(Qt.RightToLeft)
        self.centralwidget = QWidget(SettingPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setLayoutDirection(Qt.RightToLeft)
        self.user = QWidget()
        self.user.setObjectName(u"user")
        self.verticalLayout_2 = QVBoxLayout(self.user)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame_10 = QFrame(self.user)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.userCreateBox = QGroupBox(self.frame_10)
        self.userCreateBox.setObjectName(u"userCreateBox")
        self.userCreateBox.setMaximumSize(QSize(16777215, 200))
        font1 = QFont()
        font1.setFamilies([u"IRANSansWeb(FaNum)"])
        font1.setPointSize(10)
        self.userCreateBox.setFont(font1)
        self.verticalLayout_3 = QVBoxLayout(self.userCreateBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.userCreateBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.userLastName = QLineEdit(self.frame_3)
        self.userLastName.setObjectName(u"userLastName")
        self.userLastName.setMinimumSize(QSize(150, 0))
        self.userLastName.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setFamilies([u"IRANSansWeb(FaNum)"])
        font2.setPointSize(8)
        self.userLastName.setFont(font2)

        self.gridLayout_3.addWidget(self.userLastName, 0, 3, 1, 1)

        self.label_36 = QLabel(self.frame_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(150, 0))
        self.label_36.setMaximumSize(QSize(150, 16777215))
        self.label_36.setFont(font2)
        self.label_36.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_36, 2, 2, 1, 1)

        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(150, 0))
        self.label_33.setMaximumSize(QSize(150, 16777215))
        self.label_33.setFont(font2)
        self.label_33.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_33, 0, 0, 1, 1)

        self.warehouseCheck = QCheckBox(self.frame_3)
        self.warehouseCheck.setObjectName(u"warehouseCheck")
        self.warehouseCheck.setMinimumSize(QSize(150, 0))
        self.warehouseCheck.setMaximumSize(QSize(150, 16777215))
        self.warehouseCheck.setFont(font2)

        self.gridLayout_3.addWidget(self.warehouseCheck, 3, 3, 1, 1)

        self.standardCheck = QCheckBox(self.frame_3)
        self.standardCheck.setObjectName(u"standardCheck")
        self.standardCheck.setMinimumSize(QSize(150, 0))
        self.standardCheck.setMaximumSize(QSize(150, 16777215))
        self.standardCheck.setFont(font2)

        self.gridLayout_3.addWidget(self.standardCheck, 3, 1, 1, 1)

        self.username_input = QLineEdit(self.frame_3)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMinimumSize(QSize(150, 0))
        self.username_input.setMaximumSize(QSize(150, 16777215))
        self.username_input.setFont(font2)

        self.gridLayout_3.addWidget(self.username_input, 2, 1, 1, 1)

        self.testCheck = QCheckBox(self.frame_3)
        self.testCheck.setObjectName(u"testCheck")
        self.testCheck.setMinimumSize(QSize(150, 0))
        self.testCheck.setMaximumSize(QSize(150, 16777215))
        self.testCheck.setFont(font2)

        self.gridLayout_3.addWidget(self.testCheck, 3, 2, 1, 1)

        self.userJob = QLineEdit(self.frame_3)
        self.userJob.setObjectName(u"userJob")
        self.userJob.setMinimumSize(QSize(150, 0))
        self.userJob.setMaximumSize(QSize(150, 16777215))
        self.userJob.setFont(font2)

        self.gridLayout_3.addWidget(self.userJob, 0, 5, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))
        self.label_2.setMaximumSize(QSize(150, 16777215))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_34 = QLabel(self.frame_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(150, 0))
        self.label_34.setMaximumSize(QSize(150, 16777215))
        self.label_34.setFont(font2)
        self.label_34.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_34, 2, 0, 1, 1)

        self.reportCheck = QCheckBox(self.frame_3)
        self.reportCheck.setObjectName(u"reportCheck")
        self.reportCheck.setMinimumSize(QSize(150, 0))
        self.reportCheck.setMaximumSize(QSize(150, 16777215))
        self.reportCheck.setFont(font2)

        self.gridLayout_3.addWidget(self.reportCheck, 3, 4, 1, 1)

        self.label_37 = QLabel(self.frame_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(150, 0))
        self.label_37.setMaximumSize(QSize(150, 16777215))
        self.label_37.setFont(font2)
        self.label_37.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_37, 0, 4, 1, 1)

        self.password_input = QLineEdit(self.frame_3)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(150, 0))
        self.password_input.setMaximumSize(QSize(150, 16777215))
        self.password_input.setFont(font2)

        self.gridLayout_3.addWidget(self.password_input, 2, 3, 1, 1)

        self.userFirstName = QLineEdit(self.frame_3)
        self.userFirstName.setObjectName(u"userFirstName")
        self.userFirstName.setMinimumSize(QSize(150, 0))
        self.userFirstName.setMaximumSize(QSize(150, 16777215))
        self.userFirstName.setFont(font2)

        self.gridLayout_3.addWidget(self.userFirstName, 0, 1, 1, 1)

        self.label_35 = QLabel(self.frame_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(150, 0))
        self.label_35.setMaximumSize(QSize(150, 16777215))
        self.label_35.setFont(font2)
        self.label_35.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_35, 0, 2, 1, 1)

        self.createUserBtn = QPushButton(self.frame_3)
        self.createUserBtn.setObjectName(u"createUserBtn")
        self.createUserBtn.setMinimumSize(QSize(150, 0))
        self.createUserBtn.setMaximumSize(QSize(150, 16777215))
        self.createUserBtn.setFont(font2)

        self.gridLayout_3.addWidget(self.createUserBtn, 4, 5, 1, 1)

        self.assemblyCheck = QCheckBox(self.frame_3)
        self.assemblyCheck.setObjectName(u"assemblyCheck")

        self.gridLayout_3.addWidget(self.assemblyCheck, 3, 5, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_3, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.userCreateBox)

        self.userModifyBox = QGroupBox(self.frame_10)
        self.userModifyBox.setObjectName(u"userModifyBox")
        self.userModifyBox.setMaximumSize(QSize(16777215, 200))
        self.userModifyBox.setFont(font1)
        self.verticalLayout_4 = QVBoxLayout(self.userModifyBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.userModifyBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.userLastNameModify = QLineEdit(self.frame_2)
        self.userLastNameModify.setObjectName(u"userLastNameModify")
        self.userLastNameModify.setMinimumSize(QSize(150, 0))
        self.userLastNameModify.setMaximumSize(QSize(150, 16777215))
        self.userLastNameModify.setFont(font2)

        self.gridLayout_4.addWidget(self.userLastNameModify, 2, 5, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(150, 0))
        self.label_5.setMaximumSize(QSize(150, 16777215))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_5, 4, 2, 1, 1)

        self.label_41 = QLabel(self.frame_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(150, 0))
        self.label_41.setMaximumSize(QSize(150, 16777215))
        self.label_41.setFont(font2)
        self.label_41.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_41, 2, 2, 1, 1)

        self.userFirstNameModify = QLineEdit(self.frame_2)
        self.userFirstNameModify.setObjectName(u"userFirstNameModify")
        self.userFirstNameModify.setMinimumSize(QSize(150, 0))
        self.userFirstNameModify.setMaximumSize(QSize(150, 16777215))
        self.userFirstNameModify.setFont(font2)

        self.gridLayout_4.addWidget(self.userFirstNameModify, 2, 3, 1, 1)

        self.label_39 = QLabel(self.frame_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(150, 0))
        self.label_39.setMaximumSize(QSize(150, 16777215))
        self.label_39.setFont(font2)
        self.label_39.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_39, 0, 2, 1, 1)

        self.usernameCombo = QComboBox(self.frame_2)
        self.usernameCombo.setObjectName(u"usernameCombo")
        self.usernameCombo.setFont(font2)

        self.gridLayout_4.addWidget(self.usernameCombo, 0, 3, 1, 1)

        self.label_28 = QLabel(self.frame_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(150, 0))
        self.label_28.setMaximumSize(QSize(150, 16777215))
        self.label_28.setFont(font2)
        self.label_28.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_28, 0, 4, 1, 1)

        self.label_40 = QLabel(self.frame_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(150, 0))
        self.label_40.setMaximumSize(QSize(150, 16777215))
        self.label_40.setFont(font2)
        self.label_40.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_40, 2, 4, 1, 1)

        self.label_38 = QLabel(self.frame_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(150, 0))
        self.label_38.setMaximumSize(QSize(150, 16777215))
        self.label_38.setFont(font2)
        self.label_38.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_38, 2, 6, 1, 1)

        self.userJobModify = QLineEdit(self.frame_2)
        self.userJobModify.setObjectName(u"userJobModify")
        self.userJobModify.setMinimumSize(QSize(150, 0))
        self.userJobModify.setMaximumSize(QSize(150, 16777215))
        self.userJobModify.setFont(font2)

        self.gridLayout_4.addWidget(self.userJobModify, 2, 7, 1, 1)

        self.passwordModify = QLineEdit(self.frame_2)
        self.passwordModify.setObjectName(u"passwordModify")
        self.passwordModify.setMinimumSize(QSize(150, 0))
        self.passwordModify.setMaximumSize(QSize(150, 16777215))
        self.passwordModify.setFont(font2)

        self.gridLayout_4.addWidget(self.passwordModify, 0, 5, 1, 1)

        self.standardCheckModify = QCheckBox(self.frame_2)
        self.standardCheckModify.setObjectName(u"standardCheckModify")
        self.standardCheckModify.setMinimumSize(QSize(150, 0))
        self.standardCheckModify.setMaximumSize(QSize(150, 16777215))
        self.standardCheckModify.setFont(font2)

        self.gridLayout_4.addWidget(self.standardCheckModify, 4, 3, 1, 1)

        self.testCheckModify = QCheckBox(self.frame_2)
        self.testCheckModify.setObjectName(u"testCheckModify")
        self.testCheckModify.setMinimumSize(QSize(150, 0))
        self.testCheckModify.setMaximumSize(QSize(150, 16777215))
        self.testCheckModify.setFont(font2)

        self.gridLayout_4.addWidget(self.testCheckModify, 4, 4, 1, 1)

        self.reportCheckModify = QCheckBox(self.frame_2)
        self.reportCheckModify.setObjectName(u"reportCheckModify")
        self.reportCheckModify.setMinimumSize(QSize(150, 0))
        self.reportCheckModify.setMaximumSize(QSize(150, 16777215))
        self.reportCheckModify.setFont(font2)

        self.gridLayout_4.addWidget(self.reportCheckModify, 4, 6, 1, 1)

        self.warehouseCheckModify = QCheckBox(self.frame_2)
        self.warehouseCheckModify.setObjectName(u"warehouseCheckModify")
        self.warehouseCheckModify.setMinimumSize(QSize(150, 0))
        self.warehouseCheckModify.setMaximumSize(QSize(150, 16777215))
        self.warehouseCheckModify.setFont(font2)

        self.gridLayout_4.addWidget(self.warehouseCheckModify, 4, 5, 1, 1)

        self.userDeleteBtn = QPushButton(self.frame_2)
        self.userDeleteBtn.setObjectName(u"userDeleteBtn")
        self.userDeleteBtn.setFont(font2)

        self.gridLayout_4.addWidget(self.userDeleteBtn, 5, 7, 1, 1)

        self.userModifyBtn = QPushButton(self.frame_2)
        self.userModifyBtn.setObjectName(u"userModifyBtn")
        self.userModifyBtn.setFont(font2)

        self.gridLayout_4.addWidget(self.userModifyBtn, 5, 6, 1, 1)

        self.assemblycheckModify = QCheckBox(self.frame_2)
        self.assemblycheckModify.setObjectName(u"assemblycheckModify")

        self.gridLayout_4.addWidget(self.assemblycheckModify, 4, 7, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_2, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.userModifyBox)


        self.verticalLayout_2.addWidget(self.frame_10, 0, Qt.AlignTop)

        self.tabWidget.addTab(self.user, "")
        self.sensor = QWidget()
        self.sensor.setObjectName(u"sensor")
        self.verticalLayout_6 = QVBoxLayout(self.sensor)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.step1 = QGroupBox(self.sensor)
        self.step1.setObjectName(u"step1")
        self.step1.setFont(font1)
        self.verticalLayout_5 = QVBoxLayout(self.step1)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.step1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widgetPort = QComboBox(self.frame)
        self.widgetPort.setObjectName(u"widgetPort")
        self.widgetPort.setFont(font2)

        self.gridLayout_2.addWidget(self.widgetPort, 1, 1, 1, 1)

        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)
        self.label_20.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_2.addWidget(self.label_20, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.step1)

        self.step2 = QGroupBox(self.sensor)
        self.step2.setObjectName(u"step2")
        self.step2.setFont(font1)
        self.verticalLayout_7 = QVBoxLayout(self.step2)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.step2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setSpacing(5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.findBaud2 = QPushButton(self.frame_4)
        self.findBaud2.setObjectName(u"findBaud2")
        self.findBaud2.setFont(font2)

        self.gridLayout_7.addWidget(self.findBaud2, 0, 2, 1, 1)

        self.findBaud1 = QPushButton(self.frame_4)
        self.findBaud1.setObjectName(u"findBaud1")
        self.findBaud1.setFont(font2)

        self.gridLayout_7.addWidget(self.findBaud1, 0, 0, 1, 1)

        self.currentBaud2 = QLabel(self.frame_4)
        self.currentBaud2.setObjectName(u"currentBaud2")
        self.currentBaud2.setMinimumSize(QSize(150, 30))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.currentBaud2.setFont(font3)
        self.currentBaud2.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")
        self.currentBaud2.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.currentBaud2, 2, 2, 1, 1)

        self.findBaud3 = QPushButton(self.frame_4)
        self.findBaud3.setObjectName(u"findBaud3")
        self.findBaud3.setFont(font2)

        self.gridLayout_7.addWidget(self.findBaud3, 0, 3, 1, 2)

        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)
        self.label_21.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_7.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)
        self.label_22.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_7.addWidget(self.label_22, 1, 3, 1, 1)

        self.currentBaud1 = QLabel(self.frame_4)
        self.currentBaud1.setObjectName(u"currentBaud1")
        self.currentBaud1.setMinimumSize(QSize(150, 30))
        self.currentBaud1.setFont(font3)
        self.currentBaud1.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")
        self.currentBaud1.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.currentBaud1, 2, 0, 1, 1)

        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout_7.addWidget(self.label_19, 1, 2, 1, 1)

        self.currentBaud3 = QLabel(self.frame_4)
        self.currentBaud3.setObjectName(u"currentBaud3")
        self.currentBaud3.setMinimumSize(QSize(150, 30))
        self.currentBaud3.setFont(font3)
        self.currentBaud3.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout_7.addWidget(self.currentBaud3, 2, 3, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.step2)

        self.step3 = QGroupBox(self.sensor)
        self.step3.setObjectName(u"step3")
        self.step3.setFont(font1)
        self.verticalLayout_9 = QVBoxLayout(self.step3)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.frame_5 = QFrame(self.step3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label222 = QLabel(self.frame_5)
        self.label222.setObjectName(u"label222")
        self.label222.setFont(font2)
        self.label222.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.gridLayout.addWidget(self.label222, 2, 1, 1, 1)

        self.widgetBaud = QComboBox(self.frame_5)
        self.widgetBaud.setObjectName(u"widgetBaud")
        self.widgetBaud.setFont(font2)

        self.gridLayout.addWidget(self.widgetBaud, 2, 2, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_5, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.step3)

        self.step4 = QGroupBox(self.sensor)
        self.step4.setObjectName(u"step4")
        self.step4.setFont(font1)
        self.verticalLayout_10 = QVBoxLayout(self.step4)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.frame_6 = QFrame(self.step4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.baudButton2 = QPushButton(self.frame_6)
        self.baudButton2.setObjectName(u"baudButton2")
        self.baudButton2.setMinimumSize(QSize(150, 0))
        self.baudButton2.setFont(font2)

        self.gridLayout_5.addWidget(self.baudButton2, 0, 2, 1, 1)

        self.baudButton1 = QPushButton(self.frame_6)
        self.baudButton1.setObjectName(u"baudButton1")
        self.baudButton1.setMinimumSize(QSize(150, 0))
        self.baudButton1.setFont(font2)

        self.gridLayout_5.addWidget(self.baudButton1, 0, 1, 1, 1)

        self.baudButton3 = QPushButton(self.frame_6)
        self.baudButton3.setObjectName(u"baudButton3")
        self.baudButton3.setMinimumSize(QSize(150, 0))
        self.baudButton3.setFont(font2)

        self.gridLayout_5.addWidget(self.baudButton3, 0, 3, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_6, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.step4)

        self.rateTable = QGroupBox(self.sensor)
        self.rateTable.setObjectName(u"rateTable")
        self.rateTable.setFont(font1)
        self.verticalLayout_8 = QVBoxLayout(self.rateTable)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.tableWidget = QTableWidget(self.rateTable)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font2)

        self.verticalLayout_8.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.rateTable)

        self.tabWidget.addTab(self.sensor, "")
        self.datebase = QWidget()
        self.datebase.setObjectName(u"datebase")
        self.verticalLayout_11 = QVBoxLayout(self.datebase)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_9 = QFrame(self.datebase)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 5, 0, 0)
        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.frame_7)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(80, 0))
        self.label_44.setMaximumSize(QSize(80, 16777215))
        self.label_44.setFont(font2)
        self.label_44.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_44)

        self.dbIP = QLineEdit(self.frame_7)
        self.dbIP.setObjectName(u"dbIP")
        self.dbIP.setMinimumSize(QSize(150, 0))
        self.dbIP.setMaximumSize(QSize(150, 16777215))
        self.dbIP.setFont(font2)

        self.horizontalLayout.addWidget(self.dbIP)

        self.label_43 = QLabel(self.frame_7)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(100, 0))
        self.label_43.setMaximumSize(QSize(150, 16777215))
        self.label_43.setFont(font2)
        self.label_43.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_43)

        self.dbUser = QLineEdit(self.frame_7)
        self.dbUser.setObjectName(u"dbUser")
        self.dbUser.setMinimumSize(QSize(150, 0))
        self.dbUser.setMaximumSize(QSize(150, 16777215))
        self.dbUser.setFont(font2)

        self.horizontalLayout.addWidget(self.dbUser)

        self.label_42 = QLabel(self.frame_7)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(100, 0))
        self.label_42.setMaximumSize(QSize(150, 16777215))
        self.label_42.setFont(font2)
        self.label_42.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_42.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_42)

        self.dbPass = QLineEdit(self.frame_7)
        self.dbPass.setObjectName(u"dbPass")
        self.dbPass.setMinimumSize(QSize(150, 0))
        self.dbPass.setMaximumSize(QSize(150, 16777215))
        self.dbPass.setFont(font2)

        self.horizontalLayout.addWidget(self.dbPass)

        self.label_45 = QLabel(self.frame_7)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(100, 0))
        self.label_45.setMaximumSize(QSize(150, 16777215))
        self.label_45.setFont(font2)
        self.label_45.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_45)

        self.dbName = QLineEdit(self.frame_7)
        self.dbName.setObjectName(u"dbName")
        self.dbName.setMinimumSize(QSize(150, 0))
        self.dbName.setMaximumSize(QSize(150, 16777215))
        self.dbName.setFont(font2)

        self.horizontalLayout.addWidget(self.dbName)


        self.verticalLayout_12.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 50))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dbChange = QCheckBox(self.frame_8)
        self.dbChange.setObjectName(u"dbChange")
        self.dbChange.setFont(font2)

        self.horizontalLayout_2.addWidget(self.dbChange)

        self.dbModifyBtn = QPushButton(self.frame_8)
        self.dbModifyBtn.setObjectName(u"dbModifyBtn")
        self.dbModifyBtn.setMinimumSize(QSize(150, 0))
        self.dbModifyBtn.setMaximumSize(QSize(150, 16777215))
        self.dbModifyBtn.setFont(font2)

        self.horizontalLayout_2.addWidget(self.dbModifyBtn)


        self.verticalLayout_12.addWidget(self.frame_8)


        self.verticalLayout_11.addWidget(self.frame_9, 0, Qt.AlignLeft|Qt.AlignTop)

        self.tabWidget.addTab(self.datebase, "")

        self.verticalLayout.addWidget(self.tabWidget)

        SettingPage.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.userFirstName, self.userLastName)
        QWidget.setTabOrder(self.userLastName, self.userJob)
        QWidget.setTabOrder(self.userJob, self.username_input)
        QWidget.setTabOrder(self.username_input, self.password_input)
        QWidget.setTabOrder(self.password_input, self.standardCheck)
        QWidget.setTabOrder(self.standardCheck, self.testCheck)
        QWidget.setTabOrder(self.testCheck, self.warehouseCheck)
        QWidget.setTabOrder(self.warehouseCheck, self.reportCheck)
        QWidget.setTabOrder(self.reportCheck, self.usernameCombo)
        QWidget.setTabOrder(self.usernameCombo, self.passwordModify)
        QWidget.setTabOrder(self.passwordModify, self.userFirstNameModify)
        QWidget.setTabOrder(self.userFirstNameModify, self.userLastNameModify)
        QWidget.setTabOrder(self.userLastNameModify, self.userJobModify)
        QWidget.setTabOrder(self.userJobModify, self.standardCheckModify)
        QWidget.setTabOrder(self.standardCheckModify, self.testCheckModify)
        QWidget.setTabOrder(self.testCheckModify, self.warehouseCheckModify)
        QWidget.setTabOrder(self.warehouseCheckModify, self.reportCheckModify)
        QWidget.setTabOrder(self.reportCheckModify, self.userModifyBtn)
        QWidget.setTabOrder(self.userModifyBtn, self.userDeleteBtn)
        QWidget.setTabOrder(self.userDeleteBtn, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.widgetPort)
        QWidget.setTabOrder(self.widgetPort, self.findBaud1)
        QWidget.setTabOrder(self.findBaud1, self.findBaud2)
        QWidget.setTabOrder(self.findBaud2, self.findBaud3)
        QWidget.setTabOrder(self.findBaud3, self.widgetBaud)
        QWidget.setTabOrder(self.widgetBaud, self.baudButton1)
        QWidget.setTabOrder(self.baudButton1, self.baudButton2)
        QWidget.setTabOrder(self.baudButton2, self.baudButton3)
        QWidget.setTabOrder(self.baudButton3, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.dbIP)
        QWidget.setTabOrder(self.dbIP, self.dbUser)
        QWidget.setTabOrder(self.dbUser, self.dbPass)
        QWidget.setTabOrder(self.dbPass, self.dbName)
        QWidget.setTabOrder(self.dbName, self.dbChange)
        QWidget.setTabOrder(self.dbChange, self.dbModifyBtn)

        self.retranslateUi(SettingPage)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingPage)
    # setupUi

    def retranslateUi(self, SettingPage):
        SettingPage.setWindowTitle(QCoreApplication.translate("SettingPage", u"MainWindow", None))
        self.userCreateBox.setTitle(QCoreApplication.translate("SettingPage", u"\u06a9\u0627\u0631\u0628\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0631 \u062c\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u062f\u06cc\u062f", None))
        self.label_36.setText(QCoreApplication.translate("SettingPage", u"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631", None))
        self.label_33.setText(QCoreApplication.translate("SettingPage", u"\u0646\u0627\u0645", None))
        self.warehouseCheck.setText(QCoreApplication.translate("SettingPage", u"\u0627\u0646\u0628\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0627\u0631", None))
        self.standardCheck.setText(QCoreApplication.translate("SettingPage", u"\u0627\u0633\u062a\u0627\u0646\u062f\u0627\u0631\u062f\u0647\u0627", None))
        self.testCheck.setText(QCoreApplication.translate("SettingPage", u"\u062a\u0633\u062a \u062f\u0633\u062a\u06af\u0627\u0647", None))
        self.label_2.setText(QCoreApplication.translate("SettingPage", u"\u062f\u0633\u062a\u0631\u0633\u06cc:", None))
        self.label_34.setText(QCoreApplication.translate("SettingPage", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc", None))
        self.reportCheck.setText(QCoreApplication.translate("SettingPage", u"\u06af\u0632\u0627\u0631\u0634 \u0647\u0627", None))
        self.label_37.setText(QCoreApplication.translate("SettingPage", u"\u0633\u0645\u062a", None))
        self.label_35.setText(QCoreApplication.translate("SettingPage", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc", None))
        self.createUserBtn.setText(QCoreApplication.translate("SettingPage", u"\u062b\u0628\u062a \u06a9\u0627\u0631\u0628\u0631", None))
        self.assemblyCheck.setText(QCoreApplication.translate("SettingPage", u"\u0627\u06cc\u062c\u0627\u062f \u0628\u0633\u062a\u0647", None))
        self.userModifyBox.setTitle(QCoreApplication.translate("SettingPage", u"\u0648\u06cc\u0640\u0640\u0640\u0640\u0640\u0640\u0631\u0627\u06cc\u0634 \u06a9\u0627\u0631\u0628\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0631\u0627\u0646", None))
        self.label_5.setText(QCoreApplication.translate("SettingPage", u"\u062f\u0633\u062a\u0631\u0633\u06cc:", None))
        self.label_41.setText(QCoreApplication.translate("SettingPage", u"\u0646\u0627\u0645", None))
        self.label_39.setText(QCoreApplication.translate("SettingPage", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc", None))
        self.label_28.setText(QCoreApplication.translate("SettingPage", u"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631", None))
        self.label_40.setText(QCoreApplication.translate("SettingPage", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc", None))
        self.label_38.setText(QCoreApplication.translate("SettingPage", u"\u0633\u0645\u062a", None))
        self.standardCheckModify.setText(QCoreApplication.translate("SettingPage", u"\u0627\u0633\u062a\u0627\u0646\u062f\u0627\u0631\u062f\u0647\u0627", None))
        self.testCheckModify.setText(QCoreApplication.translate("SettingPage", u"\u062a\u0633\u062a \u062f\u0633\u062a\u06af\u0627\u0647", None))
        self.reportCheckModify.setText(QCoreApplication.translate("SettingPage", u"\u06af\u0632\u0627\u0631\u0634 \u0647\u0627", None))
        self.warehouseCheckModify.setText(QCoreApplication.translate("SettingPage", u"\u0627\u0646\u0628\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0627\u0631", None))
        self.userDeleteBtn.setText(QCoreApplication.translate("SettingPage", u"\u062d\u0630\u0641", None))
        self.userModifyBtn.setText(QCoreApplication.translate("SettingPage", u"\u0648\u06cc\u0631\u0627\u06cc\u0634", None))
        self.assemblycheckModify.setText(QCoreApplication.translate("SettingPage", u"\u0627\u06cc\u062c\u0627\u062f \u0628\u0633\u062a\u0647", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user), QCoreApplication.translate("SettingPage", u"\u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        self.step1.setTitle(QCoreApplication.translate("SettingPage", u"\u0642\u062f\u0645 \u0627\u0648\u0644: \u0627\u0646\u062a\u062e\u0627\u0628 \u067e\u0648\u0631\u062a \u062f\u0633\u062a\u06af\u0627\u0647", None))
        self.label_20.setText(QCoreApplication.translate("SettingPage", u"\u067e\u0648\u0631\u062a \u062f\u0633\u062a\u06af\u0627\u0647:", None))
        self.step2.setTitle(QCoreApplication.translate("SettingPage", u"\u0642\u062f\u0645 \u062f\u0648\u0645: \u0645\u0634\u0627\u0647\u062f\u0647 \u0631\u06cc\u062a \u0647\u0627\u06cc \u0641\u0639\u0644\u06cc", None))
        self.findBaud2.setText(QCoreApplication.translate("SettingPage", u"\u0628\u0631\u0648\u0632\u0631\u0633\u0627\u0646\u06cc", None))
        self.findBaud1.setText(QCoreApplication.translate("SettingPage", u"\u0628\u0631\u0648\u0632\u0631\u0633\u0627\u0646\u06cc", None))
        self.currentBaud2.setText("")
        self.findBaud3.setText(QCoreApplication.translate("SettingPage", u"\u0628\u0631\u0648\u0632\u0631\u0633\u0627\u0646\u06cc", None))
        self.label_21.setText(QCoreApplication.translate("SettingPage", u"\u0645\u0642\u062f\u0627\u0631 \u0641\u0639\u0644\u06cc \u0631\u06cc\u062a 1:", None))
        self.label_22.setText(QCoreApplication.translate("SettingPage", u"\u0645\u0642\u062f\u0627\u0631 \u0641\u0639\u0644\u06cc \u0631\u06cc\u062a 3:", None))
        self.currentBaud1.setText("")
        self.label_19.setText(QCoreApplication.translate("SettingPage", u"\u0645\u0642\u062f\u0627\u0631 \u0641\u0639\u0644\u06cc \u0631\u06cc\u062a 2:", None))
        self.currentBaud3.setText("")
        self.step3.setTitle(QCoreApplication.translate("SettingPage", u"\u0642\u062f\u0645 \u0633\u0648\u0645: \u0627\u0646\u062a\u062e\u0627\u0628 \u0631\u06cc\u062a \u0645\u0648\u0631\u062f \u0646\u0638\u0631 (\u0645\u0637\u0627\u0628\u0642 \u062c\u062f\u0648\u0644)", None))
        self.label222.setText(QCoreApplication.translate("SettingPage", u"\u0645\u0642\u062f\u0627\u0631 \u0639\u062f\u062f\u06cc \u0631\u06cc\u062a \u0645\u0648\u0631\u062f \u0646\u0638\u0631:", None))
        self.step4.setTitle(QCoreApplication.translate("SettingPage", u"\u0642\u062f\u0645 \u0622\u062e\u0631: \u062a\u063a\u06cc\u06cc\u0631 \u0631\u06cc\u062a", None))
        self.baudButton2.setText(QCoreApplication.translate("SettingPage", u"\u062a\u063a\u06cc\u06cc\u0631 \u0631\u06cc\u062a 2", None))
        self.baudButton1.setText(QCoreApplication.translate("SettingPage", u"\u062a\u063a\u06cc\u06cc\u0631 \u0631\u06cc\u062a 1", None))
        self.baudButton3.setText(QCoreApplication.translate("SettingPage", u"\u062a\u063a\u06cc\u06cc\u0631 \u0631\u06cc\u062a 3", None))
        self.rateTable.setTitle(QCoreApplication.translate("SettingPage", u"\u062c\u062f\u0648\u0644 \u0631\u06cc\u062a \u0647\u0627", None))
        ___qtablewidgetitem = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SettingPage", u"baudrate", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem1 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SettingPage", u"2400b/s", None));
        ___qtablewidgetitem2 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SettingPage", u"4800b/s", None));
        ___qtablewidgetitem3 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SettingPage", u"9600b/s", None));
        ___qtablewidgetitem4 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SettingPage", u"19200b/s", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SettingPage", u"38400b/s", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sensor), QCoreApplication.translate("SettingPage", u"\u0633\u0646\u0633\u0648\u0631", None))
        self.label_44.setText(QCoreApplication.translate("SettingPage", u"\u0622\u062f\u0631\u0633 \u062f\u06cc\u062a\u0627\u0628\u06cc\u0633", None))
        self.label_43.setText(QCoreApplication.translate("SettingPage", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc", None))
        self.label_42.setText(QCoreApplication.translate("SettingPage", u"\u0631\u0648\u0632 \u0639\u0628\u0648\u0631", None))
        self.label_45.setText(QCoreApplication.translate("SettingPage", u"\u0646\u0627\u0645 \u062f\u06cc\u062a\u0627\u0628\u06cc\u0633", None))
        self.dbChange.setText(QCoreApplication.translate("SettingPage", u"\u062f\u0631 \u0635\u0648\u0631\u062a\u06cc \u06a9\u0647 \u0633\u0631\u0648\u0631 \u062f\u06cc\u062a\u0627\u0628\u06cc\u0633 \u062a\u063a\u06cc\u06cc\u0631 \u06a9\u0631\u062f\u0647 \u0627\u0633\u062a \u0627\u06cc\u0646 \u062a\u06cc\u06a9 \u0631\u0627 \u0628\u0632\u0646\u06cc\u062f", None))
        self.dbModifyBtn.setText(QCoreApplication.translate("SettingPage", u"\u0628\u0631\u0648\u0632 \u0631\u0633\u0627\u0646\u06cc", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.datebase), QCoreApplication.translate("SettingPage", u"\u062f\u06cc\u062a\u0627\u0628\u06cc\u0633", None))
    # retranslateUi

