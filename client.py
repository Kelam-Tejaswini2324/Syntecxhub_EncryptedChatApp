import socket
import threading
from encryption import encrypt_message

HOST="127.0.0.1"
PORT=5555

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

username=input("Enter Username : ")

client.send(username.encode())

print("\nConnected Successfully")
print("Type exit to quit.\n")

def receive():

    while True:

        try:
            message=client.recv(1024).decode()

            if message:
                print("\n"+message)

        except:
            break

threading.Thread(target=receive,daemon=True).start()

while True:

    message=input("You : ")

    if message.lower()=="exit":
        break

    encrypted=encrypt_message(message)

    client.send(encrypted)

client.close()