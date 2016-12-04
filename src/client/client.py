# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from UI import Ui_mainWindow
import socket as sk
import select
import sys
from protocol import *

__author__ = "snlia"
__email__ = "chinsnlia@gmail.com"


class MainThread(QThread):
    triggle = pyqtSignal(list)

    def __init__(self, socket):
        super(MainThread, self).__init__()
        self.socket = socket
        print ("Main Thread runing...")
        pass

    def run(self):
        while(1):
            read_list, write_list, error_list = \
                select.select([self.socket], [], [])

            for sock in read_list:
                # recive all data into buf
                data = sock.recv(4096)
                if not data:
                    return
                print(list(data))
                self.triggle.emit(list(data))
        # end run


class Main(QMainWindow, Ui_mainWindow):
    entered = False
    ready = False
    PLabel = [None, None, None, None]
    namePlayer = [None, None, None, None]
    readyPlayer = [None, None, None, None]

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.SetVisible()
        self.IPEdit.setText('localhost')
        self.PortEdit.setText('5000')
        self.PLabel[0] = self.P0Label
        self.PLabel[1] = self.P1Label
        self.PLabel[2] = self.P2Label
        self.PLabel[3] = self.P3Label
        self.log = open('log', 'a')
    # end __init__

    def SetVisible(self):
        ''' set the initial visibility'''
        self.P0Label.hide()
        self.P1Label.hide()
        self.P2Label.hide()
        self.P3Label.hide()
        self.ReadyButton.hide()
    # end SetVisible

    def getID(self, Id):
        return (Id + self.totPlayer - self.myID) % self.totPlayer
    # end getID

    def getPosID(self, Id):
        return (Id + 4 - self.myID) % 4
    # end getID

    def EnterRoom(self):
        IP = self.IPEdit.text()
        port = int(self.PortEdit.text())
        name = self.NameEdit.text()
        if (len(name.encode("utf-8")) > 10):
            QMessageBox.information(self, "错误", "名字长度不能超过255字节！")
            return
        if (len(name) == 0):
            QMessageBox.information(self, "错误", "昵称不能为空！")
            return

        self.P0Label.setText(name)

        # set up the socket
        self.socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.socket.settimeout(2)

        # connect to remote host
        try:
            self.socket.connect((IP, port))
        except:
            QMessageBox.information(self, "错误", "无法连上主机！")
            return

        self.thread = MainThread(self.socket)
        self.thread.start()
        self.thread.triggle.connect(self.handleMes)

        # send name info
        self.socket.send(bytes([C_TYPE_NAME, len(name.encode("utf-8"))]) +
                         name.encode("utf-8"))
    # end EnterRoom

    def Ready(self):
        # send ready info
        self.socket.send(bytes([C_TYPE_READY]))
        self.ReadyButton.hide()

    def showAllMember(self):
        if self.entered is False:
            print ("Enter Room with name:" + self.namePlayer[self.myID])
            self.IPEdit.hide()
            self.EnterRoomButton.hide()
            self.PortEdit.hide()
            self.NameEdit.hide()
            self.P0Label.show()
            self.ReadyButton.show()
            self.entered = True
    # end showallmember

    def UpdateRoomInfo(self, mes):
        self.totPlayer = mes[1]
        self.myID = mes[2]
        x = 3
        # Update infomation
        for i in range(self.totPlayer):
            tmp = mes[x]
            x += 1
            self.namePlayer[i] = bytes(mes[x:tmp + x]).decode()
            x += tmp
        for i in range(self.totPlayer):
            self.readyPlayer[i] = mes[x + i] > 0

        for i in range(4):
            self.PLabel[i].hide()
        print(self.myID)

        # Update Labels
        for i in range(self.totPlayer):
            nameI = self.namePlayer[i]
            if (self.readyPlayer[i]):
                nameI += '[准备]'
            self.PLabel[self.getPosID(i)].setText(nameI)
            self.PLabel[self.getPosID(i)].show()
        self.showAllMember()
    # end UpdateRoomInfo

    def handleMes(self, mes):
        self.log.write(str(mes))
        if (mes[0] == S_TYPE_FULLROOM):
            QMessageBox.information(self, "错误", "房间已满！")
        elif (mes[0] == S_TYPE_GAMEHASSTART):
            QMessageBox.information(self, "错误", "游戏已经开始！")
        elif (mes[0] == S_TYPE_ROOMINFO):
            self.UpdateRoomInfo(mes)
    # end handleMes

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
