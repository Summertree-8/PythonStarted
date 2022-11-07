import codecs
import math


# ファイルの読み込み
def read_file(path):
    try:
        file = codecs.open(path, 'r', encoding='shift_jis')
        text = file.read()
        # print(text)
        file.close()
    except:
        text = "file open error"
        print('error')

    word_list = text.split()

    return word_list


# 渡された辞文書の各単語のtf（「単語 i の文書 j における出現回数）を計算し辞書で返す
def tf(doc):
    word_count = {}
    for i in doc:
        word_count[i] = word_count.get(i, 0) + 1

    return word_count


# 渡された単語のdfの値を返す
def calc_df(N, tf_score):
    df = {}
    for i in range(N):
        for key in tf_score[i].keys():
            df[key] = df.get(key, 0) + 1

    # なっきー説明用
    # df = {単語:x文書に出現}みたいな辞書を作ってる。　ex) {明治大学:5, 二井矢:2.......}みたいな
    # こうすればdf[key]で単語のdf値が呼び出せる辞書になる。

    return df


# 渡された文書のTF-IDFを計算し辞書で返す
def tf_idf(N, tf_score, calc_df):
    tf_idf = {}
    for word in tf_score:
        tf_idf[word] = tf_score[word] * math.log(N / calc_df[word])

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
    N = 10
    # 全ての文書を読み込む
    docs = []
    for i in range(N):
        docs.append(read_file('input/' + str(i) + '.txt'))
        # print(docs)

    tf_score = []
    for i in range(N):
        tf_score.append(tf(docs[i]))

    df = calc_df(N, tf_score)

    for i in range(N):
        tf_idf_score = {}
        print(f"{i}.txt開始")

        tf_idf_score = tf_idf(N, tf_score[i], df)

        for word in tf_idf_score:
          write_file('result/'+str(i)+'.txt', word+'  '+str(tf_idf_score[word])+'\n')

        print(f"{i}.txt終了")


main()