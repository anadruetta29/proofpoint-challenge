import re
from collections import Counter


def analyze_word_frequency(filepath: str, top_n: int = 10):

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found.")
        return []

    text = text.lower()

    text = re.sub(r"[^a-z0-9\s]", "", text)

    words = [w for w in text.split() if w]

    word_counts = Counter(words)

    return word_counts.most_common(top_n)


if __name__ == "__main__":

    filepath = "../data/sample_text.txt"

    results = analyze_word_frequency(filepath)

    print("Top 10 most frequent words:\n")

    for word, count in results:
        print(f"{word}: {count}")