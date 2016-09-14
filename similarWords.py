#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
param = sys.argv
keyword = param[1]
input = "word2vec.data"

from gensim.models import word2vec
import logging

def similarWords(keyword): 
	model = word2vec.Word2Vec.load(input)# load result
	return model.most_similar(positive=[keyword])

if __name__=="__main__":
	out=similarWords(keyword)
	print ("key   /   score")
	for x in out:
		print (x[0],x[1])
