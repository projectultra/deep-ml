import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	softmax_probs = []
	for score in scores:
		softmax_probs.append(np.log(np.exp(score)/np.sum(np.exp(scores), axis=0)))
	return  softmax_probs