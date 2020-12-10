# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:12:15 2020

@author: Vandan
"""

nltk.download('gutenberg')
from nltk.corpus import gutenberg
import nltk


sample = gutenberg.raw('bible-kjv.txt')
sentences = nltk.sent_tokenize(sample[1:10])
