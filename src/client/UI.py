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
        self.P0Label.setGeometry(QtCore.QRect(643, 450, 101, 20))
        self.P0Label.setScaledContents(True)
        self.P0Label.setObjectName("P0Label")
        self.P2Label = QtWidgets.QLabel(self.centralwidget)
        self.P2Label.setGeometry(QtCore.QRect(360, 10, 161, 18))
        self.P2Label.setScaledContents(True)
        self.P2Label.setObjectName("P2Label")
        self.P1Label = QtWidgets.QLabel(self.centralwidget)
        self.P1Label.setGeometry(QtCore.QRect(610, 230, 191, 18))
        self.P1Label.setScaledContents(True)
        self.P1Label.setObjectName("P1Label")
        self.P3Label = QtWidgets.QLabel(self.centralwidget)
        self.P3Label.setGeometry(QtCore.QRect(30, 230, 141, 18))
        self.P3Label.setScaledContents(True)
        self.P3Label.setObjectName("P3Label")
        self.ReadyButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReadyButton.setGeometry(QtCore.QRect(750, 450, 41, 20))
        self.ReadyButton.setObjectName("ReadyButton")
        self.NameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NameEdit.setGeometry(QtCore.QRect(320, 240, 113, 26))
        self.NameEdit.setObjectName("NameEdit")
        self.showPic0 = QtWidgets.QLabel(self.centralwidget)
        self.showPic0.setGeometry(QtCore.QRect(210, 180, 64, 18))
        self.showPic0.setText("")
        self.showPic0.setScaledContents(True)
        self.showPic0.setObjectName("showPic0")
        self.showPic1 = QtWidgets.QLabel(self.centralwidget)
        self.showPic1.setGeometry(QtCore.QRect(310, 180, 64, 18))
        self.showPic1.setScaledContents(True)
        self.showPic1.setObjectName("showPic1")
        self.showPic2 = QtWidgets.QLabel(self.centralwidget)
        self.showPic2.setGeometry(QtCore.QRect(410, 180, 64, 18))
        self.showPic2.setText("")
        self.showPic2.setScaledContents(True)
        self.showPic2.setObjectName("showPic2")
        self.showPic3 = QtWidgets.QLabel(self.centralwidget)
        self.showPic3.setGeometry(QtCore.QRect(510, 180, 64, 18))
        self.showPic3.setText("")
        self.showPic3.setScaledContents(True)
        self.showPic3.setObjectName("showPic3")
        self.handPic0 = QtWidgets.QLabel(self.centralwidget)
        self.handPic0.setGeometry(QtCore.QRect(140, 380, 64, 18))
        self.handPic0.setText("")
        self.handPic0.setScaledContents(True)
        self.handPic0.setObjectName("handPic0")
        self.handPic1 = QtWidgets.QLabel(self.centralwidget)
        self.handPic1.setGeometry(QtCore.QRect(220, 380, 64, 18))
        self.handPic1.setText("")
        self.handPic1.setScaledContents(True)
        self.handPic1.setObjectName("handPic1")
        self.handPic2 = QtWidgets.QLabel(self.centralwidget)
        self.handPic2.setGeometry(QtCore.QRect(300, 380, 64, 18))
        self.handPic2.setText("")
        self.handPic2.setScaledContents(True)
        self.handPic2.setObjectName("handPic2")
        self.handPic3 = QtWidgets.QLabel(self.centralwidget)
        self.handPic3.setGeometry(QtCore.QRect(380, 380, 64, 18))
        self.handPic3.setText("")
        self.handPic3.setScaledContents(True)
        self.handPic3.setObjectName("handPic3")
        self.handPic4 = QtWidgets.QLabel(self.centralwidget)
        self.handPic4.setGeometry(QtCore.QRect(460, 380, 64, 18))
        self.handPic4.setText("")
        self.handPic4.setScaledContents(True)
        self.handPic4.setObjectName("handPic4")
        self.handPic5 = QtWidgets.QLabel(self.centralwidget)
        self.handPic5.setGeometry(QtCore.QRect(540, 380, 64, 18))
        self.handPic5.setText("")
        self.handPic5.setScaledContents(True)
        self.handPic5.setObjectName("handPic5")
        self.descEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.descEdit.setGeometry(QtCore.QRect(170, 540, 331, 26))
        self.descEdit.setObjectName("descEdit")
        self.handButton0 = QtWidgets.QPushButton(self.centralwidget)
        self.handButton0.setGeometry(QtCore.QRect(160, 350, 31, 26))
        self.handButton0.setObjectName("handButton0")
        self.handButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.handButton1.setGeometry(QtCore.QRect(240, 350, 31, 26))
        self.handButton1.setObjectName("handButton1")
        self.handButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.handButton2.setGeometry(QtCore.QRect(320, 350, 31, 26))
        self.handButton2.setObjectName("handButton2")
        self.handButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.handButton3.setGeometry(QtCore.QRect(400, 350, 31, 26))
        self.handButton3.setObjectName("handButton3")
        self.handButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.handButton4.setGeometry(QtCore.QRect(480, 350, 31, 26))
        self.handButton4.setObjectName("handButton4")
        self.handButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.handButton5.setGeometry(QtCore.QRect(560, 350, 31, 26))
        self.handButton5.setObjectName("handButton5")
        self.showButton0 = QtWidgets.QPushButton(self.centralwidget)
        self.showButton0.setGeometry(QtCore.QRect(240, 150, 31, 26))
        self.showButton0.setAccessibleName("")
        self.showButton0.setObjectName("showButton0")
        self.showButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.showButton1.setGeometry(QtCore.QRect(340, 150, 31, 26))
        self.showButton1.setAccessibleName("")
        self.showButton1.setObjectName("showButton1")
        self.showButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.showButton2.setGeometry(QtCore.QRect(440, 150, 31, 26))
        self.showButton2.setAccessibleName("")
        self.showButton2.setObjectName("showButton2")
        self.showButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.showButton3.setGeometry(QtCore.QRect(540, 150, 31, 26))
        self.showButton3.setAccessibleName("")
        self.showButton3.setObjectName("showButton3")
        self.DescLabel = QtWidgets.QLabel(self.centralwidget)
        self.DescLabel.setGeometry(QtCore.QRect(170, 540, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DescLabel.setFont(font)
        self.DescLabel.setText("")
        self.DescLabel.setScaledContents(True)
        self.DescLabel.setObjectName("DescLabel")
        self.pickLabel0 = QtWidgets.QLabel(self.centralwidget)
        self.pickLabel0.setGeometry(QtCore.QRect(210, 180, 100, 54))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pickLabel0.setFont(font)
        self.pickLabel0.setText("")
        self.pickLabel0.setObjectName("pickLabel0")
        self.pickLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.pickLabel1.setGeometry(QtCore.QRect(310, 180, 100, 54))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pickLabel1.setFont(font)
        self.pickLabel1.setText("")
        self.pickLabel1.setTextFormat(QtCore.Qt.AutoText)
        self.pickLabel1.setObjectName("pickLabel1")
        self.pickLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.pickLabel2.setGeometry(QtCore.QRect(410, 180, 100, 54))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pickLabel2.setFont(font)
        self.pickLabel2.setText("")
        self.pickLabel2.setObjectName("pickLabel2")
        self.pickLabel3 = QtWidgets.QLabel(self.centralwidget)
        self.pickLabel3.setGeometry(QtCore.QRect(510, 180, 100, 54))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pickLabel3.setFont(font)
        self.pickLabel3.setText("")
        self.pickLabel3.setObjectName("pickLabel3")
        self.fromLabel0 = QtWidgets.QLabel(self.centralwidget)
        self.fromLabel0.setGeometry(QtCore.QRect(210, 355, 100, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fromLabel0.setFont(font)
        self.fromLabel0.setText("")
        self.fromLabel0.setObjectName("fromLabel0")
        self.fromLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.fromLabel1.setGeometry(QtCore.QRect(310, 355, 100, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fromLabel1.setFont(font)
        self.fromLabel1.setText("")
        self.fromLabel1.setObjectName("fromLabel1")
        self.fromLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.fromLabel2.setGeometry(QtCore.QRect(410, 355, 100, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fromLabel2.setFont(font)
        self.fromLabel2.setText("")
        self.fromLabel2.setObjectName("fromLabel2")
        self.fromLabel3 = QtWidgets.QLabel(self.centralwidget)
        self.fromLabel3.setGeometry(QtCore.QRect(510, 355, 100, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fromLabel3.setFont(font)
        self.fromLabel3.setText("")
        self.fromLabel3.setObjectName("fromLabel3")
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
        self.handButton0.clicked.connect(mainWindow.ChoseHand0)
        self.handButton1.clicked.connect(mainWindow.ChoseHand1)
        self.handButton2.clicked.connect(mainWindow.ChoseHand2)
        self.handButton3.clicked.connect(mainWindow.ChoseHand3)
        self.handButton4.clicked.connect(mainWindow.ChoseHand4)
        self.handButton5.clicked.connect(mainWindow.ChoseHand5)
        self.showButton0.clicked.connect(mainWindow.ChoseShow0)
        self.showButton1.clicked.connect(mainWindow.ChoseShow1)
        self.showButton2.clicked.connect(mainWindow.ChoseShow2)
        self.showButton3.clicked.connect(mainWindow.ChoseShow3)
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
        self.showPic1.setText(_translate("mainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.descEdit.setText(_translate("mainWindow", "请输入你的描述"))
        self.handButton0.setText(_translate("mainWindow", "选它"))
        self.handButton1.setText(_translate("mainWindow", "选它"))
        self.handButton2.setText(_translate("mainWindow", "选它"))
        self.handButton3.setText(_translate("mainWindow", "选它"))
        self.handButton4.setText(_translate("mainWindow", "选它"))
        self.handButton5.setText(_translate("mainWindow", "选它"))
        self.showButton0.setText(_translate("mainWindow", "选它"))
        self.showButton1.setText(_translate("mainWindow", "选它"))
        self.showButton2.setText(_translate("mainWindow", "选它"))
        self.showButton3.setText(_translate("mainWindow", "选它"))

