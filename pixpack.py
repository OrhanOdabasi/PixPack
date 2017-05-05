#!/usr/bin/env python3
# run.py
# this is the main script to run the program.
# Author: Orhan Odabasi (0rh.odabasi[at]gmail.com)

from ui import *
import sys
from PyQt5 import QtWidgets

def main():

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":

    main()
