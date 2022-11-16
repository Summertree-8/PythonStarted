#wrd
import codecs
import math
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer as PS

import os
import argparse

from gensim.models import KeyedVectors
import MeCab
import ot


#ファイルの読み込みlistで返す
def read_file(path):
  try:
    file = codecs.open(path, 'r', encoding='utf-8')
    text = file.readlines()
    file.close()
    # print('read')
  except:
    text = "file open error"

  # word_list = text.split()
  return text

def tf_idf(docs):
  # モデルの生成
  vectorizer = TfidfVectorizer(smooth_idf=False)

  # TF-IDFの計算
  values = vectorizer.fit_transform(docs).toarray()
  # print('feature_names:', vectorizer.get_feature_names_out())

  # 特徴量ラベルの取得
  words = vectorizer.get_feature_names_out()

  return values, words

#cos類似度を求める
def cos_sim(v1, v2):
  return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def write_file(path, text):
  try:
    file = codecs.open(path, "a", "utf-8")
    file.write(text)
    file.close()
  except:
    text = "file write error"
    print('error')

def get_w(text, mt, wv):
  kws = mt.parse(text).split()
  w = [np.array(wv[kw]) for kw in kws if kw in wv]
  return w


def get_z(w):
  z = 0
  for w_i in w:
    z += np.linalg.norm(w_i)
  return z

def main():
  #read files
  docs = []
  docs=(read_file('testData/STS.input.images.txt'))
  # print(docs)
  doc1 = []
  doc2 = []
  doc_all = []
  # doc1 = np.array([])
  # doc2 = np.array([])
  stop_words = stopwords.words('english')
  ps = PS()
  for i in range(len(docs)):
    # doc1.append(docs[i].split('\t')[0])
    # doc2.append(docs[i].split('\t')[1])
    doc_all.append(docs[i].split('\t')[0])
    doc_all.append(docs[i].split('\t')[1])
    # doc1 = np.append(doc1, docs[i].split('\t')[0])
    # doc2 = np.append(doc2, docs[i].split('\t')[1])
  print('doc_all: \n', doc_all)
  doc_all_new = []

  for i in range(len(doc_all)):
    _tmp = doc_all[i].replace('.', '')
    tmp = _tmp.split()
    tmp2 = ''
    # print(tmp)
    for j in range(len(tmp)):
      if tmp[j] not in stop_words:
        tmp2 += ps.stem(tmp[j]) + ' '
    doc_all_new.append(tmp2)
  print('doc_all_new: \n', doc_all_new)

  for i in range(int(len(doc_all_new)/2)):
    doc1.append(doc_all_new[i*2])
    doc2.append(doc_all_new[i*2+1])
  print(doc1)
  print(doc2)

  #calc tf-idf
  tf_idf_list = []
  tf_idf_list, tf_idf_words = tf_idf(doc_all_new)
  tf_idf1 = []
  tf_idf2 = []
  # print('tf_idf_list: \n', tf_idf_list)
  # print('tf_idf_words: \n', tf_idf_words)
  for i in range(len(docs)):
    tf_idf1.append(tf_idf_list[i * 2])
    tf_idf2.append(tf_idf_list[i * 2 + 1])
  # print('tf_idf1: \n', tf_idf1)
  # print('tf_idf2: \n', tf_idf2)

  model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin', binary=True)



  #calc similarity by wmd
  # for i in range(len(docs)):
    # print(model.wmdistance(doc1[i], doc2[i]))
    # write_file('result.txt', str(model.wmdistance(doc1[i],doc2[i])) + '\n')

  # print('cos_sim_res: \n', cos_sim_res)
  # print('res: \n', res)

  print(len(docs))
  print(len(doc_all))
  print(len(tf_idf1))
  print(len(tf_idf2))


# Input the sentences which you want to get the similarity
  s1 = '大坂なおみ 逆転で2年ぶり2度目の全米OP優勝。3度目のグランドスラム制覇'
  s2 = '大坂なおみが2年ぶり2回目のV　4大大会3勝目　全米テニス'

  mt = MeCab.Tagger('-d {} -Owakati'.format(args.mecab_dict_path)) if args.mecab_dict_path is not None else MeCab.Tagger('-Owakati')
  wv = KeyedVectors.load_word2vec_format(os.path.dirname(os.path.abspath(__file__)) + '/vecs/jawiki.word_vectors.200d.txt')

  w1 = get_w(s1, mt, wv)
  w2 = get_w(s2, mt, wv)

  z1 = get_z(w1)
  z2 = get_z(w2)

  m1 = [np.linalg.norm(w1_i) / z1 for w1_i in w1]
  m2 = [np.linalg.norm(w2_i) / z2 for w2_i in w2]

  # Compute cost matrix C
  c = []
  for w1_i in w1:
    c.append([1 - cos_sim(np.array(w1_i), np.array(w2_j)) for w2_j in w2])

  # Show the result
  print(s1)
  print(s2)
  print("{:.2f}".format(ot.emd2(m1, m2, c)))


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--mecab_dict_path', type=str,
    help='Path to MeCab custom dictionary.')
  args = parser.parse_args()

  main(args)