

import sys
param = sys.argv
keyword = param[1]

from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO) # 今どれくらい処理が進んでるか確認する用
sentences = word2vec.Text8Corpus('qiita_Python_grep_SUM_mecab.txt')
model = word2vec.Word2Vec(sentences, size=200) #MBAだと100MBで2分弱くらいかかりました

#out=model.most_similar(positive=[u'python'])
out=model.most_similar(positive=[keyword])
for x in out:
    print (x[0],x[1])
