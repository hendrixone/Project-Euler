import math

def is_primes(num):
	if num < 2:
		return False
	for i in range(2, int(math.sqrt(num) + 1)):
		if num % i == 0:
			return False
	return True

def main():
	maxa = 0
	maxb = 0
	maxn = 0
	for a in range(-999, 1000):
		for b in range(-999, 1000):
			n = 0
			while True:
				if is_primes(n**2 + a*n + b):
					n += 1
				else:
					if n > maxn:
						maxn = n
						maxb = b
						maxa = a
					break

	print(maxa, maxb ,maxn)
	print(maxa * maxb)

if __name__ == '__main__':
	main()
