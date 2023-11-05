import spacy
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import os

script_dir = os.path.dirname(__file__)
data_file = os.path.join(script_dir, "Afinn.csv")
model_file1 = os.path.join(script_dir, "knn_model.pkl")
affin = pd.read_csv(data_file, encoding='latin-1')
affinity_scores = affin.set_index('word')['value'].to_dict()

nlp = spacy.load('en_core_web_sm')
lexicons = affinity_scores


def calculate_sentiment(text: str = None):
    sent_score = 0
    if text:
        sentence = nlp(text)
        print(sentence)
        for word in sentence:
            sent_score += lexicons.get(word.lemma_, 0)
    return sent_score


def inputfunction(X):
    with open(model_file1, 'rb') as model_file:
        loaded_knn_model = pickle.load(model_file)
    y = calculate_sentiment(X)
    l = len(X.split())
    X = [X]

    cv = TfidfVectorizer(norm='l2', analyzer='word',
                         ngram_range=(1, 3), dtype=np.float64)
    y1 = cv.fit_transform(X)
    y1 = list(y1.toarray())
    # print(y1)
    finallen = len(y1[0])
    empty_df = pd.DataFrame(columns=['a', 'b', 'c'])
    empty_df['a'] = y
    empty_df['b'] = l
    empty_df['c'] = y1
    empty_df['a'] = y
    empty_df['b'] = l
    empty_df['c'] = y1
    empty_df = empty_df.to_numpy()
    empty_df = np.array([np.concatenate([a[:2], a[2]]) for a in empty_df])
    empty_df = empty_df.astype(np.float64)
    for i in range(34445-(finallen+2)):
        empty_df = np.append(empty_df, 0)
    y_predict = loaded_knn_model.predict(empty_df.reshape(1, -1))
    a = ['Negative', 'Neutral', 'Positive']
    return a[y_predict[0]]
