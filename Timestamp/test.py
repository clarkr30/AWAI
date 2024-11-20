from forcealign import ForceAlign

audioFile = "Streams/20241018 - we_just_be_doin_whatever_today_-D/we_just_be_doin_whatever_today_-D [5yrT5_Y-NfI].mp4"
transcriptFile = "Segmentation/zatsuOutput_noMarkers.txt"

# Provide path to audio_file and corresponding transcript
align = ForceAlign(audio_file=audioFile, transcript=transcriptFile)

# Runs prediction and returns alignment results
words = align.inference()

# Show predicted word-level alignments
for word in words:
	print(word.word) # The word spoken in audio at associated time
	print(word.time_start) # Time (seconds) the word starts in speech.mp3
	print(word.time_end) # Time (seconds) the word ends in speech.mp3w