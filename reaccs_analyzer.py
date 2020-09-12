from os import listdir
import json
from decimal import Decimal

#path to inbox directory
inbox_dir = '/Users/audreycui01/dev/messenger_stats/inbox/'
reax_conversion = {"\u00f0\u009f\u0098\u0086": "laugh", "\u00e2\u009d\u00a4": "heart", "\u00f0\u009f\u0098\u00a2":"sad", "\u00f0\u009f\u0091\u008d": "like", "\u00f0\u009f\u0098\u00ae": "wow", "\u00f0\u009f\u0091\u008e": "dislike", "\u00f0\u009f\u0098\u00a0": "angry"}

#this method doesnt rly work yet :p
def analyze_all():
    all_dir = listdir(inbox_dir)
    print(all_dir)
    for dir in all_dir:
        print(dir)
        analyze(dir)

def analyze(dir): #get reaccs stats for convo with one person
    msg_dir = inbox_dir + dir +'/' #+'/message_1.json'
    all_msg = listdir(msg_dir)

    ppl_arr = [] #array containing dictionaries of each person's reaccs
    ppl_dict = {} #dictionary mapping ppl to indicies
    rev_ppl_dict = {} #reverse dictionary of the above

    with open(msg_dir + "message_1.json") as f:
        data = json.load(f)  # first file for getting participants
    i = 0
    for ppl in data["participants"]:
        ppl = ppl["name"]
        print(ppl)
        ppl_arr.append(
            {"heart": 0, "sad": 0, "laugh": 0, "angry": 0, "wow": 0, "like": 0, "dislike": 0, "total_reax": 0})
        ppl_dict[ppl] = i
        rev_ppl_dict[i] = ppl
        i += 1

    for msg_file in all_msg: #iterate thru all message files to count reaccs
        if msg_file.find("message") >= 0:

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


#analyze_all()

analyze("insert directory name for chat here :)")







