# import os
# from PyQt5 import QtGui, uic, QtWidgets
# import mysql.connector
# import main
from classes.Auth import Auth

# class loginWindow(Base, Form):
#     def __init__(self, parent=None):
#         super(self.__class__, self).__init__(parent)
#         self.setupUi(self)
        
#         # Setting Focus on username Input
#         self.usernameInput.setFocus()

#         # Login Button Pressed Event
#         self.loginButton.clicked.connect(self.authenticate)
        
#         # Enter button press on Line Edit event
#         self.passwordInput.returnPressed.connect(self.loginButton.click)
#         self.usernameInput.returnPressed.connect(self.loginButton.click)
        
#         # Enter Button pressed on Login button
#         self.loginButton.setAutoDefault(True)
        
#         # Make password invisible
#         self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.display_msg = QtWidgets.QMessageBox()
#         self.display_msg.setIcon(QtWidgets.QMessageBox.Information)

#     def authenticate(self):
#         self.username = self.usernameInput.text()
#         self.password = self.passwordInput.text()
#         usern = self.username
#         lis = ()
#         db = mysql.connector.connect(
#         host="85.185.84.197",
#         user="yekta",
#         password="Yekta-5310",
#         database="qc2"
#     )
#         cursor = db.cursor()
#         cursor.execute("SELECT user_id  FROM user_info where user_name = %s  and user_pass =%s",(self.username,self.password))
#         data = cursor.fetchall()
#         if(data == lis):
#             self.display_msg.setWindowTitle('Error')
#             self.display_msg.setText('Incorrect Username or Password')
#             self.display_msg.show()
#         else:
#             self.homepageopen()
#             self.homepage.fetchUsername(self.username)



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
