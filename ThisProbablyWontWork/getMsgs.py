from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-mpnet-base-v2')

def getTimeSec(timestamp):
    time = timestamp.split(':')
    timesec = (int(time[0]) * 60 + int(time[1])) * 60 + int(time[2])
    return timesec

def parseLine(msg):
    splitmsg = msg.split(' - ')
    timestamp = splitmsg[0].split(': ')
    splitmsg[1] = splitmsg[1].split(': ')[1]
    timesec = getTimeSec(splitmsg[0])
    return splitmsg

def returnLines(time, arr):
    with open("TranscriptChatExample/zatsuSegmentsDataTest.txt", "r") as f:
        for line in f:
            sentence = line
            delimiters = [' -> ', ':  ', ' (']
            for delimiter in delimiters:
                sentence = "|".join(sentence.split(delimiter))
            splitSent = sentence.split('|')
            lineTime = getTimeSec(splitSent[0])
            if(lineTime <= time + 60 and lineTime > time - 5):
                arr.append(splitSent[2])
            elif(lineTime > time + 60):
                break
    
with open("TranscriptChatExample/chatReplay.txt", "r") as chatFile:
    gumble = []
    for line in chatFile:
        grungle = []
        parsedLine = parseLine(line)
        grungle.append(parsedLine[1])
        baseTime = getTimeSec(parsedLine[0])
        returnLines(baseTime, grungle)
        gumble.append(grungle)

# with open("TranscriptChatExample/gweh.txt", "a") as f:
#     for i in range(len(gumble)):
#         f.write(str(gumble[i]) + "\n")
# with open("TranscriptChatExample/gweh.txt", "a") as f:
#     weh = []
#     for i in range(len(gumble)):
#         wah = []
#         embeddings = model.encode(gumble[i])
#         similarity = model.similarity(embeddings, embeddings)
#         for j in range(len(similarity[0])):
#             if float(similarity[0][j]) > 0.4:
#                 # print(similarity[0][j])
#                 wah.append(gumble[i][j] + str(similarity[0][j]))
#         if(len(wah) > 1):
#             weh.append(wah)
#     for i in range(len(weh)):
#         f.write(str(weh[i]) + "\n")

with open("TranscriptChatExample/gweg.txt", "a") as f:
    for i in range(len(gumble)):
        for j in range(len(gumble[i])):
            f.write(str(gumble[i][j]) + " ")
        f.write("\n\n")