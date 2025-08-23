import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	r,c = len(dense_matrix),len(dense_matrix[0])
    val = []
    col = []
    row = [0]
    nnz=0
    for i in range(c):
        for j in range(r):
            if dense_matrix[i][j]:
                val.append(dense_matrix[i][j])
                col.append(j)
                nnz+=1

        row.append(nnz)


    return val,col,row
