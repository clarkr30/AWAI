from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-mpnet-base-v2')

chatMsg = ["hii Jelly it was my birthday 3 ago can you sing me a happy birthday"]

# sentences = [
#     "hii Jelly it was my birthday 3 ago can you sing me a happy birthday",
#     "Thank you, Gilday, for the member. Welcome. Please enjoy your stay.",
#     "Is Jorb going to be for sale?",
#     "Dude, I don't even know what the Jorb could be. Like a marble?",
#     "How many people even buy this marble?",
#     "4-Head in 4-D?",
#     "Real?",
#     "I've got a good idea.",
#     "Thank you, David, if I get 5!",
#     "Hi, Jelly, it was my birthday 3 days ago.",
#     "Happy birthday to you!",
#     "Happy birthday to you!",
#     "Happy birthday to you, David!",
#     "Happy birthday to you!",
#     "Like a snow globe Jorb?  Are we really going to Zatsu about merch ideas?",
#     "Because that would be crazy.",
#     "Thank you, Levi, I'm gonna save a month.",
#     "I could play Katawa Shoujo. I don't feel like it.",
#     "I feel like...  I feel like...",
#     "A multitude of games.",
#     "And...  And...  None of them are Katawa Shoujo.",
#     "Thank you, Kusa!",
#     "Is feeling sick after eating rat meat normal?"
# ]

sentences = [
    "Congrats on the pregnancy. pls stop smoking and drinking",
    "Was absolutely",
    "Crazy  Okay  I'm not spoiling it  I'm just saying  Dude he's done like  So many 360's  Okay  You won't even know which one it is  Okay  It's crazy  It's also crazy",
    "It's actually Kino  It's so good man  I watched it all in one sitting by the way  Unlike the first one  Where I watched it in multiple sittings",
    "It's not at Doylers",
    "Have you decided on names?",
    "On what names?",
    "Congrats on the pregnancy  Please stop smoking and drinking  I'm not pregnant",
    "I still don't get the Parkour Civilization meme  It's just a really good show  It's just a good show",
    "And I have to watch it to keep up with the zoomers  Do you have menopause?",
    "No!",
    "Congratulations on the twins jelly  I'm sure you and Lumi will be great parents  Two women can't get pregnant",
    "Parkour Civilization part 2 stream on your 8 head"
]

embeddings = model.encode(sentences)
print(embeddings.shape)

similarities = model.similarity(embeddings, embeddings)
# print(similarities)
for i in range(len(similarities[0])):
    print(sentences[i], str(float(similarities[0][i])))
