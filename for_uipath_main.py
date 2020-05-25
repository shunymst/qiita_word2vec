#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys

param = sys.argv
input = "word2vec.data"

paramLen = len(param)
if (paramLen == 3):
    input = str(param[2])  # input exist check

from gensim.models import word2vec


class Main:
    def __init__(self):
        print('init. do nothing')

    def predict(self, keyword):
        try:
            model = word2vec.Word2Vec.load(input)  # load result
            data = model.most_similar(positive=[keyword])
            return json.dumps(data)
        except Exception as e:
            return '{"Error Occured ": %s}' % str(e)

if __name__ == '__main__':
    main = Main()
    print(main.predict('java'))
