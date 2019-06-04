def get_file(name):
	file = open('p20.txt', 'r', encoding = 'UTF-8')
	names = file.read()
	file.close()
	return names

def make_list(names):

	list = []
	index = 0
	while index < len(names):
		if names[index] == '"':
			start = index + 1
			end = 0
			while True:
				index += 1
				if names[index] == '"':
					end = index
					break
			list.append(names[start : end])
		index += 1
	list.sort()
	return list

def name_score(name, index):
	total = 0
	for char in name:
		total += ord(char) - 64
	return total * index

def main():
	names = get_file('p20.txt')
	name_list = make_list(names)
	print(name_list)
	sum = 0
	index = 1
	for name in name_list:
		sum += name_score(name, index)
		index += 1
	print('Sum is', sum)

if __name__ == '__main__':
	main()