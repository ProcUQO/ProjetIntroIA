from nn import NN
import numpy as np

a = NN(0.1, 2, 2, 2, 1)
a.transition_layers[0][0, 0] = 0.5
a.transition_layers[0][0, 1] = -1.0
a.transition_layers[0][1, 0] = 1.5
a.transition_layers[0][1, 1] = -2.0
a.transition_layers[1][0, 0] = 1.0
a.transition_layers[1][0, 1] = -1.0
a.transition_layers[1][1, 0] = 3.0
a.transition_layers[1][1, 1] = -4.0
a.transition_layers[2][0, 0] = 1.0
a.transition_layers[2][1, 0] = -3.0
a.fwdprop(np.array([2, -1]))
a.backprop(np.array([1]))

print("\nA-Layers:")
for e in a.a_layers:
    print(e)

print("\nD-Layers:")
for e in a.d_layers:
    print(e)

print("\nTransition Layers:")
for e in a.transition_layers:
    print(e)