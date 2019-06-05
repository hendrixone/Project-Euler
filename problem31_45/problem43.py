'''
Problem 43
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''
'''
Enumerate all odd 0-9 Pandigital num, find the matched number
'''
from itertools import permutations
import math

def primes(bound, start=0):
    '''Generate all primes in range bound'''
    list = [True] * (bound + 1)
    list[0] ,list[1] = False, False
    for i in range(int(math.sqrt(len(list)) + 1)):
        if list[i] == True:
            for k in range(2, bound / i + 1):
                list[i*k] = False
    
    for i in range(start, len(list)):
        if list[i]:
            yield i
            

def list_to_num(list):
    '''Covert a list of number in to a integer'''
    num = 0
    len1 = len(list)
    for i in range(len1):
        num += list[i] * (10**(len1 - i - 1))
    return num


def main():
    '''Put the first 7 prime number in a list'''
    primenum = []
    for i in primes(18):
        primenum.append(i)
    
    '''Generate all odd pandigial number'''
    pandigital = []
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
    for i in permutations([0,1,2,3,4,5,6,7,8,9]):
        if i[-1] % 2 != 0:
            pandigital.append(i)
    
    '''Find the matched number and add to list result[]'''
    result = []
    for num in pandigital:
        breakout = False
        for i in range(7):
            if list_to_num(num[i+1:i+4]) % primenum[i] == 0:
                continue
            else:
                breakout = True
        if not breakout:
            result.append(list_to_num(num))
    
    sum = 0
    for i in result:
        sum += i
    print(result, sum)  


if __name__ == '__main__':
    main()
