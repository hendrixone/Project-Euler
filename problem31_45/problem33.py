'''
Problem 33    Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
def main():
    list = []
    
    '''
    the simplified version of this problem it to find a fraction that:
    ik/jk = i/j , ik/kj = i/j, ki/jk = i/j, ki/kj = i/j
    by tring out all i, j and k within the range(1, 10)
    we'll be able to find the four exact fraction
    '''
    
    '''try every number, covert them in to float for python to do the math'''
    for i1 in range(1, 10):
        i = float(i1)
        for k1 in range(1, 10):
            k = float(k1)
            for j1 in range(1, 10):
                j = float(j1)
                
                '''if the case match, store the fraction into a list'''
                if (10*i +k) / (10*j + k) == i/j:
                    list.append([i, k, j, k])
                elif (10*i +k) / (10*k + j) == i/j:
                    list.append([i, k, k, j])
                elif (10*k +i) / (10*j + k) == i/j:
                    list.append([k, i, j, k])
                elif (10*k +i) / (10*k + j) == i/j:
                    list.append([k, i, k, j])
    
    '''sort out the fraction which the numerator is smaller than its denominator'''
    final = []
    for n in list:
        if n[0] != n[2] and n[1] != n[3]:
            if n[0]*10 + n[1] < n[2]*10 + n[3]:
                final.append([n[0], n[1], n[2], n[3]])
            
    numerator = 1
    denominator = 1
    for n in final:
        print('%i%i/%i%i'% (n[0], n[1], n[2], n[3]))
        numerator *= n[0]*10 + n[1]
        denominator *= n[2]*10 + n[3]
    
    '''output the result'''
    print('%i/%i' % (numerator, denominator))
    print(denominator // numerator)

if __name__ == '__main__':
    main()
