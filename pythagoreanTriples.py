#!/bin/bash/python3

import math
import PrimeNumbers as primes

# m > n > 0
def generateTriple(m, n):
	a = m * m - n * n
	b = 2 * m * n
	c = int(math.sqrt(a * a + b * b))
	return a, b, c

# m and n are coprime, not both odd, m < n
def generateNs(m):
	start = 1
	increment = 1
	# skip odds if m is odd
	if m % 2 == 1:
		start = 2
		increment = 2
	ns = [n for n in range(start, m, increment) if gcd(n, m) == 1]
	return ns

# use euclid's algorithm to find gcd
def gcd(n, m):
	while n > 0 and m > 0:
		if n > m:
			n = n % m
		else:
			m = m % n
	return max(n, m)

def main():
	target = 1000
	sum = 0
	m = 0
	a = b = c = 0
	while sum != target:
		m += 1
		ns = generateNs(m)
		for n in ns:
			a, b, c = generateTriple(m, n)
			sum = a + b + c
			#if sum >= target:
				#break
			if target % sum == 0:
				multiplier = target // sum
				a *= multiplier
				b *= multiplier
				c *= multiplier
				sum =  a + b + c
			if sum == target:
				break
			print('sum=' + str(sum))
		if m > target:
			# give up
			break
	product = a * b * c
	print('product=' + str(product))
	print('a=' + str(a))
	print('b=' + str(b))
	print('c=' + str(c))

if __name__ == '__main__':
	main()
