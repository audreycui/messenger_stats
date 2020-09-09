import numpy
from os import listdir
import json

#path to inbox directory
inbox_dir = '/Users/audreycui01/dev/messenger_analyzer/inbox'

def analyze_all():
    all_dir = listdir(inbox_dir)

#start with one file
msg_dir = '/Users/audreycui01/dev/messenger_analyzer/inbox/AliceCheng_cPQtsVNCRQ/message_1.json'
with open(msg_dir) as f:
    data = json.load(f)
ppl_dict = {}
for ppl in data["participants"]:
    ppl_dict[ppl] = {}
messages = data["messages"]
for msg in messages:
    reax = msg["reactions"]






