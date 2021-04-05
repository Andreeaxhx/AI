from lab8 import text_processing
import numpy as np

text = open("text2", encoding="utf8").read()

training_data=text_processing.procesare_text(text) #o lista de liste cuprinzand cuvinte; fiecare sublista reprezinta o propozitie

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


class skip_gram_model(object):
    def __init__(self):
        self.N = 10 #the number of neurons present in the hidden layer.
        self.X_center_word = []
        self.Y_context = []
        self.c = 4 #c = context window is the number of words to be predicted which can occur in the range of the given word.
        self.alpha = 0.001 #learning rate
        self.words = []
        self.words_indexes = {} #dictionar care stocheaza pentru fiecare cuvant un anumit index

    def initialize(self, V, data):
        self.V = V #vocabulary = the dictionary of unique words present in our dataset or text
        self.W=(0.1) * np.random.randn(V, self.N) + (-0.1)
        self.W_prim=(0.1) * np.random.randn(self.N, V) + (-0.1)

        self.words = data
        for i in range(len(data)):
            self.words_indexes[data[i]] = i

    def forward(self, X):
        self.h = np.dot(self.W.T, X).reshape(self.N, 1) # np.dot(self.W, X.T) #X = cuvantul de intrare
        self.u = np.dot(self.W_prim.T, self.h)
        self.y = softmax(self.u)
        return self.y

    def backpropagate(self, x, t):
        e = self.y - np.asarray(t).reshape(self.V, 1) # ej = yj-tj
        #gradient 1
        dLdW_prim = np.dot(self.h, e.T) # dE/dw_prim_ij = hi*ej
        X = np.array(x).reshape(self.V, 1)
        #gradient 2
        dLdW = np.dot(X, np.dot(self.W_prim, e).T) # dE/dw_ij = hi*ej
        self.W_prim = self.W_prim - (self.alpha * dLdW_prim)
        self.W = self.W - (self.alpha * dLdW)

    def train(self, epochs):
        for x in range(1, epochs):
            self.loss = 0
            for j in range(len(self.X_center_word)):
                self.forward(self.X_center_word[j])
                self.backpropagate(self.X_center_word[j], self.Y_context[j])
                C = 0
                for m in range(self.V):
                    if (self.Y_context[j][m]):
                        self.loss += -1 * self.u[m][0]
                        C += 1
                self.loss += C * np.log(np.sum(np.exp(self.u)))
            print(self.loss)
            #self.alpha *= 1 / ((1 + self.alpha * x))

    def predict(self, word, number_of_predictions):
        if word in self.words:
            #one hot encoding
            index = self.words_indexes[word]
            X = [0 for i in range(self.V)]
            X[index] = 1
            prediction = self.forward(X)
            output = {}
            for i in range(self.V):
                output[prediction[i][0]] = i
            #print(output)

            top_context_words = []
            for k in sorted(output, reverse=True):
                top_context_words.append(self.words[output[k]])
                print(k)
                if (len(top_context_words) >= number_of_predictions):
                    break

            return top_context_words
        else:
            print("Cuvantul nu exista in vocabular")

def converting_data(sentences, skip_object):
    data = {}
    #vectorul de frecventa
    for sentence in sentences:
        for word in sentence:
            if word not in data:
                data[word] = 1
            else:
                data[word] += 1
    V = len(data)
    data = sorted(list(data.keys()))
    vocabulary = {}

    for i in range(len(data)):
        vocabulary[data[i]] = i

    print("-----", len(vocabulary))
    #se prezic cuvintele din context
    for sentence in sentences:
        for i in range(len(sentence)):
            #generarea datelor de antrenare: vectori one-hot (pentru cuvantul tinta si cuvintele din context)
            center_word = [0 for x in range(V)]
            center_word[vocabulary[sentence[i]]] = 1
            context = [0 for x in range(V)]

            for j in range(i - int(skip_object.c/2), i + int(skip_object.c/2)): # i - w2v.c, i + w2v.c
                if i != j and j >= 0 and j < len(sentence):
                    context[vocabulary[sentence[j]]] += 1
            skip_object.X_center_word.append(center_word)
            skip_object.Y_context.append(context)
    skip_object.initialize(V, data)
    return skip_object.X_center_word, skip_object.Y_context

epochs = 100
skip_object = skip_gram_model()
converting_data(training_data, skip_object)
skip_object.train(epochs)

"""for i in ["red", "vegetables", "fruits"]:
    print(skip_object.predict(i, 3))"""

print(skip_object.predict("butter", 3))