import socket
import os
import threading
import pandas as pd
from csv import writer
SEPARATOR = "<SEPARATOR>"

cols =  ['companyname', 'openingsharevalue', 'closingsharevalue', 'date']
df = pd.DataFrame(columns=cols)

if (os.stat("market.csv").st_size != 0):
    df = pd.read_csv('market.csv')
print(df)
HOST = socket.gethostname()
PORT = 1234
ADDR = (HOST, PORT)
CHUNK_SIZE = 1024
FORMAT = 'utf-8'
date='2001-07-30'
# Initialise socket obj
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to address
server.bind(ADDR)


def add_row(conn_socket, companyname, openingsharevalue, closingsharevalue,date):
        openingsharevalue=int(openingsharevalue)
        closingsharevalue=int(closingsharevalue)
        newrow = [companyname,openingsharevalue,closingsharevalue,date]
        with open('market.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(newrow)
            f_object.close()
        conn_socket.send(b"Added Row Successfully")


def send_all(conn_socket):
    df=pd.read_csv('market.csv')
    conn_socket.send(df.to_string().encode(FORMAT))

def calc_diff(conn_socket):
    df['difference'] = df['closingsharevalue'] - df['openingsharevalue']
    df.to_csv("market.csv", index=False)
    conn_socket.send(b"Difference updated successfully")

# Method to serve data to client
def on_new_client(clientsocket,addr,host):
    while True:
        msg = clientsocket.recv(1024).decode()
        args = msg.split(SEPARATOR)
        print(args)
        if (args[0] == "-1"):
            break
        elif (args[0] == "0"):
            add_row(clientsocket, args[1], args[2], args[3], args[4])
        elif (args[0] == "1"):
            send_all(clientsocket)
        elif (args[0]=="2"):
            calc_diff(clientsocket)
    clientsocket.close()


def start():
    # Listen for connections
    server.listen()
    print('[SERVER] Listening on:', ADDR)

    while True:
        conn, addr = server.accept()
        print('client connected',addr)
        thread = threading.Thread(target=on_new_client,
                                  args=(conn, addr, HOST))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')

print('[SERVER] Starting...')
start()
