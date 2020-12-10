# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:01:09 2020

@author: Vandan
"""

import nltk # Library for natutal language processings
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#nltk.download()
    
para='Machine learning involves computers discovering how they can perform tasks without being explicitly programmed to do so. It involves computers learning from data provided so that they carry out certain tasks. For simple tasks assigned to computers, it is possible to program algorithms telling the machine how to execute all steps required to solve the problem at hand; on the computer\'s part, no learning is needed. For more advanced tasks, it can be challenging for a human to manually create the needed algorithms. In practice, it can turn out to be more effective to help the machine develop its own algorithm, rather than having human programmers specify every needed step.'
sentences=nltk.sent_tokenize(para) # converts into list of sentences


# Pre processing
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
corpus = []
for i in range(len(sentences)):
    review = re.sub('[^A-Za-z]',' ', sentences[i])
    review = review.lower()
    review = review.split()
    review = [lemmatizer.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
# Creating Bag of words model using count vectorizer
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
vector = cv.fit_transform(corpus).toarray()
