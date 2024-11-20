import whisper
import time
# Maybe I could do like a linked list, with each node carrying the start, end, text, and probability data

class Segment:
    def __init__(self, start, end, text, prob):
        self.start = start
        self.end = end
        self.text = text
        self.prob = prob
        self.next = None

    def add(self, next):
        self.next = next
        return next
    
    def append(self, text, end):
        self.text = self.text + " " + text
        self.end = end

model = whisper.load_model("turbo")
result = model.transcribe("Streams/20241018 - we_just_be_doin_whatever_today_-D/we_just_be_doin_whatever_today_-D [5yrT5_Y-NfI].mp4", verbose=False, initial_prompt="Awawawawa", word_timestamps = True, logprob_threshold=-2.0)

# with open("Whisper/AudioData/transcript/zatsuSegmentsData.txt", "a") as f:
#     with open("Whisper/AudioData/transcript/zatsuSegments.txt", "a") as ff:
        # print(result["segments"])

firstSeg = Segment(None, None, None, None)
currSeg = firstSeg
for i in range(len(result["segments"])):
    if((not(result["segments"][i]["text"].isspace() or len(result["segments"][i]["text"]) == 0) or (result["segments"][i]["start"] - result["segments"][i]["end"] != 0)) and result["segments"][i]["avg_logprob"] > -2 and not result["segments"][i]["text"] == " Music"):
        if(result["segments"][i]["start"] == currSeg.end):
            currSeg.append(result["segments"][i]["text"], round(result["segments"][i]["end"], 2))
        else:
            nextSeg = Segment(round(result["segments"][i]["start"], 2), round(result["segments"][i]["end"], 2), result["segments"][i]["text"], result["segments"][i]["avg_logprob"])
            currSeg = currSeg.add(nextSeg)

currSeg = firstSeg
with open("Whisper/AudioData/transcript/zatsuSegmentsDataTest.txt", "a") as f:
    while not (currSeg.next == None):
        if not (currSeg.text == None):
            f.write(time.strftime("%H:%M:%S", time.gmtime((currSeg.start))) + " -> " + time.strftime("%H:%M:%S", time.gmtime((currSeg.end))) + ": " + currSeg.text + " (" + str(currSeg.prob) + ")\n")
        currSeg = currSeg.next
