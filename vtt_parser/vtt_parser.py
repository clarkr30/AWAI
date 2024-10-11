from pathlib import Path
import webvtt
import os
# TODO: Make better comments

# Extracts a line from the vtt file
def extractLine(srcPath):
    vtt = webvtt.read(srcPath)
    for caption in vtt:
        for line in caption.text.strip().splitlines():
            yield line

# Takes a line and filters it if it matches some keywords or is a duplicate
def filterLines(lines):
    lastLine = ""
    filteredTerms = ["[Music]", "[Applause]", "[Laughter]", "foreign"]
    for line in lines:
        if line == lastLine or line in filteredTerms:
            # print(line)
            continue
        lastLine = line
        yield line

# Converts a vt file to text
def parse_vtt(srcPath, destPath):
    with destPath.open("w") as writer:
        for line in filterLines(extractLine(srcPath)):
            writer.write(line.replace("&nbsp;", " ").strip() + "\n")

# parse_vtt("../Streams/20240216 - EP._16_-_nearing_the_end_of_an_era/EP._16_-_nearing_the_end_of_an_era [Tz0xSdrEfTc].en.vtt", Path("output.txt"))
srcPath = "../Streams"
destPath = "output"

# Iterates through the streams directory, parses every transcript, and puts the result txt file into the destination path
for dir1 in os.listdir(srcPath):
    for file in os.listdir(srcPath + "/" + dir1):
        if file.endswith(".en.vtt") and os.path.exists(srcPath + "/" + dir1 + "/" + "category2"):
            # print(file.split(" ")[0])
            parse_vtt(srcPath + "/" + dir1 + "/" + file, Path(destPath + "/" + file.split(" ")[0] + ".txt"))