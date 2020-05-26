import os
import json
import websocket
import traceback
from slacker import Slacker

token = os.environ['SLACKER_KEY'] #export SLACKER_KEY = xoxb-~~~~
slack = Slacker(token)

def echobot():
    res = slack.rtm.connect()
    endpoint = res.body['url']
    ws = websocket.create_connection(endpoint)
    ws.settimeout(60)
    while True:
        try:
            msg = json.loads(ws.recv())
            print("================")
            print(msg)
            if 'text' in msg.keys() and "client_msg_id" in msg.keys():
                slack.chat.post_message(msg['channel'], msg['text'])
        except websocket.WebSocketTimeoutException:
            print("Detect Timeout! ping!")
            ws.send(json.dumps({'type':'ping'}))
        except websocket.WebSocketConnectionClosedException:
            print("Connection Closed!")
            break
        except Exception as e:
            print("Unexpected Error!")
            print(traceback.format_exc())
            break
    ws.close()

while True:
    echobot()