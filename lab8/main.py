from nltk.tokenize import word_tokenize, sent_tokenize
import numpy as np


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

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


text = open("text2", encoding="utf8").read()

sentences=sentence_split(text)
list_of_lists_of_words=tokenization(sentences)
list_of_lists_of_words=lower_case(list_of_lists_of_words)
list_of_lists_of_words=elimina_stopwords(list_of_lists_of_words)

#print(list_of_lists_of_words)

words_indexes={}
data={}
for list_sentence in list_of_lists_of_words:
    for word in list_sentence:
        if word not in data:
            data[word] = 1
        else:
            data[word] += 1
V=len(data)
#print(V)
#print(data)
data = sorted(list(data.keys())) #toate cuvintele din text, luate o singura data, in ordine alfabetica
#print(data)
N=10
window_size=2
X_train=[]
y_train=[]
alpha=0.001

#matricele cu ponderi, initializate cu valori intre -0.1, 0.1
W=(0.1) * np.random.randn(V, N) + (-0.1)
W_prim=(0.1) * np.random.randn(N, V) + (-0.1)

vocab = {}
for i in range(len(data)):
    vocab[data[i]] = i

for sentence in list_of_lists_of_words:
    for i in range(len(sentence)):
        center_word = [0 for x in range(V)]
        center_word[vocab[sentence[i]]] = 1
        context = [0 for x in range(V)]

        #print(center_word)
        #print(context)
        for j in range(i - window_size, i + window_size):
            if i != j and j >= 0 and j < len(sentence):
                context[vocab[sentence[j]]] += 1
                #print(context)

        X_train.append(center_word)
        y_train.append(context)

def forward(cuvant):
    h = np.dot(W.T, cuvant).reshape(N, 1) #np.dot(W, X.Y)
    u = np.dot(W_prim.T, h)
    # print(self.u)
    y = softmax(u)
    return h, u, y

def backpropagate(x, t, cuvant, W, W_prim):
    h, u, y = forward(cuvant)
    e = y - np.asarray(t).reshape(V, 1) # ej = yj-tj
    # e.shape is V x 1
    dLdW_prim = np.dot(h, e.T) # dE/dw_prim_ij = hi*ej
    X = np.array(x).reshape(V, 1)
    dLdW = np.dot(X, np.dot(W_prim, e).T) # dE/dw_ij = hi*ej
    W_prim = W_prim - alpha * dLdW_prim
    W = W - alpha * dLdW

def training(no_of_epochs, alpha):
    for x in range(no_of_epochs):
        loss=0
        for j in range(len(X_train)):
            h, u, y = forward(X_train[j])
            backpropagate(X_train[j], y_train[j])
            c=0
            for m in range(V):
                if(y_train[j][m]):
                    loss+=-1*u[m][0]
                    c+=1
                loss+=c*np.log(np.sum(np.exp(u)))
            print("epoch ", x, " loss= ", loss)
            alpha *= 1 / ((1 + alpha * x))

def predict(word, number_of_predictions, words, words_indexes):
    if word in words:
        index = words_indexes[word]
        X = [0 for i in range(V)]
        X[index] = 1
        prediction = forward(X)
        output = {}
        for i in range(V):
            output[prediction[i][0]] = i

        top_context_words = []
        for k in sorted(output, reverse=True):
            top_context_words.append(words[output[k]])
            if (len(top_context_words) >= number_of_predictions):
                break

        return X, top_context_words
    else:
        print("Word not found in dicitonary")


#print(len(x_train))
#print(len(y_train))
#print(data)

#print(vocab)
no_of_epochs=100
training_data=list_of_lists_of_words
training(no_of_epochs, alpha)
X, lista=predict("fruit", 3, training_data, words_indexes)
