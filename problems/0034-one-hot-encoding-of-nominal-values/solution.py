import numpy as np

def to_categorical(x, n_col=None):
	if n_col is not None:
		ohe = np.zeros((len(x), n_col))
	else:
		ohe = np.zeros((len(x), np.max(x, axis=0)+1))

	for oh,val in zip(ohe,x,strict=True):
		oh[val] = True

	return ohe