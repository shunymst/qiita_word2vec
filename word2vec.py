#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging
input = "qiita_Python_grep_SUM_mecab.txt"
output = "word2vec.data"

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO) # 今どれくらい処理が進んでるか確認する用
sentences = word2vec.Text8Corpus(input)#target txt
model = word2vec.Word2Vec(sentences, size=200) 
model.save(output)# record result
print(input + " --->>>> " + output)

