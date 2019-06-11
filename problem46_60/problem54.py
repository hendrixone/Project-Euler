'''
Poker hands

Problem 54
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''
'''
Most interesting problem so far. This programm is alos the longest one I have made so far

check all the hands, figure out the type of combination and rank them form 1 - 10

after that, do the comparison, if the rank is heigher, wins, if the same, compare the hightest

value, if smaller lose. counter how many wins
'''
import re

def readfile(filepath):
    #import the txt from filepath
    f = open(filepath)
    result = []
    for line in f:
        result.append(line[:-1])
    return result

def convert(player):
    #put each each card into a list of five cards(hand)
    index = 0
    pattern = re.compile(r'[1-9A-Z]{2}')
    for hand in player:
        temp = []
        for card in re.findall(pattern, hand):
            temp.append(card)
        player[index] = temp
        index += 1
        
def get_value(hand):
    #return a list of values of cards in hand
    value = []
    for card in hand:
        if card[0] == 'T':
            value.append(10)
        elif card[0] == 'J':
            value.append(11)
        elif card[0] == 'Q':
            value.append(12)
        elif card[0] == 'K':
            value.append(13)
        elif card[0] == 'A':
            value.append(14)
        else:
            value.append(int(card[0]))
    return value

def get_suit(hand):
    #return a list of suits of cards in hand
    suit = []
    for card in hand:
        suit.append(card[1])
    return suit

'''
The following function determine the types of combinations of cards
'''

def is_rFlush(hand):
    #is royal flush
    if min(get_value(hand)) == 10 and is_flush(hand) and is_straight(hand):
        return True
    else:
        return False
    
def is_sFlush(hand):
    #is straight flush
    if is_flush(hand) and is_straight(hand):
        return True
    else:
        return False
    
def is_four(hand):
    value = sorted(get_value(hand))
    if value.count(value[0]) == 4 or value.count(value[-1]) == 4:
        return True
    else:
        return False
    
def is_fullhouse(hand):
    value = sorted(get_value(hand))
    if (value.count(value[0]) == 3 and value.count(value[-1]) == 2) or (value.count(value[0]) == 2 and value.count(value[-1]) == 3):
        return True
    else:
        return False
    
def is_flush(hand):
    suit = get_suit(hand)
    if suit.count(suit[0]) == 5:
        return True
    else:
        return False
def is_straight(hand):
    value = sorted(get_value(hand))
    for k in range(4):
        if value[k] + 1 == value[k+1]:
            continue
        else:
            return False
    return True
def is_three(hand):
    value = sorted(get_value(hand))
    if value.count(value[0]) == 3 or value.count(value[-1]) == 3 or value.count(value[2]) == 3:
        return True
    else:
        return False
def is_2pair(hand):
    value = sorted(get_value(hand))
    for i in value:
        if value.count(i) == 1:
            value.remove(i)
            break
    if value.count(value[0]) == 2 and value.count(value[-1]) == 2:
        return True
    else:
        return False
def is_pair(hand):
    value = sorted(get_value(hand))
    for i in value:
        if value.count(i) == 2:
            return True
    return False

def single(hand):
    value = get_value(hand)
    return max(value)

def id_pattern(hand):
    #determine the combination and return a list of rank and highest value
    if is_rFlush(hand):
        return [10]
    elif is_sFlush(hand):
        return [9, min(get_value(hand))]
    elif is_four(hand):
        value = get_value(hand)
        if value.count(value[0]) == 4:
            return [8, value[0]]
        else:
            return [8, value[-1]]
    elif is_fullhouse(hand):
        value = get_value(hand)
        if value.count(value[0]) == 3:
            return [7, value[0]]
        else:
            return [7, value[-1]]
    elif is_flush(hand):
        return [6, single(hand)]
    elif is_straight(hand):
        return [5, single(hand)]
    elif is_three(hand):
        value = get_value(hand)
        for i in value:
            if value.count(i) == 3:
                return [4, i]
    elif is_2pair(hand):
        value = sorted(get_value(hand))
        for i in value:
            if value.count(i) == 1:
                value.remove(i)
                return [3, max(value), min(value)]
    elif is_pair(hand):
        value = get_value(hand)
        for i in value:
            if value.count(i) == 2:
                return [2, i]
    else:
        return [1, single(hand)]
        
def main():
    player1 = []
    player2 = []
    
    for li in readfile('../externalresource/p54.txt'):
        player1.append(li[:14])
        player2.append(li[15:])

    convert(player1)
    convert(player2)

    cardvalue1 = []
    cardvalue2 = []
    for i in range(len(player1)):
        cardvalue1.append(id_pattern(player1[i]))
        cardvalue2.append(id_pattern(player2[i]))
    
    print(cardvalue1)
    print(cardvalue2)
    
    win = 0
    for turn in range(len(player1)):
        for i in range(3):
            try:
                if cardvalue1[turn][i] > cardvalue2[turn][i]:
                    win += 1
                    print(player1[turn], cardvalue1[turn], player2[turn], cardvalue2[turn], 'win')
                    break
                elif cardvalue1[turn][i] < cardvalue2[turn][i]:
                    print(player1[turn], cardvalue1[turn], player2[turn], cardvalue2[turn], 'lose')
                    break
                else:
                    continue
            except:
                print(player1[turn], cardvalue1[turn], player2[turn], cardvalue2[turn], 'tie')
                break
            
    print(win)

if __name__ == '__main__':
    main()
