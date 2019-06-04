class Array(object):
	def __init__(self, size, x=0, y=0, direction='right'):
		self._list = [([0]*size) for i in range(size)]
		self._x = x
		self._y = y
		self._direction = direction

	def move(self):
		if self._direction == 'left':
			self._x -= 1
		elif self._direction == 'down':
			self._y += 1
		elif self._direction == 'right':
			self._x += 1
		elif self._direction == 'up':
			self._y -= 1
				

	def set(self, number):
		self._list[self._y][self._x] = number

	def turn(self):
		if self._direction == 'up':
			self._direction = 'right'
		elif self._direction == 'right':
			self._direction = 'down'
		elif self._direction == 'down':
			self._direction = 'left'
		elif self._direction == 'left':
			self._direction = 'up'

	@property
	def list(self):
		return self._list
	

def main():
	size = 1001

	spiral = Array(size, int(size/2), int(size/2))
	num = 1
	
	spiral.set(num)

	for step in range(1, size):
		for i in range(2):
			for k in range(step):
				num += 1
				spiral.move()
				spiral.set(num)
			spiral.turn()

	for i in range(size - 1):
		num += 1
		spiral.move()
		spiral.set(num)

	'''
	for i in range(len(spiral.list)):
		print(spiral.list[i])
	'''

	sum = 0
	for line in range(int(size/2)):
		sum += spiral.list[line][line]
	
	for line in range(int(size/2)):
		sum += spiral.list[-line - 1][line]
	for line in range(int(size/2)):
		sum += spiral.list[line][-line - 1]
	for line in range(int(size/2)):
		sum += spiral.list[-line - 1][-line - 1]

	print(sum)


if __name__ == '__main__':
	main()