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
request_options = ["I", "V", "B","P"]

while True:
    request = input(
            "I : Insertion of a new row\nV : View all Rows\nP:View Popular Movies\nEnter option (B to break): ")

    if request in request_options:
        req_str = str(request)

        if request == "B":
            print('Client shutting down')
            break
        elif request == "I":
            movietitle = input("Enter Movie Title : ")
            status = input("Enter status of movie : ")
            releasedate = input("Release date : ")
            revenue=(input("Enter revenue : "))
            voteaverage=input("Enter vote average : ")
            req_str = req_str + SEPARATOR + movietitle + SEPARATOR + status + SEPARATOR + releasedate + SEPARATOR + revenue + SEPARATOR +voteaverage
        client.send(req_str.encode(FORMAT))
        print('data sent')
        print(client.recv(CHUNK).decode(FORMAT))

    else:
        print("Provide a valid request")
    print("\n")

client.close()