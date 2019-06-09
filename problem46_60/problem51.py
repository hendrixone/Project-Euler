'''
Prime digit replacements

Problem 51
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
427.88ms
'''
'''
This method isn't perfect(I believe), by go through all the possible pattern (like 56**3, and replace * with 0 to 9) until 8 prime was found
using the pattern.
I did a lot of modification and improvement to make this function perform in less than 1s
on I7-8700K processor
I will not comment this program, but it should be straight forward enough, though the naming may be tricky.
'''

from function import Primetool, digit, list_to_num
from itertools import combinations
from sortAlgorithm import Timer

def replace(list, index, list2):
    if len(list2) < len(index):
        list2 = [0]*(len(index) - len(list2)) + list2
    list1 = list[:]
    count = 0
    for i in index:
        list1[i] = list2[count]
        count += 1
    return list1

def check(list, index):
    counter = 0
    for n in range(10):
        temp2 = list[:]
        for digi in index:
            temp2[digi] = n
        if temp2[0] == 0 or not p.is_prime(list_to_num(temp2)):
            counter += 1
        if counter > 2:
            return False
    return True

    
def main():
    global p
    p = Primetool()
    template = [0,1,2,3,4,5,6,7,8,9,10]
    
    t = Timer()
    for d in range(2, 7):
        num = ['*']*d
        for i in range(1, d):
            for pattern in combinations(template[:d], i):
                reversed = template[:d]
                for digi in pattern:
                    reversed.remove(digi)
                for k in range((10**len(pattern))):
                    r = digit(k)
                    temp = replace(num, pattern, r)
                    if check(temp, reversed):
                        print(temp)
                        t.end
                        return 1
                        
if __name__ == '__main__':
    main()