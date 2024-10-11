# AWAI
Trapping the consciousness of a Vtuber into a Large Language Model

Note: I have no idea what I am doing and have no experience working with Large Language Models. This project is meant to be a learning experience for me to learn about this area.

## Training Plan
The plan for training is to continue training a preexisting LLM on the transcripts of some streams and then later on, finetune the model using prompt response pairs taken from the transcript and live chat of other streams.

## Data Organization
For now, we are using yt-dlp to go through every vod on a channel and download the vod, automatically generated subtitles, and live chat logs. From the downloaded streams, we will split them into 3 subsections. For now, all of the training data will be text.

1. Collab/Karaoke/Games with dialogue/Reactions - Data to be discarded. The transcripts in these streams include data that may interfere with training.

2. Solo gaming/activity/presentation/etx streams - The transcripts from these streams can be used for training, but since the streamer is reacting to chat as well as the game/activity/presentation/etc, we can't generate prompt/response pairs based on just the text. However, this data should still be good, so we will use the transcripts of these streams for unsupervised training.

3. Zatsus - These streams are mostly just chat and streamer talking to each other, so we should be able to generate prompt/response pairs from chat logs and stream transcripts to use for supervised fine-tuning. However, since chat is a hive mind, formatting this data will be a challenge. Some ideas I have are using other LLMs to help with merging chat into one prompt, using the fact that many times, the streamer will read a message before responding to it, or begging clipping channels for them.