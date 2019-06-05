def decimal(d):
	temp = []
	num = 1
	while True:
		if num < d:
			num *= 10
			for i in range(len(temp)):
				if temp[i] == num:
					return len(temp) - i
			temp.append(num)
		elif num % d == 0:
			return 0
		else:
			num = num % d

def main():
	digit = 0
	maximum = 0
	print(decimal(365))
	for d in range(2, 1001):
		if decimal(d) > digit:
			digit = decimal(d)
			maximum = d
	print(maximum)

if __name__ == '__main__':
	main()
