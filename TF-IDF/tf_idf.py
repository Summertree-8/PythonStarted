import codecs
import math

#ファイルの読み込みlistで返す
def read_file(path):
  try:
    file = codecs.open(path, 'r', encoding='shift_jis')
    text = file.read()
    file.close()
  except:
    text = "file open error"

  word_list = text.split()
  return word_list

#渡された辞文書の各単語のtf（「単語 i の文書 j における出現回数）を計算し辞書で返す
def tf(doc):
  word_count = {}
  for i in doc:
    word_count[i] = word_count.get(i, 0) + 1
  return word_count

#df(単語iか出現する文書数)の値をもとめ、df値の辞書に追加
def calc_df(N, tf_score):
  df = {}
  for doc in range(N):
    #tfの辞書に存在すればその文書に出現している
    for key in tf_score[doc].keys():
      df[key] = df.get(key, 0) + 1
  return df

#渡された文書(tf_score)のTF-IDFを計算し辞書で返す
def tf_idf(N, tf_score, df):
  tf_idf = {}
  for word in tf_score:
    tf_idf[word] = tf_score[word] * math.log(N/df[word])
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
  N = 10
  #全ての文書を読み込む
  docs = []
  for i in range(N):
    docs.append(read_file('input/'+str(i)+'.txt'))
  # print('docs')

  #各文書のtf値の辞書を保持するリスト
  tf_score = []
  for i in range(N):
    tf_score.append(tf(docs[i]))

  df = calc_df(N, tf_score)

  #各文書について、tf-idfの値を求める
  for i in range(N):
    tf_idf_score = {}
    tf_idf_score = tf_idf(N, tf_score[i], df)
    #出力のファイルに書き込み
    for word in tf_idf_score:
      write_file('result/'+str(i)+'.txt', word+'  '+str(tf_idf_score[word])+'\n')

if __name__ == "__main__":
  main()