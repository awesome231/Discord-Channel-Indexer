import requests
import time

PathToFile = r"/log.txt" # ENTER PATH TO THE FILE YOU WANT, IF FILE DOES NOT EXIST, IT WILL CREATE THE FILE

token = '' # ENTER DISCORD TOKEN, DO NOT SHARE EVER

channel_id = '' # ENTER CHANNEL ID

timeperrequest = 3 # CHANGE TIME PER MESSAGE GRAB 


headers = {
    'authorization': token,
    'ascending': 'True'
}

firstrequest = 0
firstmessage = 0

msg = {}
name = {}
attachments = {}
link = {}
realname = {}
messagecount = 0

messageid = 0

old = 0
end = 0
blah = 0

while True:
    if firstrequest == 0:
        msgs = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=100', headers=headers)
        firstrequest = 1
    else:
        msgs = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?before={messageid}&limit=100', headers=headers)
    msgs = msgs.json()

    messageamount = len(msgs)

    a = messageamount
    b = 0
    
    currentmessage = 0
    if firstrequest == 0:
        while a > b and messageamount > 0:
            b += 1
            if currentmessage < messageamount:
                msg[currentmessage] = msgs[currentmessage].get('content')
                name[currentmessage] = msgs[currentmessage].get('author', {}).get('global_name')
                realname[currentmessage] = msgs[currentmessage].get('author', {}).get('username')
                attachments[currentmessage] = msgs[currentmessage].get('attachments')
                if attachments[currentmessage]:
                    if name[currentmessage]:  
                        link[currentmessage] = attachments[currentmessage][0].get('url')
                        with open(f"{PathToFile}", "a", encoding="utf-8") as f:
                            f.write(f"\n{name[currentmessage]}: {msg[currentmessage]} \n{link[currentmessage]}")
                            messagecount += 1
                    else:
                        link[currentmessage] = attachments[currentmessage][0].get('url')
                        with open(f"{PathToFile}", "a", encoding="utf-8") as f:
                            f.write(f"\n{realname[currentmessage]}: {msg[currentmessage]} \n{link[currentmessage]}")
                            messagecount += 1
                else:
                    if name[currentmessage]:         
                        with open(f"{PathToFile}", "a", encoding="utf-8") as f:
                            f.write(f"\n{name[currentmessage]}: {msg[currentmessage]}")
                            messagecount += 1
                    else:
                        with open(f"{PathToFile}", "a", encoding="utf-8") as f:
                            f.write(f"\n{realname[currentmessage]}: {msg[currentmessage]}")
                            messagecount += 1
            currentmessage += 1
            firstrequest = 1
            msg = {}
            name = {}
            attachments = {}
            link = {}
            realname = {}
        if firstmessage == 0:
            messageid = msgs[-1].get('id')
            firstmessage = 1
            
    elif firstrequest == 1:
        while a > b and messageamount > 0:
            firstmessage = 0
            blah = 0
            b += 1
            if currentmessage < messageamount:
                msg[currentmessage] = msgs[currentmessage].get('content')
                name[currentmessage] = msgs[currentmessage].get('author', {}).get('global_name')
                realname[currentmessage] = msgs[currentmessage].get('author', {}).get('username')
                attachments[currentmessage] = msgs[currentmessage].get('attachments')
                if attachments[currentmessage]:
                    if name[currentmessage]:
                        link[currentmessage] = attachments[currentmessage][0].get('url')
                        with open(f"{PathToFile}", "a", encoding="utf-8") as f:
                            f.write(f"\n{name[currentmessage]}: {msg[currentmessage]} \n{link[currentmessage]}")
                            messagecount += 1
                    else:
                        link[currentmessage] = attachments[currentmessage][0].get('url')
                        with open(f"{PathToFile}", "a", encoding="utf-8") as f:
                            f.write(f"\n{realname[currentmessage]}: {msg[currentmessage]} \n{link[currentmessage]}")
                            messagecount += 1
                else:
                    if name[currentmessage]:
                        with open(f"{PathToFile}", "a", encoding="utf-8") as f:
                            f.write(f"\n{name[currentmessage]}: {msg[currentmessage]}")
                            messagecount += 1
                    else:
                        with open(f"{PathToFile}", "a", encoding="utf-8") as f:
                            f.write(f"\n{realname[currentmessage]}: {msg[currentmessage]}")
                            messagecount += 1
                currentmessage += 1
        if firstmessage == 0:
            print(f"messages counted so far: {messagecount}")
            messageid = msgs[-1].get('id')
            msgs = {}
            time.sleep(timeperrequest)
            firstmessage = 1
        else:
            print("FINISHED!!")
            print(f"TOTAL MESSAGECOUNT = {messagecount}")
            print(f"FIND LOGS AT {PathToFile}")
            input("Script has stopped! press enter to quit")
            exit()
