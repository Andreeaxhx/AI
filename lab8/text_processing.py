from nltk.tokenize import word_tokenize, sent_tokenize

def elimina_semne(cuvant):
    litere=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for litera in cuvant:
        if (litera in litere) or (litera.lower() in litere):
            pass
        else:
            return -1
    return 1

#impartirea in propozitii
def sentence_split(text):
    return sent_tokenize(text)

#tokenizarea
def tokenization(sentence_list):
    final_list=[]
    for sentence in sentence_list:
        lista=word_tokenize(sentence)
        lista_interm=[]
        for cuvant in lista:
            if elimina_semne(cuvant)==1:
                lista_interm.append(cuvant)
        if lista_interm:
            final_list.append(lista_interm)
    return final_list

#convertirea la litere mici
def lower_case(sentence_list):
    final_list=[]
    for lista in sentence_list:
        final_list.append([x.lower() for x in lista])
    return final_list

#eliminarea stopwords
def elimina_stopwords(lista_cuvinte):
    lista_finala=[]
    stopwords=open("stopwords.txt").read()
    for lista in lista_cuvinte:
        lista_interm=[word for word in lista if word not in stopwords]
        lista_finala.append(lista_interm)
    return lista_finala

def procesare_text(text):

    sentences=sentence_split(text)
    list_of_lists_of_words=tokenization(sentences)
    list_of_lists_of_words=lower_case(list_of_lists_of_words)
    list_of_lists_of_words=elimina_stopwords(list_of_lists_of_words)

    return list_of_lists_of_words