# spamfiltercode

- **Description**: Exercise for the spam filter workshop.
- **Dependencies**: Run `pip install -r reqs.txt` to install all necessary dependencies.
- **Execution**:
  1. Run `buildvocab.py`
  2. Followed by `createfreqvec.py`

Outputs an accuracy report for the trained model:

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
