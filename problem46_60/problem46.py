'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2*1^2
15 = 7 + 2*2^2
21 = 3 + 2*3^2
25 = 7 + 2*3^2
27 = 19 + 2*2^2
33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
import math

def primeGen(bound, start=0):
    '''Generate all primes in range bound'''
    list = [True] * (bound + 1)
    list[0] ,list[1] = False, False
    for i in range(int(math.sqrt(len(list)) + 1)):
        if list[i] == True:
            for k in range(2, bound / i + 1):
                list[i*k] = False
    
    return list

'''
Initiate two list, prime(store prime numbers in a boolean list) and square(store the 'Twice of Square'
in a int type list.
deduct the square from composite number, if the result is not prime, try next square until the
result is a prime number. If the result reached 0, means that composite number cannot be written as
such form, return that number.
'''
def main():
    bound = 200000
    
    square = []
    for i in range(1,100):
        square.append(2 * i**2)
    square = tuple(square)
    
    primes = primeGen(bound)
    primes = tuple(primes)
    
    breakout = False
    for i in range(9, bound):
        if not primes[i] and i % 2 != 0:
            for k in square:
                #If the square is greater than the composite number
                if k >= i:
                    breakout = True
                    break
                #If the difference is a prime number
                if primes[i - k]:
                    break
                #If not prime number, try next square
                else:
                    continue
        if breakout:
            print(i)
            break
        
if __name__ == '__main__':
    main()
