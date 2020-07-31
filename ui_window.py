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
from PySide2 import QtWidgets, QtCore

from reference import tkinter_window
from script import tor_runner
from ui_syntax_highlight import SyntaxHighlighter
from PySide2.QtCore import (QCoreApplication, QMetaObject,
                            QRect, QSize)
from PySide2.QtGui import (QIcon, QPixmap)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(574, 521)
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
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
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

        self.captureButton = QPushButton(self.centralwidget)
        self.captureButton.setObjectName(u"captureButton")
        self.captureButton.setGeometry(QRect(10, 450, 75, 23))
        self.runScriptButton = QPushButton(self.centralwidget)
        self.runScriptButton.setObjectName(u"runScriptButton")
        self.runScriptButton.setGeometry(QRect(90, 450, 75, 23))
        self.scriptlabel = QLabel(self.centralwidget)
        self.scriptlabel.setObjectName(u"scriptlabel")
        self.scriptlabel.setGeometry(QRect(10, 10, 47, 13))
        self.imagelabel = QLabel(self.centralwidget)
        self.imagelabel.setObjectName(u"imagelabel")
        self.imagelabel.setGeometry(QRect(340, 10, 71, 16))
        self.workspaceLabel = QLabel(self.centralwidget)
        self.workspaceLabel.setObjectName(u"workspaceLabel")
        self.workspaceLabel.setGeometry(QRect(10, 420, 61, 16))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 420, 401, 20))
        self.lineEdit.setReadOnly(True)
        self.WorkSpaceButton = QPushButton(self.centralwidget)
        self.WorkSpaceButton.setObjectName(u"WorkSpaceButton")
        self.WorkSpaceButton.setGeometry(QRect(480, 420, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 574, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.captureButton.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.runScriptButton.setText(QCoreApplication.translate("MainWindow", u"Run Script", None))
        self.scriptlabel.setText(QCoreApplication.translate("MainWindow", u"Script", None))
        self.imagelabel.setText(QCoreApplication.translate("MainWindow", u"Image (png)", None))
        self.workspaceLabel.setText(QCoreApplication.translate("MainWindow", u"WorkSpace", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Set Workspace path", None))
        self.WorkSpaceButton.setText(QCoreApplication.translate("MainWindow", u"Set Path", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))

        # Syntax highlight
        SyntaxHighlighter(self.textEdit.document())
    # retranslateUi


class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Mouse Tracker')
        self.label = QLabel(self)
        self.label.resize(200, 40)

    def mouseMoveEvent(self, event):
        self.label.setText('Mouse coords: ( %d : %d )' % (event.x(), event.y()))


class UI_Action(object):
    def __init__(self, MainWindow, qt_windows):
        self.qt = qt_windows
        self.test_data()
        self.action_menu_save()
        self.action_menu_exit()
        self.action_menu_help()
        self.action_button_capture()
        self.action_button_run_script()
        self.action_set_workspace()

    def test_data(self):
        # Load for Sample code
        infile = open('./resource/script.tor', 'r')
        self.qt.textEdit.setPlainText(infile.read())
        abs_path = os.path.abspath('./resource/')
        self.qt.lineEdit.setText(abs_path)
        self.list_image_load_on(abs_path)

    def action_menu_save(self):
        self.qt.actionSave.triggered.connect(lambda: self.menu_save())

    def action_set_workspace(self):
        self.qt.WorkSpaceButton.clicked.connect(lambda: self.button_workspace_selectDirectory())

    def action_menu_exit(self):
        self.qt.actionExit.triggered.connect(lambda: self.menu_exit())

    def action_menu_help(self):
        self.qt.actionAbout.triggered.connect(lambda: self.menu_help())

    def action_button_capture(self):
        if not self.workspace_empty_check():
            workspace_path = self.qt.lineEdit.text()
            qt_endpoint = self
            self.qt.captureButton.clicked.connect(lambda: tkinter_window.exec(workspace_path, qt_endpoint))

    def action_button_run_script(self):
        self.qt.runScriptButton.clicked.connect(lambda: self.button_run_script())

    def button_mouse_coord(self):
        m = MouseTracker()
        m.show()

    def button_workspace_selectDirectory(self):
        selected_directory = QFileDialog.getExistingDirectory()
        print('workspace_directory:', selected_directory)
        if selected_directory:
            self.qt.lineEdit.setText(selected_directory)
            self.list_image_load_on(selected_directory)

    def button_run_script(self):
        if not self.workspace_empty_check():
            # QMessageBox.information(None, "Information", "Start!")
            workspace_path = self.qt.lineEdit.text()
            self.menu_save()
            tor_runner.run(workspace_path)

    def menu_exit(self):
        QCoreApplication.quit()

    def menu_save(self):
        if not self.workspace_empty_check():
            text_plain = self.qt.textEdit.toPlainText()
            print(text_plain)
            file_path = self.qt.lineEdit.text() + '/' + 'script.tor'
            with open(file_path, 'w') as f:
                f.write(text_plain)

    def workspace_empty_check(self):
        wp_path = self.qt.lineEdit.text()
        if not wp_path:
            QMessageBox.warning(None, "Warning", "Please set workspace!")
            return True

    def menu_help(self):
        QMessageBox.information(None, "Information", "Created by python.")

    #def button_func_mapper(self, button, func, *args):
    #    button.clicked.connect(lambda: func(args))

    def list_image_load_on(self, dir_path):
        '''
        https://medium.com/xster-tech/pyqt-drag-images-into-list-widget-for-thumbnail-list-e4a12f906bd8
        '''
        self.qt.imglistWidget.clear()

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
