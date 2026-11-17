import sys
from PyQt5 import QtWidgets
from CheckBoxForm import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbMovie.stateChanged.connect(self.show_state)
        self.ui.cbSport.stateChanged.connect(self.show_state)
        self.ui.cbBook.stateChanged.connect(self.show_state)
        self.ui.btnSave.clicked.connect(self.showResult)
        self.ui.btnSave.clicked.connect(self.getAllChecked)

    def show_state(self, value):
        cb = self.sender()
        print(cb.text())
        print(cb.isChecked())

    def showResult(self):
        result = ""
        if self.ui.cbMovie.isChecked():
            result += "Movie "
        if self.ui.cbSport.isChecked():
            result += "Sport "
        if self.ui.cbBook.isChecked():
            result += "Book "
        self.ui.lblResult.setText("Selected: " + result)

    def getAllChecked(self):
        items = self.ui.centralwidget.findChildren(QtWidgets.QCheckBox)
        for i in items:
            print(i.text())


def App():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())


App()
