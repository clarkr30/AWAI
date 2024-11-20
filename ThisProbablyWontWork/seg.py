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
    "You literally do give off an annoying little sister vibe",
    "No, I cannot call you the word. What the heck? No, I'm not- You're a weirdo! You know that? You're a weirdo and a weeb.",
    "I know I'm an anime girl on the internet, but you're a weeb. Thank you, Jupe, for the sofa! You really do give off an annoying little sister vibe. It just happens. It just happens. If only I had a doting big brother that- Uh- That, uh, called me annoying. And- Hung out with me. I guess. Since you'd be our little sister- I'm not-",
    "I'm not calling- I ain't calling you big bro. Ew, that's disgusting. I don't want to do that anymore. I- I changed my mind. Pfft. Blah, blah, blah, blah, blah. Kind of calling the pot, Black. Yeah, I'm a hypocrite. So what? Thank you, David, for the 5!"
]

embeddings = model.encode(sentences)
print(embeddings.shape)

similarities = model.similarity(embeddings, embeddings)
# print(similarities)
for i in range(len(similarities[0])):
    print(sentences[i], str(float(similarities[0][i])))
print("\n")
for i in range(len(similarities[2])):
    print(sentences[i], str(float(similarities[2][i])))