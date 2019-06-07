'''
Self powers

Problem 48
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

'''
'''
That's why I love Python, don't you?
'''
if __name__ == '__main__':
    sum = 0
    for i in range(1, 1001):
        sum += i**i
    print(sum % 10000000000)