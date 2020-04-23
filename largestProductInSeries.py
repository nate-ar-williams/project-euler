#!/bin/bash/python3



def main():
	seriesLength = 4
	seriesDifference = seriesLength - 1
	numString = ''
	with open('thousandDigitNumber.txt') as f:
		numString = f.read()
	numLength = len(numString)
	# let start be series starting index
	start = -1
	# let end be series ending index
	end = start + seriesDifference
	maxProduct = 0
	while end < numLength:
		start += 1
		end += 1
		product = 1
		for i in range(start, end + 1):
			digit = int(numString[i])
			if digit == 0:
				start = i + 1
				end = start + seriesDifference
				product = 0
				break
			product *= digit
		if product > maxProduct:
			maxProduct = product
	print(maxProduct)

if __name__ == '__main__':
	main()
