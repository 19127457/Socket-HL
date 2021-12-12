import json
import socket


def GetPlacesList(client, addr):
    client.sendto(bytes('place_list', encoding='utf8'), addr)
    time.sleep(1)
    data = client.recvfrom(2048)
    data = data[0].decode('utf8').replace("\'", "\"")
    data = json.loads(data)
    place_list = []
    for i in data['data']:
        place_list.append((i['key'], i['location'], i['longitude'], i['latitude'], i['description']))
    return place_list


def GetPlaceInfo(client, addr, information):
    client.sendto(bytes('place_info,' + information, encoding='utf8'), addr)
    time.sleep(1)
    data = client.recvfrom(1024)
    data = json.loads(data[0].decode('utf8').replace("\'", "\""))
    return data


if __name__ == "__main__":

    """ Creating the UDP socket """
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    host = "127.0.0.1"
    port = 50000
    addr = (host, port)

    GetPlaceInfo(client, addr, 'Ho Chi Minh')
