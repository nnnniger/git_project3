import io
import random
import sys

from PyQt5 import uic, QtWidgets, Qt, QtCore
from PyQt5.QtWidgets import QApplication, QGraphicsEllipseItem, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.newcircleButton = QtWidgets.QPushButton(self.centralwidget)
        self.newcircleButton.setGeometry(QtCore.QRect(0, 0, 401, 31))
        self.newcircleButton.setObjectName("newcircleButton")
        self.view = QtWidgets.QGraphicsView(self.centralwidget)
        self.view.setGeometry(QtCore.QRect(0, 40, 401, 241))
        self.view.setObjectName("view")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.newcircleButton.setText(_translate("MainWindow", "PushButton"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('ЖЕЛТЫЕ КРУЖКИ')
        self.scene = QtWidgets.QGraphicsScene(self)
        self.view.setScene(self.scene)
        self.newcircleButton.clicked.connect(self.newCircle)

    def newCircle(self):
        colors = ["yellow", "green", "blue", "red"]
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        ellipse = QGraphicsEllipseItem(x, y, diameter, diameter)
        color = random.choice(colors)
        if color == "green":
            ellipse.setBrush(Qt.Qt.green)
        elif color == "red":
            ellipse.setBrush(Qt.Qt.red)
        elif color == "blue":
            ellipse.setBrush(Qt.Qt.blue)
        elif color == "yellow":
            ellipse.setBrush(Qt.Qt.yellow)
        self.scene.addItem(ellipse)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
