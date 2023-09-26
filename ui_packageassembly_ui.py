# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_packageassembly.ui'
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
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_AssemblyPage(object):
    def setupUi(self, AssemblyPage):
        if not AssemblyPage.objectName():
            AssemblyPage.setObjectName(u"AssemblyPage")
        AssemblyPage.resize(1217, 812)
        self.centralwidget = QWidget(AssemblyPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.input_Properties = QFrame(self.frame_2)
        self.input_Properties.setObjectName(u"input_Properties")
        self.input_Properties.setFrameShape(QFrame.StyledPanel)
        self.input_Properties.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.input_Properties)
        self.gridLayout.setObjectName(u"gridLayout")
        self.refreshPackageDB = QPushButton(self.input_Properties)
        self.refreshPackageDB.setObjectName(u"refreshPackageDB")
        self.refreshPackageDB.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamilies([u"IRANSansWeb(FaNum)"])
        self.refreshPackageDB.setFont(font)

        self.gridLayout.addWidget(self.refreshPackageDB, 15, 4, 1, 1)

        self.label_23 = QLabel(self.input_Properties)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(50, 0))
        self.label_23.setFont(font)
        self.label_23.setLayoutDirection(Qt.RightToLeft)
        self.label_23.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_23, 14, 8, 1, 1)

        self.label_25 = QLabel(self.input_Properties)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(50, 0))
        self.label_25.setFont(font)
        self.label_25.setLayoutDirection(Qt.RightToLeft)
        self.label_25.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_25, 11, 6, 1, 1)

        self.assembleBtn = QPushButton(self.input_Properties)
        self.assembleBtn.setObjectName(u"assembleBtn")
        self.assembleBtn.setMinimumSize(QSize(0, 40))
        self.assembleBtn.setFont(font)

        self.gridLayout.addWidget(self.assembleBtn, 15, 5, 1, 1)

        self.label_24 = QLabel(self.input_Properties)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(50, 0))
        self.label_24.setFont(font)
        self.label_24.setLayoutDirection(Qt.RightToLeft)
        self.label_24.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_24, 9, 6, 1, 1)

        self.label_32 = QLabel(self.input_Properties)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(50, 0))
        self.label_32.setFont(font)
        self.label_32.setLayoutDirection(Qt.RightToLeft)
        self.label_32.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_32, 11, 4, 1, 1)

        self.label_37 = QLabel(self.input_Properties)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(50, 0))
        self.label_37.setFont(font)
        self.label_37.setLayoutDirection(Qt.RightToLeft)
        self.label_37.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_37, 13, 1, 1, 1)

        self.label_39 = QLabel(self.input_Properties)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(50, 0))
        self.label_39.setFont(font)
        self.label_39.setLayoutDirection(Qt.RightToLeft)
        self.label_39.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_39, 15, 8, 1, 1)

        self.packageSerial1 = QLineEdit(self.input_Properties)
        self.packageSerial1.setObjectName(u"packageSerial1")
        self.packageSerial1.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packageSerial1.sizePolicy().hasHeightForWidth())
        self.packageSerial1.setSizePolicy(sizePolicy)
        self.packageSerial1.setMinimumSize(QSize(150, 28))
        self.packageSerial1.setMaximumSize(QSize(16777215, 28))
        self.packageSerial1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.packageSerial1, 0, 7, 1, 1)

        self.partCategory7 = QLabel(self.input_Properties)
        self.partCategory7.setObjectName(u"partCategory7")
        self.partCategory7.setMinimumSize(QSize(150, 0))
        self.partCategory7.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partCategory7, 9, 0, 1, 1)

        self.label_33 = QLabel(self.input_Properties)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(50, 0))
        self.label_33.setFont(font)
        self.label_33.setLayoutDirection(Qt.RightToLeft)
        self.label_33.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_33, 14, 4, 1, 1)

        self.partCategory10 = QLabel(self.input_Properties)
        self.partCategory10.setObjectName(u"partCategory10")
        self.partCategory10.setMinimumSize(QSize(150, 0))
        self.partCategory10.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partCategory10, 14, 0, 1, 1)

        self.packageSerial2 = QLineEdit(self.input_Properties)
        self.packageSerial2.setObjectName(u"packageSerial2")
        self.packageSerial2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.packageSerial2.sizePolicy().hasHeightForWidth())
        self.packageSerial2.setSizePolicy(sizePolicy)
        self.packageSerial2.setMinimumSize(QSize(150, 28))
        self.packageSerial2.setMaximumSize(QSize(16777215, 28))
        self.packageSerial2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.packageSerial2, 9, 7, 1, 1)

        self.label_36 = QLabel(self.input_Properties)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(50, 0))
        self.label_36.setFont(font)
        self.label_36.setLayoutDirection(Qt.RightToLeft)
        self.label_36.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_36, 9, 1, 1, 1)

        self.packageSerial4 = QLineEdit(self.input_Properties)
        self.packageSerial4.setObjectName(u"packageSerial4")
        self.packageSerial4.setEnabled(True)
        sizePolicy.setHeightForWidth(self.packageSerial4.sizePolicy().hasHeightForWidth())
        self.packageSerial4.setSizePolicy(sizePolicy)
        self.packageSerial4.setMinimumSize(QSize(150, 28))
        self.packageSerial4.setMaximumSize(QSize(16777215, 28))
        self.packageSerial4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.packageSerial4, 13, 7, 1, 1)

        self.partCategory2 = QLabel(self.input_Properties)
        self.partCategory2.setObjectName(u"partCategory2")
        self.partCategory2.setMinimumSize(QSize(150, 0))
        self.partCategory2.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partCategory2, 9, 5, 1, 1)

        self.partCategory9 = QLabel(self.input_Properties)
        self.partCategory9.setObjectName(u"partCategory9")
        self.partCategory9.setMinimumSize(QSize(150, 0))
        self.partCategory9.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partCategory9, 13, 0, 1, 1)

        self.packageSerial9 = QLineEdit(self.input_Properties)
        self.packageSerial9.setObjectName(u"packageSerial9")
        self.packageSerial9.setEnabled(True)
        sizePolicy.setHeightForWidth(self.packageSerial9.sizePolicy().hasHeightForWidth())
        self.packageSerial9.setSizePolicy(sizePolicy)
        self.packageSerial9.setMinimumSize(QSize(150, 28))
        self.packageSerial9.setMaximumSize(QSize(16777215, 28))
        self.packageSerial9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.packageSerial9, 13, 2, 1, 1)

        self.packageSerial8 = QLineEdit(self.input_Properties)
        self.packageSerial8.setObjectName(u"packageSerial8")
        self.packageSerial8.setEnabled(True)
        sizePolicy.setHeightForWidth(self.packageSerial8.sizePolicy().hasHeightForWidth())
        self.packageSerial8.setSizePolicy(sizePolicy)
        self.packageSerial8.setMinimumSize(QSize(150, 28))
        self.packageSerial8.setMaximumSize(QSize(16777215, 28))
        self.packageSerial8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.packageSerial8, 11, 2, 1, 1)

        self.partCategory6 = QLabel(self.input_Properties)
        self.partCategory6.setObjectName(u"partCategory6")
        self.partCategory6.setMinimumSize(QSize(150, 0))
        self.partCategory6.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partCategory6, 0, 0, 1, 1)

        self.label_35 = QLabel(self.input_Properties)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(50, 0))
        self.label_35.setFont(font)
        self.label_35.setLayoutDirection(Qt.RightToLeft)
        self.label_35.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_35, 0, 1, 1, 1)

        self.packageSerial5 = QLineEdit(self.input_Properties)
        self.packageSerial5.setObjectName(u"packageSerial5")
        self.packageSerial5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.packageSerial5.sizePolicy().hasHeightForWidth())
        self.packageSerial5.setSizePolicy(sizePolicy)
        self.packageSerial5.setMinimumSize(QSize(150, 28))
        self.packageSerial5.setMaximumSize(QSize(16777215, 28))
        self.packageSerial5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.packageSerial5, 14, 7, 1, 1)

        self.partCategory3 = QLabel(self.input_Properties)
        self.partCategory3.setObjectName(u"partCategory3")
        self.partCategory3.setMinimumSize(QSize(150, 0))
        self.partCategory3.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partCategory3, 11, 5, 1, 1)

        self.label_29 = QLabel(self.input_Properties)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(50, 0))
        self.label_29.setFont(font)
        self.label_29.setLayoutDirection(Qt.RightToLeft)
        self.label_29.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_29, 0, 4, 1, 1)

        self.partCategory8 = QLabel(self.input_Properties)
        self.partCategory8.setObjectName(u"partCategory8")
        self.partCategory8.setMinimumSize(QSize(150, 0))
        self.partCategory8.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partCategory8, 11, 0, 1, 1)

        self.label_31 = QLabel(self.input_Properties)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(50, 0))
        self.label_31.setFont(font)
        self.label_31.setLayoutDirection(Qt.RightToLeft)
        self.label_31.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_31, 9, 4, 1, 1)

        self.label_38 = QLabel(self.input_Properties)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(50, 0))
        self.label_38.setFont(font)
        self.label_38.setLayoutDirection(Qt.RightToLeft)
        self.label_38.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_38, 11, 1, 1, 1)

        self.partCategory1 = QLabel(self.input_Properties)
        self.partCategory1.setObjectName(u"partCategory1")
        self.partCategory1.setMinimumSize(QSize(150, 0))
        self.partCategory1.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partCategory1, 0, 5, 1, 1)

        self.label_21 = QLabel(self.input_Properties)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(50, 0))
        self.label_21.setFont(font)
        self.label_21.setLayoutDirection(Qt.RightToLeft)
        self.label_21.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_21, 11, 8, 1, 1)

        self.label_28 = QLabel(self.input_Properties)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(50, 0))
        self.label_28.setFont(font)
        self.label_28.setLayoutDirection(Qt.RightToLeft)
        self.label_28.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_28, 13, 6, 1, 1)

        self.packageSerial10 = QLineEdit(self.input_Properties)
        self.packageSerial10.setObjectName(u"packageSerial10")
        self.packageSerial10.setEnabled(True)
        sizePolicy.setHeightForWidth(self.packageSerial10.sizePolicy().hasHeightForWidth())
        self.packageSerial10.setSizePolicy(sizePolicy)
        self.packageSerial10.setMinimumSize(QSize(150, 28))
        self.packageSerial10.setMaximumSize(QSize(16777215, 28))
        self.packageSerial10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.packageSerial10, 14, 2, 1, 1)

        self.partCategory5 = QLabel(self.input_Properties)
        self.partCategory5.setObjectName(u"partCategory5")
        self.partCategory5.setMinimumSize(QSize(150, 0))
        self.partCategory5.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partCategory5, 14, 5, 1, 1)

        self.label_20 = QLabel(self.input_Properties)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(50, 0))
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(Qt.RightToLeft)
        self.label_20.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_20, 0, 8, 1, 1)

        self.packageName = QLineEdit(self.input_Properties)
        self.packageName.setObjectName(u"packageName")
        self.packageName.setEnabled(True)
        sizePolicy.setHeightForWidth(self.packageName.sizePolicy().hasHeightForWidth())
        self.packageName.setSizePolicy(sizePolicy)
        self.packageName.setMinimumSize(QSize(150, 28))
        self.packageName.setMaximumSize(QSize(16777215, 28))
        self.packageName.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.packageName, 15, 7, 1, 1)

        self.label_22 = QLabel(self.input_Properties)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(50, 0))
        self.label_22.setFont(font)
        self.label_22.setLayoutDirection(Qt.RightToLeft)
        self.label_22.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_22, 13, 8, 1, 1)

        self.packageSerial6 = QLineEdit(self.input_Properties)
        self.packageSerial6.setObjectName(u"packageSerial6")
        self.packageSerial6.setEnabled(True)
        sizePolicy.setHeightForWidth(self.packageSerial6.sizePolicy().hasHeightForWidth())
        self.packageSerial6.setSizePolicy(sizePolicy)
        self.packageSerial6.setMinimumSize(QSize(150, 28))
        self.packageSerial6.setMaximumSize(QSize(16777215, 28))
        self.packageSerial6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.packageSerial6, 0, 2, 1, 1)

        self.label_26 = QLabel(self.input_Properties)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(50, 0))
        self.label_26.setFont(font)
        self.label_26.setLayoutDirection(Qt.RightToLeft)
        self.label_26.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_26, 0, 6, 1, 1)

        self.partCategory4 = QLabel(self.input_Properties)
        self.partCategory4.setObjectName(u"partCategory4")
        self.partCategory4.setMinimumSize(QSize(150, 0))
        self.partCategory4.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.partCategory4, 13, 5, 1, 1)

        self.label_30 = QLabel(self.input_Properties)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(50, 0))
        self.label_30.setFont(font)
        self.label_30.setLayoutDirection(Qt.RightToLeft)
        self.label_30.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_30, 13, 4, 1, 1)

        self.label_19 = QLabel(self.input_Properties)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(50, 0))
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(Qt.RightToLeft)
        self.label_19.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_19, 9, 8, 1, 1)

        self.label_27 = QLabel(self.input_Properties)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(50, 0))
        self.label_27.setFont(font)
        self.label_27.setLayoutDirection(Qt.RightToLeft)
        self.label_27.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_27, 14, 6, 1, 1)

        self.label_34 = QLabel(self.input_Properties)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(50, 0))
        self.label_34.setFont(font)
        self.label_34.setLayoutDirection(Qt.RightToLeft)
        self.label_34.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_34, 14, 1, 1, 1)

        self.packageSerial3 = QLineEdit(self.input_Properties)
        self.packageSerial3.setObjectName(u"packageSerial3")
        self.packageSerial3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.packageSerial3.sizePolicy().hasHeightForWidth())
        self.packageSerial3.setSizePolicy(sizePolicy)
        self.packageSerial3.setMinimumSize(QSize(150, 28))
        self.packageSerial3.setMaximumSize(QSize(16777215, 28))
        self.packageSerial3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.packageSerial3, 11, 7, 1, 1)

        self.packageSerial7 = QLineEdit(self.input_Properties)
        self.packageSerial7.setObjectName(u"packageSerial7")
        self.packageSerial7.setEnabled(True)
        sizePolicy.setHeightForWidth(self.packageSerial7.sizePolicy().hasHeightForWidth())
        self.packageSerial7.setSizePolicy(sizePolicy)
        self.packageSerial7.setMinimumSize(QSize(150, 28))
        self.packageSerial7.setMaximumSize(QSize(16777215, 28))
        self.packageSerial7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.packageSerial7, 9, 2, 1, 1)

        self.tempBarcodeFrame = QFrame(self.input_Properties)
        self.tempBarcodeFrame.setObjectName(u"tempBarcodeFrame")
        self.tempBarcodeFrame.setMinimumSize(QSize(0, 36))
        self.tempBarcodeFrame.setLayoutDirection(Qt.LeftToRight)
        self.tempBarcodeFrame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.tempBarcodeFrame.setFrameShape(QFrame.StyledPanel)
        self.tempBarcodeFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.tempBarcodeFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 7, 3)
        self.tempBarcode = QLabel(self.tempBarcodeFrame)
        self.tempBarcode.setObjectName(u"tempBarcode")
        self.tempBarcode.setMinimumSize(QSize(200, 30))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.tempBarcode.setFont(font1)
        self.tempBarcode.setStyleSheet(u"border: remove;")
        self.tempBarcode.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.tempBarcode)

        self.label_2 = QLabel(self.tempBarcodeFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border : remove;")

        self.horizontalLayout.addWidget(self.label_2)


        self.gridLayout.addWidget(self.tempBarcodeFrame, 15, 0, 1, 2)

        self.barcodePrintBtn = QPushButton(self.input_Properties)
        self.barcodePrintBtn.setObjectName(u"barcodePrintBtn")
        self.barcodePrintBtn.setMinimumSize(QSize(70, 40))
        self.barcodePrintBtn.setFont(font)

        self.gridLayout.addWidget(self.barcodePrintBtn, 15, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.input_Properties, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.inputPartTable = QFrame(self.frame_2)
        self.inputPartTable.setObjectName(u"inputPartTable")
        self.inputPartTable.setFrameShape(QFrame.StyledPanel)
        self.inputPartTable.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.inputPartTable)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.tableWidget = QTableWidget(self.inputPartTable)
        if (self.tableWidget.columnCount() < 15):
            self.tableWidget.setColumnCount(15)
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
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_2.addWidget(self.tableWidget)


        self.verticalLayout_2.addWidget(self.inputPartTable)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        AssemblyPage.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.packageSerial1, self.packageSerial2)
        QWidget.setTabOrder(self.packageSerial2, self.packageSerial3)
        QWidget.setTabOrder(self.packageSerial3, self.packageSerial4)
        QWidget.setTabOrder(self.packageSerial4, self.packageSerial5)
        QWidget.setTabOrder(self.packageSerial5, self.packageSerial6)
        QWidget.setTabOrder(self.packageSerial6, self.packageSerial7)
        QWidget.setTabOrder(self.packageSerial7, self.packageSerial8)
        QWidget.setTabOrder(self.packageSerial8, self.packageSerial9)
        QWidget.setTabOrder(self.packageSerial9, self.packageSerial10)
        QWidget.setTabOrder(self.packageSerial10, self.packageName)
        QWidget.setTabOrder(self.packageName, self.assembleBtn)
        QWidget.setTabOrder(self.assembleBtn, self.refreshPackageDB)
        QWidget.setTabOrder(self.refreshPackageDB, self.barcodePrintBtn)
        QWidget.setTabOrder(self.barcodePrintBtn, self.tableWidget)

        self.retranslateUi(AssemblyPage)

        QMetaObject.connectSlotsByName(AssemblyPage)
    # setupUi

    def retranslateUi(self, AssemblyPage):
        AssemblyPage.setWindowTitle(QCoreApplication.translate("AssemblyPage", u"MainWindow", None))
        self.refreshPackageDB.setText(QCoreApplication.translate("AssemblyPage", u"\u0628\u0631\u0648\u0632 \u0631\u0633\u0627\u0646\u06cc \u0644\u06cc\u0633\u062a", None))
        self.label_23.setText(QCoreApplication.translate("AssemblyPage", u"\u0633\u0631\u06cc\u0627\u0644", None))
        self.label_25.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 03", None))
        self.assembleBtn.setText(QCoreApplication.translate("AssemblyPage", u"\u0627\u06cc\u062c\u0627\u062f \u0628\u0633\u062a\u0647", None))
        self.label_24.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 02", None))
        self.label_32.setText(QCoreApplication.translate("AssemblyPage", u"\u0633\u0631\u06cc\u0627\u0644", None))
        self.label_37.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 09", None))
        self.label_39.setText(QCoreApplication.translate("AssemblyPage", u"\u0639\u0646\u0648\u0627\u0646", None))
        self.partCategory7.setText("")
        self.label_33.setText(QCoreApplication.translate("AssemblyPage", u"\u0633\u0631\u06cc\u0627\u0644", None))
        self.partCategory10.setText("")
        self.label_36.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 07", None))
        self.partCategory2.setText("")
        self.partCategory9.setText("")
        self.partCategory6.setText("")
        self.label_35.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 06", None))
        self.partCategory3.setText("")
        self.label_29.setText(QCoreApplication.translate("AssemblyPage", u"\u0633\u0631\u06cc\u0627\u0644", None))
        self.partCategory8.setText("")
        self.label_31.setText(QCoreApplication.translate("AssemblyPage", u"\u0633\u0631\u06cc\u0627\u0644", None))
        self.label_38.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 08", None))
        self.partCategory1.setText("")
        self.label_21.setText(QCoreApplication.translate("AssemblyPage", u"\u0633\u0631\u06cc\u0627\u0644", None))
        self.label_28.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 04", None))
        self.partCategory5.setText("")
        self.label_20.setText(QCoreApplication.translate("AssemblyPage", u"\u0633\u0631\u06cc\u0627\u0644", None))
        self.label_22.setText(QCoreApplication.translate("AssemblyPage", u"\u0633\u0631\u06cc\u0627\u0644", None))
        self.label_26.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 01", None))
        self.partCategory4.setText("")
        self.label_30.setText(QCoreApplication.translate("AssemblyPage", u"\u0633\u0631\u06cc\u0627\u0644", None))
        self.label_19.setText(QCoreApplication.translate("AssemblyPage", u"\u0633\u0631\u06cc\u0627\u0644", None))
        self.label_27.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 05", None))
        self.label_34.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 10", None))
        self.tempBarcode.setText("")
        self.label_2.setText(QCoreApplication.translate("AssemblyPage", u"\u0633\u0631\u06cc\u0627\u0644 \u0645\u0648\u0642\u062a:", None))
        self.barcodePrintBtn.setText(QCoreApplication.translate("AssemblyPage", u"\u0686\u0627\u067e \u0628\u0627\u0631\u06a9\u062f", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AssemblyPage", u"\u062d\u0630\u0641 \u0642\u0637\u0639\u0647", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AssemblyPage", u"\u0639\u0646\u0648\u0627\u0646", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AssemblyPage", u"\u0633\u0631\u06cc\u0627\u0644 \u0645\u0648\u0642\u062a", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 01", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 02", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 03", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 04", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 05", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 06", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("AssemblyPage", u"\u062a\u0627\u0631\u06cc\u062e \u062b\u0628\u062a", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 07", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 08", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("AssemblyPage", u"\u0642\u0637\u0639\u0647 09", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("AssemblyPage", u"\u0627\u067e\u0631\u0627\u062a\u0648\u0631 \u0627\u06cc\u062c\u0627\u062f \u06a9\u0646\u0646\u062f\u0647", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("AssemblyPage", u"\u062a\u0627\u0631\u06cc\u062e \u0627\u06cc\u062c\u0627\u062f", None));
    # retranslateUi

