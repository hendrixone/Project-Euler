import math

def is_abundant(number):
	sum = 0
	for factor in range(1, int(number / 2 + 1)):
		if number % factor == 0:
			sum += factor
	if sum > number:
		return True
	else: 
		return False

def main():
	numlist = [False] * 30000
	abulist = []
	for n in range(30000):
		if is_abundant(n):
			abulist.append(n)
	
	for key in range(int(len(abulist) / 2)):
		i = 0
		while True:
			temp = abulist[key] + abulist[key + i]
			if temp > 29000:
				break
			numlist[temp] = True
			i += 1

	sum = 0
	for i in range(28125):
		if numlist[i] == False:
			print(i)
			sum += i
	print(sum)

if __name__ == '__main__':
	main()
