# AWAI
Trapping the consciousness of a Vtuber into a Large Language Model

Today's victim:

![jelly](https://github.com/user-attachments/assets/05f33d80-6d31-4fff-bb23-541cd4f5bcba)

(she said I'm allowed to: [proof](https://youtube.com/shorts/Gbg7tMGapSk?si=n-5aOienEQvvmvYG))

Note: I have no idea what I am doing and have no experience working with Large Language Models. This project is meant to be a learning experience for me to learn about this area.

Note 2: Also, development is in very early stages, so this README will contain my incoherent notes and ramblings until it is more fleshed out. If you are not me how did you get here?

## Training Plan
The plan for training is to continue training a preexisting LLM on the transcripts of some streams and then later on, finetune the model using prompt response pairs taken from the transcript and live chat of other streams.

## Data Organization
For now, we are using yt-dlp to go through every vod on a channel and download the vod, automatically generated subtitles, and live chat logs. From the downloaded streams, we will split them into 3 subsections. For now, all of the training data will be text.

1. Collab/Karaoke/Games with dialogue/Reactions - Data to be ignored. The transcripts in these streams include data from sources that are not the streamer, which may interfere with training.

2. Solo gaming/activity/presentation/etx streams - The transcripts from these streams can be used for training, but since the streamer is reacting to chat as well as the game/activity/presentation/etc, we can't generate prompt/response pairs based on just the text. However, this data should still be good, so we will use the transcripts of these streams for unsupervised training.

3. Zatsus - These streams are mostly just chat and streamer talking to each other, so we should be able to generate prompt/response pairs from chat logs and stream transcripts to use for supervised fine-tuning. However, since chat is a hive mind, formatting this data will be a challenge. Some ideas I have are using other LLMs to help with merging chat into one prompt, using the fact that many times, the streamer will read a message before responding to it, or begging clipping channels for them.

4. Anything with this tag has not been downloaded properly and is missing files. Need to fix if these VODs are to be included in the dataset.

## Potential problems
1. The transcripts taken from the streams are not punctuated, are formatted weirdly, and contain the occasional typo/incorrect word. This may interfere with training and result in the model not behaving as desired. A fix for this could be to use another LLM to fix the sentences, but a problem with this approach is the inconsistency between different chats. This problem may also play together with the problem of limited prompt sizes as if the transcripts are chopped up and fed into the LLM in different pieces, the resulting transcript may include inconsistencies from different runs. Might need to learn how to manipulate prompts so the outputs are more consistent.

2. I don't even know where to begin on getting the prompt/response pairs for fine tuning, especially with the inconsistencies in the model output as stated in the previous problem. The ideas for merging chat into one prompt along side with using the fact that the streamer often reads a message before responding to it rely on getting an LLM to do it if I don't want to do it manually. Also I really don't want to beg clippers and even if I did, I don't know if I would get enough data from them.
