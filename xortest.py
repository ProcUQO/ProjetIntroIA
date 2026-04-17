import numpy as np
from nn import NN

x_dataset = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_dataset = np.array([[0], [1], [1], [0]])

a = NN(0.1, 2, 1, 2, 1)

a.train(10000, x_dataset, y_dataset)
#a.save(".")

#a = NN(0.1, 2, 1, 2, 1)
#a.load(".")

print(f"Neural network emulating XOR")
print(f"\n0 XOR 0")
print(f"Model prediction: ")
print(f"{a.evaluate(np.array([0, 0]))[0]}")
print(f"\n0 XOR 1")
print(f"Model prediction: ")
print(f"{a.evaluate(np.array([0, 1]))[0]}")
print(f"\n1 XOR 0")
print(f"Model prediction: ")
print(f"{a.evaluate(np.array([1, 0]))[0]}")
print(f"\n1 XOR 1")
print(f"Model prediction: ")
print(f"{a.evaluate(np.array([1, 1]))[0]}")

print("\nA-Layers:")
for e in a.a_layers:
    print(e)

print("\nD-Layers:")
for e in a.d_layers:
    print(e)

print("\nW-Layers:")
for e in a.w_layers:
    print(e)

print("\nB-Layers:")
for e in a.b_layers:
    print(e)