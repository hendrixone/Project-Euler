'''
Circular primes

Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''


'''
Find all prime numbers below one million and then sort out the numbers that match the requirement

by rearrange the number and test it
'''
import math
from itertools import permutations


def is_prime(n):
    '''Return true is n is prime'''
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def primes(bound):
    '''Generate all primes in range bound'''
    list = [True] * (bound + 1)
    list[0] ,list[1] = False, False
    for i in range(int(math.sqrt(len(list)) + 1)):
        if list[i] == True:
            for k in range(2, bound / i + 1):
                list[i*k] = False
    
    for i in range(len(list)):
        if list[i]:
            yield i
    
def digit(num):
    '''return all digit in a list'''
    result = []
    for i in range(len(str(num))):
        temp = num % 10
        num /= 10
        result.append(temp)
    return result[::-1]

def list_to_num(list):
    '''Covert a list of number in to a integer'''
    num = 0
    len1 = len(list)
    for i in range(len1):
        num += list[i] * (10**(len1 - i - 1))
    return num
            
def main():
    bound = 1000000
    result = []
    temp = []
    
    '''Try all prime numbers in below bound(1000000)'''
    for num in primes(bound):
        
        '''put each digit into a list'''
        list = digit(num)
        breakout = False
        
        '''rotate the number and test with is_prime, break if not, store in result if no break'''
        for i in range(1, len(list)):
            if is_prime(list_to_num(list[i:] + list[:i])):
                continue
            else:
                breakout = True
                break
        if not breakout:  
            print(num)
            result.append(num)
        
    print(len(result))

if __name__ == '__main__':
    main()
