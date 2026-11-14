from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow


class App(QtWidgets.QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_toplama.clicked.connect(self.hesapla)
        self.ui.btn_cikarma.clicked.connect(self.hesapla)
        self.ui.btn_carpma.clicked.connect(self.hesapla)
        self.ui.btn_bolme.clicked.connect(self.hesapla)

    def hesapla(self):
        sender = self.sender().text()
        result = 0
        if sender == "Toplama":
            result = str(float(self.ui.Number1.text()) + float(self.ui.Number2.text()))

        elif sender == "Çıkarma":
            result = str(float(self.ui.Number1.text()) - float(self.ui.Number2.text()))
        elif sender == "Çarpma":
            result = str(float(self.ui.Number1.text()) * float(self.ui.Number2.text()))

        elif sender == "Bölme":
            result = str(float(self.ui.Number1.text()) / float(self.ui.Number2.text()))

        self.ui.lbl_result.setText("Sonuç: " + result)


def application():
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())


application()