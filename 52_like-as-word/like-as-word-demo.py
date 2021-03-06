import jieba
from gensim import corpora, models, similarities  # 文本相似度库gensim

doc0 = "我不喜欢上海"
doc1 = "上海是一个好地方"
doc2 = "北京是一个好地方"
doc3 = "上海好吃的在哪里"
doc4 = "上海好玩的在哪里"
doc5 = "上海是好地方"
doc6 = "上海路和上海人"
doc7 = "喜欢小吃"

doc_test = "我喜欢上海的小吃"

all_doc = []
all_doc.append(doc0)
all_doc.append(doc1)
all_doc.append(doc2)
all_doc.append(doc3)
all_doc.append(doc4)
all_doc.append(doc5)
all_doc.append(doc6)
all_doc.append(doc7)

# 对目标文档分词，保存在all_doc_list

all_doc_list = []

for doc in all_doc:
    doc_list = [word for word in jieba.cut(doc)]
    all_doc_list.append(doc_list)

print("分词结果=>", all_doc_list)

# 测试文档分词，保存在doc_test_list

doc_test_list = [word for word in jieba.cut(doc_test)]
print("需要测试的分词=>", doc_test_list)

# 制作语料库，词袋 bag-of-words
dict_lib = corpora.Dictionary(all_doc_list)
print("打印一下语料库=>", dict_lib)

print("词用数字进行编号关系=>", dict_lib.keys())

print("编号与词的对应关系=>", dict_lib.token2id)

# 使用doc2bow制作语料库
corpus = [dict_lib.doc2bow(doc) for doc in all_doc_list]
print("使用doc2bow制作语料库=>", corpus)

docs_test_vec = dict_lib.doc2bow(doc_test_list)
print("使用doc2bow制作测试语料库=>", docs_test_vec)

# 相似度分析，使用TF-IDF模型对语料库进行建模
tfidf = models.TfidfModel(corpus)

# 获取测试文档中，每个词的TF-IDF值
print("测试文档中TF-IDF值=>", tfidf[docs_test_vec])

# 对每个目标文档，分析测试文档的相似度
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dict_lib.keys()))
sim = index[tfidf[docs_test_vec]]
print("分析测试文档的相似度=>", sim)

# 根据相似度排序
print("根据相似度排序=>", sorted(enumerate(sim), key=lambda item: -item[1]))
