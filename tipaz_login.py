from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
import mysql.connector as mc
import pymysql
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QVBoxLayout, QHBoxLayout, QHeaderView,QTableWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from tipaz import Ui_MainWindow
import sys


class Ui_Mainform(object):

    def open_window(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        Mainform.close()
        self.window.show()

    def close(self):
        #sys.exit()
        app.quit() 

    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setWindowIcon(QtGui.QIcon('photo/tipaz.ico'))
        mess.setText(message)
        mess.setIcon(QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def log(self):

        user=self.user_edit.text()
        password=self.pass_edit.text()

        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="barmm")
        cur=self.conn.cursor()
        data = cur.execute ("SELECT * from login WHERE user_name = '"+user+"' AND password = '"+password+"'")
        
        if (data):
            self.messageBox("Information", "Login Successful")
            self.open_window()
        else:
            self.messageBox("Information", "Invalid Username or Password")
            return

    def setupUi(self, Mainform):
        Mainform.setObjectName("Mainform")
        Mainform.setWindowFlags( QtCore.Qt.CustomizeWindowHint )
        Mainform.resize(559, 515)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/tipaz.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Mainform.setWindowIcon(icon)
        Mainform.setStyleSheet("background-color: rgb(59, 59, 59);")
        self.centralwidget = QtWidgets.QWidget(Mainform)
        self.centralwidget.setObjectName("centralwidget")
        
        self.user_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_edit.setGeometry(QtCore.QRect(210, 220, 181, 31))
        self.user_edit.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.user_edit.setObjectName("user_edit")
        
        self.pass_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_edit.setGeometry(QtCore.QRect(210, 260, 181, 31))
        self.pass_edit.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.pass_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_edit.setObjectName("pass_edit")
        
        self.header_frame = QtWidgets.QFrame(self.centralwidget)
        self.header_frame.setGeometry(QtCore.QRect(0, 0, 571, 81))
        self.header_frame.setStyleSheet("background-color: rgb(255, 195, 44);")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        
        self.title_label = QtWidgets.QLabel(self.header_frame)
        self.title_label.setGeometry(QtCore.QRect(90, 10, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(5, 1, 96);")
        self.title_label.setObjectName("title_label")
        
        self.logo_label = QtWidgets.QLabel(self.header_frame)
        self.logo_label.setGeometry(QtCore.QRect(20, 10, 71, 61))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("photo/tipaz.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        
        self.form_frame = QtWidgets.QFrame(self.centralwidget)
        self.form_frame.setGeometry(QtCore.QRect(20, 100, 521, 391))
        self.form_frame.setMinimumSize(QtCore.QSize(2, 2))
        self.form_frame.setStyleSheet("background-color: rgb(5, 1, 96);")
        self.form_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame.setObjectName("form_frame")
        
        self.cancel_btn = QtWidgets.QPushButton(self.form_frame)
        self.cancel_btn.setGeometry(QtCore.QRect(290, 230, 91, 41))
        self.cancel_btn.setStyleSheet("background-color: rgb(59, 59, 59);color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("photo/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn.setIcon(icon1)
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.clicked.connect(self.close)
        
        self.login_btn = QtWidgets.QPushButton(self.form_frame)
        self.login_btn.setGeometry(QtCore.QRect(180, 230, 91, 41))
        self.login_btn.setStyleSheet("background-color: rgb(59, 59, 59);color: rgb(255, 255, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("photo/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon2)
        self.login_btn.setIconSize(QtCore.QSize(20, 20))
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.log)
        
        self.usesr_label = QtWidgets.QLabel(self.form_frame)
        self.usesr_label.setGeometry(QtCore.QRect(110, 130, 61, 16))
        self.usesr_label.setStyleSheet("color: rgb(254, 254, 254);")
        self.usesr_label.setObjectName("usesr_label")
        
        self.password_label = QtWidgets.QLabel(self.form_frame)
        self.password_label.setGeometry(QtCore.QRect(110, 170, 61, 16))
        self.password_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.password_label.setObjectName("password_label")
        
        self.icooBig_label = QtWidgets.QLabel(self.form_frame)
        self.icooBig_label.setGeometry(QtCore.QRect(220, 30, 111, 61))
        self.icooBig_label.setText("")
        self.icooBig_label.setPixmap(QtGui.QPixmap("photo/logo_login.png"))
        self.icooBig_label.setScaledContents(True)
        self.icooBig_label.setObjectName("icooBig_label")
        
        self.form_frame.raise_()
        self.user_edit.raise_()
        self.pass_edit.raise_()
        self.header_frame.raise_()
        Mainform.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Mainform)
        self.statusbar.setObjectName("statusbar")
        Mainform.setStatusBar(self.statusbar)

        self.retranslateUi(Mainform)
        QtCore.QMetaObject.connectSlotsByName(Mainform)

    def retranslateUi(self, Mainform):
        _translate = QtCore.QCoreApplication.translate
        Mainform.setWindowTitle(_translate("Mainform", "TIPAZ TRISKELION CHAPTER"))
        self.title_label.setText(_translate("Mainform", "TIPAZ TRISKELION CHAPTER"))
        self.cancel_btn.setText(_translate("Mainform", "Cancel"))
        self.login_btn.setText(_translate("Mainform", "Log In"))
        self.usesr_label.setText(_translate("Mainform", "Username:"))
        self.password_label.setText(_translate("Mainform", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mainform = QtWidgets.QMainWindow()
    ui = Ui_Mainform()
    ui.setupUi(Mainform)
    Mainform.show()
    sys.exit(app.exec_())
