# import os
# from PyQt5 import QtGui, uic, QtWidgets
# import mysql.connector
# import main
from classes.Auth import Auth




from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        
        self.username_label = QLabel("Username:")
        self.password_label = QLabel("Password:")
        
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        
        self.setLayout(layout)
        
    def login(self):
        # Check if the username and password are valid
        username = self.username_input.text()
        password = self.password_input.text()
        if Auth.login(Auth,username, password):
            self.accept()  # Accept the dialog and close it
        else:
            self.reject()  # Reject the dialog and keep it open
