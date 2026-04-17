from nn import NN
from read_mnist_dataset import MnistDataloader
from utils import create_folder_if_not_exists
import numpy as np
import sys

try:
    autosave_folder = sys.argv[1]
except IndexError:
    autosave_folder = 'autosave'

create_folder_if_not_exists(autosave_folder)

load_from_backup = False
try:
    backup_folder = sys.argv[2]
    load_from_backup = True
    create_folder_if_not_exists(backup_folder)
except IndexError:
    pass

output_folder = 'mnist_model'
create_folder_if_not_exists(output_folder)

mnist_dataloader = MnistDataloader('./mnist/train-images.idx3-ubyte', './mnist/train-labels.idx1-ubyte', './mnist/t10k-images.idx3-ubyte', './mnist/t10k-labels.idx1-ubyte')
(x_train, y_train_raw),(x_test, y_test) = mnist_dataloader.load_data()

for i, e in enumerate(x_train):
    x_train[i] = np.array(e).reshape(-1, 784)[0]
    x_train[i] = x_train[i] / 255.0

y_train = []
for i, e in enumerate(y_train_raw):
    pre = [0 for _ in range(e)]
    post = [0 for _ in range(e+1, 10)]
    a = [*pre, 1, *post]
    y_train.append(np.array(a))

a = NN(0.01, 784, 2, 128, 10)
if load_from_backup:
    a.load(backup_folder)

try:
    a.train(32, x_train, y_train)
except KeyboardInterrupt:
    a.save(autosave_folder)
else:
    a.save(output_folder)
