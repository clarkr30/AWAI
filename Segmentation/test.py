import spacy
from gensim import corpora, models

nlp = spacy.load('en_core_web_sm')

with open('Whisper/AudioData/transcript/transcriptFull.txt') as f:
    text = f.read()
    sents = []
    doc = nlp(text)
    for sent in doc.sents:
        sents.append(sent)
        print(sent)
    MIN_LENGTH = 8
    tokenized_sents = [[token.lemma_.lower() for token in sent 
                        if not token.is_stop and 
                        not token.is_punct and token.text.strip() and 
                        len(token) >= MIN_LENGTH] 
                        for sent in sents]
    N_TOPICS = 5
    N_PASSES = 5
    dictionary = corpora.Dictionary(tokenized_sents)
    bow = [dictionary.doc2bow(sent) for sent in tokenized_sents]
    topic_model = models.LdaModel(corpus=bow, id2word=dictionary, 
                                num_topics=N_TOPICS, passes=N_PASSES)
    # print(topic_model.show_topics())
    THRESHOLD = 0.05
    doc_topics = list(topic_model.get_document_topics(bow, minimum_probability=THRESHOLD))