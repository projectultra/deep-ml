import  numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	
	mean_val = np.mean(data, axis = 0)
	var_val = np.var(data, axis= 0)
	minimum = np.min(data, axis= 0)
	maximum = np.max(data, axis= 0)

	standardized_data = (data - mean_val)/np.sqrt(var_val)

	normalized_data = (data - minimum)/(maximum-minimum)

	return standardized_data.tolist(), normalized_data.tolist()