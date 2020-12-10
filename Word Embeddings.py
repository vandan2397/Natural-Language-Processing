# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 15:18:32 2020

@author: Vandan
"""

### Libraries Used Tensorflow> 2.0  and keras
##tensorflow >2.0
from tensorflow.keras.preprocessing.text import one_hot

### sentences
sent=[  'the glass of milk',
     'the glass of juice',
     'the cup of tea',
    'I am a good boy',
     'I am a good developer',
     'understand the meaning of words',
     'your videos are good',]


### Vocabulary size
voc_size=10000



onehot_repr=[one_hot(words,voc_size)for words in sent] 
print(onehot_repr)

from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential

import numpy as np


sent_length=8
embedded_docs=pad_sequences(onehot_repr,padding='pre',maxlen=sent_length)
print(embedded_docs)



# Dimnesions
dim=10


# Creating a model and adding embedding layer
model=Sequential()
model.add(Embedding(voc_size,10,input_length=sent_length))
model.compile('adam','mse')

model.summary()


# Vectors
print(model.predict(embedded_docs))





