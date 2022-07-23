from flask import Flask
import colorama
from colorama import Fore
import os
import time
from threading import Thread


app = Flask('')


@app.route('/')

def home():

    return 'not nuker on top'
    

def run():

  app.run(host='0.0.0.0',port=os.getenv("HostPort"))
print(Fore.CYAN + 'Connecting Bot To Nonuker Database...')
time.sleep(0)
print(Fore.RED + 'Failed To Connect! Trying Again...')
time.sleep(0)
print(Fore.YELLOW + 'Connecting...')
time.sleep(1)
print(Fore.GREEN + 'Connected!')

def keep_alive():

    t = Thread(target=run)

    t.start()