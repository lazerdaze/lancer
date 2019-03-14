# Python Modules
import math


def setRange(value, oldMin, oldMax, newMin, newMax):
	value = float(value)
	oldMin = float(oldMin)
	oldMax = float(oldMax)
	newMin = float(newMin)
	newMax = float(newMax)
	return newMin + (((value - oldMin) / (oldMax - oldMin)) * (newMax - newMin))


def percentage(value, min, max):
	return setRange(value, min, max, 0, 1) * 100


def blendWeighted(inputA, weightA, inputB, weightB):
	'''
	Performs a weighted sum of its inputs to compute the output.
	output = input(0) * weight(0) + input(1) * weight(1) + ...
	:return: float
	'''
	return (inputA * weightA) + (inputB * weightB)


def simpleBlend(*args):
	'''
	Performs a simple addition of numeric values.

	:param args float, int, list, tuple, dict
	:return float
	'''

	output = 0.0

	for arg in args:
		if isinstance(arg, (list, tuple, dict)):
			for item in arg:
				output += float(item)
		else:
			output += float(arg)
	return output


def unitConversion(value):
	'''
	Converts a linear value to be applied on rotations in degrees dependant on world units.
	When translate is 1 cm rotateX is 1 degree.

	:return float:
	'''

	return float(value) * 0.017


def matrixAsArray(matrix):
	array = []
	for i in range(16):
		array.append(matrix[i])
	return array


def addMatrix(*args):
	result = 0.0
	return result


def multiplyMatrix(*args):
	result = 0.0
	return result


def decomposeMatrix(matrix):
	result = 0.0
	return result
