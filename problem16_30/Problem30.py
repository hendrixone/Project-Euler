








def main():
	result = []
	for num in range(10,500000):
		sum = 0
		temp = num
		while True:
			sum += (temp % 10) ** 5
			temp = int(temp/10)
			if sum > num:
				break
			if temp < 10:
				sum += temp**5
				break
		if sum == num:
			result.append(num)
	print(result)
	sum = 0
	for number in result:
		sum += number
	print(sum)


if __name__ == '__main__':
	main()
