import numpy as np

def accuracy_score(y_true, y_pred):
	acc_count = 0
	for pred,true in zip(y_pred, y_true, strict=True):
		if pred == true:
			acc_count+=1

	return acc_count/len(y_true)