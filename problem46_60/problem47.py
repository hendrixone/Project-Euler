'''
Distinct primes factors

Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''
import math

def primes(bound, start=0):
    '''Generate all primes in range bound'''
    list = [True] * (bound + 1)
    list[0] ,list[1] = False, False
    for i in range(int(math.sqrt(len(list)) + 1)):
        if list[i] == True:
            for k in range(2, int(bound / i + 1)):
                list[i*k] = False
    
    return list

def primeint(bound):
    #return a list of prime number
    primeint = []
    for i in range(len(prime)):
        if prime[i]:
            primeint.append(i)
    primeint = tuple(primeint)
    return primeint

bound = 150000
prime = tuple(primes(bound))
primeint = primeint(bound)

def primeFactor(n):
    #Return the number of distinct prime factor
    if prime[n]:
        return 1
    count = 0
    temp = set([])
    while n != 1:
        for i in primeint:
            if n % i == 0:
                temp.add(i)
                count += 1
                n /= i
                break
    return len(temp)
    
    
def main():
    #make a list of number of dictince prime factor of all integer below bound
    list = [0] * bound
    for i in range(2,bound):
        print(i)
        list[i] = (primeFactor(i))
            
    for i in range(len(list)):
        print(i+2, list[i])
    
    #If from i to i+3, all number have 4 distinct prime factor, return i which is the result
    for i in range(2, len(list)):
        if list[i] == 4:
            print(i, list[i])
            breakout = False
            for k in range(1, 4):
                if list[k + i] != 4:
                    breakout = True
                    break
            if not breakout:
                print(i)
                break
    
if __name__ == '__main__':
    main()
