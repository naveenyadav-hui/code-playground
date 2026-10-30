"""Count the most common words in a text file. Usage: python word_counter.py file.txt [--all]"""
import argparse
import re
from collections import Counter

# Very common English words that are rarely interesting in a word count.
STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "of", "to", "in", "on", "at", "for",
    "with", "by", "from", "is", "are", "was", "were", "be", "it", "this", "that",
    "as", "if", "i", "you", "we", "they", "he", "she", "not", "no", "so",
    # common contractions (the regex keeps apostrophes)
    "isn't", "aren't", "wasn't", "weren't", "don't", "doesn't", "didn't",
    "can't", "won't", "it's", "i'm", "you're", "we're", "they're",
}


def top_words(text: str, n: int = 10, ignore_stop_words: bool = True):
    words = re.findall(r"[a-z']+", text.lower())
    if ignore_stop_words:
        words = [w for w in words if w not in STOP_WORDS]
    return Counter(words).most_common(n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print the most common words in a text file.")
    parser.add_argument("path", nargs="?", default=__file__, help="text file to read")
    parser.add_argument("--all", action="store_true", help="count stop words too")
    parser.add_argument("-n", type=int, default=10, help="how many words to show")
    args = parser.parse_args()
    with open(args.path, encoding="utf-8") as f:
        for word, count in top_words(f.read(), n=args.n, ignore_stop_words=not args.all):
            print(f"{count:>5}  {word}")
