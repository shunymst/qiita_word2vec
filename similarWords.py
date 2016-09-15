#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
param = sys.argv
keyword = str(param[1]).lower()#komoji ni suru noda!
input = "word2vec.data"

paramLen = len(param)
if (paramLen == 3):
    input = str(param[2]) #input exist check


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

