# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from UI import Ui_mainWindow
import socket as sk
import select
import os
import sys
import time
from protocol import *

__author__ = "snlia"
__email__ = "chinsnlia@gmail.com"


class MainThread(QThread):
    ''' 在这里进行与服务端的通信'''
    triggle = pyqtSignal(list)

    def __init__(self, socket):
        super(MainThread, self).__init__()
        self.socket = socket
        print ("Main Thread runing...")
        pass

    def run(self):
        '''接受信息，并由triggle发送信号让Main进行处理'''
        while(1):
            read_list, write_list, error_list = \
                select.select([self.socket], [], [])

            for sock in read_list:
                # recive all data into buf
                data = sock.recv(4096)
                if not data:
                    return
                self.triggle.emit(list(data))
        # end run


class Main(QMainWindow, Ui_mainWindow):
    entered = False  # 是否进入游戏
    ready = False  # 是否准备游戏
    PLabel = [None, None, None, None]  # 用于名字展示
    PHand = [None, None, None, None, None, None]  # 用于手牌展示
    LPick = [None, None, None, None]  # 用于展示每张图片有谁选
    LFrom = [None, None, None, None]  # 用于展示每张牌是谁的
    BHand = [None, None, None, None, None, None]  # 用于选择手牌
    PShow = [None, None, None, None]  # 用于展示大家选了啥牌
    BShow = [None, None, None, None]  # 用于选择展示的牌
    handCard = [-1, -1, -1, -1, -1, -1]  # 记录手牌
    showCard = [-1, -1, -1, -1]  # 记录展示的牌
    namePlayer = [None, None, None, None]  # 记录玩家的名字
    readyPlayer = [None, None, None, None]  # 记录玩家是否准备
    scorePlayer = [0, 0, 0, 0]  # 记录玩家分数
    Pending0 = []  # 优先度最高的下载队列
    Pending1 = []  # 优先度最低的下载队列
    buf = []  # 将从服务端传来的信息放到buffer中，以连续处理，或是等待消息发送
    banker = False  # 是否是庄家

    def __init__(self, app):
        super(Main, self).__init__()
        self.setupUi(self)
        self.app = app
        self.IPEdit.setText('localhost')
        self.PortEdit.setText('5000')
        self.SetVariate()
        self.SetVisible()
        for i in range(6):
            self.PHand[i].resize(80, 140)
        for i in range(4):
            self.PShow[i].resize(100, 175)
        self.log = open('log', 'a')
    # end __init__

    def SetVariate(self):
        ''' 设置一些变量 '''
        self.PLabel[0] = self.P0Label
        self.PLabel[1] = self.P1Label
        self.PLabel[2] = self.P2Label
        self.PLabel[3] = self.P3Label
        self.PHand[0] = self.handPic0
        self.PHand[1] = self.handPic1
        self.PHand[2] = self.handPic2
        self.PHand[3] = self.handPic3
        self.PHand[4] = self.handPic4
        self.PHand[5] = self.handPic5
        self.PShow[0] = self.showPic0
        self.PShow[1] = self.showPic1
        self.PShow[2] = self.showPic2
        self.PShow[3] = self.showPic3
        self.BHand[0] = self.handButton0
        self.BHand[1] = self.handButton1
        self.BHand[2] = self.handButton2
        self.BHand[3] = self.handButton3
        self.BHand[4] = self.handButton4
        self.BHand[5] = self.handButton5
        self.BShow[0] = self.showButton0
        self.BShow[1] = self.showButton1
        self.BShow[2] = self.showButton2
        self.BShow[3] = self.showButton3
        self.LPick[0] = self.pickLabel0
        self.LPick[1] = self.pickLabel1
        self.LPick[2] = self.pickLabel2
        self.LPick[3] = self.pickLabel3
        self.LFrom[0] = self.fromLabel0
        self.LFrom[1] = self.fromLabel1
        self.LFrom[2] = self.fromLabel2
        self.LFrom[3] = self.fromLabel3
    # end SetVariate

    def SetVisible(self):
        ''' set the initial visibility'''
        self.P0Label.hide()
        self.P1Label.hide()
        self.P2Label.hide()
        self.P3Label.hide()
        self.ReadyButton.hide()
        self.descEdit.hide()
        for i in range(6):
            self.PHand[i].hide()
            self.BHand[i].hide()
        for i in range(4):
            self.PShow[i].hide()
            self.BShow[i].hide()
            self.LFrom[i].hide()
            self.LPick[i].hide()
    # end SetVisible

    def ChoseHand0(self):
        self.ChoseHand(0)

    def ChoseHand1(self):
        self.ChoseHand(1)

    def ChoseHand2(self):
        self.ChoseHand(2)

    def ChoseHand3(self):
        self.ChoseHand(3)

    def ChoseHand4(self):
        self.ChoseHand(4)

    def ChoseHand5(self):
        self.ChoseHand(5)

    def ChoseShow0(self):
        self.ChoseShow(0)

    def ChoseShow1(self):
        self.ChoseShow(1)

    def ChoseShow2(self):
        self.ChoseShow(2)

    def ChoseShow3(self):
        self.ChoseShow(3)

    def getID(self, Id):
        ''' 返回相对于自己的ID '''
        return (Id + self.totPlayer - self.myID) % self.totPlayer
    # end getID

    def getPosID(self, Id):
        ''' 返回相对于自己的位置 '''
        return (Id + 4 - self.myID) % 4
    # end getPosID

    def EnterRoom(self):
        ''' 进入房间，发送信息给服务器，初始化socket并启动线程 '''
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
        ''' 准备，发送消息给服务器 '''
        # send ready info
        self.socket.send(bytes([C_TYPE_READY]))
        self.ReadyButton.hide()
    # end Ready

    def showAllMember(self):
        ''' 修改布局 '''
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
        ''' 将成员信息更新 '''
        try:
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

            # Update Labels
            for i in range(self.totPlayer):
                nameI = self.namePlayer[i]
                if (self.readyPlayer[i]):
                    nameI += '[准备]'
                self.PLabel[self.getPosID(i)].setText(nameI)
                self.PLabel[self.getPosID(i)].show()
                self.showAllMember()
            return x + self.totPlayer
        except:
            print('gg RoomInfo')
            return 0
    # end UpdateRoomInfo

    def ShowBanker(self):
        ''' 显示庄家信息 '''
        self.descEdit.show()
        for i in range(6):
            self.BHand[i].show()
            self.banker = True
        self.DescLabel.hide()
    # end ShowBanker

    def ShowShowCard(self):
        ''' 显示展示图片 '''
        for i in range(self.totPlayer):
            if self.showCard[i] != -1 and self.downloaded[self.showCard[i]] > 0:
                self.PShow[i].show()
                path = QPixmap(r'data/' + str(self.showCard[i]) + '.jpg')
                self.PShow[i].setPixmap(path)
            else:
                self.PHand[i].hide()
    # end ShowShowCard

    def ShowHandCard(self):
        ''' 更新手牌 '''
        for i in range(6):
            if self.handCard[i] != -1 and self.downloaded[self.handCard[i]] > 0:
                self.PHand[i].show()
                path = QPixmap(r'data/' + str(self.handCard[i]) + '.jpg')
                self.PHand[i].setPixmap(path)
            else:
                self.PHand[i].hide()
    # end ShowHandCard

    def BeginGame(self, mes):
        ''' 开始游戏，装载手牌信息并设置界面 '''
        try:
            for i in range(6):
                self.handCard[i] = mes[1 + i]
            for i in range(self.totPlayer):
                self.PLabel[self.getPosID(i)].setText(self.namePlayer[i] + '[0分]')
                self.scorePlayer[i] = 0
            self.DescLabel.setText('请等待庄家选择...')
            self.DescLabel.show()
            return 7
        except:
            print('gg BeginGame')
            return 0
    # end BeginGame

    def Download(self):
        ''' 根据下载队列进行任务选择'''
        x = -1
        while (self.Pending0 != []):
            if (self.downloaded[self.Pending0[0]] ==
               self.mission[self.Pending0[0]]):
                self.Pending0 = self.Pending0[1:]
            else:
                x = self.Pending0[0]
                break
        if (x != -1):
            self.socket.send(bytes([C_TYPE_DOWNLOAD, x, self.downloaded[x]]))
            return
        while (self.Pending1 != []):
            if (self.downloaded[self.Pending1[0]] ==
               self.mission[self.Pending1[0]]):
                self.Pending1 = self.Pending1[1:]
            else:
                x = self.Pending1[0]
                break
        if (x != -1):
            self.socket.send(bytes([C_TYPE_DOWNLOAD, x, self.downloaded[x]]))
            return
    # end Download

    def handleMission(self, mes):
        ''' 将任务接受，加入任务队列，并开始下载... '''
        # FIXME we only accept a pic that is less than 512K
        tot = mes[1]
        self.mission = [0] * tot
        for i in range(tot):
            self.mission[i] = mes[2 + i]
        self.downloaded = [0] * tot
        for i in range(tot):
            if os.path.exists('data/' + str(i) + '.jpg'):
                self.downloaded[i] = self.mission[i]
            else:
                self.Pending1.append(i)
                f = open('data/' + str(i) + '.jpg', 'w')
                f.close()
        for i in range(6):
            self.Pending0.append(self.handCard[i])
        self.ShowHandCard()
        self.Download()
        return tot + 2
    # end handleMission

    def handleDrawCard(self, mes):
        ''' 处理摸牌信息 '''
        try:
            self.handCard[self.handCard.index(-1)] = mes[1]
            self.ShowHandCard()
            return 2
        except:
            print('gg DrawCard')
            return 0
    # end handleDrawCard

    def handleDesc(self, mes):
        ''' 显示庄家的描述，开始选择手牌作为展示牌 '''
        try:
            endst = 2 + mes[1]
            self.DescLabel.setText('庄家描述：' + bytes(mes[2:endst]).decode())
            self.DescLabel.show()
            for i in range(6):
                self.BHand[i].show()
            return endst
        except:
            print('gg Desc')
            return 0
    # end handleDesc

    def handleAllPic(self, mes):
        ''' 将展示牌显示，开始选择哪张牌是庄家的 '''
        try:
            for i in range(self.totPlayer):
                self.showCard[i] = mes[1 + i]
                self.Pending0.append(mes[1 + i])
            if self.banker:
                self.DescLabel.setText('庄家描述:' + self.descEdit.text())
                self.DescLabel.show()
            self.ShowShowCard()
            if not self.banker:
                for i in range(self.totPlayer):
                    self.BShow[i].show()
            return 1 + self.totPlayer
        except:
            print('gg AllPic')
            return 0
    # end handleAllPic

    def handleAllPick(self, mes):
        ''' 显示各玩家选择信息 '''
        banker = mes[1]
        pickP = [0, 0, 0, 0]
        fromP = [0, 0, 0, 0]
        for i in range(self.totPlayer):
            pickP[i] = mes[2 + i]
            fromP[i] = mes[2 + i + self.totPlayer]
            self.LPick[i].setText('')
            self.LPick[i].show()
        pickRight = 0
        for i in range(self.totPlayer):
            idP = self.showCard.index(fromP[i])
            self.LFrom[idP].setText('from:' + self.namePlayer[i])
            self.LFrom[idP].show()
            if i != banker:
                idP = self.showCard.index(pickP[i])
                self.LPick[idP].setText(self.LPick[idP].text() + '\n' +
                                        self.namePlayer[i])
                if pickP[i] == fromP[banker]:
                    pickRight += 1

        if pickRight == self.totPlayer - 1 or pickRight == 0:
            for i in range(self.totPlayer):
                if i != banker:
                    self.scorePlayer[i] += 2
        else:
            self.scorePlayer[banker] += 3
            for i in range(self.totPlayer):
                if i != banker:
                    if pickP[i] != fromP[banker]:
                        idP = fromP.index(pickP[i])
                        self.scorePlayer[idP] += 1
                    else:
                        self.scorePlayer[i] += 1
        self.app.processEvents()
        self.banker = False
        # FIXME: 使用更好的展示效果
        time.sleep(2)
        for i in range(self.totPlayer):
            self.PLabel[self.getPosID(i)].setText(self.namePlayer[i] +
                                                  '[' +
                                                  str(self.scorePlayer[i]) +
                                                  ']')
        for i in range(self.totPlayer):
            self.PShow[i].hide()
            self.LPick[i].hide()
            self.LFrom[i].hide()
        self.DescLabel.setText('请等待庄家选择...')
        self.DescLabel.show()
        return 2 + 2 * self.totPlayer
    # end handleAllPick

    def handleEndGame(self):
        ''' 结束游戏 '''
        QMessageBox.information(self, "游戏结束！", "获胜的是" +
                                self.namePlayer[self.scorePlayer.index(
                                    max(self.scorePlayer))] + '!')
        sys.exit()
    # end handleEndGame

    def handleDownload(self, mes):
        try:
            # TODO : 接受从服务器传来的消息，更新手牌和展示牌的显示
            # do_something
            self.Download()
        except:
            print('gg Download')
            return 0

    def handleMes(self, mes):
        ''' 处理由服务器发出的信息，该函数会被线程中的run启用 '''
        self.buf += mes
        self.log.write(str(mes) + '\n')
        while self.buf != []:
            print(self.buf)
            if (self.buf[0] == S_TYPE_FULLROOM):
                QMessageBox.information(self, "错误", "房间已满！")
                self.buf = self.buf[1:]
            elif (self.buf[0] == S_TYPE_GAMEHASSTART):
                QMessageBox.information(self, "错误", "游戏已经开始！")
                self.buf = self.buf[1:]
            elif (self.buf[0] == S_TYPE_ROOMINFO):
                length = self.UpdateRoomInfo(self.buf)
                if (length == 0):
                    break
                self.buf = self.buf[length:]
            elif (self.buf[0] == S_TYPE_BEGINGAME):
                length = self.BeginGame(self.buf)
                if (length == 0):
                    break
                self.buf = self.buf[length:]
            elif (self.buf[0] == S_TYPE_MISSION):
                length = self.handleMission(self.buf)
                if (length == 0):
                    break
                self.buf = self.buf[length:]
            elif (self.buf[0] == S_TYPE_BANKER):
                self.ShowBanker()
                self.buf = self.buf[1:]
            elif (self.buf[0] == S_TYPE_DRAWCARD):
                length = self.handleDrawCard(self.buf)
                if (length == 0):
                    break
                self.buf = self.buf[length:]
            elif (self.buf[0] == S_TYPE_BANKERDESC):
                length = self.handleDesc(self.buf)
                if (length == 0):
                    break
                self.buf = self.buf[length:]
            elif (self.buf[0] == S_TYPE_ALLPIC):
                length = self.handleAllPic(self.buf)
                if (length == 0):
                    break
                self.buf = self.buf[length:]
            elif (self.buf[0] == S_TYPE_ALLPICK):
                length = self.handleAllPick(self.buf)
                if (length == 0):
                    break
                self.buf = self.buf[length:]
            elif (self.buf[0] == S_TYPE_ENDGAME):
                self.handleEndGame()
                self.buf = self.buf[1:]
            elif (self.buf[0] == S_TYPE_DOWNLOAD):
                length = self.handleDownload(self.buf)
                if (length == 0):
                    break
                self.buf = self.buf[length:]
    # end handleMes

    def ChoseShow(self, x):
        ''' 选择展示牌 '''
        self.socket.send(bytes([C_TYPE_CHOSESHOW, self.showCard[x]]))
        for i in range(4):
            self.BShow[i].hide()
    # end ChoseShow

    def ChoseHand(self, x):
        ''' 选择手牌 '''
        if self.banker:
            if len(self.descEdit.text()) == 0:
                QMessageBox.information(self, "错误", "描述不能为空！")
                return
            if len(self.descEdit.text().encode('utf-8')) > 255:
                QMessageBox.information(self,
                                        "错误", "描述长度不能超过255字节！")
                return
            self.socket.send(bytes([C_TYPE_BANKERINFO, self.handCard[x],
                                    len(self.descEdit.text().encode('utf-8'))]
                                   ) + self.descEdit.text().encode('utf-8'))
            for i in range(6):
                self.BHand[i].hide()
            self.handCard[x] = -1
            self.ShowHandCard()
            self.descEdit.hide()
            self.DescLabel.setText('请等待其他玩家选择...')
            self.DescLabel.show()
            self.socket.send(bytes([C_TYPE_DRAWCARD]))
        else:
            self.socket.send(bytes([C_TYPE_CHOSEHAND, self.handCard[x]]))
            for i in range(6):
                self.BHand[i].hide()
            self.handCard[x] = -1
            self.ShowHandCard()
            self.socket.send(bytes([C_TYPE_DRAWCARD]))
    # end ChoseHand


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main(app)
    main.show()
    sys.exit(app.exec_())
