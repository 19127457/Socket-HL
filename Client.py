import json
import socket
import tkinter
import sys
import select

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from geopy.geocoders import Nominatim

def Main_Screen():

    global tab_control
    global btn_back

    tab_control = ttk.Notebook(screen)

    ListID = ReceiveListID()
    count = int(0)
    for i in ListM:
        # Hiển thị danh sách
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text =  " (" + i[4] + ") " + i[1] + " " + i[3] + " " + i[2] + " " + i[5] )
        # Hiển thị thông tin
        Info = ReceivePlaceInfo(i[0])
        countI = int(0)
        for k in Info:
            lb1 = Label(tab, text = k[2] + ": " + k[1])
            lb1.grid(column = 0, row = countI, padx= 10, pady = 10)
            countI=countI+1
        print(Dnow + " Server: " + s.recv(1024).decode("utf8"))
        count=count+1
        tab_control.pack(expand = 1, fill = "both")


    btn_back = Button(screen, text="Back", width=5, height=0, bg="skyblue", fg="black", command=back)
    btn_back.pack()

def Search_Screen():
    global lb_noteID
    global lb_search
    global txt_search
    global btn_search
    global btn_list

    lb_search = Label(screen, text="SEARCH BELOW", background='pink')
    lb_search.pack()

    txt_search = Entry(screen,width=70)
    txt_search.pack()
    txt_search.get()

    btn_search = Button(screen, text="Search", width=15, height=0, bg="skyblue", fg="black", command=search)
    btn_search.pack()

    btn_list = Button(screen, text="List all", width=15, height=0, bg="skyblue", fg="black", command=listall)
    btn_list.pack()

    lb_noteID = Label(screen, text="Note: Search ID to see a place", background='pink')
    lb_noteID.pack()

def listall(): #cho xem tất cả danh sách
    lb_search.destroy()
    txt_search.destroy()
    btn_search.destroy()
    btn_list.destroy()
    lb_note.destroy()
    #copy main screen qua và bỏ hàm main screen
    Main_Screen()

def ReceiveListPlace ():
    server = s
    server.sendall(bytes("list all", "utf8"))
    number = server.recv(1024).decode("utf8")
    print(Dnow + " Server: " + number)
    server.sendall(bytes("RECEIVED", "utf8"))
    number = int(server.recv(1024).decode("utf8"))
    print(Dnow + " Server: " + str(number))
    server.sendall(bytes("RECEIVED", "utf8"))
    listID = []
    if (number == "0"): return
    for i in range (int(0), int(number)):

        MaDiaDiem = server.recv(1024).decode("utf8")
        print(Dnow + " Server: " + MaDiaDiem)
        server.sendall(bytes("RECEIVED", "utf8"))
        nameplace = server.recv(1024).decode("utf8")
        print(Dnow + " Server: " + nameplace)
        server.sendall(bytes("RECEIVED", "utf8"))
        latitude = server.recv(1024).decode("utf8")
        print(Dnow + " Server: " + latitude)
        server.sendall(bytes("RECEIVED", "utf8"))
        longtitude = server.recv(1024).decode("utf8")
        print(Dnow + " Server: " + longtitude)
        server.sendall(bytes("RECEIVED", "utf8"))
        summary = server.recv(1024).decode("utf8")
        print(Dnow + " Server: " + summary)
        server.sendall(bytes("RECEIVED", "utf8"))

        place = (MaDiaDiem,nameplace,latitude,longtitude,summary)
        if (len(listM) > 0):
            if not (place == listM[len(listM)-1]):
                listM.append(place) # add place into list
        else: listM.append(place) # add place into list
    print(Dnow + " Server: " + server.recv(1024).decode("utf8"))
    return listM

def ReceivePlaceInfo(id):
    s.sendall(bytes("Info", "utf8"))
    msg = s.recv(1024).decode("utf8")
    s.sendall(bytes(id, "utf8"))
    n = s.recv(1024).decode("utf8")
    s.sendall(bytes("RECEIVED","utf8"))
    number = int(n)
    listInfo = []
    Info = ()
    for i in range(0,number):
        id = s.recv(1024).decode("utf8")
        s.sendall(bytes("RECEIVED","utf8"))
        nameplace = s.recv(1024).decode("utf8")
        s.sendall(bytes("RECEIVED","utf8"))
        latitude = s.recv(1024).decode("utf8")
        s.sendall(bytes("RECEIVED","utf8"))
        longtitude = s.recv(1024).decode("utf8")
        s.sendall(bytes("RECEIVED","utf8"))
        summary = s.recv(1024).decode("utf8")
        s.sendall(bytes("RECEIVED","utf8"))
        Info = (id, nameplace, latitude, longtitude, summary)
        listInfo.append(Info)
    return listInfo


# các lệnh trong button:
def back():
    tab_control.destroy()
    btn_back.destroy()
    Search_Screen()
def search(): # tim 1 dia diem
    lb_search.destroy()
    btn_search.destroy()
    btn_list.destroy()

if __name__ == "__main__":

    """ Creating the UDP socket """
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    host = "127.0.0.1"
    port = 50000
    client.bind((host,port))
    addr = (host, port)

    f = open("NetworkingData.txt",'wb')

    data = client.recvfrom(1024)
    print(data)
    try:
        while(data):
            f.write(data[0])
            client.settimeout(2)
            data = client.recvfrom(1024)
    except TimeoutError:
        f.close()
        client.close()
        print("File Downloaded")

    #while True:
    #    f = open('NetworkingData.txt', 'r', encoding='UTF-8')

    #    if f == "EXIT":
    #        with open('NetworkingData.txt') as json_file:
    #            data = json.load(json_file)
    #            for p in data['people']:
    #                print('Name: ' + p['name'])
    #                print('Website: ' + p['website'])
    #                print('From: ' + p['from'])
    #                print('')
    #        #f = data.encode("utf-8")
    #        client.sendto(f, addr)

    #        print("Disconnected from the server.")
    #        break

        #f = f.encode("utf-8")
        #client.sendto(f, addr)

        #f, addr = client.recvfrom(1024)
        #f = f.decode("utf-8")
        #print(f"Server: {data}")
