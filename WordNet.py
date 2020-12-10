# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 10:30:36 2020

@author: Vandan
"""

from nltk.corpus import wordnet
syn = wordnet.synsets('hello')[0] 
  
print ("Synset name :  ", syn.name()) 
  
# Defining the word 
print ("\nSynset meaning : ", syn.definition()) 
  
# list of phrases that use the word in context 
print ("\nSynset example : ", syn.examples()) 



# Hypernyms
# More abstract terms  
print ("\nSynset abstract term :  ", syn.hypernyms()) 


# Hyponyms
# More specific terms   
print ("\nSynset specific term :  ",  syn.hypernyms()[0].hyponyms()) 
  

syn.root_hypernyms() 
  
print ("\nSynset root hypernerm :  ", syn.root_hypernyms()) 



# synonyms and antonyms

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())



# Part of speech in synset
syn = wordnet.synsets('hello')[0] 
print ("Syn tag : ", syn.pos()) 
  
syn = wordnet.synsets('doing')[0] 
print ("Syn tag : ", syn.pos()) 
  
syn = wordnet.synsets('beautiful')[0] 
print ("Syn tag : ", syn.pos()) 
  
syn = wordnet.synsets('quickly')[0] 
print ("Syn tag : ", syn.pos()) 


# Calculating similarity
w1 = wordnet.synset('dog.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))


w3 = wordnet.synset('ship.n.01')
w4 = wordnet.synset('car.n.01')
print(w4.wup_similarity(w3))








