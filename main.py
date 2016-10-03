from cvxopt.solvers import qp
from cvxopt.base import matrix
import math, random, numpy, pylab


def linearKernel(vect1, vect2): #Produces K(x,y), which is the dot product of x^T and y + 1 (Linear Kernel)
	vect1 = numpy.transpose(vect1)
	dotProduct = numpy.dot(vect1, vect2)
	return dotProduct + 1

def buildPMatrix(nrOfDataPoints):
	i = 0; j = 0
	for i in range(nrOfDataPoints): #Go through the rows
		for j in range(nrOfDataPoints): #Go through the columns

		print(i)
	p = 1
	return p


classA = [(random.normalvariate(-1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(5)] + \
	[(random.normalvariate(1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(5)]
classB = [(random.normalvariate(0.0, 0.5), random.normalvariate( -0.5, 0.5 ), -1.0) for i in range(10)]
data = classA + classB
random.shuffle(data)

buildPMatrix(20)
#print(data)