import socket
from jproperties import Properties

HOST = "127.0.0.1"
PORT = 1337
ANSWER_LIMIT = 1024
ENCODING = "utf-8"

SUCCESSFULL_RESPONSE = "OK"
PAYLOAD_DELIM = ":"
PAYLOAD_END = ":END"

def read_config():
    global HOST, PORT
    
    config = Properties()
    with open('config.env', 'rb') as config_file:
        config.load(config_file)

        HOST = config.get("SOCKET_HOST").data
        PORT = int(config.get("SOCKET_PORT").data)
        ENCODING = config.get("ENCODING").data
        
def send_message_data(email, message):
    global HOST, PORT
    
    payload = email + PAYLOAD_DELIM + message + PAYLOAD_END
    payload_bytes = payload.encode(ENCODING)
    print("Connecting to {}:{}".format(HOST, PORT))
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(payload_bytes)
            data = s.recv(ANSWER_LIMIT)
        
            return data.decode(ENCODING)
    except Exception as error:
        return error
    
def read_message_data():
    email = input("Input e-mail: ")
    message = input("Input message: ")
    
    return email, message


read_config()
while True:
    print("+-----------+")
    email, message = read_message_data()
    response = send_message_data(email, message)
    if response == SUCCESSFULL_RESPONSE:
        print("Message successfuly sent!")
        break
    else:
        print("Error: {}".format(response))
    

    