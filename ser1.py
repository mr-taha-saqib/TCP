import socket

def main():
    server_ip = '127.0.0.1'
    server_port = 2000 

    # Create TCP socket
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind((server_ip, server_port))
        tcp_socket.listen(1)  # Listen for incoming connections
        print("Server is listening for connections...\n")
    except socket.error as err:
        print(f"Could not create or bind socket. Error: {err}")
        return
    client_socket, client_address = tcp_socket.accept()
    print(f"Connection established with {client_address[0]} on port {client_address[1]}")

    # Receive message from the client
    try:
        client_message = client_socket.recv(1024).decode()
        print(f"Received Message from Client: {client_message}")
    except socket.error as err:
        print(f"Receive Failed. Error: {err}")
    try:
        response_message = "Message received!"
        client_socket.send(response_message.encode())
    except socket.error as err:
        print(f"Send Failed. Error: {err}")

    # Close the client and server sockets
    client_socket.close()
    tcp_socket.close()

if __name__ == "__main__":
    main()