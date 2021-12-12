import json
import socket
import pyodbc
import sys
global cnxn
global cursor
import tkinter
import time
import datetime
from threading import Thread
from geopy.geocoders import Nominatim

from tkinter import *
from tkinter import scrolledtext


def ConnectSQL():
    global cnxn
    global cursor
    server = 'LAPTOP-EAK56VKK\SQLEXPRESS'
    database = 'Networking Data'
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database)
    if not cnxn: return False
    cursor = cnxn.cursor()
    return True

def insertPlace(id, nameplace, latitude, longitude, summary):
    val = (id, nameplace, latitude, longitude, summary)
    sql = "insert into ThongTinDiaDiem (id, nameplace, latitude, longitude, summary)" +  "values (?, ?, ?, ?, ?)"
    cursor.execute(sql,val)
    cnxn.commit()
    return True

def GetPlacesList():
    f = open("PlacesList.txt",'r')
    listplace = 
    return listplace

def Main_Screen():
    global scroll
    scroll = scrolledtext.ScrolledText(screen,width=50,height=20)
    scroll.grid(column=2,row=0)

    lb = Label(screen, text="", background='pink')
    lb.grid(column=0, row=1)

    lb = Label(screen, text="Message", background='pink')
    lb.grid(column=0, row=2)
    txt_linkUpdate = Entry(screen,width=40)
    txt_linkUpdate.grid(column=2, row=2)

    btn_send = Button(screen, text="Send", width=5, height=0, bg="skyblue", fg="black", command=Send)
    btn_send.grid(column=3, row=2)

    scroll.insert(INSERT,"""\
    Information
    """)
    scroll.insert(INSERT,'Information')

if __name__ == "__main__":

    """ Creating the UDP socket """
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = "127.0.0.1"
    port = 50000
    addr = (host,port)
    file_name="concac" #sys.argv[2]

    """ Bind the host address with the port """
    server.bind((host, port))

    request = server.recvfrom(1024)
    while request:
        request = request.decode("utf-8")
        if  request == "place_list":
            data = GetPlacesList()
        elif request == "place_info":
            pass
        elif request == "place_image":
            pass
        else:
            pass



    server.sendto(bytes(file_name, encoding='utf8'),addr)
    # server.sendto(data,addr)
    while (data):
        if server.sendto(data,addr):
            print ("sending ...")
            data = f.read(1024)
    server.close()
    f.close()
    #while True:
    #    data, addr = server.recvfrom(1024)
    #    #data = data.decode("utf-8")
    #    print(data)

    #    if data == "EXIT":
    #        print("Client disconnected.")
    #        break

    #    print(f"Client: {data}")

    #    data = data.upper()
    #    data = data.encode("utf-8")
    #    server.sendto(data, addr)