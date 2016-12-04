# -*- coding: utf-8 -*-

from protocol import *
import socket
import select
import sys
import os
from random import shuffle

__author__ = "snlia"
__email__ = "chinsnlia@gmail.com"

PlayerList = []
ReadyList = []
NameList = []
BeginGame = False
totPlayer = 0


# Function to broadcast chat messages to all connected clients
def broadcastData(sock, message):
    ''' broadcast message to all client except sock'''
    for socketN in CONNECTION_LIST:
        if socketN != server_socket and socketN != sock:
            try:
                socketN.send(message)
            except:
                # broken socket connection may be, chat client pressed ctrl+c
                # for example
                socketN.close()
                CONNECTION_LIST.remove(socketN)
    # end broadcastData


def sendData(sock, message):
    print(list(message))
    ''' send message to sock'''
    global totPlayer
    try:
        sock.send(message)
    except:
        sock.close()
        totPlayer -= 1
        CONNECTION_LIST.remove(sock)
        Id = PlayerList.index(sock)
        PlayerList.remove(sock)
        ReadyList.pop(Id)
        NameList.pop(Id)
        broadcastRoom(None)
    # end sendData


def roomInfo(sock):
    Id = PlayerList.index(sock)
    data = [S_TYPE_ROOMINFO]
    data.append(totPlayer)
    data.append(Id)
    # name info
    for i in range(totPlayer):
        data.append(len(NameList[i]))
        data += NameList[i]
    # ready info
    for i in range(totPlayer):
        data.append(ReadyList[i] == True)
    return bytes(data)
    # end roomInfo


def broadcastRoom(sock):
    ''' broadcast room info'''
    for socketN in CONNECTION_LIST:
        if socketN != server_socket and socketN != sock:
            sendData(socketN, roomInfo(socketN))
    # end broadcastRoom


def handleName(mes, sock):
    ''' handle name info recived from client'''
    global totPlayer
    if totPlayer == 4:
        sendData(sock, bytes([S_TYPE_FULLROOM]))
        sock.close()
        CONNECTION_LIST.remove(sock)
    elif BeginGame:
        sendData(sock, bytes([S_TYPE_GAMEHASSTART]))
        sock.close()
        CONNECTION_LIST.remove(sock)
    else:
        PlayerList.append(sock)
        ReadyList.append(False)
        NameList.append(mes[2:2 + mes[1]])
        totPlayer += 1
        broadcastRoom(None)
    return 2 + mes[1]
    # end handleName


def handleReady(sock):
    global card
    Id = PlayerList.index(sock)
    ReadyList[Id] = True
    broadcastRoom(None)
    if ((False not in ReadyList) and totPlayer > 1):
        for i in range(totPlayer):
            sendData(PlayerList[i], bytes([S_TYPE_BEGINGAME] + card[:6]))
            card = card[6:]
        broadcastData(None, mission)
    # end handleReady


def handleDownload(mes, sock):
    pass


def handleDrawCard(sock):
    pass


def handleMes(mes, sock):
    ''' handle messages recieved from sock'''
    while mes != []:
        print("here!")
        if mes[0] == C_TYPE_NAME:
            mes = mes[handleName(mes, sock):]
        elif mes[0] == C_TYPE_READY:
            handleReady(sock)
            mes = mes[1:]
        elif mes[0] == C_TYPE_DOWNLOAD:
            handleDownload(mes, sock)
        elif mes[0] == C_TYPE_DRAWCARD:
            handleDrawCard(sock)
            mes = mes[1:]


if __name__ == "__main__":
    global CONNECTION_LIST, totPlayer, card

    # List to keep track of socket descriptors
    CONNECTION_LIST = []
    TOTCARD = 80
    BLOCKSIZE = 2048
    mission = [S_TYPE_MISSION, TOTCARD]
    for i in range(TOTCARD):
        mission.append(os.path.getsize('data/' + str(i) + '.jpg') // BLOCKSIZE)
    mission = bytes(mission)
    card = list(range(TOTCARD))
    shuffle(card)
    RECV_BUFFER = 4096  # Advisable to keep it as an exponent of 2
    PORT = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)

    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)

    print ("Chat server started on port " + str(PORT))

    while 1:
        # Get the list sockets which are ready to be read through select
        read_sockets, write_sockets, error_sockets = \
            select.select(CONNECTION_LIST + [sys.stdin], [], [])

        for sock in read_sockets:
            # New connection
            if sock == server_socket:
                ''' Handle the case in which there is a new connection
                recieved through server_socket '''
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print ("Client (%s, %s) connected" % addr)

            # read from input
            elif sock == sys.stdin:
                msg = sys.stdin.readline()
                broadcastData(None, msg.encode("utf-8"))
            # Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    # In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)
                    handleMes(list(data), sock)

                except:
                    print ("Client (%s, %s) is offline" % addr)
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    totPlayer -= 1
                    Id = PlayerList.index(sock)
                    PlayerList.remove(sock)
                    ReadyList.pop(Id)
                    NameList.pop(Id)
                    broadcastRoom(None)
                    continue
