from cvxopt.solvers import qp
from cvxopt.base import matrix
import math, random, numpy, pylab

def linearKernel(vect1, vect2): #Produces K(x,y), which is the dot product of x^T and y + 1 (Linear Kernel)
	return numpy.dot(numpy.transpose(vect1), vect2) + 1

def polynomialKernel(vect1, vect2, p=2):
	return (numpy.dot(numpy.transpose(vect1), vect2) + 1)**p

def radialBasisFunctionKernel(vect1, vect2, sigma=0.01):
	return math.exp(-1*((vect1-vect2)**2/(2*(sigma**2))))

def sigmoidKernel():
	return

def kernel(vect1, vect2):
	#return linearKernel(vect1, vect2)
	#return polynomialKernel(vect1, vect2)
	return radialBasisFunctionKernel(vect1, vect2)
	#return sigmoidKernel(vect1, vect2)

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
			newValue = t1 * t2 * kernel(x1,x2)
			rowVector.append(newValue)
		P.append(rowVector)
	return P

def buildqGh(N): #Returns the correct q, G and h
	q = []; G = []; h = []
	for i in range(N):
		q.append(float(-1))
		G = -1*numpy.identity(N, float)
		h.append(float(0))
	return q, G, h

def getAlpha(P, q, G, h):
	r = qp(matrix(P), matrix(q), matrix(G), matrix(h))
	alpha = list(r['x'])
	return alpha

def saveNonZeroAlpha(alpha, data):
	listOfLargeAlphas = []
	for i in range(len(alpha)):
		if alpha[i] > 10**-5:
			listOfLargeAlphas.append([alpha[i], data[i]])
	return listOfLargeAlphas

def indicator(point, listOfLargeAlphas):
	summa = 0
	for i in range(len(listOfLargeAlphas)):
		lista = listOfLargeAlphas[i]
		#print('\n\nLista: ', lista)
		alpha2 = lista[0]
		#print('\nalpha2: ', alpha2)
		pointForAlpha2 = lista[1] 
		#print('\npointForAlpha2: ', pointForAlpha2)
		ti = pointForAlpha2[2]
		summa += alpha2*ti*kernel(point, [pointForAlpha2[0], pointForAlpha2[1]])
	return summa

def createClasses():
	classA = [(random.normalvariate(-1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(2)] + \
		[(random.normalvariate(1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(2)]
	classB = [(random.normalvariate(0.0, 0.5), random.normalvariate( -0.5, 0.5 ), -1.0) for i in range(4)]
	data = classA + classB
	random.shuffle(data)
	#print(data)
	return data, classA, classB

def plot(classA, classB, listOfLargeAlphas):
	pylab.hold(True)
	pylab.plot([p[0] for p in classA], 
		[p[1] for p in classA], 
		'bo') #Blaa är positiva, 1
	pylab.plot([p[0] for p in classB], 
		[p[1] for p in classB], 
		'ro') #Roeda är negativa, -1
	x_range = numpy.arange(-4, 4, 0.05)
	y_range = numpy.arange(-4, 4, 0.05)
	summa = 0.0
	grid = matrix([[indicator([x, y], listOfLargeAlphas) for y in y_range] for x in x_range])
	pylab.contour(x_range, y_range, grid, (-1.0, 0.0, 1.0), colors = ('red', 'black', 'blue'), 
		linewidths = (1, 3, 1))
	pylab.show()
	return
	
def main():
	data, classA, classB = createClasses()
	P = buildPMatrix(data)
	q, G, h = buildqGh(len(data))
	print('\n\n\n', q, '\n\n\n', G,'\n\n\n', h)
	alpha = getAlpha(P, q, G, h)
	print(alpha)
	listOfLargeAlphas = saveNonZeroAlpha(alpha, data)
	print(listOfLargeAlphas)
	point = [1, 1]
	summa = indicator(point, listOfLargeAlphas)
	plot(classA, classB, listOfLargeAlphas)
	print('Summa: ', summa)
	return

main()