from konlpy.tag import Kkma
from tqdm import tqdm as tq

kkma = Kkma()

F = open("news_2020_july_12699.txt",'r+', encoding='utf-8')
F_list = F.readlines()

len_nouns = []

for nouns in tq(F_list) : 
    ex_nouns = kkma.nouns(nouns)
    len_nouns.append(len(ex_nouns))


print('min :', min(len_nouns))
print('max :', max(len_nouns))
print('avg :', sum(len_nouns)/len(len_nouns))
print('total :', sum(len_nouns))
