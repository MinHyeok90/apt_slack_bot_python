import os
from slacker import Slacker

token = os.environ['SLACKER_KEY'] #export SLACKER_KEY = xoxb-~~~~
slack = Slacker(token)

slack.chat.post_message("#random", "반가워!!")