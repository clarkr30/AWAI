from pydub import AudioSegment
import math

filePath = "Whisper/AudioData/full/EP._16_-_nearing_the_end_of_an_era [Tz0xSdrEfTc].f140.m4a"
targetDir = "Whisper/AudioData/chopped"

fullAudio = AudioSegment.from_file(filePath, "m4a")

# 5 min chunks
interval = 5 * 60 * 1000

total_segs = math.ceil(fullAudio.duration_seconds/(interval / 1000))
print(total_segs)
print("starting to chop")

for i in range(total_segs):
    print("chopping" + str(i))
    beginning = i * interval
    end = (i + 1) * interval
    split_audio = fullAudio[beginning:end]
    split_audio.export(targetDir + "/chopped_" + str(i) + ".m4a", format="ipod")
