import os
import time

def show_message(storage_location):
    start_time = time.time()
    with open(storage_location, 'r') as file:
        encoded_message = file.read()
        decoded_message = ''.join(chr(int(binary, 2)) for binary in encoded_message.split())
        print(decoded_message)
    end_time = time.time()
    execution_time = end_time - start_time
    print("show_message execution time:", execution_time, "seconds")

def write_message(encoded_message, storage_location):
    start_time = time.time()
    with open(storage_location, 'a') as file:
        file.write(encoded_message)
    end_time = time.time()
    execution_time = end_time - start_time
    print("write_message execution time:", execution_time, "seconds")

if __name__ == "__main__":
    storage_location = "message.txt"
    message = "this is a message!"
    encoded_message = ' '.join(format(ord(char), '08b') for char in message)
    write_message(encoded_message, storage_location)
    show_message(storage_location)
