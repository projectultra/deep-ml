import numpy as np

def make_diagonal(x):
    length = len(x)
    result = np.zeros(shape=((length,length)))
	for i in range (length):
        result[i][i]=x[i]
    return result