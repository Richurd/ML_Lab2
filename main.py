from cvxopt.solvers import qp
from cvxopt.base import matrix
import math, random, numpy, pylab

# Uppgift 3

def linearKernel(vect1, vect2): #Produces K(x,y), which is the dot product of x^T and y + 1 (Linear Kernel)
	vect1 = numpy.transpose(vect1)
	dotProduct = numpy.dot(vect1, vect2)
	return dotProduct + 1

def buildPMatrix(data): #Calculates and returns the matrix P
	i = 0; j = 0; P = []
	for i in range(len(data)): #Go through the rows
		rowVector = []
		point = data[i]
		t1 = point[2]
		x1 = [point[0], point[1]]
		for j in range(len(data)): #Go through the columns
			point = data[j]
			t2 = point[2]
			x2 = [point[0], point[1]]
			newValue = t1 * t2 * linearKernel(x1,x2)
			rowVector.append(newValue)
		P.append(rowVector)
	return P


def buildqGh(N): # Next step
	q = []; G = []; h = []
	for i in range(N):
		q.append(float(-1))
		G = -1*numpy.identity(N, float)
		h.append(float(0))
	return q, G, h




# Uppgift 4

classA = [(random.normalvariate(-1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(5)] + \
	[(random.normalvariate(1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(5)]
classB = [(random.normalvariate(0.0, 0.5), random.normalvariate( -0.5, 0.5 ), -1.0) for i in range(10)]
data = classA + classB
random.shuffle(data)
print(data)

# test
def main():
	data = [(1.,2.,1.), (0.,0.,-1.), (0.9, 2.2, 1), (0., 0.1, -1.), (1.1,2.01,1.), (0.02,0.1,-1.), (0.95, 2.25, 1), (0.03, 0.1, -1.)]
	P = buildPMatrix(data)
	q, G, h = buildqGh(len(data))
	print('\n\n\n', q, '\n\n\n', G,'\n\n\n', h)

	r = qp(matrix(P), matrix(q), matrix(G), matrix(h))
	alpha = list(r['x'])
	print(alpha)


	return


main()