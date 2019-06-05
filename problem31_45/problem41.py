'''
Pandigital prime

Problem 41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
'''
Known that if the digit sum of a is divisible by some number, the number it

self is also divisible that some that some number.

from that we can prove the 9 digit Pandigital number cannot be prime because

1 + 2 + ... + 8 + 9 = 45 which is divisible by 9 or 3, so do the 9 digit number

Thus, the answer will be a 7 digit number
'''
from itertools import permutations
import math
  
            
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


def main():
    '''
    Find the full permutation of 7 digit Pandigital number
    and sort out the primenumber
    '''
    for list in permutations(range(1, 8)):
        if is_prime(list_to_num(list)):
            print list_to_num(list)
    
if __name__ == '__main__':
    main()
