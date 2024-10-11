#!/bin/sh
# This script iterates through all of the .txt files in output and runs ollama on them
# Requires ollama to be already running to work
# The prompt character limit cuts off a large portion of the total transcript, so if this will actually be used, we must split it up into smaller transcripts
for filename in ./output/*.txt; do
    base_name=$(basename ${filename})
    ollama run llama3.2 "reformat this transcript for correct punctuation without changing any words. Also, just give me the reformatted transcript without telling me 'Here is the reformatted transcript'" < output/${base_name} >> reformatted/${base_name}
done
