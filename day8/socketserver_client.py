import socket
import sys

HOST, PORT = "localhost", 9999


# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    while True:
        data = input(">>").strip()
        sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print("Sent:     {}".format(data))
        print("Received: {}".format(received))
finally:
    sock.close()

