import numpy as np

data = np.genfromtxt(r"C:\Users\navee\Downloads\Transactions.xlsx", delimiter=',', skip_header=1, dtype=str)

X = np.column_stack((data[:, 1:4].astype(float), data[:, 4].astype(float)))
y = (data[:, -1] == 'Yes').astype(int)

X = np.hstack((np.ones((X.shape[0], 1)), X))

weights = np.zeros(X.shape[1])
learning_rate = 0.1

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def train_perceptron(X, y, weights, learning_rate, num_epochs):
    for epoch in range(num_epochs):
        y_pred = sigmoid(np.dot(X, weights))
        error = y - y_pred
        weights += learning_rate * np.dot(X.T, error)
    return weights

num_epochs = 1000
final_weights = train_perceptron(X, y, weights, learning_rate, num_epochs)

y_pred = sigmoid(np.dot(X, final_weights))
y_pred = (y_pred >= 0.5).astype(int)
accuracy = np.mean(y_pred == y)
print(f"Training accuracy: {accuracy * 100:.2f}%")

print("Final weights:")
print(final_weights)