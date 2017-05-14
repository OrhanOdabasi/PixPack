#!/usr/bin/env python3
# run.py
# this is entry point of the program.
# Author: Orhan Odabasi (0rh.odabasi[at]gmail.com)

from pixpack import ui
import sys
from PyQt5 import QtWidgets

def main():
    # main function
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    interface = ui.Ui_MainWindow()
    interface.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    # executing the main function
    main()
