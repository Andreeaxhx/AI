import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter, defaultdict
from nltk import bigrams, trigrams
import random

def tokenizare(text):
    lst = []
    for i in sent_tokenize(text):
        #print(i)
        lst.append(list(word_tokenize(i)))
    return lst

def converteste_litere_mici(lista_cuvinte):
    final_list=[]

    for lista in lista_cuvinte:
        interm_list=[]
        for cuvant in lista:
            interm_list.append(cuvant.lower())
        final_list.append(interm_list)
        #print(interm_list)
    return final_list

def elimina_semne(cuvant):
    litere=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "ă", "â", "ș", "ț"]
    for litera in cuvant:
        if (litera in litere) or (litera.lower() in litere) or litera=='-':
            pass
        else:
            return -1
    return 1

def elimina_semne_propozitie(lista_cuvinte):
    lista_noua=[]
    for lista in lista_cuvinte:
        lista_interm=[]
        for cuvant in lista:
            if elimina_semne(cuvant)==1:
                lista_interm.append(cuvant)
        #print(lista_interm)
        lista_noua.append(lista_interm)
    return lista_noua

text=''
file=open("alt_text.txt", "r")

for line in file.readlines():
    text+=line

cuvinte=tokenizare(text)
#print(cuvinte)
cuvinte=converteste_litere_mici(cuvinte)
#print(cuvinte)
cuvinte=elimina_semne_propozitie(cuvinte)
#print(cuvinte)
stop_words = list(stopwords.words('romanian'))
#print(cuvinte)
#filtered_sentence = [w for w in cuvinte if not w in stop_words]

filtered_sentence = []
for lista in cuvinte:
    lista_interm=[]
    for cuvant in lista:
        if not cuvant in stop_words:
            lista_interm.append(cuvant)
    filtered_sentence.append(lista_interm)

"""for w in cuvinte:
    if w not in stop_words:
        filtered_sentence.append(w)"""

#print(filtered_sentence)

nr_aparitii={}
#print(propozitii)
#print(cuvinte)
for lista in filtered_sentence:
    for cuvant in lista:
        if cuvant in nr_aparitii:
            nr_aparitii[cuvant]+=1
        else:
            nr_aparitii[cuvant]=1

suma=sum(nr_aparitii.values())
print(suma)
new_dict={}
for key, value in nr_aparitii.items():
    new_dict[key]=(value/suma)*1000000

for key, value in new_dict.items():
    print("% s : % d" % (key, value))

with open('file_alt_text.txt', 'w') as file:
    file.write(json.dumps(new_dict))
#print(stopwords.words('romanian'))

model = defaultdict(lambda: defaultdict(lambda: 0))

# Count frequency of co-occurance
#print(len(filtered_sentence))
for sentence in filtered_sentence:
    for cuv1, cuv2, cuv3 in trigrams(sentence, pad_right=True, pad_left=True):
        model[(cuv1, cuv2)][cuv3] += 1

for cuv12 in model:
    #print(cuv12)
    total_count = float(sum(model[cuv12].values()))
    for cuv3 in model[cuv12]:
        model[cuv12][cuv3] /= total_count

text = [None, None]
sentence_finished = False

while not sentence_finished:
    r = random.random()
    accumulator = .0

    for word in model[tuple(text[-2:])].keys():
        accumulator += model[tuple(text[-2:])][word]
        if accumulator >= r:
            #print(accumulator)
            text.append(word)
            #print(text)
            break

    if text[-2:] == [None, None]:
        sentence_finished = True

print("Trigrams --- ", ' '.join([t for t in text if t]))



#-------------------------------------------------


counts = Counter(nr_aparitii)
total_count = len(nr_aparitii.keys())

for word in counts:
    counts[word] /= float(total_count)

text = []

for _ in range(100):
    r = random.random() #[0, 1)
    accumulator = .0

    for word, freq in nr_aparitii.items():
        accumulator += freq/1000000

        if accumulator >= r:
            text.append(word)
            break

print("Cate un cuvant --- ", ' '.join(text))
