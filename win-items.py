import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("My First App")
        self.setGeometry(200, 200, 600, 600)
        self.setWindowIcon(QIcon("download.png"))
        self.setToolTip("This is my first app")
        self.initUI()

    def initUI(self):
        self.label_name = QtWidgets.QLabel(self)
        self.label_name.setText("Name:")
        self.label_name.move(50, 50)

        self.label_surname = QtWidgets.QLabel(self)
        self.label_surname.setText("Surname:")
        self.label_surname.move(50, 80)

        self.label_result = QtWidgets.QLabel(self)
        self.label_result.move(100, 130)
        self.label_result.resize(300, 32)

        self.text_name = QtWidgets.QLineEdit(self)
        self.text_name.move(100, 50)
        self.text_name.resize(200, 32)

        self.text_surname = QtWidgets.QLineEdit(self)
        self.text_surname.move(100, 80)
        self.text_surname.resize(200, 32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.move(100, 110)
        self.btn_save.setText("Save")
        self.btn_save.clicked.connect(self.clicked)

    def clicked(self):
        self.label_result.setText(
            "Result: " + self.text_name.text() + " " + self.text_surname.text()
        )


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
