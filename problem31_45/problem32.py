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
