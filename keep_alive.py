from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello.  I am alive, serving the NeonPuppyNFT community!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

#https://uptimerobot.com/dashboard?activated=1#790686269

