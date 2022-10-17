import codecs
import math

#ファイルの読み込み
def read_file(path):
  try:
    file = codecs.open(path, 'r', encoding='shift_jis')
    text = file.read()
    # print(text)
    file.close()
  except:
    text = "file open error"

  word_list = text.split()

  return word_list

#渡された辞文書の各単語のtf（「単語 i の文書 j における出現回数）を計算し辞書で返す
def tf(doc):
  word_count = {}
  for i in doc:
    word_count[i] = doc.count(i)
  # print(word_count)
  return word_count

#渡された単語のdfの値を返す
def calc_df(word, docs):
  df = 0
  for doc in docs:
    if word in doc:
      df += 1
  return df

#渡された文書の各単語のIDFを計算し辞書で返す
def idf(N, doc, docs):
  idf = {}
  for word in doc:
    idf[word] = math.log(N/calc_df(word, docs))
  return idf

#渡された文書のTF-IDFの計算
def tf_idf(doc, tf_score, idf_score):
  tf_idf = {}
  for word in doc:
    tf_idf[word] = tf_score[word]*idf_score[word]
  return tf_idf

def write_file(path, text):
  try:
    file = codecs.open(path, "a", "utf-8")
    file.write(text)
    file.close()
  except:
    text = "file write error"
    print('error')

def main():
  #文書の数
  N = 3
  #全ての文書を読み込む
  docs = []
  for i in range(N):
    # docs.append(read_file('input/'+str(i)+'.txt'))
    docs.append(read_file(str(i) + '.txt'))
  print(docs)

  for i in range(N):
    tf_score = tf(docs[i])
    print('tf_score',tf_score)
    idf_score = idf(N, docs[i], docs)
    print('idf_score',idf_score)
    tf_idf_score = tf_idf(docs[i], tf_score, idf_score)
    print('tf_idf_score', tf_idf_score)
    for word in tf_idf_score:
      write_file('result/'+str(i)+'.txt', word+'  '+str(tf_idf_score[word])+'\n')

if __name__ == "__main__":
  main()