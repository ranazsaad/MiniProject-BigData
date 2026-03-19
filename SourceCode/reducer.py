#!/usr/bin/env python3
import sys
from collections import defaultdict

# Store counts per word per document
word_doc_count = defaultdict(lambda: defaultdict(int))

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    word, doc = line.split("\t")
    word_doc_count[word][doc] += 1

# Output the reverse index
for word in sorted(word_doc_count.keys()):
    doc_counts = word_doc_count[word]
    doc_list = [f"{doc}:{count}" for doc, count in sorted(doc_counts.items())]
    print(f"{word} -> {', '.join(doc_list)}")
