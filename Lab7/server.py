import socket
import threading
import re
from jproperties import Properties
import uuid
from smtplib import SMTP

HOST = "127.0.0.1"
PORT = 1337
POCKET_LIMIT = 1024
ENCODING = "utf-8"
SOCKET_POOL = 2

SUCCESSFULL_RESPONSE = "OK"
PAYLOAD_DELIM = ":"
PAYLOAD_END = ":END"
EMAIL_REGEXP = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

EMAIL_LOGIN=None
EMAIL_PASSWORD=None
SMTP_HOST=None
SMTP_PORT=None
SUBJECT_PATTERN = 'Subject: {}\n\n{}'

def read_config():
    global HOST, PORT, ENCODING, EMAIL_LOGIN, EMAIL_PASSWORD, SMTP_HOST, SMTP_PORT
    
    config = Properties()
    with open('config.env', 'rb') as config_file:
        config.load(config_file)

        HOST = config.get("SOCKET_HOST").data
        PORT = int(config.get("SOCKET_PORT").data)
        ENCODING = config.get("ENCODING").data
        
        EMAIL_LOGIN = config.get("EMAIL_LOGIN").data
        EMAIL_PASSWORD = config.get("EMAIL_PASSWORD").data
        SMTP_HOST = config.get("SMTP_HOST").data
        SMTP_PORT = int(config.get("SMTP_PORT").data)
    
def parse_data(data):
    data_parts = data.split(sep=PAYLOAD_DELIM, maxsplit=1)
    if len(data_parts) != 2:
        raise Exception("Wrong message structure!")
        
    email = data_parts[0]
    if not re.match(EMAIL_REGEXP, email):  
        raise Exception("Wrong email!")
    message = data_parts[1].split(sep=PAYLOAD_END, maxsplit=1)[0]
    
    return email, message
    
def create_id():
    return uuid.uuid4()

def send_error(address, data):
    global SMTP_HOST, SMTP_PORT, EMAIL_LOGIN, EMAIL_PASSWORD
    
    print("[{}] Sending error report by SMTP".format(address[0]))
    if SMTP_HOST is not None and EMAIL_LOGIN is not None:
        with SMTP("{}:{}".format(SMTP_HOST, SMTP_PORT)) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_LOGIN, EMAIL_PASSWORD)
            
            admin_email_msg = SUBJECT_PATTERN.format("Aborted message", "[{}] {}".format(address[0], data))
            
            smtp.sendmail(EMAIL_LOGIN, EMAIL_LOGIN, admin_email_msg)
    
def send_message(address, email, msg):
    global SMTP_HOST, SMTP_PORT, EMAIL_LOGIN, EMAIL_PASSWORD
    
    print("[{}] Resending message by SMTP".format(address[0]))
    if SMTP_HOST is not None and EMAIL_LOGIN is not None:
        with SMTP("{}:{}".format(SMTP_HOST, SMTP_PORT)) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_LOGIN, EMAIL_PASSWORD)
            
            id = create_id()
            admin_email_msg = SUBJECT_PATTERN.format(id, "[{}] {}".format(address[0], msg))
            email_msg = SUBJECT_PATTERN.format(id, msg)
            
            smtp.sendmail(EMAIL_LOGIN, EMAIL_LOGIN, admin_email_msg)
            smtp.sendmail(EMAIL_LOGIN, email, email_msg)
    else:
        raise Exception("Wrong server SMTP configuration! Sending aborted.")

def process_request(connection, address):
    data = None
    with connection:
        data_bytes = b''
        is_data_parsed = False
        try:
            while True:
                pocket_bytes = connection.recv(POCKET_LIMIT)

                if not pocket_bytes:
                    break
                data_bytes = data_bytes + pocket_bytes
                
                data = data_bytes.decode(ENCODING)
                
                if data.endswith(PAYLOAD_END):
                    break
            
            print('Message from {}'.format(address[0]))
            email, message = parse_data(data)
            print('[{}] {}: {}'.format(address[0], email, message))
            send_message(address, email, message)
            
            connection.sendall(SUCCESSFULL_RESPONSE.encode(ENCODING))
        except Exception as e:
            print("[{}] {}".format(address[0], e))
            if data is not None:
                send_error(address, data)
            connection.sendall(str(e).encode(ENCODING))

def start_server():
    print('Starting server at {}:{}'.format(HOST, PORT))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(SOCKET_POOL)
        while True:
            conn, addr = s.accept() 
            thread = threading.Thread(target=process_request, args=(conn,addr,))
            thread.start()    
         
read_config()
start_server()