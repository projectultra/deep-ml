def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	r,c = len(dense_matrix),len(dense_matrix[0])
    val = []
    col = [0]
    row = []
    nnz=0
    for j in range(r):
        for i in range(c):
            if dense_matrix[i][j]:
                val.append(dense_matrix[i][j])
                row.append(i)
                nnz+=1

        col.append(nnz)

    return val,row,col
