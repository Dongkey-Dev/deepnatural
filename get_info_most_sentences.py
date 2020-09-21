from konlpy.tag import Kkma
from tqdm import tqdm as tq
from collections import Counter
import pprint
import re

kkma = Kkma()

pp = pprint.PrettyPrinter(indent = 4)
F = open("news_2020_july_12699.txt",'r+', encoding='utf-8')
F_list = F.readlines()
F = open('rm_element.txt','r', encoding='utf-8')
rm_list = F.readlines()

for i in range(len(rm_list)) :
    if rm_list[i][-1:] == '\n' :
        rm_list[i] = rm_list[i][:-1]

res = { i:0 for i in rm_list }

for i in range(len(F_list)) :
    for j in range(len(rm_list)) :
        if rm_list[j] in F_list[i] :
            F_list[i] = F_list[i].replace(rm_list[j], '')
            res[rm_list[j]]+=1

pp.pprint(res)

all_sentence = []
article_sentence = []
print('1단계 mundan for loop')
for mundan in tq(F_list) : 
    article = []
    ex_sent = kkma.sentences(mundan)
    all_sentence.extend(ex_sent)
    article.extend(ex_sent)
    article_sentence.append(article)

# cnt = Counter(all_sentence)

# with open('most_common.txt', 'w', encoding='utf-8') as f :
#     for item in cnt.most_common(37) :
#         f.write("%s\n" %item[0])

# rm_sentence_list = set()
# for i in cnt.most_common(37) :
#     rm_sentence_list.add(i[0])

# F =  open('most_common.txt', 'r', encoding='utf-8')
# f_rm_sentence = F.readlines()

# for i in range(len(f_rm_sentence)) : 
#     if f_rm_sentence[i][:2] == '\n' :
#         f_rm_sentence[i] = f_rm_sentence[i][:-2]


# after_sentence = [ x for x in sentence if x not in rm_sentence_list ]
print('1')
after_article_sentence = []
after_sentence = []
for sentences in article_sentence :
    after_sentences = []
    for sentence in sentences : 
        if sentence not in rm_list : 
            after_sentences.append(sentence)
            after_sentence.append(sentence)
    after_article_sentence.append(after_sentences)

print('2')
for i in range(len(after_sentence)) :
    after_sentence[i] = re.sub('[^\w\s]', '', after_sentence[i])
    if len(after_sentence[i]) == 1 or len(after_sentence[i]) == 2 : 
        after_sentence[i] = ''
after_sentence = list(filter(None, after_sentence))
with open('after_news_nospstr.txt', 'w', encoding='utf-8') as f :        
    for i in range(len(after_sentence)) :
        f.write("%s\n" %after_sentence[i])

print('3')
for i in range(len(after_article_sentence)) :
    after_article_sentence[i] = ' '.join(after_article_sentence[i])
    after_article_sentence[i] = re.sub('[^\w\s]', '', after_article_sentence[i])
    if len(after_article_sentence[i]) == 1 : 
        after_article_sentence[i] = ''    
after_article_sentence = list(filter(None, after_article_sentence))
with open('after_news_article_nospstr.txt', 'w', encoding='utf-8') as f :
    for i in range(len(after_article_sentence)) :
        f.write("%s\n" %after_article_sentence[i])

print('4')
with open('after_news.txt', 'w', encoding='utf-8') as f :
    for item in after_sentence :
        f.write("%s\n" %item)

print('5')
with open('after_news_article.txt', 'w', encoding='utf-8') as f :
    for i in range(len(after_article_sentence)) :
        after_article_sentence[i] = ' '.join(after_article_sentence[i])
        f.write("%s\n" %after_article_sentence[i])

print('6')
F = open('after_after_news_nospstr.txt', 'r', encoding='utf-8')
F_source = F.readlines()

F_source = list(filter(None, F_source))

print('처리이후 total 문장 :',len(F_source), '처리이전 total 문장:',len(all_sentence))

len_nouns = []

for nouns in tq(F_source) : 
    ex_nouns = kkma.nouns(nouns)
    len_nouns.append(len(ex_nouns))

total_umjual = [ len(x) for x in after_sentence ]
print('total_umjual :', sum(total_umjual))
print('avg umjual :', sum(total_umjual)/len(total_umjual))
print('num of sentence : ',len(after_sentence))
print('total ujual :', sum(len_nouns))
print('avg ujual :', sum(len_nouns)/len(len_nouns))

res = []
res.append('total_umjual :' + str(sum(total_umjual)))
res.append('avg umjual  :' + str(sum(total_umjual)/len(total_umjual)))
res.append('num of sentence :' + str(len(after_sentence)))
res.append('total ujual  :' + str(sum(len_nouns)))
res.append('avg ujual :' + str(sum(len_nouns)/len(len_nouns)))

with open('Result.txt', 'w', encoding='utf-8') as f :
    for i in res :
        f.write("%s\n" %i)




