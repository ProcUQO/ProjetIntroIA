from utils import logistic, logistic_derivative, softmax, relu, relu_derivative, get_nn_filenames, load_np_arrays_from_file
import numpy as np

# The transitions t going from the nth neuron on the left are at the nth row (a[n, tx])
# The transitions t going to the nth neuron on the right are at the nth column (a[tx, n])
# j0 -> k2 : a[0, 2]
# >>> a[0, 2] += 1.4
# array([[0. , 0. , 1.4, 0. , 0. ],
#        [0. , 0. , 0. , 0. , 0. ],
#        [0. , 0. , 0. , 0. , 0. ]])

class NN:
    alpha: float
    a_layers: list[np.array]
    d_layers: list[np.array]

    w_layers: list[np.array]
    b_layers: list[np.array]

    def add_layer(self, numNeurons):
        self.a_layers.append(np.array([0.0] * numNeurons, dtype=np.float64))
        self.d_layers.append(np.array([0.0] * numNeurons, dtype=np.float64))

    def init_layers(self, numInputNeurons, numHiddenLayers, numHiddenLayerNeurons, numOutputNeurons):
        self.add_layer(numInputNeurons)

        for i in range(numHiddenLayers):
            self.add_layer(numHiddenLayerNeurons)

        self.add_layer(numOutputNeurons)

    def create_weight(numNeuronsLeftLayer, numNeuronsRightLayer):
        return np.random.rand(numNeuronsLeftLayer, numNeuronsRightLayer) - 0.5
    
    def create_bias(numNeuronsRightLayer):
        return np.random.rand(numNeuronsRightLayer) - 0.5

    def init_transitions(self):
        for q, r in zip(self.a_layers, self.a_layers[1:]):
            self.w_layers.append(NN.create_weight(len(q), len(r)))
            self.b_layers.append(NN.create_bias(len(r)))

    def __init__(self, learningRate, numInputNeurons, numHiddenLayers, numHiddenLayerNeurons, numOutputNeurons):
        self.alpha = learningRate
        self.a_layers = []
        self.d_layers = []
        self.w_layers = []
        self.b_layers = []

        self.init_layers(numInputNeurons, numHiddenLayers, numHiddenLayerNeurons, numOutputNeurons)
        self.init_transitions()

    def fwdprop(self, vInputA: np.array):
        # Initialize input layer with given input vector
        self.a_layers[0] = vInputA

        # Calc a layer
        for i, w_layer in enumerate(self.w_layers[:-1]):
            self.a_layers[i+1] = logistic(np.dot(self.a_layers[i], w_layer) + self.b_layers[i])
        self.a_layers[-1] = softmax(np.dot(self.a_layers[-2], self.w_layers[-1]) + self.b_layers[-1])

    def backprop(self, vOutputY: np.array):
        # Initialize output layer deltas
        a = self.a_layers[-1]
        self.d_layers[-1] = (vOutputY - a)

        # Calc delta layer
        for i in range(len(self.w_layers) - 1, -1, -1): # iterating backwards (we ball tho)
            w_layer = self.w_layers[i]

            num_neurons_left = w_layer.shape[0]
            for j in range(num_neurons_left):
                aj = self.a_layers[i][j]
                self.d_layers[i][j] = logistic_derivative(aj) * np.dot(self.d_layers[i+1], w_layer[j, :])

        # Update weights
        for i, w_layer in enumerate(self.w_layers):
            num_neurons_left = w_layer.shape[0]
            for j in range(num_neurons_left):
                self.w_layers[i][j, :] += self.alpha * self.a_layers[i][j] * self.d_layers[i+1]
            self.b_layers[i] += self.alpha * self.d_layers[i+1]
    
    def show_progress(i, successes, total):
        if total != 0:
            percentage = successes / total * 100
            s = f'{successes}/{total} ({percentage}%)'
        else:
            s = f'{total}'
        print(f"Epoch {i}: {s}")

    def train(self, epochs, x_dataset, y_dataset):
        for i in range(epochs):
            j = 0
            successes = 0
            for x, y in zip(x_dataset, y_dataset):
                if (j % 10000) == 0:
                    self.show_progress(i, successes, j)
                
                self.fwdprop(x)

                yhat = self.a_layers[-1]
                if (np.argmax(yhat) == np.argmax(y)):
                    successes += 1
                
                self.backprop(y)
                j += 1
    
    def evaluate(self, vInputA: np.array):
        self.fwdprop(vInputA)
        return self.a_layers[-1]

    def save(self, folder):
        weights, biases = get_nn_filenames(folder)
        np.savez(weights, *self.w_layers, allow_pickle=False)
        np.savez(biases, *self.b_layers, allow_pickle=False)
    
    def load(self, folder):
        weights, biases = get_nn_filenames(folder)
        self.w_layers = load_np_arrays_from_file(weights)
        self.b_layers = load_np_arrays_from_file(biases)

if __name__ == '__main__':
    pass
