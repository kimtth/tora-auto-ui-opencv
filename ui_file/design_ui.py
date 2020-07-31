# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
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
    # retranslateUi

