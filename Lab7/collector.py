from imaplib import IMAP4_SSL
import email
import time
import datetime
from dateutil.parser import parse
from jproperties import Properties
from uuid import UUID

EMAIL_LOGIN = None
EMAIL_PASSWORD = None
IMAP_HOST = None
IMAP_PORT = None
PERIOD_CHECK = 10

PAYLOAD_LIMIT = 64

DATETIME_PATTERN = '%a, %d %b %Y %H:%M:%S %z'

last_mail_date_time = None

def read_config():
    global EMAIL_LOGIN, EMAIL_PASSWORD, IMAP_HOST, IMAP_PORT, PERIOD_CHECK
    
    config = Properties()
    with open('config.env', 'rb') as config_file:
        config.load(config_file)
        EMAIL_LOGIN = config.get("EMAIL_LOGIN").data
        EMAIL_PASSWORD = config.get("EMAIL_PASSWORD").data
        IMAP_HOST = config.get("IMAP_HOST").data
        IMAP_PORT = int(config.get("IMAP_PORT").data)
        PERIOD_CHECK = int(config.get("PERIOD_CHECK").data)

def is_valid_uuid(uuid_to_test, version=4):
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False

    return str(uuid_obj) == uuid_to_test

def write_to_file(filename, messages):
    if len(messages) > 0:
        with open(filename, "a+") as file:
            for message in messages:
                file.write(message + "\n")

read_config()
with IMAP4_SSL(IMAP_HOST, IMAP_PORT) as M:
    #global EMAIL_LOGIN, EMAIL_PASSWORD, IMAP_HOST, IMAP_PORT, PERIOD_CHECK
    
    rc, resp = M.login(EMAIL_LOGIN, EMAIL_PASSWORD)
    
    while True:
        print("Looking for a new mails...")
        total_mail_count = 0
        new_mail_count = 0
        last_mail_in_loop_date_time = None
        errors = []
        mails = []
        
        M.select()
        typ, data = M.search(None, 'ALL')
        for num in data[0].split():
            typ, data = M.fetch(num, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    total_mail_count += 1
                    
                    msg = email.message_from_string(response_part[1].decode("utf-8"))
                    date = msg['date']
                    date_time = parse(date)
                    
                    if last_mail_date_time is None or last_mail_date_time < date_time:
                        new_mail_count += 1
                        
                        if last_mail_in_loop_date_time is None or last_mail_in_loop_date_time < date_time:
                            last_mail_in_loop_date_time = date_time
                        
                        subject = msg['subject']
                        
                        payload = ""
                        if msg.is_multipart():
                            for payload_part in msg.get_payload():
                                payload += str(payload_part).strip()
                        else:
                            payload = str(msg.get_payload()).strip()
                        
                        if len(payload) > PAYLOAD_LIMIT:
                            payload = payload[:PAYLOAD_LIMIT] + "..."
                        
                        if is_valid_uuid(subject):
                            mails.append("{}: {}".format(subject, payload))
                        else:
                            errors.append(payload)
                   
        if (last_mail_in_loop_date_time is not None and 
            (last_mail_date_time is None or 
                last_mail_date_time < last_mail_in_loop_date_time)): 
            
            last_mail_date_time = last_mail_in_loop_date_time
        
        write_to_file("success_request.log", mails)
        write_to_file("error_request.log", errors)
        
        print("{} new mails found! ({} total)".format(new_mail_count, total_mail_count))            
        time.sleep(PERIOD_CHECK)