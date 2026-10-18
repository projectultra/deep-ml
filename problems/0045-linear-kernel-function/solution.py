import numpy as np

def kernel_function(x1, x2):

	result = 0
	for x,y in zip(x1,x2,strict=True):
		result += x * y
	return  result