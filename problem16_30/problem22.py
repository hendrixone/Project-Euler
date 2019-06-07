'''
Names scores

Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
from function import import_txt

def name_score(name, index):
    #Calculate name score
    sum = 0
    for char in name:
        sum += (ord(char) - 64)
    return sum * index

def main():
    index = 1
    sum = 0
    names = []
    for name in import_txt('p22.txt'):
        names.append(name)
    
    #sort
    names = sorted(names, key=None, reverse=False)
    
    #add up the sum
    for name in names:
        print(name, name_score(name, index), index)
        sum += name_score(name, index)
        index += 1
        
    print(sum)


if __name__ == '__main__':
    main()