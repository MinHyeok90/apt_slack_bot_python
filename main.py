import os
import schedule
import time
from slacker import Slacker

token = os.environ['SLACKER_KEY'] #export SLACKER_KEY = xoxb-~~~~
slack = Slacker(token)

chatroom = "#random"

# def send_message(chatroom, message):
    # slack.chat.post_message(chatroom, message)
    # slack.chat.post_message(chatroom, "사랑해!")
    # slack.chat.post_message("#random", "사랑해!")

def send_message():
    slack.chat.post_message("#random", "사랑해!")

schedule.every(10).seconds.do(send_message)

while True: 
    schedule.run_pending()
    time.sleep(1)
