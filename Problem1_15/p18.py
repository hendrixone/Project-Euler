def num_to_list(list, inputnum):
	line = 0
	index = 0
	key = 0
	while key < len(inputnum):
		if inputnum[key] == '\n':
			line += 1
			index = 0
			key += 1
		elif inputnum[key] == ' ':
			key += 1
			index += 1
		list[line][index] = (ord(inputnum[key]) * 10) + ord(inputnum[key + 1]) - 528
		key += 2
	return list

def init_list(string):
	line = 1
	for item in range(len(string)):
		if string[item] == '\n':
			line += 1
	list = []
	for i in range(line):
		list.append([0]*(i+1))
	list = num_to_list(list, string)
	return list

def readfile(name):
	try:
		file = open(name, 'r', encoding = 'UTF-8')
		return file.read()
	except IOError as e:
		print(IOError)
	finally:
		file.close()
	
def findsum(list):
	for line in range(len(list)-2, -1, -1):
		for item in range(len(list[line])):
			if list[line + 1][item] > list[line + 1][item + 1]:
				list[line][item] += list[line + 1][item]
			else:
				list[line][item] += list[line + 1][item + 1]
	return list[0][0]

def main():
	inputnum = readfile('p18.txt')
	list = init_list(inputnum)
	print(list)
	print(findsum(list))
if __name__ == '__main__':
	main()