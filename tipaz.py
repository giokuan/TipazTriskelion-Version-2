from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import mysql.connector as mc
import pymysql
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QVBoxLayout, QHBoxLayout, QHeaderView,QTableWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QFileDialog
import sys


class Ui_MainWindow(object):

    def browse_image(self):
        filename = QFileDialog.getOpenFileName( caption = "Open file", directory=None, \
                                                            filter="Image (*.png * .jpg);;All Files(*.*)")   
        self.addPic_edit.setText(filename[0])
        self.load_image()

    def popup(self):
        msg=QMessageBox() 
        msg.setWindowIcon(QtGui.QIcon('photo/tipaz.ico'))
        msg.setWindowTitle("Exit")
        msg.setText("Are you sure you wan't to Exit?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok| QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        
        res = msg.exec_()
        if res == QMessageBox.Ok:  
            sys.exit()
        if res == QMessageBox.Cancel:
            pass 

    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowIcon(QtGui.QIcon('photo/tipaz.ico'))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setIcon(QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def load_image(self):
        p = self.addPic_edit.text()
        self.pic_label.setPixmap(QtGui.QPixmap(p))

    def search(self):    
        row = 0
        try: 
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password= "noahkuan03",
                database = "myproject"
            )
            mycursor = mydb.cursor()
            se = self.search_edit.text()
            mycursor.execute("SELECT * FROM projecttau WHERE last_name = '"+se+"'" );
            result = mycursor.fetchall()
          
            self.tableWidget.setRowCount(0)
           
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                  
        except mc.Error as e:
            print ("Error Occured")

    def insert_data(self):
        
        p = self.addPic_edit.text()
        with open(p, 'rb') as f:
            m=f.read()


        lname=self.lname_edit.text()
        fname=self.fname_edit.text()
        aka1=self.aka_edit.text()
        batch=self.batch_edit.text()
        tbirth=self.tbirth_edit.text()
        current=self.current_edit.text()
        root=self.root_edit.text()
        status=self.status_edit.text()
        address=self.address_edit.text()

        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="myproject")
       
        query=("INSERT INTO projecttau (last_name, first_name, aka, batch_name, T_birth, current_chapter, root_chapter, stat, address, photo) VALUES  (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        cur=self.conn.cursor()
        data= cur.execute(query, (lname.upper(),fname.upper(),aka1.upper(),batch.upper(),tbirth.upper(),current.upper(),root.upper(),status.upper(),address.upper(),m))
        

        if (data):
            msg=QMessageBox()
            if    len(lname) == 0:
                self.messageBox("Information", " Last Name Cannot be empty!")
                return
            elif  len(fname) == 0:
                self.messageBox("Information", " First Name Cannot be empty!")
                return
            elif  len(aka1)  == 0:
                self.messageBox("Information", " A.K.A Cannot be empty!")
                return
            elif  len(batch) == 0:
                self.messageBox("Information", " Batch Name Cannot be empty!")
                return
            elif  len(tbirth)== 0:
                self.messageBox("Information", " Triskelion Birth Cannot be empty!")
                return
            elif  len(current)== 0:
                self.messageBox("Information", " Current Chapter Cannot be empty!")
                return
            elif  len(root)== 0:
                self.messageBox("Information", " Root Chapter Cannot be empty!")
                return
            elif  len(status)== 0:
                self.messageBox("Information", " Status Cannot be empty!")
                return
            elif  len(address) == 0:
                self.messageBox("Information", " Address Cannot be empty!")
                return
                

            else:
                self.messageBox("Saved", " Member Data Saved")
                self.conn.commit()
                self.loadData()
                self.cancel()
                #self.add_btn.setEnabled(True)
                #self.save_btn.setEnabled(False)
                #self.cancel_btn.setEnabled(False)

    def update(self):
        
        p = self.addPic_edit.text() 
        with open(p, 'rb') as f:
            m=f.read()
     
        mem_id=self.id_edit.text()
        lname=self.lname_edit.text()
        fname=self.fname_edit.text()
        aka1=self.aka_edit.text()
        batch=self.batch_edit.text()
        tbirth=self.tbirth_edit.text()
        current=self.current_edit.text()
        root=self.root_edit.text()
        status=self.status_edit.text()
        address=self.address_edit.text()
        
        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="myproject")
        cur=self.conn.cursor()

        sql = "UPDATE projecttau SET last_name = '"+ lname.upper() +"', first_name= '" + fname.upper() + "', aka = '" + aka1.upper() + "', batch_name= '" + batch.upper()\
                 + "', T_birth = '" + tbirth.upper() + "', current_chapter = '" + current.upper()+ "', root_chapter = '" + root.upper() + "', stat = '" + status.upper() + "', address = '"\
                  + address.upper() + "', photo= %s WHERE member_id = '"+mem_id+"' "
        
        if (sql):
            #msg=QMessageBox()
            if    len(lname) == 0:
                self.messageBox("Information", " Last Name Cannot be empty!")
                return
            elif  len(fname) == 0:
                self.messageBox("Information", " First Name Cannot be empty!")
                return
            elif  len(aka1)  == 0:
                self.messageBox("Information", " A.K.A Cannot be empty!")
                return
            elif  len(batch) == 0:
                self.messageBox("Information", " Batch Name Cannot be empty!")
                return
            elif  len(tbirth)== 0:
                self.messageBox("Information", " Triskelion Birth Cannot be empty!")
                return
            elif  len(current)== 0:
                self.messageBox("Information", " Current Chapter Cannot be empty!")
                return
            elif  len(root)== 0:
                self.messageBox("Information", " Root Chapter Cannot be empty!")
                return
            elif  len(status)== 0:
                self.messageBox("Information", " Status Cannot be empty!")
                return
            elif  len(address) == 0:
                self.messageBox("Information", " Address Cannot be empty!")
                return
                

            else:
                cur.execute(sql,m)
                self.messageBox("Updated", " Member Data Updated")
                self.conn.commit()
                self.loadData()
                self.cancel()
              

    def add_new_button(self):
        self.lname_edit.setEnabled(True)
        self.fname_edit.setEnabled(True)
        self.current_edit.setEnabled(True)
        self.status_edit.setEnabled(True)
        self.batch_edit.setEnabled(True)
        self.address_edit.setEnabled(True)
        self.aka_edit.setEnabled(True)
        self.root_edit.setEnabled(True)
        self.tbirth_edit.setEnabled(True)
        self.save_btn.setEnabled(True)
        self.aka_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.current_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.root_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.lname_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.batch_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.fname_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.tbirth_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.status_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.address_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.clearfield()
        self.addPic_edit.setText("photo/Men.png")
        self.pic_label.setPixmap(QtGui.QPixmap("photo/Men.png"))
        #self.save_btn.setEnabled(True)
        self.cancel_btn.setEnabled(True)
        self.add_btn.setEnabled(False)
        self.save_btn.show()
        self.update_btn.hide()
        self.addPic_btn.setEnabled(True)
        self.edit_btn.setEnabled(False)


    def cancel(self):
        self.lname_edit.setEnabled(False)
        self.fname_edit.setEnabled(False)
        self.current_edit.setEnabled(False)
        self.status_edit.setEnabled(False)
        self.batch_edit.setEnabled(False)
        self.address_edit.setEnabled(False)
        self.aka_edit.setEnabled(False)
        self.root_edit.setEnabled(False)
        self.tbirth_edit.setEnabled(False)
       
        self.aka_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.current_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.root_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.lname_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.batch_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.fname_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.tbirth_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.status_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.address_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        
        self.cancel_btn.setEnabled(False)
        self.add_btn.setEnabled(True)
        self.update_btn.hide()
        self.save_btn.show()
        self.save_btn.setEnabled(False)
        self.addPic_btn.setEnabled(False)
        self.refresh_btn.setEnabled(True)
        self.edit_btn.setEnabled(True)

    def clearfield(self):    
        self.lname_edit.clear()
        self.fname_edit.clear()
        self.current_edit.clear()
        self.status_edit.clear()
        self.batch_edit.clear()
        self.address_edit.clear()
        self.address_edit.clear()
        self.aka_edit.clear()
        self.root_edit.clear()
        self.tbirth_edit.clear()
        self.id_edit.clear()
        self.search_edit.clear()
        self.addPic_edit.setText("photo/Men.png")
        self.pic_label.setPixmap(QtGui.QPixmap("photo/Men.png"))
        #self.editbutton.setEnabled(False)

    def edit(self):
        mem_id = self.id_edit.text()
        if len(mem_id) == 0:
            self.messageBox("Information", "No Data Found")
            return
        self.lname_edit.setEnabled(True)
        self.fname_edit.setEnabled(True)
        self.current_edit.setEnabled(True)
        self.status_edit.setEnabled(True)
        self.batch_edit.setEnabled(True)
        self.address_edit.setEnabled(True)
        self.aka_edit.setEnabled(True)
        self.root_edit.setEnabled(True)
        self.tbirth_edit.setEnabled(True)
        self.aka_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.current_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.root_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.lname_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.batch_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.fname_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.tbirth_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.status_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.address_edit.setStyleSheet("background-color: rgb(255, 195, 44);color: blue")
        self.save_btn.hide()
        self.update_btn.show()
        self.cancel_btn.setEnabled(True)
        self.addPic_btn.setEnabled(True)
        self.refresh_btn.setEnabled(False)
        self.edit_btn.setEnabled(False)

    def cell_click(self,columnCount,rowCount):
        
        #self.editbutton.setEnabled(True)
        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="myproject")
        cur=self.conn.cursor()
        item = self.tableWidget.selectedItems()
        i = (item[0].text())
        if rowCount != (0):
            return

        else:
            cur.execute ("SELECT * from projecttau WHERE member_id=" +str(i))
            col = cur.fetchone()
            #print (col)           
            lname = col[1]
            fname = col[2]
            aka1 = col[3]
            batch = col [4]
            tbirth = col[5]
            current = col[6]
            root = col[7]
            status = col[8]
            add = col[9]
            pic = col[10]



        self.id_edit.setText(i)
        self.lname_edit.setText(lname)
        self.fname_edit.setText(fname)
        self.aka_edit.setText(aka1)
        self.batch_edit.setText(batch)
        self.tbirth_edit.setText(tbirth)
        self.current_edit.setText(current)
        self.root_edit.setText(root)
        self.status_edit.setText(status)
        self.address_edit.setText(add)

        with open('photo/pic.png', 'wb') as f:
                f.write(pic)
                self.addPic_edit.setText('photo/pic.png')
                self.pic_label.setPixmap(QtGui.QPixmap("photo/pic.png"))
    
    def loadData(self):
       
        row = 0
        try: 
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password= "noahkuan03",
                database = "myproject"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM projecttau ORDER BY last_name ASC" )
            result = mycursor.fetchall()
            
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                  
        except mc.Error as e:
            print ("Error Occured")
              

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.setWindowFlags( QtCore.Qt.CustomizeWindowHint )
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/tipaz.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowFlags( QtCore.Qt.WindowCloseButtonHint )
        MainWindow.setWindowIcon(icon)
        MainWindow.resize(1098, 822)
        MainWindow.setStyleSheet("background-color: rgb(59, 59, 59);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #HEADER FRAME
        self.header_frame = QtWidgets.QFrame(self.centralwidget)
        self.header_frame.setGeometry(QtCore.QRect(0, 0, 1191, 91))
        self.header_frame.setStyleSheet("background-color: rgb(255, 195, 44);")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        
        #TIPAZ TRISKELION TITLE
        self.title_label = QtWidgets.QLabel(self.header_frame)
        self.title_label.setGeometry(QtCore.QRect(180, 20, 891, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(5, 1, 96);")
        self.title_label.setObjectName("title_label")
        
        #SMALL LOGO HEADER
        self.logo_label = QtWidgets.QLabel(self.header_frame)
        self.logo_label.setGeometry(QtCore.QRect(70, 0, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(4)
        self.logo_label.setFont(font)
        self.logo_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("photo/tipaz.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        
        #FORM FRAME
        self.form_frame = QtWidgets.QFrame(self.centralwidget)
        self.form_frame.setGeometry(QtCore.QRect(20, 110, 1058, 701))
        self.form_frame.setMinimumSize(QtCore.QSize(2, 2))
        self.form_frame.setStyleSheet("background-color: rgb(5, 1, 96);")
        self.form_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame.setObjectName("form_frame")
        
        #TABLE WIDGET
        self.tableWidget = QtWidgets.QTableWidget(self.form_frame)
        self.tableWidget.setGeometry(QtCore.QRect(18, 20, 1020, 251))
        self.tableWidget.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        
        #item = QtWidgets.QTableWidgetItem()
        #self.tableWidget.setHorizontalHeaderItem(10, item)

        self.tableWidget.cellClicked.connect(self.cell_click)
        self.tableWidget.verticalHeader().setVisible(False)
        self.loadData()
        
        #ADD PICTURE BUTTON
        self.addPic_btn = QtWidgets.QPushButton(self.form_frame)
        self.addPic_btn.setGeometry(QtCore.QRect(20, 300, 181, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.addPic_btn.setFont(font)
        self.addPic_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.addPic_btn.setObjectName("addPic_btn")
        #self.addPic_btn.clicked.connect(self.load_image)
        self.addPic_btn.clicked.connect(self.browse_image)
        self.addPic_btn.setEnabled(False)

       
        
        #SEARCH BUTTON
        self.search_button = QtWidgets.QPushButton(self.form_frame)
        self.search_button.setGeometry(QtCore.QRect(210, 300, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search_button.setFont(font)
        self.search_button.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.search_button.setObjectName("search_button")
        self.search_button.clicked.connect(self.search)

        #ADD NEW BUTTON
        self.add_btn = QtWidgets.QPushButton(self.form_frame)
        self.add_btn.setGeometry(QtCore.QRect(20, 620, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_btn.setFont(font)
        self.add_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.add_new_button)
        
        #SAVE BUTTON
        self.save_btn = QtWidgets.QPushButton(self.form_frame)
        self.save_btn.setGeometry(QtCore.QRect(160, 620, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.save_btn.setObjectName("save_btn")
        self.save_btn.clicked.connect(self.insert_data)
        self.save_btn.setEnabled(False)

        #UPDATE BUTTON
        self.update_btn = QtWidgets.QPushButton(self.form_frame)
        self.update_btn.setGeometry(QtCore.QRect(160, 620, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.update_btn.setFont(font)
        self.update_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.update_btn.setObjectName("save_btn")
        self.update_btn.clicked.connect(self.update)
        self.update_btn.hide()
        
        #CANCEL BUTTON
        self.cancel_btn = QtWidgets.QPushButton(self.form_frame)
        self.cancel_btn.setGeometry(QtCore.QRect(290, 620, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.clicked.connect(self.cancel)
        self.cancel_btn.setEnabled(False)
        
        #EDIT BUTTON
        self.edit_btn = QtWidgets.QPushButton(self.form_frame)
        self.edit_btn.setGeometry(QtCore.QRect(430, 620, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.edit_btn.setFont(font)
        self.edit_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.edit_btn.setObjectName("edit_btn")
        self.edit_btn.clicked.connect(self.edit)
        
        #REFRESH BUTTON
        self.refresh_btn = QtWidgets.QPushButton(self.form_frame)
        self.refresh_btn.setGeometry(QtCore.QRect(570, 620, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.refresh_btn.setFont(font)
        self.refresh_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.refresh_btn.setObjectName("refresh_btn")
        self.refresh_btn.clicked.connect(self.loadData)
        self.refresh_btn.clicked.connect(self.clearfield)
        self.refresh_btn.clicked.connect(lambda: self.addPic_edit.setText("photo/Men.png"))
        self.refresh_btn.clicked.connect(lambda:self.pic_label.setPixmap(QtGui.QPixmap("photo/Men.png")))
        
        #EXIT BUTTON
        self.exit_btn = QtWidgets.QPushButton(self.form_frame)
        self.exit_btn.setGeometry(QtCore.QRect(710, 620, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(self.popup)
        #self.exit_btn:hover(background-color: 4CAF50; color: white;}
        #self.exit_btn.setStyleSheet("QPushButton::hover" "{background-color : white;}")

        #ADD PICTURE EDIT TEXTBOX
        self.addPic_edit = QtWidgets.QLineEdit(self.form_frame)
        self.addPic_edit.setGeometry(QtCore.QRect(20, 325, 181, 21))
        self.addPic_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.addPic_edit.setCursorPosition(0)
        self.addPic_edit.setObjectName("addPic_edit")
        self.addPic_edit.setText("photo/Men.png")
        self.addPic_edit.hide()


        #MEMBER ID EDIT TEXTBOX
        self.id_edit = QtWidgets.QLineEdit(self.form_frame)
        self.id_edit.setGeometry(QtCore.QRect(210, 370, 201, 31))
        self.id_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.id_edit.setCursorPosition(0)
        self.id_edit.setObjectName("id_edit")
        self.id_edit.setEnabled(False)
        
        #AKA EDIT TEXTBOX
        self.aka_edit = QtWidgets.QLineEdit(self.form_frame)
        self.aka_edit.setGeometry(QtCore.QRect(430, 370, 201, 31))
        self.aka_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.aka_edit.setObjectName("aka_edit")
        self.aka_edit.setEnabled(False)
        
        #CURRENT CHAPTER EDIT TEXTBOX
        self.current_edit = QtWidgets.QLineEdit(self.form_frame)
        self.current_edit.setGeometry(QtCore.QRect(650, 370, 201, 31))
        self.current_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.current_edit.setCursorPosition(0)
        self.current_edit.setObjectName("current_edit")
        self.current_edit.setEnabled(False)
        
        #ROOT CHAPTER EDIT TEXTBOX
        self.root_edit = QtWidgets.QLineEdit(self.form_frame)
        self.root_edit.setGeometry(QtCore.QRect(650, 430, 201, 31))
        self.root_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.root_edit.setObjectName("root_edit")
        self.root_edit.setEnabled(False)
        
        #LAST NAME EDIT TEXTBOX
        self.lname_edit = QtWidgets.QLineEdit(self.form_frame)
        self.lname_edit.setGeometry(QtCore.QRect(210, 430, 201, 31))
        self.lname_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.lname_edit.setObjectName("lname_edit")
        self.lname_edit.setEnabled(False)
        
        #BATCH NAME EDIT TEXTBOX
        self.batch_edit = QtWidgets.QLineEdit(self.form_frame)
        self.batch_edit.setGeometry(QtCore.QRect(430, 430, 201, 31))
        self.batch_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.batch_edit.setObjectName("batch_edit")
        self.batch_edit.setEnabled(False)
        
        #FIRST NAME EDIT TEXTBOX
        self.fname_edit = QtWidgets.QLineEdit(self.form_frame)
        self.fname_edit.setGeometry(QtCore.QRect(210, 490, 201, 31))
        self.fname_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.fname_edit.setObjectName("fname_edit")
        self.fname_edit.setEnabled(False)
        
        #T-BIRTH TEXTBOX
        self.tbirth_edit = QtWidgets.QLineEdit(self.form_frame)
        self.tbirth_edit.setGeometry(QtCore.QRect(430, 490, 201, 31))
        self.tbirth_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.tbirth_edit.setObjectName("tbirth_edit")
        self.tbirth_edit.setEnabled(False)
        
        #STATUS EDIT TEXTBOX
        self.status_edit = QtWidgets.QLineEdit(self.form_frame)
        self.status_edit.setGeometry(QtCore.QRect(650, 490, 201, 31))
        self.status_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.status_edit.setObjectName("status_edit")
        self.status_edit.setEnabled(False)
        
        #ADDRESS EDIT TEXTBOX
        self.address_edit = QtWidgets.QLineEdit(self.form_frame)
        self.address_edit.setGeometry(QtCore.QRect(20, 550, 831, 31))
        self.address_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.address_edit.setObjectName("address_edit")
        self.address_edit.setEnabled(False)
    
        #SEARCH EDIT TEXTBOX
        self.search_edit = QtWidgets.QLineEdit(self.form_frame)
        self.search_edit.setGeometry(QtCore.QRect(430, 300, 201, 31))
        self.search_edit.setTabletTracking(False)
        self.search_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.search_edit.setCursorPosition(0)
        self.search_edit.setObjectName("search_edit")

        #PICTURE OF BROD LABEL
        self.pic_label = QtWidgets.QLabel(self.form_frame)
        self.pic_label.setGeometry(QtCore.QRect(20, 350, 181, 171))
        self.pic_label.setMinimumSize(QtCore.QSize(0, 0))
        self.pic_label.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pic_label.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.pic_label.setFrameShape(QtWidgets.QFrame.Box)
        self.pic_label.setText("")
        self.pic_label.setObjectName("pic_label")
        self.pic_label.setScaledContents(True)
        self.pic_label.setPixmap(QtGui.QPixmap("photo/Men.png"))



        #MEMBER ID LABEL
        self.id_label = QtWidgets.QLabel(self.form_frame)
        self.id_label.setGeometry(QtCore.QRect(210, 350, 71, 16))
        self.id_label.setStyleSheet("color: rgb(185, 185, 185);")
        self.id_label.setObjectName("id_label")
        
        #LAST NAME LABEL
        self.lname_label = QtWidgets.QLabel(self.form_frame)
        self.lname_label.setGeometry(QtCore.QRect(210, 410, 71, 16))
        self.lname_label.setStyleSheet("color: rgb(185, 185, 185);")
        self.lname_label.setObjectName("lname_label")
        
        #FIRST NAME LABEL
        self.fname_label = QtWidgets.QLabel(self.form_frame)
        self.fname_label.setGeometry(QtCore.QRect(210, 470, 71, 16))
        self.fname_label.setStyleSheet("color: rgb(185, 185, 185);")
        self.fname_label.setObjectName("fname_label")
        
        #ADDRESS LABEL
        self.address_label = QtWidgets.QLabel(self.form_frame)
        self.address_label.setGeometry(QtCore.QRect(20, 530, 71, 16))
        self.address_label.setStyleSheet("color: rgb(185, 185, 185);")
        self.address_label.setObjectName("address_label")
        
        #AKA LABEL
        self.aka_label = QtWidgets.QLabel(self.form_frame)
        self.aka_label.setGeometry(QtCore.QRect(430, 350, 71, 16))
        self.aka_label.setStyleSheet("color: rgb(185, 185, 185);")
        self.aka_label.setObjectName("aka_label")
        
        #BATCH NAME LABEL
        self.batch_label = QtWidgets.QLabel(self.form_frame)
        self.batch_label.setGeometry(QtCore.QRect(430, 410, 71, 16))
        self.batch_label.setStyleSheet("color: rgb(185, 185, 185);")
        self.batch_label.setObjectName("batch_label")
       
        #T-BIRTH LABEL
        self.tbirth_label = QtWidgets.QLabel(self.form_frame)
        self.tbirth_label.setGeometry(QtCore.QRect(430, 470, 71, 16))
        self.tbirth_label.setStyleSheet("color: rgb(185, 185, 185);")
        self.tbirth_label.setObjectName("tbirth_label")
        
        #CURRENT CHAPTER LABEL
        self.current_label = QtWidgets.QLabel(self.form_frame)
        self.current_label.setGeometry(QtCore.QRect(650, 350, 81, 16))
        self.current_label.setStyleSheet("color: rgb(185, 185, 185);")
        self.current_label.setObjectName("current_label")
        
        #ROOT CHAPTER LABEL
        self.root_label = QtWidgets.QLabel(self.form_frame)
        self.root_label.setGeometry(QtCore.QRect(650, 410, 71, 16))
        self.root_label.setStyleSheet("color: rgb(185, 185, 185);")
        self.root_label.setObjectName("root_label")
        
        #STATUS LABEL
        self.status_label = QtWidgets.QLabel(self.form_frame)
        self.status_label.setGeometry(QtCore.QRect(650, 470, 71, 16))
        self.status_label.setStyleSheet("color: rgb(185, 185, 185);")
        self.status_label.setObjectName("status_label")
        
        #BIG TIPAZ LOGO LABEL
        self.bigLogo_label = QtWidgets.QLabel(self.form_frame)
        self.bigLogo_label.setGeometry(QtCore.QRect(872, 370, 171, 171))
        self.bigLogo_label.setText("")
        self.bigLogo_label.setPixmap(QtGui.QPixmap("photo/tipaz.png"))
        self.bigLogo_label.setScaledContents(True)
        self.bigLogo_label.setObjectName("bigLogo_label")
        
        #FRAME OF 3 AND 3 TECH LOGO
        self.frame = QtWidgets.QFrame(self.form_frame)
        self.frame.setGeometry(QtCore.QRect(880, 590, 161, 71))
        self.frame.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setMidLineWidth(3)
        self.frame.setObjectName("frame")
        
        # 3 AND 3 TECH LOGO
        self.threeand3_label = QtWidgets.QLabel(self.frame)
        self.threeand3_label.setGeometry(QtCore.QRect(0, 0, 171, 71))
        self.threeand3_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.threeand3_label.setLineWidth(2)
        self.threeand3_label.setText("")
        self.threeand3_label.setPixmap(QtGui.QPixmap("photo/and3.png"))
        self.threeand3_label.setScaledContents(True)
        self.threeand3_label.setObjectName("threeand3_label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TIPAZ TRISKELION CHAPTER"))
        self.title_label.setText(_translate("MainWindow", "TIPAZ TRISKELION CHAPTER"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Member ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "AKA"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "T-Birth"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Batch Name"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Current Chapter"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Root Chapter"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Address"))
        
        #item = self.tableWidget.horizontalHeaderItem(10)
        #item.setText(_translate("MainWindow", "Photo"))
        
        self.add_btn.setText(_translate("MainWindow", "ADD NEW"))
        self.addPic_btn.setText(_translate("MainWindow", "ADD PHOTO"))
        self.save_btn.setText(_translate("MainWindow", "SAVE"))
        self.update_btn.setText(_translate("MainWindow", "UPDATE"))
        self.cancel_btn.setText(_translate("MainWindow", "CANCEL"))
        self.edit_btn.setText(_translate("MainWindow", "EDIT"))
        self.refresh_btn.setText(_translate("MainWindow", "REFRESH"))
        self.exit_btn.setText(_translate("MainWindow", "EXIT"))
        self.search_button.setText(_translate("MainWindow", "SEARCH"))
        self.id_label.setText(_translate("MainWindow", "Member ID"))
        self.lname_label.setText(_translate("MainWindow", "Last Name"))
        self.fname_label.setText(_translate("MainWindow", "First Name"))
        self.address_label.setText(_translate("MainWindow", "Address"))
        self.aka_label.setText(_translate("MainWindow", "AKA"))
        self.batch_label.setText(_translate("MainWindow", "Batch Name"))
        self.tbirth_label.setText(_translate("MainWindow", "T-Birth"))
        self.current_label.setText(_translate("MainWindow", "Current Chapter"))
        self.root_label.setText(_translate("MainWindow", "Root Chapter"))
        self.status_label.setText(_translate("MainWindow", "Status"))
        self.tbirth_edit.setPlaceholderText(_translate("MainWindow", "MM/DD/YYYY"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
