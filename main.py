import sys

from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import uic


class Model:
    def __init__(self):
        self.count=0

    def changeLabel(self,label):
        label.setText(str(self.count))
    def increment(self,label):
        self.count += 1
        self.changeLabel(label)

    def decrement(self,label):
        self.count -= 1
        self.changeLabel(label)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.model=Model()
        self.start()
        self.call()

    def start(self):
        self.ui=uic.loadUi("window.ui")
        self.ui.show()

    def call(self):
        self.ui.btnIncrem.clicked.connect(lambda:self.model.increment(self.ui.countText))
        self.ui.btnDecrem.clicked.connect(lambda:self.model.decrement(self.ui.countText))

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Window()

    sys.exit(app.exec_())