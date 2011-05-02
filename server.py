#!/usr/bin/python
# server.py
# Copyright (C) 2011 Ershad K <ershad92@gmail.com>

import socket
import os
HOST = ''
PORT = 50008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while True:
    s.listen(1)
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data: break

    #for mtail to function correctly
    f = open('lanmessages', 'a')
    f.writelines( data + "\n")
    f.close();
    
    splitted = data.split(":")
    data = data[len(splitted[0])+1:]
    os.system('notify-send '+ splitted[0] + ' "' + data + '"')
    conn.send(data)
conn.close()
