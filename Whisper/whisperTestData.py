import whisper

model = whisper.load_model("turbo")
result = model.transcribe("Streams/20241018 - we_just_be_doin_whatever_today_-D/we_just_be_doin_whatever_today_-D [5yrT5_Y-NfI].mp4", verbose=False, initial_prompt="Awawawawa", word_timestamps = True, logprob_threshold=-2.0)

with open("Whisper/AudioData/transcript/zatsuSegmentsData.txt", "a") as f:
    with open("Whisper/AudioData/transcript/zatsuSegments.txt", "a") as ff:
        print(result["segments"])
        for i in range(len(result["segments"])):
            if((not(result["segments"][i]["text"].isspace() or len(result["segments"][i]["text"]) == 0) or (result["segments"][i]["start"] - result["segments"][i]["end"] != 0)) and result["segments"][i]["avg_logprob"] > -2 and not result["segments"][i]["text"] == " Music"):
                f.write(str(result["segments"][i]["start"]) + " -> " + str(result["segments"][i]["end"]) + ": [" + result["segments"][i]["text"] + "] (" + str(result["segments"][i]["avg_logprob"]) + ")" + "\n")
                ff.write(result["segments"][i]["text"] + "\n")
