import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	batches = []
	for i in range(0, len(X), batch_size):
		if y is not None:
			batches.append([X[i:i+batch_size],y[i:i+batch_size]])
		else:
			batches.append([X[i:i+batch_size]])
	
	return batches