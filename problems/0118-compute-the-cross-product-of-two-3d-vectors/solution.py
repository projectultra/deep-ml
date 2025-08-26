import numpy as np

def cross_product(a, b):
    result = []
    result.append(a[1]*b[2] - a[2]*b[1])
    result.append(a[2]*b[0] - a[0]*b[2])
    result.append(a[0]*b[1] - a[1]*b[0])
 
    return result