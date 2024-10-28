# This one only does like the first 30 seconds
import whisper

model = whisper.load_model("turbo")

# audio = whisper.load_audio("/home/Clark/Documents/AWAI/Streams/20240216 - EP._16_-_nearing_the_end_of_an_era/EP._16_-_nearing_the_end_of_an_era [Tz0xSdrEfTc].f140.m4a")
audio = whisper.load_audio("Whisper/AudioData/chopped/chopped_1.m4a")
audio = whisper.pad_or_trim(audio)

mel = whisper.log_mel_spectrogram(audio=audio, n_mels=128).to(model.device)

_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

print(result.text)