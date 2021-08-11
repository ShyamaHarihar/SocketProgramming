import socket

client = socket.socket()
HOST = socket.gethostname()
PORT = 1234
ADDR = (HOST, PORT)
IP_ADDR = socket.gethostbyname(HOST)
SEPARATOR = '<SEPARATOR>'
FORMAT = 'utf-8'
CHUNK = 2048
date= '2001.02.02'
client.connect(ADDR)
request_options = ["I", "U", "V", "B", "M"]
#2 is for updating difference

while True:
    request = input(
            "I : Insertion of a new row\nV : View all Rows\nU :Update (Difference)\nM :Modification of Opening Stock Value\nEnter option (B to break): ")

    if request in request_options:
        req_str = str(request)

        if request == "B":
            print('Client shutting down')
            break
        elif request == "I":
            companyname = input("Enter company name")
            openingsharevalue = (input("Enter opening share value: "))
            closingsharevalue = (input("Enter closing share value: "))
            date=input("Enter date")
            req_str = req_str + SEPARATOR + companyname + SEPARATOR + openingsharevalue + SEPARATOR + closingsharevalue + SEPARATOR + date
        client.send(req_str.encode(FORMAT))
        print('data sent')
        print(client.recv(CHUNK).decode(FORMAT))

    else:
        print("Provide a valid request number")
    print("\n")

client.close()