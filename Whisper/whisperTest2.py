import whisper

model = whisper.load_model("turbo")
result = model.transcribe("/home/Clark/Documents/AWAI/Streams/20240216 - EP._16_-_nearing_the_end_of_an_era/EP._16_-_nearing_the_end_of_an_era [Tz0xSdrEfTc].f140.m4a")
print(result["text"])