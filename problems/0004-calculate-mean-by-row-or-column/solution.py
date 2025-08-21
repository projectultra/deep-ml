def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means=[]
	if mode == "row":
        for i in range(len(matrix)):
            means.append(sum(matrix[i])/len(matrix[0]))
    else:
        for i in range(len(matrix)):
            sums=0
            for j in range(len(matrix[0])):
                sums += matrix[j][i]

            means.append(sums/len(matrix))
            # print("row", means)

    return means