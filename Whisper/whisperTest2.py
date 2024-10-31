import whisper

model = whisper.load_model("turbo")
# result = model.transcribe("/home/Clark/Documents/AWAI/Streams/20240216 - EP._16_-_nearing_the_end_of_an_era/EP._16_-_nearing_the_end_of_an_era [Tz0xSdrEfTc].f140.m4a")
# result = model.transcribe("Streams/20241018 - we_just_be_doin_whatever_today_-D/we_just_be_doin_whatever_today_-D [5yrT5_Y-NfI].mp4", verbose=False, initial_prompt="Awawawawa", hallucination_silence_threshold=5)
result = model.transcribe("Streams/20241018 - we_just_be_doin_whatever_today_-D/we_just_be_doin_whatever_today_-D [5yrT5_Y-NfI].mp4", verbose=False, initial_prompt="Awawawawa")
# result = model.transcribe("Whisper/AudioData/chopped/chopped_1.m4a", verbose=False, initial_prompt="Awawawawa", word_timestamps=True)
# result = model.transcribe("Streams/20240216 - EP._16_-_nearing_the_end_of_an_era/EP._16_-_nearing_the_end_of_an_era [Tz0xSdrEfTc].temp.mp4", verbose=False, initial_prompt="Awawawawa")
# print(result["text"])
# print(result["segments"])
with open("Whisper/AudioData/transcript/zatsuTranscript.txt", "a") as f:
    f.write(result["text"])