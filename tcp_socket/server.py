#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from socket import *
from time import ctime

HOST = "localhost"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(2)

while True:
    print "waiting for connection..."
    tcpCliSock, addr = tcpSerSock.accept()
    print "...connected from: ", addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print "from client:%s" % (data)
        tcpCliSock.send('[%s] %s' % (ctime(), data))
        #tcpCliSock.close()
tcpSerSock.close()
