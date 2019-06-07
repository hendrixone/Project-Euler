'''
Consecutive prime sum

Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
from function import primes

'''
Make prime into two type of list boolean and int as usual for faster access.
Enumerate all primes below 1million, the sum of all consecutive primes start from that prime and count the term.
find the longest one
'''
def main():
    #prepare the list of primes
    bound = 1000000
    primelist = []
    primebool = [False] * bound
    for i in primes(bound):
        primelist.append(i)
        primebool[i] = True
    primelist = tuple(primelist)
    primebool = tuple(primebool)
    
    #Do the enumeration
    list = []
    for i in range(len(primelist)):
        sum = 0
        counter = 0
        for k in range(i, len(primelist)):
            counter += 1
            sum += primelist[k]
            if sum >= bound:
                break
            if primebool[sum]:
                list.append([sum, counter])
    
    #find the length of the longest term    
    max = [0,0]
    for i in list:
        if i[1] > max[1]:
            max[0] = i[0]
            max[1] = i[1]
    print(max)

if __name__ == '__main__':
    main()