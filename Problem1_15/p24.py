from itertools import *
if __name__ == '__main__':
	x = 1
	for num in permutations([0,1,2,3,4,5,6,7,8,9]):
		if x == 1000000:
			print(num)
			break
		x+=1