'''
Powerful digit sum

Problem 56
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''
'''
No explanation needed, love python
'''
def digit_sum(num):
    sum = 0
    while num >= 10:
        sum += num % 10
        num //= 10
    return sum + num

def main():
    max = 0
    for a in range(1,100):
        for b in range(1,100):
            num = digit_sum(a**b)
            if num > max:
                max = num
    print(max)

if __name__ == '__main__':
    main()
