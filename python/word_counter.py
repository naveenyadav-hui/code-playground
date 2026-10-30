"""Count the most common words in a text file. Usage: python word_counter.py file.txt"""
import re
import sys
from collections import Counter


def top_words(text: str, n: int = 10):
    words = re.findall(r"[a-z']+", text.lower())
    return Counter(words).most_common(n)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else __file__
    with open(path, encoding="utf-8") as f:
        for word, count in top_words(f.read()):
            print(f"{count:>5}  {word}")
