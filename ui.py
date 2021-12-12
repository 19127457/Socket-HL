from tkinter import *
from PIL import ImageTk, Image
from Client import GetPlacesList, GetPlaceInfo, GetImage
import Server
import socket


img = Image.open("Image/blank.png").convert("RGBA")
client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
host = "127.0.0.1"
port = 50000
addr = (host, port)

datas = None

def Func1():
    global datas
    global client
    global addr
    datas = GetPlacesList(client, addr)

    for i in datas:
        lst.insert(int(i[0]), f"{i[1]}")


def Func2(information):
    global datas
    global client
    global addr
    datas = GetPlaceInfo(client, addr, information)


def Func3(information):
    global client
    global addr
    GetImage(client, addr, information)
    
    
def selected_item():
    global img
    global label1
    item = lst.get(lst.curselection())

    Func2(item)
    #Func3(datas['key'])
    
    txt.insert(INSERT, f"Name: {datas['location']}\n")
    txt.insert(INSERT, f"Longtitude: {datas['longitude']}\n")
    txt.insert(INSERT, f"Lattitude: {datas['latitude']}\n")
    txt.insert(INSERT, f"Description: {datas['description']}\n")

    img = Image.open('Image/' + datas['key'] + '.png').convert("RGBA")
    width, height = 300, 150
    resize_image = img.resize((width, height))
    img = ImageTk.PhotoImage(resize_image)
    label1.configure(image=img)
    label1.image = img


root = Tk()
root.title("Application")
root.geometry("750x500+150+150")

"""
    widgets and other user interface components
"""
result = StringVar()

btn = Button(root, text="Load locations", padx=50, command=Func1)
btn.place(bordermode=INSIDE, width=150, x=25, y=15)

btn2 = Button(root, text="Show information", padx=50, command=selected_item)
btn2.place(bordermode=INSIDE, width=150, x=175, y=15)

lst = Listbox(root)
lst.place(bordermode=INSIDE, width=300, height=430, x=25, y=50)

width, height = 300, 150
resize_image = img.resize((width, height))

img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.place(bordermode=INSIDE, x=400, y=15)

txt = Text(root)
txt.place(bordermode=INSIDE, width=300, height=300, x=400, y=180)

 
# Execute Tkinter
root.mainloop()