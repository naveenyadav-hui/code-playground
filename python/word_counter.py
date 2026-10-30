"""Count the most common words in a text file. Usage: python word_counter.py file.txt [--all]"""
import re
import sys
from collections import Counter

# Very common English words that are rarely interesting in a word count.
STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "of", "to", "in", "on", "at", "for",
    "with", "by", "from", "is", "are", "was", "were", "be", "it", "this", "that",
    "as", "if", "i", "you", "we", "they", "he", "she", "not", "no", "so",
}


def top_words(text: str, n: int = 10, ignore_stop_words: bool = True):
    words = re.findall(r"[a-z']+", text.lower())
    if ignore_stop_words:
        words = [w for w in words if w not in STOP_WORDS]
    return Counter(words).most_common(n)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    path = args[0] if args else __file__
    keep_all = "--all" in sys.argv
    with open(path, encoding="utf-8") as f:
        for word, count in top_words(f.read(), ignore_stop_words=not keep_all):
            print(f"{count:>5}  {word}")
