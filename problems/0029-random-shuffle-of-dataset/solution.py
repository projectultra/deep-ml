import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
	n = len(y)
	np.random.seed(seed)
	shuffled_indices = np.random.permutation(n)

	return X[shuffled_indices], y[shuffled_indices]