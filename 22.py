from konlpy.tag import Kkma
from tqdm import tqdm as tq
from collections import Counter
import pprint
import re

kkma = Kkma()

print('6')
F = open('after_after_news_nospstr.txt', 'r', encoding='utf-8')
F_source = F.readlines()

for i in range(len(F_source)) :
    F_source[i] = F_source[i].strip()

F_source = list(filter(None, F_source))

print('처리이후 total 문장 :',len(F_source))

# len_nouns = []

# for nouns in tq(F_source) : 
#     ex_nouns = kkma.nouns(nouns)
#     len_nouns.append(len(ex_nouns))

for_umjual = F_source[:]

total_umjual = []
for i in range(len(for_umjual)) :
    for_umjual[i] = for_umjual[i].replace(' ','')
    total_umjual.append(len(for_umjual[i]))

ujual = []
for i in F_source :
    ujual.append(len(i.split(' ')))


print('avg ujual :', sum(ujual)/len(F_source))
print('total_umjual :', sum(total_umjual))
print('avg umjual :', sum(total_umjual)/len(total_umjual))
# print('num of sentence : ',len(after_sentence))
# print('total ujual :', sum(len_nouns))
# print('avg ujual :', sum(len_nouns)/len(len_nouns))

res = []
res.append('total_umjual :' + str(sum(total_umjual)))
res.append('avg umjual  :' + str(sum(total_umjual)/len(total_umjual)))
# res.append('num of sentence :' + str(len(after_sentence)))
# res.append('total ujual  :' + str(sum(len_nouns)))
# res.append('avg ujual :' + str(sum(len_nouns)/len(len_nouns)))

# with open('Result.txt', 'w', encoding='utf-8') as f :
#     for i in res :
#         f.write("%s\n" %i)




