def main():
	digit = 1000
	num1, num2 = [0] * digit, [0] * digit
	num1[0] = 1
	index = 0
	

	while True:
		num1 = list_add(num1, num2)
		arrange(num1, digit)
		index += 1
		print(num1, index)
		if num1[digit - 1] != 0:
			break
		num2 = list_add(num2, num1)
		arrange(num2, digit)
		print(num2)
		index += 1
		if num2[digit - 1] != 0:
			break
		

	print(index)

def list_add(list1, list2):
	for i in range(len(list1)):
		list1[i] += list2[i]
	return list1

def arrange(num1, digit):
	for i in range(digit):
		if num1[i] >= 10:
			num1[i+1] += int(num1[i] / 10)
			num1[i] = num1[i] % 10

if __name__ == '__main__':
	main()
