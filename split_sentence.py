import KoreanNLP as knp
from tqdm import tqdm as tq
import re

F = open('after_news_2020_july_12699.txt', 'r', encoding='utf-8')
F_source = F.readlines()

for i in range(len(F_source)) :
    F_source[i] = re.sub('[^\w\s.]','',F_source[i])
    F_source[i] = re.sub('([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)','',F_source[i])
    F_source[i] = re.sub('((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*','',F_source[i])

total = []
for i in tq(F_source) :
    total.extend(knp.split_sentence_u(i))

len_total = []

# for i in range(len(total)) :
#     len_total.extend(total[i].strip().replace(' ',''))
# print(len(len_total))

for i in total :
    len_total.append(i)

print(len(total))

total_umjual = []
for i in total : 
    for j in i :
        total_umjual.extend(j.strip().split(' '))

print(total_umjual[:10])
total_umjual = list(filter(None, total_umjual))
print(total_umjual[:10])
print('total_umjual :', len(total_umjual))
# print('total_ujual :', sum(total_ujual))
# print('total_umjual :', sum(total_umjual))

# with open('knp_test.txt', 'w', encoding='utf-8') as F :
#     for i in len_total :
#         F.write("%s\n" %i)
