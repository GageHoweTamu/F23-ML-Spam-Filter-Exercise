# This outputs an accuracy report for the trained model, such as:

'''
(5728, 37441)
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
Accuracy: 0.9895287958115183
Classification Report:               precision    recall  f1-score   support

           0       1.00      0.99      0.99       856
           1       0.97      0.99      0.98       290

    accuracy                           0.99      1146
   macro avg       0.98      0.99      0.99      1146
weighted avg       0.99      0.99      0.99      1146

'''

import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load vocabulary
vocabulary = {}
with open("vocabulary.txt", "r") as vocab_file:
    for line in vocab_file:
        word, index = line.strip().split("\t")
        vocabulary[word] = int(index)

# Load the dataset
data_sample = pd.read_csv("data/emails.csv")
X_sample = np.zeros((len(data_sample['text']), len(vocabulary))) # Create a matrix of zeros with the same number of rows as the dataset and the same number of columns as the vocabulary
print(X_sample.shape)
print(X_sample)
y_sample = data_sample['spam']

# Convert emails to frequency vectors
for i, email in enumerate(data_sample['text']):
    email_words = email.split()
    for word in email_words:
        if word in vocabulary:
            X_sample[i, vocabulary.get(word.lower(), 0)] += 1 # Increment the count for this word in email 

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_sample, y_sample, test_size=0.2, random_state=42)
'''
train_test_split takes in these inputs:
    X_sample: feature matrix. Each row is a sample (email freq vector) and each column is a feature (count of a word from vocab)
    y_sample: target vector. Each entry represents a label (whether the email is spam or not)
    test_size: split the data into training and testing sets. 20% will be used for testing, rest training
    random_state: seed for the random number generator. Use any number
    
train_test_split outputs these:
    X_train: subset of the feature matrix for training. Should contain 80% of the original data
    X_test: subset of the feature matrix for testing. Should contain 20% of the original data
    y_train & y_test: labels for training and testing data
'''


# Train Naive Bayes
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Predict and evaluate
yy_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, yy_pred)
classification_rep = classification_report(y_test, yy_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:", classification_rep)