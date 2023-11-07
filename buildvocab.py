# This generates vocabulary.txt, which is a list of words and the number of times they appear in spammy emails.
# Top words included selectable, hypercube, toughest, critic, and desiring, with counts ranging from 37435 to 37440. That's insanely close.

import pandas as pd
data_sample = pd.read_csv("data/emails.csv")
vocabulary = {}

# Build the vocabulary dictionary. If the word isn't in the vocabulary, add it
def build_vocabulary(email_words):
    for word in email_words:
        if word not in vocabulary:
            vocabulary[word] = len(vocabulary)

# For every email in the dataset, split the email into individual words and call build_vocabulary
for email in data_sample['text']:
    email_words = email.split()
    build_vocabulary(email_words)


# Save the vocabulary to a file for further use
with open("vocabulary.txt", "w") as vocab_file:
    for word, index in vocabulary.items():
        vocab_file.write(f"{word}\t{index}\n") #seperate words and index with a tab

