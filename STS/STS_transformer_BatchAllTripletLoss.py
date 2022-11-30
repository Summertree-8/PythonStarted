#sentence transformer

#import libraly
import codecs
import math
import numpy as np

import transformers
import sentence_transformers
transformers.BertTokenizer = transformers.BertJapaneseTokenizer
from sentence_transformers import SentenceTransformer
from sentence_transformers import models
from sentence_transformers.losses import TripletDistanceMetric, TripletLoss
from sentence_transformers.readers import TripletReader
from sentence_transformers.datasets import SentencesDataset
from torch.utils.data import DataLoader
from sentence_transformers.readers import InputExample
from sentence_transformers import losses

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer as PS


#ファイルの読み込みlistで返す
def read_file(path):
  try:
    file = codecs.open(path, 'r', encoding='utf-8-sig')
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
# def cos_sim(v1, v2):
#   return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def write_file(path, text):
  try:
    file = codecs.open(path, "a", "utf-8")
    file.write(text)
    file.close()
  except:
    text = "file write error"
    print('error')

def main():
  #read files
  docs = []
  # docs=(read_file('testData/STS.input.images.txt'))
  # doc1 = []
  # doc2 = []
  # doc_all = []
  # stop_words = stopwords.words('english')
  # ps = PS()
  # for i in range(len(docs)):
  #   doc_all.append(docs[i].split('\t')[0])
  #   doc_all.append(docs[i].split('\t')[1])
  # doc_all_new = []
  #
  # for i in range(len(doc_all)):
  #   _tmp = doc_all[i].replace('.', '')
  #   tmp = _tmp.split()
  #   tmp2 = ''
  #   for j in range(len(tmp)):
  #     if tmp[j] not in stop_words:
  #       tmp2 += ps.stem(tmp[j]) + ' '
  #   doc_all_new.append(tmp2)


  # #define model
  transformer = models.Transformer('sentence-transformers/all-MiniLM-L6-v2')
  pooling = models.Pooling(
    transformer.get_word_embedding_dimension(),
    pooling_mode_mean_tokens=True,
    pooling_mode_cls_token=False,
    pooling_mode_max_tokens=False
  )
  model = SentenceTransformer(modules=[transformer, pooling])

  # #read train data
  train_examples = []
  input = (read_file('learnData/STS.input.OnWN.txt'))
  input1 = []
  input2 = []
  for i in range(len(input)):
    input1.append(input[i].split('\t')[0].replace('.', ''))
    input2.append(input[i].split('\t')[1].replace('.\n', ''))
  input_similality = (read_file('learnData/STS.gs.OnWN.txt'))
  for i in range(len(input_similality)):
    input_similality[i] = input_similality[i].replace('\n', '')
  for i in range(len(input)):
    if float(input_similality[i]) > 4:
      train_examples.append(InputExample(texts=[input1[i], input2[i], input1[i-1]]))

  train_data = SentencesDataset(train_examples, model)

  BATCH_SIZE = 64
  NUM_EPOCH = 4
  EVAL_STEPS = 100
  WARMUP_STEPS = int(len(train_data) // BATCH_SIZE * 0.1)


  train_dataloader = DataLoader(train_data, shuffle=True, batch_size=BATCH_SIZE)
  #ロスに TripletLossを使用
  train_loss = losses.BatchAllTripletLoss(
    model=model
  )

  # #学習
  model.fit(
    train_objectives=[(train_dataloader, train_loss)],
    epochs=NUM_EPOCH,
    evaluation_steps=EVAL_STEPS,
    warmup_steps=WARMUP_STEPS,
    output_path="./sbert",
  )

  #文書ベクトルを得る
  sbert = SentenceTransformer('./sbert')
  test_data = (read_file('testData/STS.input.images.txt'))
  test_data1 = []
  test_data2 = []
  for i in range(len(test_data)):
    test_data1.append(test_data[i].split('\t')[0].replace('.', ''))
    test_data2.append(test_data[i].split('\t')[1].replace('.\n', ''))
  vec1 = []
  vec2 = []
  for i in range(len(test_data)):
    vec1.append(sbert.encode(test_data1[i]))
    vec2.append(sbert.encode(test_data2[i]))

  #calc cos similarity
  cos_sim_res = []
  # tf_idf1_n = np.array(tf_idf1).reshape(-1,1)
  # tf_idf2_n = np.array(tf_idf2).reshape(-1, 1)
  cos_sim_res = cosine_similarity(vec1, vec2)

  res = []
  for i in range(len(vec1)):
    res.append(cos_sim_res[i][i])
    write_file('result.txt', str(cos_sim_res[i][i]) + '\n')

if __name__ == "__main__":
  main()