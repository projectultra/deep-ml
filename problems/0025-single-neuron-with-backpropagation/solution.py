import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	
	def mse(y_true, y_pred):
		err = np.sum((y_true-y_pred)**2)/len(y_true)
		return err

	mse_values = []
	updated_weights = initial_weights
	updated_bias = initial_bias

	for epoch in range(epochs):
		z = (features @ updated_weights) + updated_bias
		preds = 1 / (1 + np.exp(-z))

		mse_values.append(mse(labels, preds))

		err_grad = (preds - labels) *  2 / len(preds) * preds * (1-preds) 

		grad_w = features.T @ err_grad
		updated_weights -= learning_rate * grad_w

		grad_b = np.sum(err_grad)

		updated_bias -= learning_rate * grad_b

	return updated_weights, updated_bias, mse_values