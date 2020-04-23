#!/usr/bin/python3

import math
import sys

def sumSeries(x):
	return int((x + 1) * x / 2)

def squareOfSum(x):
	sumOfSeries = sumSeries(x)
	return sumOfSeries * sumOfSeries

def sumOfSquares(x):
	sumSquares = 0
	for i in range(x):
		sumSquares += (i + 1) * (i + 1)
	return sumSquares

def main():
	for arg in sys.argv[1::]:
		x = int(arg)
		#print(sumOfSquares(x))
		square = squareOfSum(x)
		sum = sumOfSquares(x)
		print(square - sum)

if __name__ == '__main__':
	main()
