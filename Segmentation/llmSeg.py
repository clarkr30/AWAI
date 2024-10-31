import spacy
from sentence_transformers import SentenceTransformer
from itertools import islice
from utils import window, get_depths, get_local_maxima, get_threshold_segments, compute_threshold
from sklearn.metrics.pairwise import cosine_similarity

MODEL_STR = "sentence-transformers/all-MiniLM-L6-v2"
model = SentenceTransformer(MODEL_STR)

nlp = spacy.load('en_core_web_sm')

with open('Whisper/AudioData/transcript/zatsuTranscript.txt') as f:
    text = f.read()
    sents = []
    doc = nlp(text)
    i = 0
    for sent in doc.sents:
        sents.append(sent)
        # print(sent)
        # print(i)
    
WINDOW_SIZE = 3
window_sent = list(window(sents, WINDOW_SIZE))
window_sent = [' '.join([sent.text for sent in window]) for window in window_sent]

encoded_sent = model.encode(window_sent)
coherence_scores = [cosine_similarity([pair[0]], [pair[1]])[0][0] for pair in zip(encoded_sent, encoded_sent[1:])]

depth_scores = get_depths(coherence_scores)
filtered_scores = get_local_maxima(depth_scores, order=1)

threshold = compute_threshold(filtered_scores)
segments_ids = get_threshold_segments(filtered_scores, threshold)
# print(threshold)
# print(segments_ids)

with open("Segmentation/zatsuOutput.txt", "w") as f:
    segIndex = 0
    for i in range(len(sents)):
        if i == segments_ids[segIndex]:
            f.write("\n<NEW_TOPIC>\n")
            if(segIndex < len(segments_ids) - 1):
                segIndex += 1
                # print(segIndex)
        f.write(str(sents[i]) + " ")