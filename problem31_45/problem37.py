'''
Truncatable primes

Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

'''
Haven't yet figure out a proper way to calculate the upper-bound. Thus, this function is using 

a forever loop until the 11th prime is found 
'''

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

def is_prime(n):
    '''Return true is n is prime'''
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def list_to_num(list):
    '''Covert a list of number in to a integer'''
    num = 0
    len1 = len(list)
    for i in range(len1):
        num += list[i] * (10**(len1 - i - 1))
    return num


def check(num):
    
    '''try from 123 to 23 ,3'''
    strnum = str(num)
    lenth = len(strnum) - 1
    for i in range(lenth):
        strnum = strnum[1:]
        if not is_prime(int(strnum)):
            return False
    
    '''oppsite'''
    strnum = str(num)
    for i in range(lenth):
        strnum = strnum[:-1]
        if not is_prime(int(strnum)):
            return False
    
    '''if the test were passed return True, Else False'''
    return True
        
def main():
    result = []
    count = 0
    
    '''Try all primes from 11 to 10million until the 13th were found'''
    for i in primes(10000000, 11):
        if check(i):
            count += 1
            result.append(i)
        if count == 13:
            break
     
    '''Output'''
    sum = 0
    for i in result:
        sum += i
    print(sum)
    
if __name__ == '__main__':
    main()
