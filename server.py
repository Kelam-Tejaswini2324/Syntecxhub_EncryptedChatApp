import socket
import threading
from datetime import datetime
from encryption import decrypt_message

HOST = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print("=" * 60)
print("🔐 ENCRYPTED CHAT SERVER")
print("=" * 60)
print(f"Listening on {HOST}:{PORT}")

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                pass

def handle_client(client, address):

    username = client.recv(1024).decode()

    print(f"✅ {username} joined from {address}")

    while True:

        try:

            encrypted = client.recv(1024)

            if not encrypted:
                break

            message = decrypt_message(encrypted)

            current_time = datetime.now().strftime("%H:%M:%S")

            print(f"[{current_time}] {username}: {message}")

            with open("chat_log.txt","a") as file:
                file.write(
                    f"[{current_time}] {username}: {message}\n"
                )

            broadcast(
                f"[{current_time}] {username}: {message}".encode(),
                client
            )

        except:
            break

    clients.remove(client)
    client.close()

while True:

    client,address = server.accept()

    clients.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client,address)
    )

    thread.start()