import codecs
import math
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

  print('feature_names:', vectorizer.get_feature_names_out())

  # 特徴量ラベルの取得
  # words = vectorizer.get_feature_names()

  return values

#cos類似度を求める
# def cos_sim(v1, v2):
#   return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def main():
  #read files
  docs = []
  docs=(read_file('learnData/STS.input.OnWN.txt'))
  # print(docs)
  doc1 = []
  doc2 = []
  doc_all = []
  # doc1 = np.array([])
  # doc2 = np.array([])
  for i in range(len(docs)):
    doc1.append(docs[i].split('\t')[0])
    doc2.append(docs[i].split('\t')[1])
    doc_all.append(docs[i].split('\t')[0])
    doc_all.append(docs[i].split('\t')[1])
    # doc1 = np.append(doc1, docs[i].split('\t')[0])
    # doc2 = np.append(doc2, docs[i].split('\t')[1])
  print('doc_all: \n', doc_all)

  #calc tf-idf
  tf_idf_list = []
  tf_idf_list = tf_idf(doc_all)
  tf_idf1 = []
  tf_idf2 = []
  print('tf_idf_list: \n', tf_idf_list)
  for i in range(len(docs)):
    tf_idf1.append(tf_idf_list[i * 2])
    tf_idf2.append(tf_idf_list[i * 2 + 1])
  print('tf_idf1: \n', tf_idf1)
  print('tf_idf2: \n', tf_idf2)

  #calc cos similarity
  cos_sim_res = []
  # tf_idf1_n = np.array(tf_idf1).reshape(-1,1)
  # tf_idf2_n = np.array(tf_idf2).reshape(-1, 1)
  for i in range(len(docs)):
    print('cosine_similarity: \n', cosine_similarity(tf_idf1[i], tf_idf2[i]))
    # cos_sim_res = cosine_similarity(tf_idf1,tf_idf2)
  # print('cos_sim_res: \n', cos_sim_res)



if __name__ == "__main__":
  main()