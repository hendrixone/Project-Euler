from math import factorial
'''
Combinatoric selections
Problem 53

Unable to write the question in this file, pleas go to Project Euler problem 53 for the original
problem description
'''
'''
nCr=n!/r!(n-r)!
The function nCr is  symmetrical about r = n/2, I don't know how to prove it in pure math but
if you look into the formula carefully. Treat n as a constant, this function have two root at
r = 0 and r = n, and for sure the r is within (0, n) which r is in the set of all integer. 
'''
def E(n, r):
    #input n and r, return nCr
    return factorial(n)/((factorial(r) * factorial(n - r)))

def main():
    counter = 0
    for n in range(1, 101):
        for r in range(1, n):
            if E(n, r) > 1000000:
                counter += 1
    print(counter)
    
if __name__ == '__main__':
    main()
