def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if len(a[0]) != len(b):
        return -1
    else:
        result = []
        for vala in a:
            suma=0
            for val,valb in zip(vala,b):
                # print(val,valb,"xx")
                suma += val * valb
            result.append(suma)
        return result

