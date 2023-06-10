import csv
import json
from collections import Counter

def get_top_words(file_path, word_length, top_count):
    words = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row
        for row in reader:
            word = row[0]
            if word_length[0] <= len(word) <= word_length[1]:
                words.append(word)

    counter = Counter(words)
    top_words = [word for word, _ in counter.most_common(top_count)]
    return top_words

file_path = 'unigram_freq.csv'  # Replace with the path to your CSV file
word_length = (10, 1000000)  # Specify the word length range
top_count = 1000  # Number of top words to retrieve

top_words = get_top_words(file_path, word_length, top_count)

output_file = 'top_words-impossible.json'  # Specify the output file name

with open(output_file, 'w') as file:
    json.dump(top_words, file)

print(f"Top {top_count} words saved to {output_file}.")
