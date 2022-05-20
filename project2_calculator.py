# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt, cos, sin, tan

margin = 10
fontsize = 30

# cot = lambda x: 1/tan(x)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(361, 588)
        MainWindow.resize(361, 658)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setObjectName("outputLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.sign_button())
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("C"))
        self.cButton.setGeometry(QtCore.QRect(102, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.remove_button())
        self.arrowButton.setGeometry(QtCore.QRect(191, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("+"))
        self.addButton.setGeometry(QtCore.QRect(277, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.substractButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("-"))
        self.substractButton.setGeometry(QtCore.QRect(275, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.substractButton.setFont(font)
        self.substractButton.setObjectName("substractButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("3"))
        self.threeButton.setGeometry(QtCore.QRect(189, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("1"))
        self.oneButton.setGeometry(QtCore.QRect(margin, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(275, 289, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("6"))
        self.sixButton.setGeometry(QtCore.QRect(189, 289, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("4"))
        self.fourButton.setGeometry(QtCore.QRect(margin, 289, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 289, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("/"))
        self.divideButton.setGeometry(QtCore.QRect(275, 379, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("9"))
        self.nineButton.setGeometry(QtCore.QRect(189, 379, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("7"))
        self.sevenButton.setGeometry(QtCore.QRect(margin, 379, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 379, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("0"))
        self.zeroButton.setGeometry(QtCore.QRect(margin, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.decimal_button())
        self.decimalButton.setGeometry(QtCore.QRect(101, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.eqaul_button())
        self.equalButton.setGeometry(QtCore.QRect(276, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.sqrtButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("x^y"))
        self.sqrtButton.setGeometry(QtCore.QRect(190, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.sqrtButton.setFont(font)
        self.sqrtButton.setObjectName("sqrtButton")

        self.tanxButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("tan"))
        self.tanxButton.setGeometry(QtCore.QRect(189, 561, 75, 75))        
        font = QtGui.QFont()
        font.setPointSize(fontsize)        
        self.tanxButton.setFont(font)
        self.tanxButton.setObjectName("tanxButton")
        self.cotxButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("cot"))
        self.cotxButton.setGeometry(QtCore.QRect(275, 561, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.cotxButton.setFont(font)
        self.cotxButton.setObjectName("cotxButton")
        self.cosxButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("cos"))
        self.cosxButton.setGeometry(QtCore.QRect(98, 561, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.cosxButton.setFont(font)
        self.cosxButton.setObjectName("cosxButton")
        self.sinxButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_button("sin"))
        self.sinxButton.setGeometry(QtCore.QRect(margin, 561, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(fontsize)
        self.sinxButton.setFont(font)
        self.sinxButton.setObjectName("sinxButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def remove_button(self):
        # Grap the text from screen
        text = self.outputLabel.text()
        # Remove the last item
        text = text[:-1]        
        # Output back the rest text
        self.outputLabel.setText(text)
        
    def sign_button(self):
        text = self.outputLabel.text()
        # Do a simple math for sign change
        answer = (-1) * eval(text)
        self.outputLabel.setText(str(answer))
    
    # Let's do some simple math
    def eqaul_button(self):
        # Grap the text from screen
        text = self.outputLabel.text()
        try:
            # if "rt" in text:
            #     base, power = self.outputLabel.text().split("rt")
            #     answer = eval(base) ** eval(power) # x**y
            # else:
            answer = eval(text)
            self.outputLabel.setText(str(answer)) 
        except:
            # Output the error to screen
            self.outputLabel.setText("Error") 
            
    # Add a decimal after number
    def decimal_button(self):
        # Grap the entire text
        text = self.outputLabel.text()
        # Check if the last item is a dot 
        if text[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f"{text}.")
    
    def press_button(self, pressed):
        # self.outputLabel.setText(pressed)
        left_parethesis = r"("
        right_parethesis = r")"
        double_star = r"**"
        if pressed == "C":
            self.outputLabel.setText("0")  
        elif pressed in ["sin", "cos", "tan"]:
            self.outputLabel.setText(f"{pressed}{left_parethesis}{self.outputLabel.text()}{right_parethesis}") 
        elif pressed == "x^y":
            self.outputLabel.setText(f"{self.outputLabel.text()}{double_star}")               
        else:
            # Check if the number string starts with "0"
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("") 
            # Concatenate the pressed button with what was already there
            self.outputLabel.setText(f"{self.outputLabel.text()}{pressed}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        # self.outputLabel.setText(_translate("MainWindow", "0"))
        # self.percentButton.setText(_translate("MainWindow", "%"))
        # self.cButton.setText(_translate("MainWindow", "C"))
        # self.arrowButton.setText(_translate("MainWindow", "<<"))
        # self.addButton.setText(_translate("MainWindow", "+"))
        # self.substractButton.setText(_translate("MainWindow", "-"))
        # self.threeButton.setText(_translate("MainWindow", "3"))
        # self.oneButton.setText(_translate("MainWindow", "1"))
        # self.twoButton.setText(_translate("MainWindow", "2"))
        # self.multiplyButton.setText(_translate("MainWindow", "*"))
        # self.sixButton.setText(_translate("MainWindow", "6"))
        # self.fourButton.setText(_translate("MainWindow", "4"))
        # self.fiveButton.setText(_translate("MainWindow", "5"))
        # self.divideButton.setText(_translate("MainWindow", "/"))
        # self.nineButton.setText(_translate("MainWindow", "9"))
        # self.sevenButton.setText(_translate("MainWindow", "7"))
        # self.eightButton.setText(_translate("MainWindow", "8"))
        # self.zeroButton.setText(_translate("MainWindow", "0"))
        # self.decimalButton.setText(_translate("MainWindow", "."))
        # self.equalButton.setText(_translate("MainWindow", "="))
        # self.sqrtButton.setText(_translate("MainWindow", "rt"))

        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "+/-"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.substractButton.setText(_translate("MainWindow", "-"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.multiplyButton.setText(_translate("MainWindow", "*"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.sqrtButton.setText(_translate("MainWindow", "x^y"))
        self.tanxButton.setText(_translate("MainWindow", "Tan"))
        self.cotxButton.setText(_translate("MainWindow", "Cot"))
        self.cosxButton.setText(_translate("MainWindow", "Cos"))
        self.sinxButton.setText(_translate("MainWindow", "Sin"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

