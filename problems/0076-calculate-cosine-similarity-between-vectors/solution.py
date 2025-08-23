
import numpy as np

def cosine_similarity(v1, v2):
	result = 0

    num = sum(v1 * v2)

    aprod = sum([x*x for x in v1])

    bprod = sum([x*x for x in v2])

    denom = np.sqrt(aprod) * np.sqrt(bprod)
    
    result = num/denom
    return round(result,3)