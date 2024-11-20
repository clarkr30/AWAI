import json
import os
import time

# BRO ARE THESE TIMESTAMPS IN UNIX TIME
# yes it is. the first entry in every file seems to the notification that the chat replay is on and the timestamp is set to the time of download.
# I think the solution is to skip the first line and take the timestamp from the second line as the base time, then compare every other timestamp to it to get the time relative to the start of the stream.
# This implementation may result in some chat delay, but it should be fine
# we are not parsing emotes, just text chat messages
# Wait I think it would be fun to write a thing that plays the stream as well as live chat simultaneously 

# chatFile = "Streams/20240216 - EP._16_-_nearing_the_end_of_an_era/EP._16_-_nearing_the_end_of_an_era [Tz0xSdrEfTc].live_chat.json"
chatFile = "Streams/20241018 - we_just_be_doin_whatever_today_-D/we_just_be_doin_whatever_today_-D [5yrT5_Y-NfI].live_chat.json"
count = 0
firstLine = True
baseTimeSet = False
f = open("chatReplay.txt", "w")
with open(chatFile) as file:
    for line in file:
        if(firstLine):
            firstLine = False
            continue
        chat_dict = json.loads(line)
        # print(chat_dict)
        # print chat message in text
        try:
            # print(chat_dict['replayChatItemAction']['actions'][0])
            # print(str(chat_dict['replayChatItemAction']['actions'][0]['addLiveChatTickerItemAction']['item']['liveChatTickerPaidMessageItemRenderer']['showItemEndpoint']['showLiveChatItemEndpoint']['renderer']['liveChatPaidMessageRenderer']['authorName']['simpleText']) + "\n\n")
            # f.write(str(chat_dict['replayChatItemAction']['actions'][0]['addLiveChatTickerItemAction']) + "\n")
            # if("addLiveChatTickerActionItem" in chat_dict['replayChatItemAction']['actions'][0]):
            #     print("weh" + str(count))
            #     count += 1
            if(not baseTimeSet):
                baseTime = timestampUsec = int(chat_dict['replayChatItemAction']['actions'][0]['addChatItemAction']['item']['liveChatTextMessageRenderer']['timestampUsec'])
                timeOffset = chat_dict['replayChatItemAction']['actions'][0]['addChatItemAction']['item']['liveChatTextMessageRenderer']['timestampText']['simpleText'].replace('-','').split(':')
                baseTime += (int(timeOffset[0]) * 60 + int(timeOffset[1])) * 1000000
                # print(chat_dict['replayChatItemAction']['actions'][0]['addChatItemAction']['item']['liveChatTextMessageRenderer']['timestampText']['simpleText'].replace('-','').split(':'))
                print(baseTime)
                baseTimeSet = True

            msg = chat_dict['replayChatItemAction']['actions'][0]['addLiveChatTickerItemAction']['item']['liveChatTickerPaidMessageItemRenderer']['showItemEndpoint']['showLiveChatItemEndpoint']['renderer']['liveChatPaidMessageRenderer']['message']['runs'][0]['text']
            # print(msg)
            timestampUsec = int(chat_dict['replayChatItemAction']['actions'][0]['addLiveChatTickerItemAction']['item']['liveChatTickerPaidMessageItemRenderer']['showItemEndpoint']['showLiveChatItemEndpoint']['renderer']['liveChatPaidMessageRenderer']['timestampUsec'])
            author = chat_dict['replayChatItemAction']['actions'][0]['addLiveChatTickerItemAction']['item']['liveChatTickerPaidMessageItemRenderer']['showItemEndpoint']['showLiveChatItemEndpoint']['renderer']['liveChatPaidMessageRenderer']['authorName']['simpleText']
            
            

            timestamp = time.strftime("%H:%M:%S", time.gmtime((timestampUsec - baseTime) / 1000000))
            # print("weh")
            # print(timestamp + " - " + author + ": " + msg)
            f.write(timestamp + " - " + author + ": " + msg + "\n")
        except Exception as e:
            # print("error", e)
            continue
f.close()