import random
#Setting up the hand
hand = []
points = 0
for i in range(4):
    print("Please input a card from your hand.")
    hand.append(int(input(">")))
print("Please input the cut card.")
hand.append(int(input(">")))

#checking for pairs
for i in range(5):
    points+= (hand.count(hand[i])-1)

#checking for fifteens in two cards
for i in range(5):
    for j in range(5):
        if i!=j and hand[i]+hand[j] == 15:
            points+=(2/2)


#checking for fifteens in three cards
for i in range(5):
    for j in range(5):
        for l in range(5):
            if i!=j and j!=l and hand[i]+hand[j]+hand[l] == 15:
                points+=(2/3)

#checking for fifteens in four cards
for i in range(5):
    for j in range(5):
        for l in range(5):
            for k in range(5):
                if i!=j and j!=l and l!=k and hand[i]+hand[j]+hand[l]+hand[k] == 15:
                    points+=(2/4)

#checkiong for fifteens in all the cards
if hand[0]+hand[1]+hand[2]+hand[3]+hand[4] == 15:
    points+=2

#checking for runs
hand.sort()
do4 = True
do3 = True

#checking for runs of 5
for a in range(len(hand)):
    for b in range(len(hand)):
        for c in range(len(hand)):
            for d in range(len(hand)):
                for e in range(len(hand)):
                    if hand[a]+1 == hand[b] and hand[b]+1 == hand[c] and hand[c]+1 == hand[d] and hand[d]+1 == hand[e]:
                        points+=5
                        do4 = False
                        do3 = False
#checking for runs of 4
if do4:
    for a in range(len(hand)):
        for b in range(len(hand)):
            for c in range(len(hand)):
                for d in range(len(hand)):
                    if hand[a]+1 == hand[b] and hand[b]+1 == hand[c] and hand[c]+1 == hand[d]:
                        points+=4
                        do3 = False
#checking for runs 3
if do3:
    for a in range(len(hand)):
        for b in range(len(hand)):
            for c in range(len(hand)):
                if hand[a]+1 == hand[b] and hand[b]+1 == hand[c]:
                    points+=3

print("")
print("You hand has",points,"points")
