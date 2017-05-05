#!/usr/bin/env python3
# iu.py
# Created by: PyQt5 UI code generator 5.5.1
# This script consists of ui script of PixPack
# Author: Orhan Odabasi (0rh.odabasi[at]gmail.com)

from PyQt5 import QtCore, QtGui, QtWidgets
from process import *
import json
import threading
import os.path
import shutil

photo_dataset = []

class Ui_MainWindow(object):

    def __init__(self):

        # initialize system language variables and translation file
        self.lang = sysTransVar()
        with open('translate.json', 'r') as f:
            self.trans = json.load(f)

    def setupUi(self, MainWindow):

        # MainWindow properties
        MainWindow.setFixedSize(582, 500)
        MainWindow.setWindowTitle(self.trans["title"][self.lang])
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)

        # introlabel properties
        self.introLabel = QtWidgets.QLabel(self.centralwidget)
        self.introLabel.setGeometry(QtCore.QRect(20, 10, 531, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.introLabel.setFont(font)
        self.introLabel.setText(self.trans["intro_label"][self.lang])
        self.introLabel.setAlignment(QtCore.Qt.AlignCenter)

        # srcpath properties
        self.srcPath = QtWidgets.QLineEdit(self.centralwidget)
        self.srcPath.setGeometry(QtCore.QRect(190, 110, 360, 25))

        # sourcelabel properties
        self.sourceLabel = QtWidgets.QLabel(self.centralwidget)
        self.sourceLabel.setGeometry(QtCore.QRect(25, 110, 151, 25))
        self.sourceLabel.setText(self.trans["path_label"][self.lang])
        self.sourceLabel.setAlignment(QtCore.Qt.AlignCenter)

        # line properties
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 60, 541, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # scanlabel properties
        self.scanLabel = QtWidgets.QLabel(self.centralwidget)
        self.scanLabel.setGeometry(QtCore.QRect(250, 80, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scanLabel.setFont(font)
        self.scanLabel.setText(self.trans["scan_label"][self.lang])
        self.scanLabel.setAlignment(QtCore.Qt.AlignCenter)

        # csvcheckbox properties
        self.csvCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.csvCheckBox.setGeometry(QtCore.QRect(25, 150, 360, 22))
        self.csvCheckBox.setText(self.trans["save_check"][self.lang])

        # scanbutton properties
        self.scanButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanButton.setGeometry(QtCore.QRect(420, 150, 111, 30))
        self.scanButton.setText(self.trans["scan_bttn"][self.lang])
        self.scanButton.clicked.connect(self.scanProcess)

        # pcountlabel properties
        self.pcountLabel = QtWidgets.QLabel(self.centralwidget)
        self.pcountLabel.setGeometry(QtCore.QRect(110, 230, 161, 20))
        self.pcountLabel.setText(self.trans["pcount_label"][self.lang])
        self.pcountLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)

        # psizelabel properties
        self.psizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.psizeLabel.setGeometry(QtCore.QRect(110, 260, 161, 20))
        self.psizeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.psizeLabel.setText(self.trans["psize_label"][self.lang])
        self.psizeLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)

        #fcountlabel properties
        self.fcountLabel = QtWidgets.QLabel(self.centralwidget)
        self.fcountLabel.setGeometry(QtCore.QRect(80, 290, 191, 20))
        self.fcountLabel.setText(self.trans["fcount_label"][self.lang])
        self.fcountLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)

        # statslabel properties
        self.statsLabel = QtWidgets.QLabel(self.centralwidget)
        self.statsLabel.setGeometry(QtCore.QRect(240, 200, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.statsLabel.setFont(font)
        self.statsLabel.setText(self.trans["stats_label"][self.lang])
        self.statsLabel.setAlignment(QtCore.Qt.AlignCenter)

        # targetlabel properties
        self.targetLabel = QtWidgets.QLabel(self.centralwidget)
        self.targetLabel.setGeometry(QtCore.QRect(25, 330, 155, 25))
        self.targetLabel.setText(self.trans["pathout_label"][self.lang])

        # targetpath properties
        self.targetPath = QtWidgets.QLineEdit(self.centralwidget)
        self.targetPath.setGeometry(QtCore.QRect(190, 330, 360, 25))

        # progressbar properties
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(380, 430, 171, 25))
        self.progressBar.setValue(0)
        self.progressBar.setMinimum(0)
        self.progressBar.setFormat('%v/{}'.format("-"))

        # startbutton properties
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(420, 370, 111, 30))
        self.startButton.setText(self.trans["start_bttn"][self.lang])
        self.startButton.clicked.connect(self.copyProcess)

        # processlabel properties
        self.processLabel = QtWidgets.QLabel(self.centralwidget)
        self.processLabel.setGeometry(QtCore.QRect(20, 430, 50, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.processLabel.setFont(font)
        self.processLabel.setText(self.trans["proc_label"][self.lang])

        # procoutlabel properties
        self.procOutLabel = QtWidgets.QLabel(self.centralwidget)
        self.procOutLabel.setGeometry(QtCore.QRect(71, 430, 281, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPixelSize(11)
        self.procOutLabel.setFont(font)
        self.procOutLabel.setText(self.trans["proc_NA"][self.lang])

        #pcountoutlabel properties
        self.pcountOutLabel = QtWidgets.QLabel(self.centralwidget)
        self.pcountOutLabel.setGeometry(QtCore.QRect(300, 230, 80, 20))

        # psizeoutlabel properties
        self.psizeOutLabel = QtWidgets.QLabel(self.centralwidget)
        self.psizeOutLabel.setGeometry(QtCore.QRect(300, 260, 80, 20))

        # fcountoutlabel properties
        self.fcountOutLabel = QtWidgets.QLabel(self.centralwidget)
        self.fcountOutLabel.setGeometry(QtCore.QRect(300, 290, 80, 20))


        MainWindow.setCentralWidget(self.centralwidget)


        # menubar properties
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 582, 23))
        self.menuBar.setDefaultUp(False)


        # aboutmenu properties
        self.aboutMenu = QtWidgets.QAction(self.trans["about_menu"][self.lang], self.menuBar)
        self.aboutMenu.triggered.connect(self.aboutMenuWidget)
        #self.menuBar.addAction(self.aboutMenu.menuAction())

        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.aboutMenu)

    def bttnEnable(self):

        # setting all buttons available
        self.targetPath.setEnabled(True)
        self.scanButton.setEnabled(True)
        self.srcPath.setEnabled(True)
        self.csvCheckBox.setEnabled(True)
        self.scanButton.setEnabled(True)

    def bttnDisable(self):

        # setting all button unavailable
        self.targetPath.setEnabled(False)
        self.scanButton.setEnabled(False)
        self.srcPath.setEnabled(False)
        self.csvCheckBox.setEnabled(False)
        self.scanButton.setEnabled(False)

    # NOTE: edited
    def thrforScan(self,p):
        # Thread process for scanning
        self.bttnDisable()
        self.procOut(self.trans["proc_scan"][self.lang], 2)
        try:
            global photo_dataset, video_dataset
            p_count, p_size, folder_count, photo_dataset, video_dataset = scanDir(p)
            self.pcountOutLabel.setText(str(p_count))
            self.psizeOutLabel.setText(str(p_size))
            self.fcountOutLabel.setText(str(folder_count))
            self.progressBar.setMaximum(len(photo_dataset)+len(video_dataset))
            self.progressBar.setFormat('%v/{}'.format(self.progressBar.maximum()))
            if self.csvCheckBox.checkState():
                saveReport(photo_dataset, video_dataset, p)
                self.procOut(self.trans["proc_saveTrue"][self.lang], 1)
            else:
                self.procOut(self.trans["proc_saveFalse"][self.lang], 1)
        except Exception as e:
            self.procOut(self.trans["proc_blankpath"][self.lang], 0)
            print(e)
        self.bttnEnable()

    # NOTE: edited
    def thrforCopy(self, target_path, photodata, videodata, copy_suffix):
        # Thread process for copying
        self.bttnDisable()
        self.procOut(self.trans["process"][self.lang], 2)
        try:
            self.bttf(target_path, photodata, videodata, copy_suffix)
            self.procOut(self.trans["proc_ok"][self.lang], 1)
        except:
            self.procOut(self.trans["proc_fail"][self.lang], 0)
        self.bttnEnable()

    def scanProcess(self):

        # scan button connection
        path = self.srcPath.text()
        t1 = threading.Thread(target=self.thrforScan, args=(path,))
        t1.start()

    # NOTE: edited
    def copyProcess(self):
        # copy button connection
        if not photo_dataset and not video_dataset:
            self.procOut(self.trans["proc_NULL"][self.lang], 0)
            return 0
        else:
            target_path = self.targetPath.text()
            if target_path == "":
                target_path = self.srcPath.text()
            elif not os.path.exists(target_path) and target_path != "":
                target_path = os.path.join(self.srcPath.text(), target_path)

        copy_suffix = self.trans["copy"][self.lang]
        t2 = threading.Thread(target=self.thrforCopy, args=(target_path, photo_dataset, video_dataset, copy_suffix))
        t2.start()


    def bttf(self, destination, photodata, videodata, copy_suffix):
        # copy process
        progress_status = 0
        for x in photodata:
            dest_dir = os.path.join(destination, str(x[7]))
            if os.path.exists(dest_dir):
                dest_file = os.path.join(dest_dir, x[0])
                i = 1
                while os.path.exists(dest_file):
                    dest_file = os.path.join(dest_dir, x[0])
                    base_name = os.path.basename(dest_file)
                    name, ext = os.path.splitext(base_name)
                    name = name + "_" + str(copy_suffix) + str(i)
                    base_name = name + ext
                    dest_file = os.path.join(os.path.dirname(dest_file), base_name)
                    i += 1
                shutil.copy2(x[1], dest_file)
            else:
                os.makedirs(dest_dir)
                shutil.copy2(x[1], dest_dir)
            progress_status += 1
            self.progressBar.setValue(progress_status)

        for x in videodata:
            dest_dir = os.path.join(destination, "VIDEOS")
            if os.path.exists(dest_dir):
                dest_file = os.path.join(dest_dir, x[0])
                i = 1
                while os.path.exists(dest_file):
                    dest_file = os.path.join(dest_dir, x[0])
                    base_name = os.path.basename(dest_file)
                    name, ext = os.path.splitext(base_name)
                    name = name + "_" + str(copy_suffix) + str(i)
                    base_name = name + ext
                    dest_file = os.path.join(os.path.dirname(dest_file), base_name)
                    i += 1
                shutil.copy2(x[1], dest_file)
            else:
                os.makedirs(dest_dir)
                shutil.copy2(x[1], dest_dir)
            progress_status += 1
            self.progressBar.setValue(progress_status)

    def procOut(self, text, signal):

        # process line configuration
        # signal 0: Warning
        # signal 1: Success
        # signal 2: process
        if signal == 0:
            self.procOutLabel.setStyleSheet("color:red;")
            self.procOutLabel.setText(text)
            return
        elif signal == 1:
            self.procOutLabel.setStyleSheet("color:green;")
            self.procOutLabel.setText(text)
            return
        elif signal == 2:
            self.procOutLabel.setStyleSheet("color:orange;")
            self.procOutLabel.setText(text)
            return

    def aboutMenuWidget(self):

        self.aboutWidget = QtWidgets.QWidget()
        self.aboutWidget.setWindowTitle(self.trans["about_menu"][self.lang])
        self.aboutWidget.setFixedSize(300, 180)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutWidget.setWindowIcon(icon)

        fontAbout = QtGui.QFont()
        fontAbout.setPointSize(8)
        fontAbout.setBold(True)

        self.label = QtWidgets.QLabel(self.aboutWidget)
        self.label.setGeometry(QtCore.QRect(13, 30, 270, 25))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText(self.trans["prog_info"][self.lang])

        self.label2 = QtWidgets.QLabel(self.aboutWidget)
        self.label2.setGeometry(QtCore.QRect(13, 60, 270, 25))
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setText(self.trans["programmer"][self.lang])

        self.label3 = QtWidgets.QLabel(self.aboutWidget)
        self.label3.setGeometry(QtCore.QRect(13, 90, 270, 25))
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setText(self.trans["contact"][self.lang])

        self.label4 = QtWidgets.QLabel(self.aboutWidget)
        self.label4.setGeometry(QtCore.QRect(13, 120, 270, 25))
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setText(self.trans["prog_lang"][self.lang])

        z = [self.label, self.label2, self.label3, self.label4]

        for x in z:
            x.setFont(fontAbout)
            x.setEnabled(True)

        self.aboutWidget.show()
