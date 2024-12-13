import socket
import threading

def invert_words_with_vowels(s):
    vowels = "aeiou"
    words = s.split()
    inverted_words = []
    for word in words:
        if any(vowel in word.lower() for vowel in vowels):
            inverted_words.append(word[::-1])
        else:
            inverted_words.append(word)
    return " ".join(inverted_words)

def handle_client(client_socket, client_address):
    # receive data from the client
    data = client_socket.recv(1024).decode()

    # process the data
    inverted_data = invert_words_with_vowels(data)

    print(f"Received from client: {data}")
    print(f"Sending to client: {inverted_data}")

    # send the response back to the client
    client_socket.send(inverted_data.encode())

    # close the client socket
    client_socket.close()

def server_program():
    # create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to a address and port
    server_socket.bind(("localhost", 12345))

    # listen for connections
    server_socket.listen(5)

    print("Server is listening for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established.")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    server_program()