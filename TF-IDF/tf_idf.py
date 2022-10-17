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

#tf（「単語 i の文書 j における出現回数）の計算
def tf(word, doc):
  word_count = 0
  for i in doc:
    if i == word:
      word_count += 1
  return word_count

def calc_df(word, docs):
  df = 0
  for doc in docs:
    if word in doc:
      df += 1
  return df

#IDFの計算
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
  list_a = read_file('0.txt')
  print(list_a)
  tf_score = {}
  for i in list_a:
    tf_score[i] = tf(i, list_a)
  print(tf_score)
  idf_score = {}
  for i in list_a:
    idf_score[i] = tf(i, docs)

if __name__ == "__main__":
  main()