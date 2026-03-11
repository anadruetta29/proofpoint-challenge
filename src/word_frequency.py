from collections import Counter

def analyze_word_frequency(filepath: str, top_n: int = 10):

    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()

    text = text.lower()

    cleaned_text = ""
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text += char

    words = [w for w in cleaned_text.split() if w]

    word_counts = Counter(words)

    return word_counts.most_common(top_n)


if __name__ == "__main__":

    filepath = "data/sample_text.txt"

    try:
        results = analyze_word_frequency(filepath)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        exit(1)

    print("Top 10 most frequent words:\n")
    for word, count in results:
        print(f" Word: {word} - Frequency: {count}")

