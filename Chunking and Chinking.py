# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:38:02 2020

@author: Vandan
"""

import nltk


para='''a beautiful young lady is walking on the pavement. an innocent cool boy is sitting on the bench'''
               
words = nltk.word_tokenize(para)
tagged = nltk.pos_tag(words)


# Chunking

# Define a grammer
grammar = "NP: {<DT>?<JJ>*<NN>}"

# Create Parser
parser = nltk.RegexpParser(grammar)
output = parser.parse(tagged)

output.draw()


# Chinking
grammar = r'''NP: 
{<DT>?<JJ>*<NN>}  
}<JJ.*>{'''

# Create Parser
parser = nltk.RegexpParser(grammar)
output = parser.parse(tagged)

output.draw()






