from sys import argv, exit
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton 
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor, QPen
from random import randint

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Кнопка"))

class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.paintstate = False

    def paint(self):
        self.paintstate = True
        self.repaint()

    def paintEvent(self, event):
        if self.paintstate:
            qp = QPainter()
            qp.begin(self)
            self.getcircles(qp)
            qp.end()

    def getcircles(self, qp):
        qp.setPen(QPen(QColor(randint(0, 255), randint(0, 255), randint(0,255)), 5))
        qp.drawEllipse(randint(0, 600), randint(0, 400), randint(0, 200), randint(0, 200))

def main():
    app = QApplication(argv)
    window = App()
    window.show()
    exit(app.exec())

if __name__ == "__main__":
    main()
