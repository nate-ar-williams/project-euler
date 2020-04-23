#!/bin/bash/python3

import math
import sys

def getPrimes(max):
	primes = [True] * max
	primes[0] = False
	lastPrime = 2
	# max is len(primes)
	while lastPrime < max:
		for composite in range(lastPrime * lastPrime, max + 1, lastPrime):
			primes[composite - 1] = False
		lastPrime += 1
		while primes[lastPrime - 1] == False and lastPrime < max:
			lastPrime += 1
	return primes

def getNthPrime(n):
	# estimate one prime for every 10 numbers .. wild guess, trying to be conservative
	primes = [True] * n * 25
	primes[0] = False
	lastPrime = 2
	length = len(primes)
	numPrimes = 1
	while lastPrime < length and numPrimes < n:
		for composite in range(lastPrime * lastPrime, length + 1, lastPrime):
			primes[composite - 1] = False
		lastPrime += 1
		while primes[lastPrime - 1] == False and lastPrime < length:
			lastPrime += 1
		numPrimes += 1
		if numPrimes == n:
			return lastPrime
	print('uh oh, lastPrime: ' + str(lastPrime))
	print(primes)

def convertPrimes(boolPrimes):
	primes = []
	for i in range(len(boolPrimes)):
		if boolPrimes[i]:
			primes.append(i + 1)
	return primes

# returns dict prime -> numFactors
def getPrimeFactors(x):
	primeFactors = {}
	max = x
	primes = convertPrimes(getPrimes(max))
	factoredX = x
	for prime in primes:
		while factoredX % prime == 0:
			factoredX = factoredX // prime
			if prime not in primeFactors:
				primeFactors[prime] = 1
			else:
				primeFactors[prime] += 1
	return primeFactors

def main():
	for arg in sys.argv[1::]:
		n = int(arg)
		product = 1
		allPrimeFactors = {}
		for i in range(n):
			i += 1
			primeFactors = getPrimeFactors(i)
			for key in primeFactors.keys():
				if key not in allPrimeFactors or allPrimeFactors[key] < primeFactors[key]:
					allPrimeFactors[key] = primeFactors[key]

		for primeFactor in allPrimeFactors.items():
			product *= int(math.pow(primeFactor[0], primeFactor[1]))
		print(product)

if __name__ == '__main__':
	main()
