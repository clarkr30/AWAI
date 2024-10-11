# This program takes a long time and is slow. Bash is faster so maybe use that instead?
# The results are really inconsistent and some of them are really bad. Maybe ditch this and come back to it later if necessary?
import ollama

srcdir = "output"

with open(srcdir + "/" + "doing_my_weekly_quota_of_2_a_day_Baba_is_You.txt", 'r') as file:
    file_content = file.read()

print(file_content)

# result = ollama.generate(model='llama3.1', prompt="reformat this transcript for correct punctuation without changing any words. Also, just give me the reformatted transcript without telling me 'Here is the reformatted transcript'" + file_content)

# prompt = "reformat this transcript for correct punctuation without changing any words. Also, just give me the reformatted transcript without telling me 'Here is the reformatted transcript':\n" + file_content

prompt = file_content + "\nreformat this transcript for correct punctuation without changing any words. Also, just give me the reformatted transcript without telling me 'Here is the reformatted transcript'"

# If the prompt is too long, the beginning gets cut. The limit should be 20,000 characters.
stream = ollama.chat(
    model='llama3.1',
    messages=[{'role': 'user', 'content': prompt}],
    stream=True,
)

with open("result.txt", "a") as file:
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        file.write(chunk['message']['content'])
# with open("result.txt", "w") as text_file:
#     text_file.write(result)