from konlpy.tag import Kkma
from tqdm import tqdm as tq
from collections import Counter
import re
kkma = Kkma()
F = open("after_news_article_nospstr.txt",'r+', encoding='utf-8')
source = F.readlines()

F =  open('most_common.txt', 'r', encoding='utf-8')
f_rm_sentence = F.readlines()

rm_sentence_list = set()
for i in f_rm_sentence :
    rm_sentence_list.add(i)

# after_sentence = [ x for x in sentence if x not in rm_sentence_list ]
after_article_sentence = []
after_sentence = []
for sentence in source :
    after_sentences = []
    if sentence not in rm_sentence_list : 
        after_sentences.append(sentence)
        after_sentence.append(sentence)
    after_article_sentence.append(after_sentences)

len_nouns = []

for nouns in tq(after_sentence) : 
    ex_nouns = kkma.nouns(nouns)
    len_nouns.append(len(ex_nouns))

total_umjual = [ len(x) for x in after_sentence ]
print('total_umjual :', sum(total_umjual))
print('avg umjual :', sum(total_umjual)/len(total_umjual))
print('num of sentence : ',len(after_sentence))
print('total ujual :', sum(len_nouns))
print('avg ujual :', sum(len_nouns)/len(len_nouns))
