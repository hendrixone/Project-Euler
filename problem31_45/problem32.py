'''
Problem 32  Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

def digit(number):
    return len(str(number))

def get_range(len):
    for i in range(10**(4-len), 10**(5-len)):
        yield i

def main():
    a = []
    products = []
    
    for i in range(1, 100):
        for k in get_range(digit(i)):
            c = i * k
            '''print('%i * %i = %i' % (i, k, c))'''
            if digit(i) + digit(k) + digit(c) < 9:
                continue
            if digit(i) + digit(k) + digit(c) == 9:
                a.append('%i%i%i' % (i, k, c))
                products.append(c)
            if digit(i) + digit(k) + digit(c) > 9:
                break
            
    '''for i in range(len(a)):
        print(products[i])
    print(a)'''
    
    
    result = {0, 0}
    for item in a:
        breakout = False
        for i in range(1, 10):
            if item.find('%i' % i) == -1:
                breakout = True
        if not breakout:
            result.add(products[a.index(item)])
        
    print(result)
    sum = 0
    for item in result:
        sum += item
    print(sum)
    
if __name__ == '__main__':
    main()
