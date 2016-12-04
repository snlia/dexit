# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EnterRoomButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnterRoomButton.setGeometry(QtCore.QRect(440, 210, 81, 26))
        self.EnterRoomButton.setObjectName("EnterRoomButton")
        self.IPEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IPEdit.setGeometry(QtCore.QRect(320, 180, 113, 26))
        self.IPEdit.setObjectName("IPEdit")
        self.PortEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PortEdit.setGeometry(QtCore.QRect(320, 210, 113, 26))
        self.PortEdit.setObjectName("PortEdit")
        self.P0Label = QtWidgets.QLabel(self.centralwidget)
        self.P0Label.setGeometry(QtCore.QRect(323, 450, 101, 20))
        self.P0Label.setObjectName("P0Label")
        self.P2Label = QtWidgets.QLabel(self.centralwidget)
        self.P2Label.setGeometry(QtCore.QRect(360, 10, 161, 18))
        self.P2Label.setObjectName("P2Label")
        self.P1Label = QtWidgets.QLabel(self.centralwidget)
        self.P1Label.setGeometry(QtCore.QRect(610, 230, 191, 18))
        self.P1Label.setObjectName("P1Label")
        self.P3Label = QtWidgets.QLabel(self.centralwidget)
        self.P3Label.setGeometry(QtCore.QRect(30, 230, 141, 18))
        self.P3Label.setObjectName("P3Label")
        self.ReadyButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReadyButton.setGeometry(QtCore.QRect(430, 450, 41, 20))
        self.ReadyButton.setObjectName("ReadyButton")
        self.NameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NameEdit.setGeometry(QtCore.QRect(320, 240, 113, 26))
        self.NameEdit.setObjectName("NameEdit")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.EnterRoomButton.clicked.connect(mainWindow.EnterRoom)
        self.ReadyButton.clicked.connect(mainWindow.Ready)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.EnterRoomButton.setText(_translate("mainWindow", "进入房间"))
        self.IPEdit.setText(_translate("mainWindow", "IP地址"))
        self.PortEdit.setText(_translate("mainWindow", "端口"))
        self.P0Label.setText(_translate("mainWindow", "Player0"))
        self.P2Label.setText(_translate("mainWindow", "Player2"))
        self.P1Label.setText(_translate("mainWindow", "Player1"))
        self.P3Label.setText(_translate("mainWindow", "Player3"))
        self.ReadyButton.setText(_translate("mainWindow", "准备"))
        self.NameEdit.setText(_translate("mainWindow", "昵称"))

