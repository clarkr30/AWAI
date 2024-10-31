import os
import whisper

model = whisper.load_model("turbo")

destFile = "Whisper/AudioData/transcript/transcriptChopped.txt"
srcDir = "Whisper/AudioData/chopped"

with open(destFile, "a") as f:
    lst = os.listdir(srcDir)
    numFiles = len(lst)
    for i in range(numFiles):
        filename = "chopped_" + str(i) + ".m4a"
        if filename.endswith(".m4a"):
            print("transcribing " + filename)
            result = model.transcribe(srcDir + "/" + filename, verbose = False, initial_prompt="Awawawawa")
            f.write(result["text"])
            # print(result["text"])