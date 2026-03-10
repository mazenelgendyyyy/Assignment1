import numpy as np

np.random.seed(42)

W1 = np.random.uniform(-0.5, 0.5, (2, 2))
W2 = np.random.uniform(-0.5, 0.5, (1, 2))
b1 = 0.5
b2 = 0.7

def tanh(x):
    return np.tanh(x)

x = np.array([0.6, -0.2])

z1 = np.dot(W1, x) + b1
a1 = tanh(z1)

z2 = np.dot(W2, a1) + b2
output = tanh(z2)

print(output)