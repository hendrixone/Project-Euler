'''
Pandigital multiples

Problem 38
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 

192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 

giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 

concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

'''
Since the list[1,2,3] must have at least two element. Thus the highest value of the number can not

exceed 10000.(when the list is [1, 2] and the number is 10000, the sum is 1000020000 which have 10 digit.

enumerate all possible outcome that have 9 digit and then sort out answer
'''
def calc(i, list):
    '''calculate use the way the problem asked'''
    temp = ''
    for n in list:
        temp += str(n*i)
    return int(temp)

def digit(num):
    '''Return all digit in a list'''
    result = []
    for i in range(len(str(num))):
        temp = num % 10
        num /= 10
        result.append(temp)
    return result[::-1]


def main():
    '''Initialize a list from 1 to 1000'''
    result = []
    list = []
    for i in range(1, 1000):
        list.append(i)
     
       
    max = 0
    '''Try from 1 to 10000'''
    for i in range(1, 10000):
        '''Try from n = 2 to n = 10'''
        for k in range(2, 10):
            '''Stored the number with 9 digit'''
            temp = calc(i, list[:k])
            if max < temp and temp < 1000000000 and temp > 99999999:
                result.append(temp)
    
    '''Sort out the number which contain all 1-9'''
    result.sort()
    for n in result:
        breakout = False
        for i in range(1, 10):
            if str(digit(n)).find(str(i)) == -1:
                breakout = True
                break
        if not breakout:
            print(n)

if __name__ == '__main__':
    main()
