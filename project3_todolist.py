from PyQt5 import QtCore, QtGui, QtWidgets

fontsize = 12

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.additem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.add_item())
        self.additem_pushButton.setGeometry(QtCore.QRect(10, 110, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.additem_pushButton.setFont(font)
        self.additem_pushButton.setObjectName("additem_pushButton")
        self.deleteitem_pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.deleteitem_pushButton_2.setGeometry(QtCore.QRect(180, 110, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deleteitem_pushButton_2.setFont(font)
        self.deleteitem_pushButton_2.setObjectName("deleteitem_pushButton_2")
        self.export_pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.export_pushButton_3.setGeometry(QtCore.QRect(370, 110, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.export_pushButton_3.setFont(font)
        self.export_pushButton_3.setObjectName("export_pushButton_3")
        self.date_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.date_lineEdit.setGeometry(QtCore.QRect(100, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date_lineEdit.setFont(font)
        self.date_lineEdit.setObjectName("date_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(10, 160, 521, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mylist_listWidget.setFont(font)
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        self.date_pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.date_pushButton_4.setGeometry(QtCore.QRect(10, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date_pushButton_4.setFont(font)
        self.date_pushButton_4.setObjectName("date_pushButton_4")
        self.name_lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.name_lineEdit_2.setGeometry(QtCore.QRect(350, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_lineEdit_2.setFont(font)
        self.name_lineEdit_2.setObjectName("name_lineEdit_2")
        self.name_pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.name_pushButton_5.setGeometry(QtCore.QRect(260, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_pushButton_5.setFont(font)
        self.name_pushButton_5.setObjectName("name_pushButton_5")
        self.description_pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.description_pushButton_6.setGeometry(QtCore.QRect(10, 60, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.description_pushButton_6.setFont(font)
        self.description_pushButton_6.setObjectName("description_pushButton_6")
        self.description_lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.description_lineEdit_3.setGeometry(QtCore.QRect(130, 60, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.description_lineEdit_3.setFont(font)
        self.description_lineEdit_3.setObjectName("name_lineEdit_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget, clicked = lambda: self.grab_date())
        self.calendarWidget.setGeometry(QtCore.QRect(540, 10, 272, 411))
        self.calendarWidget.setObjectName("calendarWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def grab_date(self):
        # Select date from calendar
        date = self.calendarWidget.selectedDate().toPyDate()
        
        # Add the date
        self.date_lineEdit.setText(str(date))
        
    # Add item to list
    def add_item(self):
        # Grab item from box
        item = self.date_lineEdit.text() + \
               " | " + self.name_lineEdit_2.text() + \
               " | " + self.description_lineEdit_3.text()
        
        # Add item to list
        self.mylist_listWidget.addItem(item)
        
        # Clear item from box 
        self.date_lineEdit.setText("")
        self.name_lineEdit_2.setText("")
        self.description_lineEdit_3.setText("")

    
    # Delete item from list
    def delete_item(self):
        # Grab selected row 
        current = self.mylist_listWidget.currentRow()
        
        # Delete select row
        self.mylist_listWidget.takeItem(current)
                
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDoList"))
        self.additem_pushButton.setText(_translate("MainWindow", "Add Item to List"))
        self.deleteitem_pushButton_2.setText(_translate("MainWindow", "Del Item From List"))
        self.export_pushButton_3.setText(_translate("MainWindow", "Export Data"))
        self.date_pushButton_4.setText(_translate("MainWindow", "Date"))
        self.name_pushButton_5.setText(_translate("MainWindow", "Name"))
        self.description_pushButton_6.setText(_translate("MainWindow", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

