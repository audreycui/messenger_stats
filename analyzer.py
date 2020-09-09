from os import listdir
import json
from decimal import Decimal

#path to inbox directory
inbox_dir = '/Users/audreycui01/dev/messenger_stats/inbox/'
reax_conversion = {"\u00f0\u009f\u0098\u0086": "laugh", "\u00e2\u009d\u00a4": "heart", "\u00f0\u009f\u0098\u00a2":"sad", "\u00f0\u009f\u0091\u008d": "like", "\u00f0\u009f\u0098\u00ae": "wow", "\u00f0\u009f\u0091\u008e": "dislike", "\u00f0\u009f\u0098\u00a0": "angry"}
def analyze_all():
    all_dir = listdir(inbox_dir)
    for dir in all_dir:
        print(dir)
        analyze(dir)

def analyze(dir):
    #start with one file
    msg_dir = '/Users/audreycui01/dev/messenger_stats/inbox/'+dir +'/message_1.json'
    reax_count = {"heart": 0, "sad": 0, "laugh": 0, "angry": 0, "wow":0, "like": 0, "dislike": 0}
    with open(msg_dir) as f:
        data = json.load(f)
    ppl_arr = []
    ppl_dict = {}
    rev_ppl_dict = {}
    i =0
    for ppl in data["participants"]:
        ppl = ppl["name"]
        print(ppl)
        ppl_arr.append({"heart": 0, "sad": 0, "laugh": 0, "angry": 0, "wow":0, "like": 0, "dislike": 0, "total_reax":0})
        ppl_dict[ppl] = i
        rev_ppl_dict[i] = ppl
        i+=1
    messages = data["messages"]
    for msg in messages:
        #actor = msg["reactions"][0]["actor"]
        try:
            actor = (msg["reactions"][0])["actor"]
            actor_index = ppl_dict[actor]
            reax = msg["reactions"][0]["reaction"]
            reax = reax_conversion[reax]
            ppl_arr[actor_index][reax] += 1
            ppl_arr[actor_index]["total_reax"] += 1
        except KeyError:
            x=0 #do nothing lol

    i=0

    #raw numbers
    for a in ppl_arr:
        print(rev_ppl_dict[i])
        print(a)
        i+=1

    i=0
    #frequency
    for a in ppl_arr:
        print(rev_ppl_dict[i])
        freq_dict={}
        try:
            for reax in a:
                n = a[reax]/a["total_reax"]
                freq_dict[reax] = round(n, 3)
        except ZeroDivisionError:
            x=0 #do nothing lol
        print (freq_dict)
        i+=1












