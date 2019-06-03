'''
Problem 35    Double-base palindromes
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
from ipalib.output import result

'''
Simply find all palindromes number below one million

and sort out those whose binary is also palindromes
'''

def is_palindromes(num):
    '''Return true is num is palindromes'''
    if num < 1:
        return False
    else:
        if str(num) == str(num)[::-1]:
            return True
        else:
            return False

def int_to_bin(num):
    '''Convert int to int type binary'''
    binnum = bin(num)
    strnum = str(binnum)
    return int(strnum[2::])

def main():

    '''Initialize a set to store number'''
    result = set([])
    
    '''Try all number from 0 to 1000000'''
    for i in range(1000000):
        if is_palindromes(i) and is_palindromes(int_to_bin(i)):
            result.add(i)
    result = sorted(result)

    for number in result:
        print(number, int_to_bin(number))
    
    sum = 0
    for number in result:
        sum += number
    print(sum)
    
if __name__ == '__main__':
    main()
