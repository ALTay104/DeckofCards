import random
import pickle
import operator
from collections import Counter

infile = open("DeckOfCardsList.dat", 'rb')
deckOfCards = pickle.load(infile)
infile.close()
pokerHand = random.sample(deckOfCards, 5)
pokerSeparate = list(''.join(pokerHand))  #split everything into list
print(pokerHand)

#To combine 1,0 into single list
for i in range(len(pokerSeparate)):
    if pokerSeparate[i] == '1':
        pokerSeparate[i] = ''.join(operator.itemgetter(i,i+1)(pokerSeparate))

#after combine, need to remove 0 from list
for item in pokerSeparate[:]:
    if item == '0':
        pokerSeparate.remove(item)

counter = dict(Counter(pokerSeparate)) #to create key and values
pokerShape = ['♠', '♥', '♣', '♦']
pokerNumber = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

#check whether it is single, pair, triple or quadruple
single, pair, triple = 0, 0, 0
for key, value in counter.items():
    if key in pokerNumber:
        if value >= 4:
            print("4-OF-A-KIND")
        elif value == 1:
            single += 1
        elif value == 2:
            pair += 1
        elif value == 3:
            triple += 1

#To analyze the possible cases
if triple == 1 and single == 2:
    print('Three-of-a-kind')
elif triple == 1 and pair == 1:
    print('Full House')
elif pair == 2:
    print('Two pairs')
elif pair == 1:
    print('One pair')
elif single == 5:
    print('Ranks-all-different')


