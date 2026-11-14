import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("My First App")
    win.setGeometry(200, 200, 600, 600)
    win.setWindowIcon(QIcon("download.png"))
    win.setToolTip("This is my first app")

    win.show()
    sys.exit(app.exec_())


window()
