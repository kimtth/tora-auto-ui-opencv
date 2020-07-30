# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import os

from PIL import Image, ImageQt

from reference import tkinter_window
from ui_syntax_highlight import SyntaxHighlighter
from PySide2.QtCore import (QCoreApplication, QMetaObject,
                            QRect, QSize)
from PySide2.QtGui import (QIcon, QPixmap)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(573, 485)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"E:/qt_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 321, 381))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(340, 30, 221, 381))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.imglistWidget = QListWidget(self.gridLayoutWidget_2)
        self.imglistWidget.setObjectName(u"imglistWidget")

        self.gridLayout_2.addWidget(self.imglistWidget, 0, 0, 1, 1)

        self.loadButton = QPushButton(self.centralwidget)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setGeometry(QRect(480, 420, 75, 23))
        self.captureButton = QPushButton(self.centralwidget)
        self.captureButton.setObjectName(u"captureButton")
        self.captureButton.setGeometry(QRect(10, 420, 75, 23))
        self.runScriptButton = QPushButton(self.centralwidget)
        self.runScriptButton.setObjectName(u"runScriptButton")
        self.runScriptButton.setGeometry(QRect(90, 420, 75, 23))
        self.scriptlabel = QLabel(self.centralwidget)
        self.scriptlabel.setObjectName(u"scriptlabel")
        self.scriptlabel.setGeometry(QRect(10, 10, 47, 13))
        self.imagelabel = QLabel(self.centralwidget)
        self.imagelabel.setObjectName(u"imagelabel")
        self.imagelabel.setGeometry(QRect(340, 10, 71, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 573, 21))
        self.menuExit = QMenu(self.menubar)
        self.menuExit.setObjectName(u"menuExit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuExit.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.captureButton.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.runScriptButton.setText(QCoreApplication.translate("MainWindow", u"Run Script", None))
        self.scriptlabel.setText(QCoreApplication.translate("MainWindow", u"Script", None))
        self.imagelabel.setText(QCoreApplication.translate("MainWindow", u"Image (png)", None))
        self.menuExit.setTitle(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))

        # Syntax highlight
        SyntaxHighlighter(self.textEdit.document())
        # Load for Sample code
        infile = open('./resource/script.tor', 'r')
        self.textEdit.setPlainText(infile.read())
    # retranslateUi


class UI_Action(object):
    def __init__(self, MainWindow, qt_windows):
        self.qt = qt_windows

        self.action_menu_exit()
        self.action_menu_help()
        self.action_button_load()
        self.action_button_capture()
        self.action_button_run_script()

    def action_menu_exit(self):
        self.qt.actionExit.triggered.connect(lambda: self.menu_exit())

    def action_menu_help(self):
        self.qt.actionAbout.triggered.connect(lambda: self.menu_help())

    def action_button_load(self):
        self.qt.loadButton.clicked.connect(lambda: self.button_load_selectDirectory())

    def action_button_capture(self):
        self.qt.captureButton.clicked.connect(lambda: tkinter_window.exec())

    def action_button_run_script(self):
        self.qt.runScriptButton.clicked.connect(lambda: self.button_run_script())

    def button_load_selectDirectory(self):
        selected_directory = QFileDialog.getExistingDirectory()
        print('selected_directory:', selected_directory)
        if selected_directory:
            self.list_image_load_on(selected_directory)

    def button_run_script(self):
        ret = QMessageBox.information(None, "Information", "Not ready yet!")

    def menu_exit(self):
        QCoreApplication.quit()

    def menu_help(self):
        ret = QMessageBox.information(None, "Information", "Created by python.")

    def button_func_mapper(self, button, func, *args):
        button.clicked.connect(lambda: func(args))

    def list_image_load_on(self, dir_path):
        '''
        https://medium.com/xster-tech/pyqt-drag-images-into-list-widget-for-thumbnail-list-e4a12f906bd8
        '''
        for img_file_name in os.listdir(dir_path):
            img_file_path = dir_path + '/' + img_file_name
            if os.path.exists(img_file_path) and img_file_name.lower().endswith(".png"):
                picture = Image.open(img_file_path)
                picture.thumbnail((72, 72), Image.ANTIALIAS)
                icon = QIcon(QPixmap.fromImage(ImageQt.ImageQt(picture)))
                item = QListWidgetItem(os.path.basename(img_file_path)[:20], self.qt.imglistWidget)
                item.setStatusTip(img_file_path)
                item.setIcon(icon)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()  # <-- Instantiate QMainWindow object.
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    action = UI_Action(MainWindow, ui)

    MainWindow.show()
    app.exec_()
