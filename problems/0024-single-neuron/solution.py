import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	probabilities = []
	error = 0
	for feature,label in zip(features,labels, strict=True):
		tot = 0
		for i in range(len(feature)):
			tot += weights[i] * feature[i]
		tot += bias
		probability = np.round((1/ (1 + np.exp(-tot))), 4)
		error += np.power(label - probability, 2)
		probabilities.append(probability)

	mse = error / len(labels)

	return probabilities, mse