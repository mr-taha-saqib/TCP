import socket
import threading

def invert_words_without_vowels(s):
    vowels = "aeiou"
    words = s.split()
    inverted_words = []
    for word in words:
        if not any(vowel in word.lower() for vowel in vowels):
            inverted_words.append(word[::-1])
        else:
            inverted_words.append(word)
    return " ".join(inverted_words)

def send_data(client_socket, message):
    # send data to the server
    client_socket.send(message.encode())

    # receive response from the server
    response = client_socket.recv(1024).decode()

    # invert words without vowels
    inverted_response = invert_words_without_vowels(response)

    print(f"Received from server: {response}")
    print(f"Inverted response: {inverted_response}")

def client_program():
    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    client_socket.connect(("localhost", 12345))

    while True:
        # get input from the user
        message = input("Enter a string (or 'quit' to exit): ")

        if message.lower() == 'quit':
            break

        # create a new thread to send data to the server
        send_thread = threading.Thread(target=send_data, args=(client_socket, message))
        send_thread.start()
        send_thread.join()
    client_socket.close()

if __name__ == "__main__":
    client_program()