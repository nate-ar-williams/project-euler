#!/usr/bin/python3

import sys
import math

def getDigits(x):
	digits = []
	while x > 0:
		digits.append(x % 10)
		x = x // 10
	digits.reverse()
	return digits

def getInt(digits):
	num = 0
	digits.reverse()
	multiplier = 1
	for digit in digits:
		num += digit * multiplier
		multiplier *= 10
	return num

# doesn't work if next largest palindrome is fewer digits than original, or if x isn't a palindrome
def genNextLargestPalindrome(x):
     digits = getDigits(x)
     numDigits = len(digits)
     isEvenLength = numDigits % 2 == 0
     innermostIndex = numDigits // 2
     rightIndex = innermostIndex + 1
     leftIndex = innermostIndex - 1
     if isEvenLength:
             leftIndex -= 1
     if digits[innermostIndex] != 0:
             digits[innermostIndex] -= 1
             if isEvenLength:
                     digits[innermostIndex - 1] -= 1
     else:
             digits[innermostIndex] = 9
             if isEvenLength:
                     digits[innermostIndex - 1] = 9
             while digits[leftIndex] == 0:
                     digits[leftIndex] = 9
                     leftIndex -= 1
                     digits[rightIndex] = 9
                     rightIndex += 1
             digits[leftIndex] -= 1
             digits[rightIndex] -= 1
     return getInt(digits)




def main():
	maxDivisor = divisor = 999
	maxProduct = palindromeCandidate = (maxDivisor + 1) * (maxDivisor + 1) - 1

	while True:
		quotient, remainder = divmod(palindromeCandidate, divisor)
		isViableCandidate = True
		squareRootOfCandidate = math.sqrt(palindromeCandidate)		

		while isViableCandidate:
			while quotient < maxDivisor:
				if remainder == 0:
					print(palindromeCandidate)
					print(quotient)
					print(divisor)
					return palindromeCandidate
				else:
					divisor -= 1
					quotient, remainder = divmod(palindromeCandidate, divisor)
					if divisor < squareRootOfCandidate:
						isViableCandidate = False
			isViableCandidate = False
				
		palindromeCandidate = genNextLargestPalindrome(palindromeCandidate)
		divisor = maxDivisor

#	for arg in sys.argv[1::]:
#		print(genNextLargestPalindrome(int(arg)))


if __name__ == '__main__':
	main()