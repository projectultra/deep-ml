def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:

    lena = len(a) 
    # 2

    lenb = len(a[0])
    # 3

    b = [[0] * lena for _ in range(lenb)]

    for i in range(lena):
        for j in range(lenb):
            b[j][i] = a[i][j]
	return b