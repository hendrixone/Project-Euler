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
    if i <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def digit(num):
    '''return all digit in a list'''
    result = []
    for i in range(len(str(num))):
        temp = num % 10
        num /= 10
        result.append(temp)
    return result[::-1]
