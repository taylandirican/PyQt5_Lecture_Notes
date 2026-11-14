import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200, 200, 600, 600)
        self.initUI()

    def initUI(self):
        self.number1_lbl = QtWidgets.QLabel(self)
        self.number1_lbl.setText("Number 1:")
        self.number1_lbl.move(50, 50)

        self.number2_lbl = QtWidgets.QLabel(self)
        self.number2_lbl.setText("Number 2:")
        self.number2_lbl.move(50, 80)

        self.txt1 = QtWidgets.QLineEdit(self)
        self.txt1.move(100, 50)
        self.txt1.resize(200, 32)

        self.txt2 = QtWidgets.QLineEdit(self)
        self.txt2.move(100, 80)
        self.txt2.resize(200, 32)

        self.btn_plus = QtWidgets.QPushButton(self)
        self.btn_plus.move(100, 110)
        self.btn_plus.setText("+")
        self.btn_plus.clicked.connect(self.calculate)

        self.btn_minus = QtWidgets.QPushButton(self)
        self.btn_minus.move(100, 140)
        self.btn_minus.setText("-")
        self.btn_minus.clicked.connect(self.calculate)

        self.btn_times = QtWidgets.QPushButton(self)
        self.btn_times.move(100, 170)
        self.btn_times.setText("*")
        self.btn_times.clicked.connect(self.calculate)

        self.btn_divide = QtWidgets.QPushButton(self)
        self.btn_divide.move(100, 200)
        self.btn_divide.setText("/")
        self.btn_divide.clicked.connect(self.calculate)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Result:")
        self.lbl_result.move(100, 230)

    def calculate(self):
        sender = self.sender()

        if sender.text() == "+":
            self.lbl_result.setText(
                "Result: " + str(float(self.txt1.text()) + float(self.txt2.text()))
            )
        elif sender.text() == "-":
            self.lbl_result.setText(
                "Result: " + str(float(self.txt1.text()) - float(self.txt2.text()))
            )
        elif sender.text() == "*":
            self.lbl_result.setText(
                "Result: " + str(float(self.txt1.text()) * float(self.txt2.text()))
            )
        elif sender.text() == "/":
            self.lbl_result.setText(
                "Result: " + str(float(self.txt1.text()) / float(self.txt2.text()))
            )


def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())


app()
