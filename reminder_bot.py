import os
import json
import websocket
import traceback
from slacker import Slacker

token = os.environ['SLACKER_RTM_KEY'] #export SLACKER_KEY = xoxb-~~~~
slack = Slacker(token)
plan = []

def show_plan():
    return "\n".join(plan)

def getKey(msg):
    return msg.split(' ')[1]

def getKeys(msg):
    return msg.split(' ')[1:]

def echobot():
    global plan
    res = slack.rtm.connect()
    endpoint = res.body['url']
    ws = websocket.create_connection(endpoint)
    ws.settimeout(60)
    while True:
        try:
            msg = json.loads(ws.recv())
            print("================")
            print(plan)
            print(msg)
            if 'text' in msg.keys() and "client_msg_id" in msg.keys():
                text = msg['text']
                if "help" in text or "도움" in text:
                    slack.chat.post_message(msg['channel'], "사용방법: \n일정보기\n일정추가 key\n일정삭제 key\n일정초기화")
                elif "일정보기" in text:
                    slack.chat.post_message(msg['channel'], "일정들\n{0}".format(show_plan()))
                elif "일정추가" in text:
                    plan.extend(getKeys(text))
                    slack.chat.post_message(msg['channel'], "{0} 일정이 추가되었습니다.".format(getKeys(text)))
                elif "일정삭제" in text:
                    del plan[plan.index(getKey(text))]
                    slack.chat.post_message(msg['channel'], "{0} 일정이 삭제되었습니다.".format(getKey(text)))
                elif "일정초기화" in text:
                    plan = []
                    slack.chat.post_message(msg['channel'], "일정이 초기화 되었습니다.")
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