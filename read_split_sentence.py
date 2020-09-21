import KoreanNLP as knp
from tqdm import tqdm as tq
import re

F = open('after_news_2020_july_12699.txt', 'r', encoding='utf-8')
F_source = F.readlines()

# for i in range(len(F_source)) :
#     F_source[i] = re.sub('[^\w\s.]','',F_source[i])
#     F_source[i] = re.sub('([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)','',F_source[i])
#     F_source[i] = re.sub('((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*','',F_source[i])

total = []
for i in tq(F_source) :
    total.extend(knp.split_sentence_u(i))

print('len total : ', len(total))

for i in range(len(F_source)) : 
    F_source[i] = F_source[i].strip()
F_source = list(filter(None, F_source))
print(len(F_source))

len_umjual = []
for i in range(len(F_source)) :
    len_umjual.extend(F_source[i])

for i in range(len(len_umjual)) :
    if len_umjual[i] == ' ' :
        len_umjual[i] = ''
len_umjual = list(filter(None, len_umjual))

len_ujual = []
for i in F_source : 
    len_ujual.extend(i.split(' '))

print('len_ujual :', len(len_ujual))

print(len(len_ujual[:10]))

cnt = 0
for i in len_ujual : 
    cnt+=len(i)

print('ujual :', cnt)

print(len_ujual[:10])
len(len_ujual)

len_total = []


# for i in range(len(F_source)) :
#     len_total.extend(F_source[i].strip().replace(' ',''))
# print("total_umjual :",len(len_total))
# print(len_total[:1000])

# for i in total :
#     len_total.append(i)

# print(len(total))

# total_ujual = []
# for i in total : 
#     for j in i :
#         total_ujual.append(len(j.strip().split(' ')))

# print('len_total :', len(len_total))
# print('total_ujual :', sum(total_ujual))

# with open('knp_test.txt', 'w', encoding='utf-8') as F :
#     for i in len_total :
#         F.write("%s\n" %i)
