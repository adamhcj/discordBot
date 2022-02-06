from flask import Flask
from threading import Thread
import asyncio

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

async def background_task():
  print("hello, background task here")
  await asyncio.sleep(600) #sleep for 10 mins


keep_alive()

while True:
  background_task()