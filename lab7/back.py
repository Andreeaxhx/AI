import numpy as np
X=np.loadtxt("data", usecols=range(4, 2), dtype=int)

function=input("Enter the function: ")
if function=="si":
    y=np.array(([0], [0], [0], [1]), dtype=int)
elif function=="xor":
    y = np.array(([1], [0], [0], [1]), dtype=int)
elif function=="sau":
    y = np.array(([0], [1], [1], [1]), dtype=int)
else:
    print("Invalid function")
    exit()


class NeuralNetwork(object):
    def __init__(self):

        self.alpha=float(input("Enter alpha: "))
        self.w_input_hidden = (0.1) * np.random.randn(2, 2) + (-0.1)
        self.w_hidden_output = (0.1) * np.random.randn(2, 1) + (-0.1)

        self.thetas = (0.1) * np.random.randn(4, 2) + (-0.1)


    def forward(self, X): #3.propagarea inainte
        self.sum=np.dot(X, self.w_input_hidden)-self.thetas
        self.y_j=self.sigmoid(self.sum)

        self.sum=np.dot(self.y_j, self.w_hidden_output)
        y_k=self.sigmoid(self.sum)

        #self.E_max=max(np.sum(np.dot((y-y_k), (y-y_k).T)/2), self.E_max)
        #self.E=np.sum(np.dot((y - y_k), (y - y_k).T) / 2)

        return y_k

    def sigmoid(self, x, deriv=False): #2.functia de activare sigmoida
        if deriv==True:
            return x*(1-x)
        return 1/(1+np.exp(-x))

    def backward(self, X, y, y_k):
        self.error_k=y-y_k
        self.delta_k=self.error_k*self.sigmoid(y_k, deriv=True)

        self.w_hidden_output += (self.alpha * self.y_j.T.dot(self.delta_k))#!!!
        #4.corectia ponderilor pentru stratul de iesire


        self.sum=self.delta_k.dot(self.w_hidden_output.T)
        self.delta_j=self.sum*self.sigmoid(self.y_j, deriv=True)
        #calcularea gradientilor erorilor pentru neuronii din stratul ascuns


        self.w_input_hidden += (self.alpha*X.T.dot(self.delta_j)) #!!!
        #5.corectia ponderilor pentru stratul ascuns

    def train(self, X, y):
        output=self.forward(X)
        self.backward(X, y, output)


NN=NeuralNetwork()
epochs=int(input("Enter number of epochs: "))
for i in range(epochs):
    NN.train(X, y)


print("predicted output: \n", str(NN.forward(X)))