# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:23:06 2020

@author: Vandan
"""

import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
from nltk import bigrams, trigrams
from nltk.corpus import reuters
#nltk.download('reuters')

text = "I need to write a program in NLTK that breaks a corpus (a large collection of \
txt files) into unigrams, bigrams, trigrams, fourgrams and fivegrams.\ I need to write a program in NLTK that breaks a corpus"

token = nltk.word_tokenize(text)
#bigrams = ngrams(token,2)
#trigrams = ngrams(token,3)
fourgrams = ngrams(token,4)
fivegrams = ngrams(token,5)

print(Counter(bigrams))




# N-Gram Model

from collections import Counter, defaultdict
model = defaultdict(lambda: defaultdict(lambda: 0))

# Count frequency of co-occurance  
for sentence in reuters.sents():
    for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
        model[(w1, w2)][w3] += 1
 
# Let's transform the counts to probabilities
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count
        
dict(model['This','is'])
#
#for w1_w2 in model:
#    print(w1_w2)
#
#print(model[('begin', 'a')].values())



# Sentence generator

import random

# starting words
text = ["today", "the"]
sentence_finished = False
 
while not sentence_finished:
  # select a random probability threshold  
  r = random.random()
  accumulator = .0

  for word in model[tuple(text[-2:])].keys():
      accumulator += model[tuple(text[-2:])][word]
      # select words that are above the probability threshold
      if accumulator >= r:
          text.append(word)
          break

  if text[-2:] == [None, None]:
      sentence_finished = True
 
print (' '.join([t for t in text if t]))
