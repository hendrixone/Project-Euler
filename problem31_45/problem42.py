'''
Coded triangle numbers

Problem 42
The nth term of the sequence of triangle numbers is given by, tn = 1/2n * (n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''
'''
Generate a list of triangle number, then try to match the word value with triangle number

output the number of word
'''
import re

def tri_num(n):
    '''return the nth triangle number'''
    temp = 0.5 * n * (n + 1)
    return int(temp)

def word_value(word):
    '''calculate the word_value'''
    sum = 0
    for char in word.upper():
        sum += ord(char) - 64
    return sum

def main():
    '''make a list containing n triangle number'''
    triangle_number = []
    for i in range(1, 50):
        triangle_number.append(tri_num(i))
    
    '''Move the words into a string'''
    try:
        file = open('p42.txt')
        text = file.read()
        file.close()
    except :
        print('No file found')
        return -1
    
    '''For every word in the list, try to match the word value with the triangle number list'''
    pattern = re.compile(r'\"([A-Z]*)\",')
    counter = 0
    for word in pattern.findall(text):
        try:
            triangle_number.index(word_value(word))
            print(word, word_value(word))
            counter += 1
        except:
            continue
    print(counter)
    
if __name__ == '__main__':
    main()
