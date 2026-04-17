from nn import NN
from read_mnist_dataset import MnistDataloader
import numpy as np

mnist_dataloader = MnistDataloader('./mnist/train-images.idx3-ubyte', './mnist/train-labels.idx1-ubyte', './mnist/t10k-images.idx3-ubyte', './mnist/t10k-labels.idx1-ubyte')
(x_train, y_train_raw),(x_test, y_test) = mnist_dataloader.load_data()

for i, e in enumerate(x_test):
    x_test[i] = np.array(e).reshape(-1, 784)[0]
    x_test[i] = x_test[i] / 255.0

a = NN(0.01, 784, 2, 128, 10)
a.load('test_784_64_64_10_005_relu')

success = 0
for x, y in zip(x_test, y_test):
    vOutput = a.evaluate(x)
    if np.argmax(vOutput) == y:
        success += 1

n = len(y_test)
print(f"Success: {success}/{n} ({success/n*100}%)")