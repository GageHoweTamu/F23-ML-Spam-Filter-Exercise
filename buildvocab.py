import pandas as pd

data_sample = pd.read_csv("data\emails.csv")

vocabulary = {}

# Build the vocabulary dictionary. If the word isn't in the vocabulary, add it
def build_vocabulary(email_words):


# For every email in the dataset, split the email into individual words and call build_vocabulary


# Save the vocabulary to a file for further use
with open("vocabulary.txt", "w") as vocab_file:
    for word, index in vocabulary.items():
        vocab_file.write(f"{word}\t{index}\n") #seperate words and index with a tab

