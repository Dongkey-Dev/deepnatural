from konlpy.tag import Kkma
from tqdm import tqdm as tq
from collections import Counter
import pprint
import re

kkma = Kkma()

F = open('news_2020_july_12699.txt', 'r', encoding='utf-8')
F_source = F.readlines()

for i in range(len(F_source)) :
    F_source[i] = re.sub('[^\w\s.]','',F_source[i])
    F_source[i] = re.sub('([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)','',F_source[i])
    F_source[i] = re.sub('((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*','',F_source[i])


F = open('rm_list.txt', 'r', encoding='utf-8')
rm_list = F.readlines()

for i in range(len(rm_list)):
    if rm_list[i][-1:] == '\n' :
        rm_list[i] = rm_list[i][:-1] 

for i in range(len(F_source)) :
    for j in range(len(rm_list)) : 
        if rm_list[j] in F_source[i] :
            F_source[i] = F_source[i].replace(rm_list[j], '')

with open('result_last.txt', 'w', encoding='utf-8') as f :
    for i in F_source :
        f.write("%s" %i)

# for i in range(len(F_source)) :
#     F_source[i] = F_source[i].strip()

# total_ujual = []
# for i in F_source : 
#     total_ujual.append(i.strip().split(' '))



# print('처리이후 total 문장 :',len(F_source))

# # len_nouns = []

# # for nouns in tq(F_source) : 
# #     ex_nouns = kkma.nouns(nouns)
# #     len_nouns.append(len(ex_nouns))

# for_umjual = F_source[:]

# total_umjual = []
# for i in range(len(for_umjual)) :
#     for_umjual[i] = for_umjual[i].replace(' ','')
#     total_umjual.append(len(for_umjual[i]))
    
# print(total_umjual)

# ujual = []
# for i in F_source :
#     ujual.append(len(i.split(' ')))


# print('avg ujual :', sum(ujual)/len(F_source))
# print('total_umjual :', sum(total_umjual))
# print('avg umjual :', sum(total_umjual)/len(total_umjual))
# # print('num of sentence : ',len(after_sentence))
# # print('total ujual :', sum(len_nouns))
# # print('avg ujual :', sum(len_nouns)/len(len_nouns))

# res = []
# res.append('total_umjual :' + str(sum(total_umjual)))
# res.append('avg umjual  :' + str(sum(total_umjual)/len(total_umjual)))
# # res.append('num of sentence :' + str(len(after_sentence)))
# # res.append('total ujual  :' + str(sum(len_nouns)))
# # res.append('avg ujual :' + str(sum(len_nouns)/len(len_nouns)))

# # with open('Result.txt', 'w', encoding='utf-8') as f :
# #     for i in res :
# #         f.write("%s\n" %i)




