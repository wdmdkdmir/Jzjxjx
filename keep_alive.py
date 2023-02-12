
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# YUKARIYA : from keep_alive import keep_alive
# aşağıya: keep_alive()

# NOT = dosyanın adı keep_alive olacak
