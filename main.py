# -*- coding: utf-8 -*-
import sys
import os
from PyQt5 import QtCore
from PyQt5.Qt import *
from PyQt5.QtWidgets import QDockWidget, QMainWindow, QApplication
from Ui_MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets
import data_rating


class myWin(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(myWin, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Widget = myWin()
    Widget.show()
    sys.exit(app.exec_())
"""
main.py
"""