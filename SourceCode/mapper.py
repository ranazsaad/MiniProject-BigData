#!/usr/bin/env python3
import sys
import string

stopwords = set()
with open("stopwords.txt", "r") as f:
    for line in f:
        stopwords.add(line.strip().lower())

# Process input
for line in sys.stdin:
    line = line.strip().lower()  # lowercase
    line = line.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    words = line.split()
    for word in words:
        if word and word not in stopwords:
            import os
            filename = os.environ.get('map_input_file', 'unknown')
            filename = filename.split('/')[-1]
            print(f"{word}\t{filename}")
