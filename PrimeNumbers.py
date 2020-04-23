#!/bin/bash/python3

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

def convertPrimes(boolPrimes):
	primes = []
	for i in range(len(boolPrimes)):
		if boolPrimes[i]:
			primes.append(i + 1)
	return primes
