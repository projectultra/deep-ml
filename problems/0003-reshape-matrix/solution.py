def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    rows, cols = len(a), len(a[0])
    total_elements = rows * cols

    # Check if reshape is possible
    if new_shape[0] * new_shape[1] != total_elements:
        return []

    # Flatten the original matrix row-wise
    flat = [elem for row in a for elem in row]

    # Build reshaped matrix
    reshaped_matrix = [
        flat[i * new_shape[1]:(i + 1) * new_shape[1]] 
        for i in range(new_shape[0])
    ]

    return reshaped_matrix

