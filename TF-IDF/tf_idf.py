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

#tf（「単語 i の文書 j における出現回数）を計算し辞書で返す
def tf(doc):
  word_count = {}
  for i in doc:
    word_count[i] = doc.count(i)
  # print(word_count)
  return word_count

def calc_df(word, docs):
  df = 0
  for doc in docs:
    if word in doc:
      df += 1
  return df

#IDFを計算し辞書で返す
def idf(word, docs):
  #文書数
  N = 10
  #単語iが出現する文書の数
  df = calc_df(word, docs)
  #idfを計算し返す
  return math.log2(N/df)

#TF-IDFの計算
def tf_idf():
  return tf*idf

def write_file(path, text):
  try:
    file = codecs.open(path, "w", "utf-8")
    file.write(text)
    file.close()
  except:
    text = "file write error"

def main():
  #全ての文書を保持
  docs = []
  for i in range(10):
    docs.append(read_file('input/'+str(i)+'.txt'))
  # print(docs)
  list_2 = read_file('0_1.txt')
  # print(list_a)
  # tf_score = tf(list_1)
  # for i in list_a:
  #   tf_score[i] = tf(i, list_a)
  # print(tf_score)
  idf_score = {}
  # for i in list_a:
  #   idf_score[i] = tf(i, docs)

if __name__ == "__main__":
  main()