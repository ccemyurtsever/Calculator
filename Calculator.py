import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import math


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle("CY - Calculator")
        self.setGeometry(200, 200, 370, 487)
        self.initUI()

    def initUI(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Number 1 = ")
        self.label1.move(20, 30)
        self.label1.setStyleSheet("background-color: #4180b3")

        self.entry1 = QtWidgets.QLineEdit(self)
        self.entry1.move(120, 30)
        self.entry1.resize(200, 30)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Number 2 = ")
        self.label2.move(20, 80)
        self.label2.setStyleSheet("background-color: #4180b3")

        self.entry2 = QtWidgets.QLineEdit(self)
        self.entry2.move(120, 80)
        self.entry2.resize(200, 30)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("+")
        self.btn_topla.move(20, 170)
        self.btn_topla.setFixedSize(60, 40)
        self.btn_topla.clicked.connect(self.hesapla)

        self.btn_fark = QtWidgets.QPushButton(self)
        self.btn_fark.setText("-")
        self.btn_fark.move(90, 170)
        self.btn_fark.setFixedSize(60, 40)
        self.btn_fark.clicked.connect(self.hesapla)

        self.btn_çarp = QtWidgets.QPushButton(self)
        self.btn_çarp.setText("*")
        self.btn_çarp.move(160, 170)
        self.btn_çarp.setFixedSize(60, 40)
        self.btn_çarp.clicked.connect(self.hesapla)

        self.btn_böl = QtWidgets.QPushButton(self)
        self.btn_böl.setText("/")
        self.btn_böl.move(230, 170)
        self.btn_böl.setFixedSize(60, 40)
        self.btn_böl.clicked.connect(self.hesapla)

        self.btn_modulus = QtWidgets.QPushButton(self)
        self.btn_modulus.setText("%")
        self.btn_modulus.move(300, 170)
        self.btn_modulus.setFixedSize(60, 40)
        self.btn_modulus.clicked.connect(self.hesapla)

        self.btn_fact = QtWidgets.QPushButton(self)
        self.btn_fact.setText("!")
        self.btn_fact.move(300, 220)
        self.btn_fact.setFixedSize(60, 40)
        self.btn_fact.clicked.connect(self.hesapla)

        self.btn_kök = QtWidgets.QPushButton(self)
        self.btn_kök.setText("√")
        self.btn_kök.move(230, 380)
        self.btn_kök.setFixedSize(60, 40)
        self.btn_kök.clicked.connect(self.hesapla)

        self.sonuc = QtWidgets.QLabel(self)
        self.sonuc.setText(" Result = ")
        self.sonuc.move(20, 120)
        self.sonuc.setStyleSheet("background-color: #00e100")
        self.sonuc.resize(200, 40)

        self.bt1 = QtWidgets.QPushButton(self)
        self.bt1.setText("1")
        self.bt1.resize(60, 60)
        self.bt1.move(20, 220)
        self.bt1.clicked.connect(self.hesapla)

        self.bt2 = QtWidgets.QPushButton(self)
        self.bt2.setText("2")
        self.bt2.resize(60, 60)
        self.bt2.move(90, 220)
        self.bt2.clicked.connect(self.hesapla)

        self.bt3 = QtWidgets.QPushButton(self)
        self.bt3.setText("3")
        self.bt3.resize(60, 60)
        self.bt3.move(160, 220)
        self.bt3.clicked.connect(self.hesapla)

        self.bt4 = QtWidgets.QPushButton(self)
        self.bt4.setText("4")
        self.bt4.resize(60, 60)
        self.bt4.move(230, 220)
        self.bt4.clicked.connect(self.hesapla)

        self.bt5 = QtWidgets.QPushButton(self)
        self.bt5.setText("5")
        self.bt5.resize(60, 60)
        self.bt5.move(20, 300)
        self.bt5.clicked.connect(self.hesapla)

        self.bt6 = QtWidgets.QPushButton(self)
        self.bt6.setText("6")
        self.bt6.resize(60, 60)
        self.bt6.move(90, 300)
        self.bt6.clicked.connect(self.hesapla)

        self.bt7 = QtWidgets.QPushButton(self)
        self.bt7.setText("7")
        self.bt7.resize(60, 60)
        self.bt7.move(160, 300)
        self.bt7.clicked.connect(self.hesapla)

        self.bt8 = QtWidgets.QPushButton(self)
        self.bt8.setText("8")
        self.bt8.resize(60, 60)
        self.bt8.move(230, 300)
        self.bt8.clicked.connect(self.hesapla)

        self.bt9 = QtWidgets.QPushButton(self)
        self.bt9.setText("9")
        self.bt9.resize(60, 60)
        self.bt9.move(20, 380)
        self.bt9.clicked.connect(self.hesapla)

        self.bt0 = QtWidgets.QPushButton(self)
        self.bt0.setText("0")
        self.bt0.resize(60, 60)
        self.bt0.move(90, 380)
        self.bt0.clicked.connect(self.hesapla)

        self.info = QtWidgets.QPushButton(self)
        self.info.setText("?")
        self.info.resize(50, 25)
        self.info.move(320, 0)
        self.info.clicked.connect(self.hesapla)

        self.clear = QtWidgets.QPushButton(self)
        self.clear.setText("AC")
        self.clear.resize(60,60)
        self.clear.move(160,380)
        self.clear.clicked.connect(self.hesapla)


    def hesapla(self):
        if self.entry1.text() == "" or self.entry2.text() == "":
            QMessageBox.about(self, "CY - Warning", "Please enter a number")
            
        sender = self.sender().text()
        result = 0
        if sender == "+":
            result = int(self.entry1.text()) + int(self.entry2.text())
        elif sender == "-":
            result = int(self.entry1.text()) - int(self.entry2.text())
        elif sender == "*":
            result = int(self.entry1.text()) * int(self.entry2.text())
        elif sender == "/":
            result = int(self.entry1.text()) / int(self.entry2.text())
        elif sender == "%":
            result = int(self.entry1.text()) % int(self.entry2.text())
        elif sender == "!":
            fact = int(self.entry1.text())
            x = 1
            for i in range(fact):
                x = x * (i + 1)
            result = x
        elif sender == "√":
            result = math.sqrt(int(self.entry1.text()))
        elif sender == "1":
            self.entry1.setText(self.entry1.text() + "1")
        elif sender == "2":
            self.entry1.setText(self.entry1.text() + "2")
        elif sender == "3":
            self.entry1.setText(self.entry1.text() + "3")
        elif sender == "4":
            self.entry1.setText(self.entry1.text() + "4")
        elif sender == "5":
            self.entry1.setText(self.entry1.text() + "5")
        elif sender == "6":
            self.entry1.setText(self.entry1.text() + "6")
        elif sender == "7":
            self.entry1.setText(self.entry1.text() + "7")
        elif sender == "8":
            self.entry1.setText(self.entry1.text() + "8")
        elif sender == "9":
            self.entry1.setText(self.entry1.text() + "9")
        elif sender == "0":
            self.entry1.setText(self.entry1.text() + "0")
        elif sender == "?":
            QMessageBox.about(self, "CY - İnfo", "For communication: https://cemyurtsever.dev/")
        elif sender == "AC":
            self.entry1.clear()
            self.entry2.clear()

        self.sonuc.setText(f"Result {result}")


def app():
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec_())


app()
