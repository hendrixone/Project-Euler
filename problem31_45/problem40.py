'''
Champernowne's constant

Problem 40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d100000
'''

'''
'''
def digit(num):
    '''Return all digit in a list'''
    result = []
    for i in range(len(str(num))):
        temp = num % 10
        num /= 10
        result.append(temp)
    return result[::-1]


def main():
    list = []
    index = 0
    '''Make a list follow the instruction, size over 1000000'''
    for i in range(1,200000):
        for n in digit(i):
            list.append(n)
            index += 1
        if index >= 1000000:
            break
    
    '''Calculate the product and print'''
    print(list[0] * list[9] * list[99] * list[999] * list[9999] *
           list[99999] * list[999999])
    
if __name__ == '__main__':
    main()
