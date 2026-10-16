def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:

	rows = len(vectors)
	cols = len(vectors[0])
	cov = [[0.0 for _ in range(rows)] for _ in range(rows)]
	for i in range(rows):
		vec_i = vectors[i]
		i_mean = sum(vec_i) / cols

		for j in range(rows):
			x_sum = 0
			vec_j = vectors[j]
			j_mean = sum(vec_j) / rows
			for n in range(cols):
				x_sum += (vectors[i][n] - i_mean) * (vectors[j][n] - j_mean)

			denom = cols - 1 if cols > 1 else 1
			cov[i][j] = (x_sum / denom)

	return cov