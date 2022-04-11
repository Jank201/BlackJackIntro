from re import L
import random
import sys

from pyrsistent import v

deck = []

for x in range(2,10):
    for y in range(4):
        deck.append(x)
for x in range(4):
    for y in range(4):
        deck.append(10)
for x in range(4):
    deck.append([1,11])

userHand = []
dealerHand = []
userHand2 = []
dealerHand2 = []

def InitDeal():
    for x in range(2):
        y = random.choice(deck)
        userHand.append(y)
        deck.remove(y)
        
    for x in range(2):
        t = random.choice(deck)
        dealerHand.append(t)
        deck.remove(t)
    if dealerHand[0] == [1,11]:
        return "your hand is {}, dealers showing an Ace".format(userHand)
    else:   
        return "your hand is {}, dealer showing {}".format(userHand, dealerHand[0])


def hit():
    l = aceList
    if max(l) == 21:
        return l
    else:
        for e in range(1,100):
            if len(l) > 1:
                    dec = input('Your Possible Totals: {}, hit? '.format(l))
                    if dec.lower() == 'y':
                        x = random.choice(deck)
                        deck.remove(x)
                        print('You hit {}'.format(x))
                        userHand2.append(x)
                        if type(x) == int:
                            l[0] += x
                            l[1] += x
                        else:
                            for p in range(len(l)):
                                l[p] += 1
                                l.append(l[p] + 10) 
                        if min(l) > 21:
                            print('you bust, Dealer wins!')
                            print('Your Cards: '+ str(userHand2))
                            print('Dealer Cards: '+ str(dealerHand2))
                            sys.exit()
                        else:
                            continue
                    else:
                        break       
        
            else:
                dec = input("Your total is " + str(l[0]) + ' would you like to hit? y/n ')
                if dec.lower() == 'y':
                    x = random.choice(deck)
                    deck.remove(x)
                    print('You hit {}'.format(x))
                    userHand2.append(x)
                    if type(x) == int:
                        l[0] += x
                    else:
                        l[0] += 1
                        l.append(l[0]+10)
                    if min(l) > 21:
                        print('You Bust, Dealer Wins!')
                        print('Your Cards: '+ str(userHand2))
                        print('Dealer Cards: '+ str(dealerHand2))
                        sys.exit()
                    else: 
                        continue    
                else:
                    break
        return l 


def findCard():
    hand = hit()
    for x in hand:
        if x > 21:
            hand.remove(x)
    bestCard = max(hand)
    return bestCard  

def dealerHit():
    l = daceList
    if bestie == 21 and max(l) != 21 and len(userHand2) == 2:
        print('Blackjack! you Win!')
        print(max(l))
        print('Your Cards: '+ str(userHand2))
        print('Dealer Cards: '+ str(dealerHand2))
        sys.exit()
    elif max(l) == 21:
        print('Dealer hits Blackjack, dealer wins.')
        print('Your Cards: '+ str(userHand2))
        print('Dealer Cards: '+ str(dealerHand2))
        sys.exit()
    else:
        for e in range(1,100):
            if max(l) > bestie and max(l) > 16  and max(l) < 21:
                print('dealer has {}, dealer wins'.format(str(max(l))))
                print('Your Cards: '+ str(userHand2))
                print('Dealer Cards: '+ str(dealerHand2))
                sys.exit()
            elif max(l) < bestie and max(l) > 16:
                print('dealer has {}, player has {}. player wins.'.format(max(l),bestie))
                print('Your Cards: '+ str(userHand2))
                print('Dealer Cards: '+ str(dealerHand2))
                sys.exit()
            elif max(l) == bestie and max(l) > 16:
                print('you Tie!')
                print('Your Cards: '+ str(userHand2))
                print('Dealer Cards: '+ str(dealerHand2))
                sys.exit()
                
            else:
                if len(l) > 1:
                    print('Dealer Possible Totals: {}. '.format(l))
                    x = random.choice(deck)
                    deck.remove(x)
                    dealerHand2.append(x)
                    print('Dealer hits {}'.format(x))
                    if type(x) == int:
                            l[0] += x
                            l[1] += x
                    else:
                        for p in range(len(l)):
                            l[p] += 1
                            l.append(l[p] + 10) 
                        if min(l) > 21:
                            print('Dealer busts, you win!')
                            print('Your Cards: '+ str(userHand2))
                            print('Dealer Cards: '+ str(dealerHand2))
                            sys.exit 
                    s = filter(lambda num:num < 21, l)
                    l = list(s)

                else:
                    print("Dealer total is " + str(l[0]))
                    x = random.choice(deck)
                    deck.remove(x)
                    dealerHand2.append(x)
                    print('Dealer hits {}'.format(x))
                    if type(x) == int:
                        l[0] += x
                    else:
                        l[0] += 1
                        l.append(l[0]+10)
                    if min(l) > 21:
                        print('Dealer busts, you win!')
                        print('Your Cards: '+ str(userHand2))
                        print('Dealer Cards: '+ str(dealerHand2))
                        sys.exit()
                    s = filter(lambda num:num < 21, l)
                    l = list(s)

        return l   


print(InitDeal())

uTotalInit = 0
u2TotalInit = 0
aceList = [0]
if [1,11] in userHand:
    if userHand.index([1,11]) == 1 and userHand.index([1,11]) == 2:
        aceList[0] = 2
        aceList.append(12)
        aceList.append(22)
    else:
        aInd = userHand.index([1,11])
        if aInd == 1:
            uTotalInit = 1 + userHand[0]
        else: 
            uTotalInit = 1 + userHand[1]
        u2TotalInit = 10 + uTotalInit
        aceList[0] = uTotalInit
        aceList.append(u2TotalInit)
else:
    aceList[0] = sum(userHand)

dTotalInit = 0
d2TotalInit = 0
daceList = [0]
if [1,11] in dealerHand:
    daInd = dealerHand.index([1,11])
    if daInd == 1:
        dTotalInit = 1 + dealerHand[0]
    else: 
        dTotalInit = 1 + dealerHand[1]
    d2TotalInit = 10 + dTotalInit
    daceList[0] = dTotalInit
    daceList.append(d2TotalInit)
else:
    daceList[0] = sum(dealerHand)

userHand2 = userHand
dealerHand2 = dealerHand

bestie = findCard()
print('Your Cards: '+ str(userHand2))

dTotal = dealerHit()

print('Your Cards: '+ str(userHand2))
print('Dealer Cards: '+ str(dealerHand2))
