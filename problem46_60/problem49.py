'''
Prime permutations

Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''
'''
My method is to make a list of A.P.(Arithmetic Progression) using all 4 digits prime numbers and making sure all terms are prime numbers. 

Then check if all three terms are made up with same digits

Works Really Fast
'''
from function import primes, digit

def main():
    #Make two list to stored prime numbers and check is_prime
    upperbound = 10000
    primelist = []
    primebool = [False] * upperbound
    
    for i in primes(upperbound,1000):
        primelist.append(i)
        primebool[i] = True
    primelist = tuple(primelist)
    primebool = tuple(primebool)
    
    #If the A.P. contains 3 primes, store it in a list
    list = []
    for i in primelist:
        for d in range(1, int((upperbound - i)/2)):
            if primebool[i + d]:
                if primebool[i + d + d]:
                    list.append([i, i+d, i + d + d])
    
    #If they have the same digits, print it out
    for i in list:
        temp = [digit(i[0]), digit(i[1]), digit(i[2])]
        breakout = False
        for n in range(4):
            if temp[0][n] in temp[1] and temp[0][n] in temp[2]:
                continue
            else:
                breakout = True
                break
        if not breakout:
            if len(set(temp[0])) == len(set(temp[1])) and len(set(temp[0])) == len(set(temp[2])):
                print(i)
        
if __name__ == '__main__':
    main()