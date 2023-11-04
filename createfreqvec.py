import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load vocabulary
vocabulary = {}


# Load the dataset


# Convert emails to frequency vectors


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


# Predict and evaluate

