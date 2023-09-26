# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1229, 866)
        MainWindow.setMinimumSize(QSize(0, 500))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Header = QFrame(self.centralwidget)
        self.Header.setObjectName(u"Header")
        self.Header.setMinimumSize(QSize(0, 50))
        self.Header.setMaximumSize(QSize(16777215, 50))
        self.Header.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.Header.setFrameShape(QFrame.StyledPanel)
        self.Header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logoFrame = QFrame(self.Header)
        self.logoFrame.setObjectName(u"logoFrame")
        self.logoFrame.setMinimumSize(QSize(0, 50))
        self.logoFrame.setMaximumSize(QSize(200, 50))
        self.logoFrame.setStyleSheet(u"")
        self.logoFrame.setFrameShape(QFrame.StyledPanel)
        self.logoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.logoFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Logo = QPushButton(self.logoFrame)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMaximumSize(QSize(200, 50))
        self.Logo.setStyleSheet(u"background-color: none;\n"
"border: remove;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Logo.setIcon(icon)
        self.Logo.setIconSize(QSize(180, 20))

        self.verticalLayout_6.addWidget(self.Logo)


        self.horizontalLayout.addWidget(self.logoFrame)

        self.titleFrame = QFrame(self.Header)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.titleFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.menuTitle = QLabel(self.titleFrame)
        self.menuTitle.setObjectName(u"menuTitle")
        font = QFont()
        font.setFamilies([u"IRANSansWeb(FaNum) Medium"])
        font.setPointSize(20)
        self.menuTitle.setFont(font)

        self.verticalLayout_5.addWidget(self.menuTitle)


        self.horizontalLayout.addWidget(self.titleFrame)

        self.User_Info = QFrame(self.Header)
        self.User_Info.setObjectName(u"User_Info")
        self.User_Info.setMinimumSize(QSize(150, 50))
        self.User_Info.setMaximumSize(QSize(150, 50))
        self.User_Info.setFrameShape(QFrame.StyledPanel)
        self.User_Info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.User_Info)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 5, 5, 5)
        self.User_Job = QLabel(self.User_Info)
        self.User_Job.setObjectName(u"User_Job")
        font1 = QFont()
        font1.setFamilies([u"IRANSansWeb(FaNum) Medium"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.User_Job.setFont(font1)
        self.User_Job.setLayoutDirection(Qt.RightToLeft)
        self.User_Job.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.verticalLayout_7.addWidget(self.User_Job)

        self.User_Name = QLabel(self.User_Info)
        self.User_Name.setObjectName(u"User_Name")
        font2 = QFont()
        font2.setFamilies([u"IRANSansWeb(FaNum) Medium"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.User_Name.setFont(font2)
        self.User_Name.setLayoutDirection(Qt.RightToLeft)
        self.User_Name.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.verticalLayout_7.addWidget(self.User_Name)


        self.horizontalLayout.addWidget(self.User_Info, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.Header)

        self.Body = QFrame(self.centralwidget)
        self.Body.setObjectName(u"Body")
        self.Body.setFrameShape(QFrame.StyledPanel)
        self.Body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Body)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Main_Body = QFrame(self.Body)
        self.Main_Body.setObjectName(u"Main_Body")
        self.Main_Body.setFrameShape(QFrame.StyledPanel)
        self.Main_Body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Main_Body)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Stacked_Pages = QStackedWidget(self.Main_Body)
        self.Stacked_Pages.setObjectName(u"Stacked_Pages")
        self.Stacked_Pages.setEnabled(True)
        self.Test_Page = QWidget()
        self.Test_Page.setObjectName(u"Test_Page")
        self.Stacked_Pages.addWidget(self.Test_Page)
        self.Standards_Page = QWidget()
        self.Standards_Page.setObjectName(u"Standards_Page")
        self.Stacked_Pages.addWidget(self.Standards_Page)
        self.Reports_Page = QWidget()
        self.Reports_Page.setObjectName(u"Reports_Page")
        self.Stacked_Pages.addWidget(self.Reports_Page)
        self.Warehouse_Page = QWidget()
        self.Warehouse_Page.setObjectName(u"Warehouse_Page")
        self.Stacked_Pages.addWidget(self.Warehouse_Page)
        self.Settings_Page = QWidget()
        self.Settings_Page.setObjectName(u"Settings_Page")
        self.Stacked_Pages.addWidget(self.Settings_Page)
        self.Help_Page = QWidget()
        self.Help_Page.setObjectName(u"Help_Page")
        self.Stacked_Pages.addWidget(self.Help_Page)
        self.Logout_Page = QWidget()
        self.Logout_Page.setObjectName(u"Logout_Page")
        self.Stacked_Pages.addWidget(self.Logout_Page)

        self.horizontalLayout_3.addWidget(self.Stacked_Pages)


        self.horizontalLayout_4.addWidget(self.Main_Body)

        self.Side_Menu = QFrame(self.Body)
        self.Side_Menu.setObjectName(u"Side_Menu")
        self.Side_Menu.setMinimumSize(QSize(0, 0))
        self.Side_Menu.setMaximumSize(QSize(100, 16777215))
        self.Side_Menu.setFrameShape(QFrame.StyledPanel)
        self.Side_Menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Side_Menu)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.Full_Menu_Widget = QWidget(self.Side_Menu)
        self.Full_Menu_Widget.setObjectName(u"Full_Menu_Widget")
        self.Full_Menu_Widget.setMinimumSize(QSize(170, 200))
        self.Full_Menu_Widget.setMaximumSize(QSize(170, 200))
        self.formLayout = QFormLayout(self.Full_Menu_Widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.Test_Btn_Text = QPushButton(self.Full_Menu_Widget)
        self.Test_Btn_Text.setObjectName(u"Test_Btn_Text")
        self.Test_Btn_Text.setMinimumSize(QSize(90, 20))
        self.Test_Btn_Text.setMaximumSize(QSize(90, 20))
        font3 = QFont()
        font3.setFamilies([u"IRANSansWeb(FaNum) Medium"])
        font3.setPointSize(6)
        font3.setKerning(True)
        self.Test_Btn_Text.setFont(font3)
        self.Test_Btn_Text.setLayoutDirection(Qt.RightToLeft)
        self.Test_Btn_Text.setStyleSheet(u"")
        self.Test_Btn_Text.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.Test_Btn_Text.setIconSize(QSize(25, 25))
        self.Test_Btn_Text.setCheckable(True)
        self.Test_Btn_Text.setAutoExclusive(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.Test_Btn_Text)

        self.Standards_Btn_Text = QPushButton(self.Full_Menu_Widget)
        self.Standards_Btn_Text.setObjectName(u"Standards_Btn_Text")
        self.Standards_Btn_Text.setMinimumSize(QSize(90, 20))
        self.Standards_Btn_Text.setMaximumSize(QSize(90, 20))
        self.Standards_Btn_Text.setFont(font3)
        self.Standards_Btn_Text.setLayoutDirection(Qt.RightToLeft)
        self.Standards_Btn_Text.setStyleSheet(u"")
        self.Standards_Btn_Text.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.Standards_Btn_Text.setIconSize(QSize(25, 25))
        self.Standards_Btn_Text.setCheckable(True)
        self.Standards_Btn_Text.setAutoExclusive(True)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.Standards_Btn_Text)

        self.Reporst_Btn_Text = QPushButton(self.Full_Menu_Widget)
        self.Reporst_Btn_Text.setObjectName(u"Reporst_Btn_Text")
        self.Reporst_Btn_Text.setMinimumSize(QSize(90, 20))
        self.Reporst_Btn_Text.setMaximumSize(QSize(90, 20))
        self.Reporst_Btn_Text.setFont(font3)
        self.Reporst_Btn_Text.setLayoutDirection(Qt.RightToLeft)
        self.Reporst_Btn_Text.setStyleSheet(u"")
        self.Reporst_Btn_Text.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.Reporst_Btn_Text.setIconSize(QSize(25, 25))
        self.Reporst_Btn_Text.setCheckable(True)
        self.Reporst_Btn_Text.setAutoExclusive(True)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.Reporst_Btn_Text)

        self.Warehouse_Btn_Text = QPushButton(self.Full_Menu_Widget)
        self.Warehouse_Btn_Text.setObjectName(u"Warehouse_Btn_Text")
        self.Warehouse_Btn_Text.setMinimumSize(QSize(90, 20))
        self.Warehouse_Btn_Text.setMaximumSize(QSize(90, 20))
        self.Warehouse_Btn_Text.setFont(font3)
        self.Warehouse_Btn_Text.setLayoutDirection(Qt.RightToLeft)
        self.Warehouse_Btn_Text.setStyleSheet(u"")
        self.Warehouse_Btn_Text.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.Warehouse_Btn_Text.setIconSize(QSize(25, 25))
        self.Warehouse_Btn_Text.setCheckable(True)
        self.Warehouse_Btn_Text.setAutoExclusive(True)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.Warehouse_Btn_Text)

        self.Pack_Btn_Text = QPushButton(self.Full_Menu_Widget)
        self.Pack_Btn_Text.setObjectName(u"Pack_Btn_Text")
        self.Pack_Btn_Text.setMinimumSize(QSize(90, 20))
        self.Pack_Btn_Text.setMaximumSize(QSize(90, 20))
        self.Pack_Btn_Text.setFont(font3)
        self.Pack_Btn_Text.setLayoutDirection(Qt.RightToLeft)
        self.Pack_Btn_Text.setStyleSheet(u"")
        self.Pack_Btn_Text.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.Pack_Btn_Text.setIconSize(QSize(25, 25))
        self.Pack_Btn_Text.setCheckable(True)
        self.Pack_Btn_Text.setAutoExclusive(True)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.Pack_Btn_Text)

        self.Logout_Btn_Text = QPushButton(self.Full_Menu_Widget)
        self.Logout_Btn_Text.setObjectName(u"Logout_Btn_Text")
        self.Logout_Btn_Text.setMinimumSize(QSize(90, 20))
        self.Logout_Btn_Text.setMaximumSize(QSize(90, 20))
        self.Logout_Btn_Text.setFont(font3)
        self.Logout_Btn_Text.setLayoutDirection(Qt.RightToLeft)
        self.Logout_Btn_Text.setStyleSheet(u"")
        self.Logout_Btn_Text.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.Logout_Btn_Text.setIconSize(QSize(25, 25))
        self.Logout_Btn_Text.setCheckable(True)
        self.Logout_Btn_Text.setAutoExclusive(True)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.Logout_Btn_Text)

        self.Settings_Btn_Text = QPushButton(self.Full_Menu_Widget)
        self.Settings_Btn_Text.setObjectName(u"Settings_Btn_Text")
        self.Settings_Btn_Text.setMinimumSize(QSize(90, 20))
        self.Settings_Btn_Text.setMaximumSize(QSize(90, 20))
        self.Settings_Btn_Text.setFont(font3)
        self.Settings_Btn_Text.setLayoutDirection(Qt.RightToLeft)
        self.Settings_Btn_Text.setStyleSheet(u"")
        self.Settings_Btn_Text.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.Settings_Btn_Text.setIconSize(QSize(25, 25))
        self.Settings_Btn_Text.setCheckable(True)
        self.Settings_Btn_Text.setAutoExclusive(True)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.Settings_Btn_Text)


        self.verticalLayout_2.addWidget(self.Full_Menu_Widget, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.Blank = QFrame(self.Side_Menu)
        self.Blank.setObjectName(u"Blank")
        self.Blank.setStyleSheet(u"")
        self.Blank.setFrameShape(QFrame.StyledPanel)
        self.Blank.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.Blank)

        self.Footer = QFrame(self.Side_Menu)
        self.Footer.setObjectName(u"Footer")
        self.Footer.setMinimumSize(QSize(0, 20))
        self.Footer.setMaximumSize(QSize(16777215, 20))
        self.Footer.setStyleSheet(u"")
        self.Footer.setFrameShape(QFrame.StyledPanel)
        self.Footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Footer)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 8, 0)
        self.Version = QLabel(self.Footer)
        self.Version.setObjectName(u"Version")

        self.verticalLayout_3.addWidget(self.Version)


        self.verticalLayout_2.addWidget(self.Footer)


        self.horizontalLayout_4.addWidget(self.Side_Menu)


        self.verticalLayout.addWidget(self.Body)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Test_Btn_Text, self.Standards_Btn_Text)
        QWidget.setTabOrder(self.Standards_Btn_Text, self.Pack_Btn_Text)
        QWidget.setTabOrder(self.Pack_Btn_Text, self.Warehouse_Btn_Text)
        QWidget.setTabOrder(self.Warehouse_Btn_Text, self.Reporst_Btn_Text)
        QWidget.setTabOrder(self.Reporst_Btn_Text, self.Settings_Btn_Text)
        QWidget.setTabOrder(self.Settings_Btn_Text, self.Logout_Btn_Text)
        QWidget.setTabOrder(self.Logout_Btn_Text, self.Logo)

        self.retranslateUi(MainWindow)

        self.Stacked_Pages.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Logo.setText("")
        self.menuTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.User_Job.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:7pt;\">\u0627\u067e\u0631\u0627\u062a\u0648\u0631 \u062a\u0633\u062a \u062f\u0633\u062a\u06af\u0627\u0647</span></p></body></html>", None))
        self.User_Name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:6pt;\">\u0622\u0631\u06cc\u0627 \u0628\u0631\u0627\u062a \u0632\u0627\u062f\u0647</span></p></body></html>", None))
        self.Test_Btn_Text.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0633\u062a \u062f\u0633\u062a\u06af\u0627\u0647", None))
        self.Standards_Btn_Text.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u062a\u0640\u0640\u0627\u0646\u062f\u0627\u0631\u062f\u0647\u0627", None))
        self.Reporst_Btn_Text.setText(QCoreApplication.translate("MainWindow", u"\u06af\u0640\u0640\u0640\u0640\u0632\u0627\u0631\u0634 \u0647\u0627", None))
        self.Warehouse_Btn_Text.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0646\u0628\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0627\u0631", None))
        self.Pack_Btn_Text.setText(QCoreApplication.translate("MainWindow", u"\u0627\u06cc\u062c\u0627\u062f \u0628\u0633\u062a\u0647", None))
        self.Logout_Btn_Text.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0631\u0648\u062c", None))
        self.Settings_Btn_Text.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0646\u0638\u06cc\u0645\u0640\u0640\u0640\u0640\u0640\u0627\u062a", None))
        self.Version.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">V 1.0.1</p></body></html>", None))
    # retranslateUi

