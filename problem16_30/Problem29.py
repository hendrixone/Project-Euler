from itertools import *
def main():
	set1 = {4}
	for base in range(2, 101):
		for power in range(2, 101):
			set1.add(base**power)
	set2 = sorted(set1)
	print(len(set2))







if __name__ == '__main__':
	main()
