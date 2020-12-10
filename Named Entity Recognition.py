# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:45:08 2020

@author: Vandan
"""
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Named entity recognition
sent1 = "Apple is looking at buying U.K. startup for $1 billion. 18.75% Apple is situated in America. Established in 12/02/1998"
words = nltk.word_tokenize(sent1)
tagged = nltk.pos_tag(words)

# NER
named_ent = nltk.ne_chunk(tagged)
named_ent.draw()
