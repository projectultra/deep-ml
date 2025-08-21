import math

def softmax(scores: list[float]) -> list[float]:
    probabilities = []
    for i in range(len(scores)):
    	probabilities.append(math.exp(scores[i])/sum([math.exp(x) for x in scores]))
	return probabilities