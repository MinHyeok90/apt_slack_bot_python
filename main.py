import os
import schedule
import time
import json
from slacker import Slacker

token = os.environ['SLACKER_KEY'] #export SLACKER_KEY = xoxb-~~~~
slack = Slacker(token)

parseurl = "https://new.land.naver.com/api/articles/complex/1782?realEstateType=APT%3AABYG%3AJGC&tradeType=B2&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page=1&complexNo=1782&buildingNos=&areaNos=&type=list&order=rank"
chatroom = "#random"
prev_count = 0
attachments_dict = dict()
attachments_dict['pretext'] = "attachments 블록 전에 나타나는 text"
attachments_dict['title'] = "다른 텍스트 보다 크고 볼드되어서 보이는 title"
attachments_dict['title_link'] = "https://corikachu.github.io"
attachments_dict['fallback'] = "클라이언트에서 노티피케이션에 보이는 텍스트 입니다. attachment 블록에는 나타나지 않습니다"
attachments_dict['text'] = "본문 텍스트! 5줄이 넘어가면 *show more*로 보이게 됩니다."
attachments_dict['mrkdwn_in'] = ["text", "pretext"]  # 마크다운을 적용시킬 인자들을 선택합니다.
attachments = [attachments_dict]


def send_message(chatroom = "#random", message = "휴먼.. 메세지가 누락된 것 같습니다만..?"):
    slack.chat.post_message(channel=chatroom, text=message)

def notify(chatroom = "#random", message = "휴먼.. 메세지가 누락된 것 같습니다만..?", attachments = attachments):
    slack.chat.post_message(channel="#random", text=None, attachments=attachments)

def parsing():
    pass



send_message()
notify()
# schedule.every(10).seconds.do(send_message)

# while True: 
    # schedule.run_pending()
    # time.sleep(1)
