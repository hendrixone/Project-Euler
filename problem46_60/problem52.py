'''
Permuted multiples

Problem 52
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
'''
Solved by brute force, enumerate all integer until matched
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
    for integer in range(1, 1000000):
        d = sorted(digit(integer))
        breakout = False
        for multiple in range(2, 7):
            if d == sorted(digit(multiple * integer)):
                continue
            else:
                breakout = True
                break
        if not breakout:
            print(integer)
            break
            
if __name__ == '__main__':
    main()
