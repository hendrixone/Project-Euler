import math
'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

'''
Since 9! = 362880, the highest sum a 7 digit number can reach is sum of 7 9! which is 2540160. As you can see

the sum already reached 7 digit, which means that the highest number can not exceed 2540160
'''

def digit(num):
    '''return every digit in num'''
    for i in range(len(str(num))):
        temp = num % 10
        num /= 10
        yield temp

def main():
    result = []
    '''Try all integer from 10 to 2500000'''
    for num in range(10, 2500000):
        sum = 0
        for i in digit(num):
            sum += math.factorial(i)
        if sum == num:
            result.append(num)
    
    ''''output'''
    print(result)
    sum = 0
    for num in result:
        sum += num
    print(sum)
    
if __name__ == '__main__':
    main()
