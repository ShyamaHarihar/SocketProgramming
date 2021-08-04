import socket

client = socket.socket()
HOST = socket.gethostname()
PORT = 1234
ADDR = (HOST, PORT)
IP_ADDR = socket.gethostbyname(HOST)
SEPARATOR = '<SEPARATOR>'
FORMAT = 'utf-8'
CHUNK = 2048
from datetime import date
date= '20010202'
client.connect(ADDR)
request_options = [-1, 0, 1, 2]
#2 is for updating difference

while True:
    request = int(
        input(
            "0: Add new row\n1: View All\n2:Update Difference\nEnter option (-1 to break): "))

    if request in request_options:
        req_str = str(request)

        if request == -1:
            print('Client shutting down')
            break
        elif request == 0:
            companyname = input("Enter company name")
            openingsharevalue = (input("Enter opening share value: "))
            closingsharevalue = (input("Enter closing share value: "))
            #date = str(input("Enter date: (yyyy-mm-dd): "))
            req_str = req_str + SEPARATOR + companyname + SEPARATOR + openingsharevalue + SEPARATOR + closingsharevalue + SEPARATOR + date
        client.send(req_str.encode(FORMAT))
        print('data sent')
        print(client.recv(CHUNK).decode(FORMAT))

    else:
        print("Provide a valid request number")
    print("\n")

client.close()