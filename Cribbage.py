import random
#Setting up the hand
hand = []
points = 0
for i in range(4):
    print("Please input a card from your hand.")
    hand.append(int(input(">")))
hand.append(random.randint(1,10))

#checks for fifteens by groups of two
for i in range(5):
    for l in range(5):
        if i!=l:
            if hand[i] + hand[l] == 15:
                points+=2
points/=2

#checks for fifteens by groups of three
for i in range(5):
    for l in range(5):
        for k in range(5):
            if i!=l and i!=k:
                if hand[i] + hand[l] + hand[k] == 15:
                    points+=2
points/=3

#checks for fifteens by groups of four
for i in range(5):
    for l in range(5):
        for k in range(5):
            for j in range(5):
                if i!=l and j!=k and j!=i:
                    if hand[i] + hand[l] + hand[k] + hand[j] == 15:
                        points+=2
points/=4

#checks for fifteens by groups of five
if hand[0] + hand[1] + hand[2] + hand[3] + hand[4] == 15:
    points+=2

#checks for pairs
for i in range(len(hand)):
    if hand.countof(hand[i]) == 2:
        points+=2
    elif hand.countof(hand[i]) == 3:
        points+=6
    elif hand.countof(hand[i]) == 4:
        points +=12

