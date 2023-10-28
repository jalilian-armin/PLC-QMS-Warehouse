# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1229, 866)
        MainWindow.setMinimumSize(QtCore.QSize(0, 500))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header = QtWidgets.QFrame(self.centralwidget)
        self.Header.setMinimumSize(QtCore.QSize(0, 50))
        self.Header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Header.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logoFrame = QtWidgets.QFrame(self.Header)
        self.logoFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.logoFrame.setMaximumSize(QtCore.QSize(200, 50))
        self.logoFrame.setStyleSheet("")
        self.logoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logoFrame.setObjectName("logoFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.logoFrame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Logo = QtWidgets.QPushButton(self.logoFrame)
        self.Logo.setMaximumSize(QtCore.QSize(200, 50))
        self.Logo.setStyleSheet("background-color: none;\n"
"border: remove;")
        self.Logo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Logo.setIcon(icon)
        self.Logo.setIconSize(QtCore.QSize(180, 20))
        self.Logo.setObjectName("Logo")
        self.verticalLayout_6.addWidget(self.Logo)
        self.horizontalLayout.addWidget(self.logoFrame)
        self.titleFrame = QtWidgets.QFrame(self.Header)
        self.titleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleFrame.setObjectName("titleFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.titleFrame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.menuTitle = QtWidgets.QLabel(self.titleFrame)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum) Medium")
        font.setPointSize(20)
        self.menuTitle.setFont(font)
        self.menuTitle.setObjectName("menuTitle")
        self.verticalLayout_5.addWidget(self.menuTitle)
        self.horizontalLayout.addWidget(self.titleFrame)
        self.User_Info = QtWidgets.QFrame(self.Header)
        self.User_Info.setMinimumSize(QtCore.QSize(150, 50))
        self.User_Info.setMaximumSize(QtCore.QSize(150, 50))
        self.User_Info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.User_Info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.User_Info.setObjectName("User_Info")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.User_Info)
        self.verticalLayout_7.setContentsMargins(0, 5, 5, 5)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.User_Job = QtWidgets.QLabel(self.User_Info)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum) Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.User_Job.setFont(font)
        self.User_Job.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.User_Job.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.User_Job.setObjectName("User_Job")
        self.verticalLayout_7.addWidget(self.User_Job)
        self.User_Name = QtWidgets.QLabel(self.User_Info)
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum) Medium")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.User_Name.setFont(font)
        self.User_Name.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.User_Name.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.User_Name.setObjectName("User_Name")
        self.verticalLayout_7.addWidget(self.User_Name)
        self.horizontalLayout.addWidget(self.User_Info, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.Header)
        self.Body = QtWidgets.QFrame(self.centralwidget)
        self.Body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Body.setObjectName("Body")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Body)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Main_Body = QtWidgets.QFrame(self.Body)
        self.Main_Body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main_Body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_Body.setObjectName("Main_Body")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Main_Body)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Stacked_Pages = QtWidgets.QStackedWidget(self.Main_Body)
        self.Stacked_Pages.setEnabled(True)
        self.Stacked_Pages.setObjectName("Stacked_Pages")
        self.Test_Page = QtWidgets.QWidget()
        self.Test_Page.setObjectName("Test_Page")
        self.Stacked_Pages.addWidget(self.Test_Page)
        self.Standards_Page = QtWidgets.QWidget()
        self.Standards_Page.setObjectName("Standards_Page")
        self.Stacked_Pages.addWidget(self.Standards_Page)
        self.Reports_Page = QtWidgets.QWidget()
        self.Reports_Page.setObjectName("Reports_Page")
        self.Stacked_Pages.addWidget(self.Reports_Page)
        self.Warehouse_Page = QtWidgets.QWidget()
        self.Warehouse_Page.setObjectName("Warehouse_Page")
        self.Stacked_Pages.addWidget(self.Warehouse_Page)
        self.Settings_Page = QtWidgets.QWidget()
        self.Settings_Page.setObjectName("Settings_Page")
        self.Stacked_Pages.addWidget(self.Settings_Page)
        self.Help_Page = QtWidgets.QWidget()
        self.Help_Page.setObjectName("Help_Page")
        self.Stacked_Pages.addWidget(self.Help_Page)
        self.Logout_Page = QtWidgets.QWidget()
        self.Logout_Page.setObjectName("Logout_Page")
        self.Stacked_Pages.addWidget(self.Logout_Page)
        self.horizontalLayout_3.addWidget(self.Stacked_Pages)
        self.horizontalLayout_4.addWidget(self.Main_Body)
        self.Side_Menu = QtWidgets.QFrame(self.Body)
        self.Side_Menu.setMinimumSize(QtCore.QSize(0, 0))
        self.Side_Menu.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Side_Menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Side_Menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Side_Menu.setObjectName("Side_Menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Side_Menu)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Full_Menu_Widget = QtWidgets.QWidget(self.Side_Menu)
        self.Full_Menu_Widget.setMinimumSize(QtCore.QSize(170, 200))
        self.Full_Menu_Widget.setMaximumSize(QtCore.QSize(170, 200))
        self.Full_Menu_Widget.setObjectName("Full_Menu_Widget")
        self.formLayout = QtWidgets.QFormLayout(self.Full_Menu_Widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.Test_Btn_Text = QtWidgets.QPushButton(self.Full_Menu_Widget)
        self.Test_Btn_Text.setMinimumSize(QtCore.QSize(90, 20))
        self.Test_Btn_Text.setMaximumSize(QtCore.QSize(90, 20))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum) Medium")
        font.setPointSize(6)
        font.setKerning(True)
        self.Test_Btn_Text.setFont(font)
        self.Test_Btn_Text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Test_Btn_Text.setStyleSheet("")
        self.Test_Btn_Text.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.Test_Btn_Text.setIconSize(QtCore.QSize(25, 25))
        self.Test_Btn_Text.setCheckable(True)
        self.Test_Btn_Text.setAutoExclusive(True)
        self.Test_Btn_Text.setObjectName("Test_Btn_Text")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Test_Btn_Text)
        self.Standards_Btn_Text = QtWidgets.QPushButton(self.Full_Menu_Widget)
        self.Standards_Btn_Text.setMinimumSize(QtCore.QSize(90, 20))
        self.Standards_Btn_Text.setMaximumSize(QtCore.QSize(90, 20))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum) Medium")
        font.setPointSize(6)
        font.setKerning(True)
        self.Standards_Btn_Text.setFont(font)
        self.Standards_Btn_Text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Standards_Btn_Text.setStyleSheet("")
        self.Standards_Btn_Text.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.Standards_Btn_Text.setIconSize(QtCore.QSize(25, 25))
        self.Standards_Btn_Text.setCheckable(True)
        self.Standards_Btn_Text.setAutoExclusive(True)
        self.Standards_Btn_Text.setObjectName("Standards_Btn_Text")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Standards_Btn_Text)
        self.Reporst_Btn_Text = QtWidgets.QPushButton(self.Full_Menu_Widget)
        self.Reporst_Btn_Text.setMinimumSize(QtCore.QSize(90, 20))
        self.Reporst_Btn_Text.setMaximumSize(QtCore.QSize(90, 20))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum) Medium")
        font.setPointSize(6)
        font.setKerning(True)
        self.Reporst_Btn_Text.setFont(font)
        self.Reporst_Btn_Text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Reporst_Btn_Text.setStyleSheet("")
        self.Reporst_Btn_Text.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.Reporst_Btn_Text.setIconSize(QtCore.QSize(25, 25))
        self.Reporst_Btn_Text.setCheckable(True)
        self.Reporst_Btn_Text.setAutoExclusive(True)
        self.Reporst_Btn_Text.setObjectName("Reporst_Btn_Text")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Reporst_Btn_Text)
        self.Warehouse_Btn_Text = QtWidgets.QPushButton(self.Full_Menu_Widget)
        self.Warehouse_Btn_Text.setMinimumSize(QtCore.QSize(90, 20))
        self.Warehouse_Btn_Text.setMaximumSize(QtCore.QSize(90, 20))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum) Medium")
        font.setPointSize(6)
        font.setKerning(True)
        self.Warehouse_Btn_Text.setFont(font)
        self.Warehouse_Btn_Text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Warehouse_Btn_Text.setStyleSheet("")
        self.Warehouse_Btn_Text.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.Warehouse_Btn_Text.setIconSize(QtCore.QSize(25, 25))
        self.Warehouse_Btn_Text.setCheckable(True)
        self.Warehouse_Btn_Text.setAutoExclusive(True)
        self.Warehouse_Btn_Text.setObjectName("Warehouse_Btn_Text")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Warehouse_Btn_Text)
        self.Pack_Btn_Text = QtWidgets.QPushButton(self.Full_Menu_Widget)
        self.Pack_Btn_Text.setMinimumSize(QtCore.QSize(90, 20))
        self.Pack_Btn_Text.setMaximumSize(QtCore.QSize(90, 20))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum) Medium")
        font.setPointSize(6)
        font.setKerning(True)
        self.Pack_Btn_Text.setFont(font)
        self.Pack_Btn_Text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Pack_Btn_Text.setStyleSheet("")
        self.Pack_Btn_Text.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.Pack_Btn_Text.setIconSize(QtCore.QSize(25, 25))
        self.Pack_Btn_Text.setCheckable(True)
        self.Pack_Btn_Text.setAutoExclusive(True)
        self.Pack_Btn_Text.setObjectName("Pack_Btn_Text")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Pack_Btn_Text)
        self.Logout_Btn_Text = QtWidgets.QPushButton(self.Full_Menu_Widget)
        self.Logout_Btn_Text.setMinimumSize(QtCore.QSize(90, 20))
        self.Logout_Btn_Text.setMaximumSize(QtCore.QSize(90, 20))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum) Medium")
        font.setPointSize(6)
        font.setKerning(True)
        self.Logout_Btn_Text.setFont(font)
        self.Logout_Btn_Text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Logout_Btn_Text.setStyleSheet("")
        self.Logout_Btn_Text.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.Logout_Btn_Text.setIconSize(QtCore.QSize(25, 25))
        self.Logout_Btn_Text.setCheckable(True)
        self.Logout_Btn_Text.setAutoExclusive(True)
        self.Logout_Btn_Text.setObjectName("Logout_Btn_Text")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Logout_Btn_Text)
        self.Settings_Btn_Text = QtWidgets.QPushButton(self.Full_Menu_Widget)
        self.Settings_Btn_Text.setMinimumSize(QtCore.QSize(90, 20))
        self.Settings_Btn_Text.setMaximumSize(QtCore.QSize(90, 20))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb(FaNum) Medium")
        font.setPointSize(6)
        font.setKerning(True)
        self.Settings_Btn_Text.setFont(font)
        self.Settings_Btn_Text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Settings_Btn_Text.setStyleSheet("")
        self.Settings_Btn_Text.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.Settings_Btn_Text.setIconSize(QtCore.QSize(25, 25))
        self.Settings_Btn_Text.setCheckable(True)
        self.Settings_Btn_Text.setAutoExclusive(True)
        self.Settings_Btn_Text.setObjectName("Settings_Btn_Text")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Settings_Btn_Text)
        self.verticalLayout_2.addWidget(self.Full_Menu_Widget, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Blank = QtWidgets.QFrame(self.Side_Menu)
        self.Blank.setStyleSheet("")
        self.Blank.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Blank.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Blank.setObjectName("Blank")
        self.verticalLayout_2.addWidget(self.Blank)
        self.Footer = QtWidgets.QFrame(self.Side_Menu)
        self.Footer.setMinimumSize(QtCore.QSize(0, 20))
        self.Footer.setMaximumSize(QtCore.QSize(16777215, 20))
        self.Footer.setStyleSheet("")
        self.Footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Footer.setObjectName("Footer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Footer)
        self.verticalLayout_3.setContentsMargins(0, 0, 8, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Version = QtWidgets.QLabel(self.Footer)
        self.Version.setObjectName("Version")
        self.verticalLayout_3.addWidget(self.Version)
        self.verticalLayout_2.addWidget(self.Footer)
        self.horizontalLayout_4.addWidget(self.Side_Menu)
        self.verticalLayout.addWidget(self.Body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Stacked_Pages.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Test_Btn_Text, self.Standards_Btn_Text)
        MainWindow.setTabOrder(self.Standards_Btn_Text, self.Pack_Btn_Text)
        MainWindow.setTabOrder(self.Pack_Btn_Text, self.Warehouse_Btn_Text)
        MainWindow.setTabOrder(self.Warehouse_Btn_Text, self.Reporst_Btn_Text)
        MainWindow.setTabOrder(self.Reporst_Btn_Text, self.Settings_Btn_Text)
        MainWindow.setTabOrder(self.Settings_Btn_Text, self.Logout_Btn_Text)
        MainWindow.setTabOrder(self.Logout_Btn_Text, self.Logo)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.User_Job.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:7pt;\">اپراتور تست دستگاه</span></p></body></html>"))
        self.User_Name.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:6pt;\">آریا برات زاده</span></p></body></html>"))
        self.Test_Btn_Text.setText(_translate("MainWindow", "تست دستگاه"))
        self.Standards_Btn_Text.setText(_translate("MainWindow", "استــانداردها"))
        self.Reporst_Btn_Text.setText(_translate("MainWindow", "گــــزارش ها"))
        self.Warehouse_Btn_Text.setText(_translate("MainWindow", "انبــــــــــار"))
        self.Pack_Btn_Text.setText(_translate("MainWindow", "ایجاد بسته"))
        self.Logout_Btn_Text.setText(_translate("MainWindow", "خــــــــروج"))
        self.Settings_Btn_Text.setText(_translate("MainWindow", "تنظیمـــــات"))
        self.Version.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">V 1.0.1</p></body></html>"))
