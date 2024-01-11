# encoding: utf-8
"""
@author: xiao nian
@contact: xiaonian030@163.com
@date: 2022-09-08
"""

from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) (2022-2022) QF Inc. All Rights Reserved"
__author__ = "Xiao Nian"
__date__ = "2022-09-10:14:13:24"
__version__ = "1.0.0"

from gensim.models import KeyedVectors
import os
import sys
import wget
import jieba

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
stopwords_path = os.path.join(current_dir, '../data', 'stopwords.txt')
model_url = "https://696e-infobird-4682b5-1302949103.tcb.qcloud.la/words.vector.gz"
model_file = os.path.join(current_dir, '../data', 'words.vector.gz')
exist_model = os.path.exists(model_file)
if not exist_model:
    print(">> 模型下载中...")
    wget.download(model_url, out=model_file)
    print(">> 模型下载完成！")
print(">> 模型加载中...")
model_vectors = KeyedVectors.load_word2vec_format(model_file, binary=True)
print(">> 模型加载完成！")
print(">> 停用词加载中...")
_stopwords = set()
words = open(stopwords_path, 'r', encoding='utf-8')
stopwords = words.readlines()
for w in stopwords:
    _stopwords.add(w.strip())
print(">> 停用词加载完成！")


def compare(sen_one, sen_two):
    # 为求多个词之间的相似性 [0,1]
    global model_vectors
    score = model_vectors.n_similarity(sen_one, sen_two)
    if score < 0:
        score = abs(score)
    score = min(score, 1.0)
    return float("%.4f" % score)


def sentence_cut(sentence_text):
    # 分词
    global _stopwords
    sentence_list = list(jieba.cut(sentence_text.strip()))
    word_list = []
    for word in sentence_list:
        if word not in _stopwords:
            word_list.append(word)
    return word_list


def multi_compare(item):
    text_id = item[0]
    text_title = item[1]
    text_input = item[2]
    try:
        score = compare(text_title, text_input)
    except:
        score = 0
    return text_id, text_title, score
