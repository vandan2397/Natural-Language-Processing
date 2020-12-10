# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 15:37:25 2020

@author: Vandan
"""

import nltk # Library for natutal language processings
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#nltk.download()
    
para='Machine learning involves computers discovering how they can perform tasks without being explicitly programmed to do so. It involves computers learning from data provided so that they carry out certain tasks. For simple tasks assigned to computers, it is possible to program algorithms telling the machine how to execute all steps required to solve the problem at hand; on the computer\'s part, no learning is needed. For more advanced tasks, it can be challenging for a human to manually create the needed algorithms. In practice, it can turn out to be more effective to help the machine develop its own algorithm, rather than having human programmers specify every needed step.'
sentences=nltk.sent_tokenize(para) # converts into list of sentences
words = nltk.word_tokenize(para) # converts into list of words



#stemming
stemmer = PorterStemmer()
stem_sentences = []
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    #stem_sentences[i]= ' '.join(words)
    stem_sentences.append(' '.join(words))
    
#lematization
lem_sentences=[]
lemmatizer = WordNetLemmatizer()
for i in range(0,len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    #sentences[i]= ' '.join(words)    
    lem_sentences.append(' '.join(words))
    

# word frequency distribution
from nltk.probability import FreqDist
fdist = FreqDist(words)
print(fdist)

import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()


