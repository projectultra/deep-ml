import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
	"""
	Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

	Args:
		data (list[float]): A list of numerical values to transform.
		degree (int): The degree of the polynomial expansion.

	"""
    result = []
	for d in data:
        temp =[]
        for i in range(degree+1):
            temp.append(pow(d,i))
        result.append(temp)
    return result