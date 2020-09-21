from konlpy.tag import Kkma
from tqdm import tqdm as tq

kkma = Kkma()

F = open("news_2020_july_12699.txt",'r+', encoding='utf-8')
F_list = F.readlines()

len_sentence = []

for i in tq(F_list) :
    len_sentence.append(len(i))

# for mundan in tq(F_list) : 
#     ex_sent = kkma.sentences(mundan)
#     len_sentence.append(len(ex_sent))

print('min :', min(len_sentence))
print('max :', max(len_sentence))
print('avg :', sum(len_sentence)/len(len_sentence))
print('total :', sum(len_sentence))
