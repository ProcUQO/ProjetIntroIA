import numpy as np
import os

def logistic(x):
    return 1 / (1 + np.exp(-x))

def logistic_derivative(x):
    return x * (1 - x)

def softmax(x):
    e = np.exp(x - np.max(x))
    return e / np.sum(e)

def relu(x):
    return np.maximum(x, 0.0)

def relu_derivative(x):
    return (x > 0) * 1

def get_nn_filenames(folder):
    weights = os.path.join(folder, "weights.npz")
    biases = os.path.join(folder, "biases.npz")
    return weights, biases

def load_np_arrays_from_file(f):
    d = np.load(f)
    return [d[e] for e in d.keys()]

def create_folder_if_not_exists(foldername):
    if not os.path.isdir(foldername):
        os.mkdir(foldername)
