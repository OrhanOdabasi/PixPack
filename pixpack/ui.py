#!/usr/bin/env python3
# iu.py
# Created by: PyQt5 UI code generator 5.5.1
# This script consists of ui script of PixPack
# Author: Orhan Odabasi (0rh.odabasi[at]gmail.com)

from PyQt5 import QtCore, QtGui, QtWidgets
from pixpack import utils
from pixpack import process
from pixpack import grouping
import json
import threading
import os
import shutil


CW_DIR = os.path.dirname(os.path.dirname(__file__)) # main directory


class Ui_MainWindow(object):

    def __init__(self):
        # initialize system language variables and translation file
        # TODO: photo_dataset will be set in __init__ with 'self'
        self.lang = utils.sys_trans_var()
        json_dir = os.path.join(CW_DIR, 'json/translate.json')
        with open(json_dir, 'r') as f:
            self.trans = json.load(f)

    def setupUi(self, MainWindow):
        # MainWindow properties
        MainWindow.setFixedSize(620, 520)
        MainWindow.setWindowTitle(self.trans["title"][self.lang])
        icon = QtGui.QIcon()
        icon_dir = os.path.join(CW_DIR, "img/icon.ico")
        icon.addPixmap(QtGui.QPixmap(icon_dir), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)

        # introlabel properties
        self.introLabel = QtWidgets.QLabel(self.centralwidget)
        self.introLabel.setGeometry(QtCore.QRect(40, 10, 531, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.introLabel.setFont(font)
        self.introLabel.setText(self.trans["intro_label"][self.lang])
        self.introLabel.setAlignment(QtCore.Qt.AlignCenter)

        # srcpath properties
        self.srcPath = QtWidgets.QLineEdit(self.centralwidget)
        self.srcPath.setGeometry(QtCore.QRect(220, 115, 300, 25))

        # srcpathfinder properties
        self.srcPathFinder = QtWidgets.QPushButton(self.centralwidget)
        self.srcPathFinder.setGeometry(QtCore.QRect(530, 115, 50, 25))
        self.srcPathFinder.setText(self.trans["finder_bttn"][self.lang])
        self.srcPathFinder.clicked.connect(self.srcpathFinder)

        # sourcelabel properties
        self.sourceLabel = QtWidgets.QLabel(self.centralwidget)
        self.sourceLabel.setGeometry(QtCore.QRect(25, 115, 181, 25))
        self.sourceLabel.setText(self.trans["path_label"][self.lang])
        self.sourceLabel.setAlignment(QtCore.Qt.AlignCenter)

        # line properties
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 60, 541, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # scanlabel properties
        self.scanLabel = QtWidgets.QLabel(self.centralwidget)
        self.scanLabel.setGeometry(QtCore.QRect(270, 80, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scanLabel.setFont(font)
        self.scanLabel.setText(self.trans["scan_label"][self.lang])
        self.scanLabel.setAlignment(QtCore.Qt.AlignCenter)

        # csvcheckbox properties
        self.csvCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.csvCheckBox.setGeometry(QtCore.QRect(44, 150, 341, 22))
        self.csvCheckBox.setText(self.trans["save_check"][self.lang])

        # scanbutton properties
        self.scanButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanButton.setGeometry(QtCore.QRect(460, 150, 111, 30))
        self.scanButton.setText(self.trans["scan_bttn"][self.lang])
        self.scanButton.clicked.connect(self.scanProcess)

        # pcountlabel properties
        self.pcountLabel = QtWidgets.QLabel(self.centralwidget)
        self.pcountLabel.setGeometry(QtCore.QRect(80, 230, 191, 20))
        self.pcountLabel.setText(self.trans["pcount_label"][self.lang])
        self.pcountLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)

        # psizelabel properties
        self.psizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.psizeLabel.setGeometry(QtCore.QRect(80, 260, 191, 20))
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
        self.statsLabel.setGeometry(QtCore.QRect(260, 196, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.statsLabel.setFont(font)
        self.statsLabel.setText(self.trans["stats_label"][self.lang])
        self.statsLabel.setAlignment(QtCore.Qt.AlignCenter)

        # targetlabel properties
        self.targetLabel = QtWidgets.QLabel(self.centralwidget)
        self.targetLabel.setGeometry(QtCore.QRect(30, 330, 171, 25))
        self.targetLabel.setText(self.trans["pathout_label"][self.lang])
        self.targetLabel.setAlignment(QtCore.Qt.AlignCenter)

        # targetpath properties
        self.targetPath = QtWidgets.QLineEdit(self.centralwidget)
        self.targetPath.setGeometry(QtCore.QRect(220, 330, 300, 25))

        # targetpathfinder properties
        self.targetPathFinder = QtWidgets.QPushButton(self.centralwidget)
        self.targetPathFinder.setGeometry(QtCore.QRect(530, 330, 50, 25))
        self.targetPathFinder.setText(self.trans["finder_bttn"][self.lang])
        self.targetPathFinder.clicked.connect(self.targetpathFinder)

        # progressbar properties
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(410, 430, 171, 25))
        self.progressBar.setValue(0)
        self.progressBar.setMinimum(0)
        self.progressBar.setFormat('%v/{}'.format("-"))

        # combobox properties
        self.sorting = QtWidgets.QComboBox(self.centralwidget)
        self.sorting.setGeometry(QtCore.QRect(250, 370, 200, 30))
        self.sorting_options = ["YYYY (2017)", "YYYY-MM (2017-03)", "SEASON (WINTER)"]
        for o in self.sorting_options:
            self.sorting.addItem(o)
        self.sorting.setCurrentIndex(1)

        # startbutton properties
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(460, 370, 111, 30))
        self.startButton.setText(self.trans["start_bttn"][self.lang])
        self.startButton.clicked.connect(self.copyProcess)

        # processlabel properties
        self.processLabel = QtWidgets.QLabel(self.centralwidget)
        self.processLabel.setGeometry(QtCore.QRect(30, 430, 51, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.processLabel.setFont(font)
        self.processLabel.setText(self.trans["proc_label"][self.lang])

        # procoutlabel properties
        self.procOutLabel = QtWidgets.QLabel(self.centralwidget)
        self.procOutLabel.setGeometry(QtCore.QRect(90, 430, 301, 25))
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

        self.all_widgets = [self.targetPath,
                            self.scanButton,
                            self.srcPath,
                            self.csvCheckBox,
                            self.scanButton,
                            self.startButton,
                            self.srcPathFinder,
                            self.targetPathFinder,
                            self.sorting,]


    def bttnEnable(self):
        # set all buttons active
        for wdgts in self.all_widgets:
            wdgts.setEnabled(True)

    def bttnDisable(self):
        # setting all button unavailable
        for wdgts in self.all_widgets:
            wdgts.setEnabled(False)

    def srcpathFinder(self):
        # source directory dialog
        finder_title = self.trans["srcfinder_dialog_title"][self.lang]
        target_path = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, finder_title, '/home')
        self.srcPath.setText(target_path)

    def targetpathFinder(self):
        # target directory dialog
        finder_title = self.trans["targetfinder_dialog_title"][self.lang]
        target_path = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, finder_title, '/home')
        self.targetPath.setText(target_path)

    def thrforScan(self,p):
        # Thread process for scanning
        self.bttnDisable()
        self.procOut(self.trans["proc_scan"][self.lang], 2)
        try:
            global photo_dataset, video_dataset
            p_count, p_size, folder_count, photo_dataset, video_dataset = process.scanDir(p)
            self.pcountOutLabel.setText(str(p_count))
            self.psizeOutLabel.setText(str(p_size))
            self.fcountOutLabel.setText(str(folder_count))
            self.progressBar.setMaximum(len(photo_dataset)+len(video_dataset))
            self.progressBar.setFormat('%v/{}'.format(self.progressBar.maximum()))
            if self.csvCheckBox.checkState():
                process.saveReport(photo_dataset, video_dataset, p)
                self.procOut(self.trans["proc_saveTrue"][self.lang], 1)
            else:
                self.procOut(self.trans["proc_saveFalse"][self.lang], 1)
        except Exception as e:
            self.procOut(self.trans["proc_blankpath"][self.lang], 0)
        self.bttnEnable()

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
        # scan button functionality
        path = self.srcPath.text()
        t1 = threading.Thread(target=self.thrforScan, args=(path,))
        t1.start()

    def copyProcess(self):
        # copy button functionality
        try:
            photo_dataset
            video_dataset
            datasets_exist = True
        except:
            datasets_exist = False
        if not datasets_exist:
            self.procOut(self.trans["proc_NULL"][self.lang], 0)
        else:
            target_path = self.targetPath.text().strip()
            if target_path == "":
                # If target path is not set, target path is set as source path
                target_path = self.srcPath.text()
            elif not os.path.exists(target_path) and target_path != "":
                # If target path is a word or a phrase
                # then target path will be in source directory with specified word or phrase
                target_path = os.path.join(self.srcPath.text(), target_path)
            copy_suffix = self.trans["copy"][self.lang]
            t2 = threading.Thread(target=self.thrforCopy, args=(target_path, photo_dataset, video_dataset, copy_suffix))
            t2.start()

    def bttf(self, destination, photodata, videodata, copy_suffix):
        # setting grouping algorithms
        # check out grouping.py for more about sorting options
        if self.sorting.currentIndex() == 0:
            pattern = "yr"
        elif self.sorting.currentIndex() == 1:
            pattern = "ym"
        elif self.sorting.currentIndex() == 2:
            pattern = "ss"

        # copy process
        progress_status = 0
        for photo in photodata:
            dest_dir = grouping.group_by_dates(photo[3], destination, pattern=pattern)
            if os.path.exists(dest_dir):
                dest_file = os.path.join(dest_dir, photo[0])
                dest_file = utils.name_existing_photos(dest_dir, dest_file, copy_suffix)
                shutil.copy2(photo[1], dest_file)
            else:
                os.makedirs(dest_dir)
                shutil.copy2(photo[1], dest_dir)
            progress_status += 1
            self.progressBar.setValue(progress_status)

        for photo in videodata:
            dest_dir = os.path.join(destination, "VIDEO")
            if os.path.exists(dest_dir):
                dest_file = os.path.join(dest_dir, photo[0])
                dest_file = utils.name_existing_photos(dest_dir, dest_file, copy_suffix)
                shutil.copy2(photo[1], dest_file)
            else:
                os.makedirs(dest_dir)
                shutil.copy2(photo[1], dest_dir)
            progress_status += 1
            self.progressBar.setValue(progress_status)

    def procOut(self, text, signal):
        # process line configuration
        if signal == 0: # warning
            self.procOutLabel.setStyleSheet("color:red;")
            self.procOutLabel.setText(text)
        elif signal == 1: # success
            self.procOutLabel.setStyleSheet("color:green;")
            self.procOutLabel.setText(text)
        elif signal == 2: # processing
            self.procOutLabel.setStyleSheet("color:orange;")
            self.procOutLabel.setText(text)

    def aboutMenuWidget(self):
        # about menu
        self.aboutWidget = QtWidgets.QWidget()
        self.aboutWidget.setWindowTitle(self.trans["about_menu"][self.lang])
        self.aboutWidget.setFixedSize(300, 220)
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

        self.label5 = QtWidgets.QLabel(self.aboutWidget)
        self.label5.setGeometry(QtCore.QRect(13, 150, 270, 25))
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setText(self.trans["version"][self.lang] + utils.versioncontrol()[0])

        self.label6 = QtWidgets.QLabel(self.aboutWidget)
        self.label6.setGeometry(QtCore.QRect(13, 180, 270, 25))
        self.label6.setAlignment(QtCore.Qt.AlignCenter)
        self.label6.setText(self.trans["versionCodeName"][self.lang] + utils.versioncontrol()[1])

        z = [self.label5, self.label6]

        for x in z:
            x.setFont(fontAbout)
            x.setEnabled(True)

        self.aboutWidget.show()
