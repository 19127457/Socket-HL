import json
import socket
import codecs
import os
import time


def GetPlacesList():
    f = codecs.open('Socket-data.json', 'r', 'utf-8-sig')
    place_list = json.load(f)
    return place_list


def GetPlaceInfo(information):
    place_list = GetPlacesList()
    for i in place_list['data']:
        if i['key'] == information or i['location'] == information or i['longitude'] == information \
                or i['latitude'] == information or i['description'] == information:
            return i
    return None


def GetImage(information, server, client_addr):
    place_list = GetPlacesList()
    for i in place_list['data']:
        if i['key'] == information or i['location'] == information or i['longitude'] == information \
                or i['latitude'] == information or i['description'] == information:
            filename = i['key'] + '.png'
            server.sendto(bytes(str(filename), encoding='utf8'), client_addr)
            message = server.recvfrom(1024)
            f = open('Image/' + filename, "rb")
            data = f.read(1024)
            while data:
                if server.sendto(data, client_addr):
                    data = f.read(1024)
                    time.sleep(0.5)


if __name__ == "__main__":

    """ Creating the UDP socket """
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 50000

    """ Bind the host address with the port """
    server.bind(('', port))

    while True:
        request, client_addr = server.recvfrom(1024)
        request = request.decode("utf-8")
        if "place_list" in request:
            data = GetPlacesList()
            server.sendto(bytes(str(data), encoding='utf8'), client_addr)
        elif "place_info" in request:
            info = request.split(',')[1]
            data = GetPlaceInfo(info)
            server.sendto(bytes(str(data), encoding='utf8'), client_addr)
        elif "place_image" in request:
            info = request.split(',')[1]
            GetImage(info, server, client_addr)
        else:
            pass

    server.close()