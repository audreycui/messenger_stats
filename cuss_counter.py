#count number of times ppl cuss (fuck, shit, bitch, and its variations)
#work in progress :))

from os import listdir
import json

inbox_dir = '/Users/audreycui01/dev/messenger_stats/inbox/'
def analyze(dir): #get cuss stats for convo with one person
    msg_dir = inbox_dir + dir +'/' #+'/message_1.json'
    all_msg = listdir(msg_dir)

    ppl_arr = [] #array containing dictionaries of each person's cuss counts
    ppl_dict = {} #dictionary mapping ppl to indicies
    rev_ppl_dict = {} #reverse dictionary of the above

    with open(msg_dir + "message_1.json") as f:
        data = json.load(f)  # first file for getting participants
    i = 0
    for ppl in data["participants"]:
        ppl = ppl["name"]
        print(ppl)
        ppl_arr.append(
            {"fuck": 0, "shit":0, "bitch": 0, "total cuss": 0, "total messages": 0})
        ppl_dict[ppl] = i
        rev_ppl_dict[i] = ppl
        i += 1

    for msg_file in all_msg: #iterate thru all message files to count reaccs
        if msg_file.find("message") >= 0:

            messages = data["messages"]
            for msg in messages:
                #actor = msg["reactions"][0]["actor"]
                try:
                    sender = (msg["sender_name"])
                    actor_index = ppl_dict[sender]
                    message = msg["content"].lower()
                    ppl_arr[actor_index]["total messages"] += 1
                    fuck = message.count("fuck")
                    shit = message.count("shit")
                    bitch = message.count("bitch")
                    ppl_arr[actor_index]["fuck"] += fuck
                    ppl_arr[actor_index]["shit"] += shit
                    ppl_arr[actor_index]["bitch"] += bitch
                    ppl_arr[actor_index]["total cuss"] += (fuck + shit + bitch)

                except KeyError:
                    x=0 #do nothing lol

    i = 0
    # raw numbers
    for a in ppl_arr:
        print(rev_ppl_dict[i])
        print(a)
        i += 1

    i = 0
    # frequency of cuss words per message
    for a in ppl_arr:
        print(rev_ppl_dict[i])
        freq_dict = {}
        try:
            for word in a:
                n = a[word] / a["total messages"]
                freq_dict[word] = round(n, 3)
        except ZeroDivisionError:
            x = 0  # do nothing lol
        print(freq_dict)
        i += 1

analyze("insert directory name for chat here :)")
