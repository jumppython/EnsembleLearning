import numpy as np

def clz_to_prob(clz):
	l = sorted(list(set(clz)))
	m = [l.index(c) for c in clz]
	z = np.zeros((len(clz), len(l)))
	for i, j in enumerate(m):
		z[i, j] = 1.0
	return z, list(map(str, l))

def prob_to_clz(prob, cl):
	i = pred.
