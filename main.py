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
		x1 = point[0]
		for j in range(len(data)): #Go through the columns
			point = data[j]
			t2 = point[2]
			x2 = point[1]
			newValue = t1 * t2 * linearKernel(x1,x2)
			rowVector.append(newValue)
		P.append(rowVector)
	return P


def buildqGh(): # Next step
	pass


# Uppgift 4

classA = [(random.normalvariate(-1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(5)] + \
	[(random.normalvariate(1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(5)]
classB = [(random.normalvariate(0.0, 0.5), random.normalvariate( -0.5, 0.5 ), -1.0) for i in range(10)]
data = classA + classB
random.shuffle(data)


# test

#P = buildPMatrix(data)
P = buildPMatrix([(2,5,1),(3,4,-1)])
print(P)