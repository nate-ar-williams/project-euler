#!/bin/bash/python3

def main():
	filename = 'largestProductInGrid.txt'
	grid = []
	with open(filename) as f:
		grid = list(f)
	#for i in range(len(grid)):
	grid = [[l for l in map(int, grid[i].split())] for i in range(len(grid))]

	# looking for largest product of 4 adjacent numbers in same direction
	# check each direction separately

	print(*grid)

if __name__ == '__main__':
	main()
