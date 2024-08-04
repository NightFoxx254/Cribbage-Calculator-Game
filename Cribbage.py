import random
#Setting up the hand
hand = []
points = 0
for i in range(4):
    print("Please input a card from your hand.")
    hand.append(int(input(">")))
hand.append(random.randint(1,10))
print(hand)

for i in range(5):
    points+= (hand.count(hand[i])-1)

 
for i in range(5):
    for j in range(5):
        if i!=j and hand[i]+hand[j] == 15:
            points+=(2/2)

for i in range(5):
    for j in range(5):
        for l in range(5):
            if i!=j and j!=l and hand[i]+hand[j]+hand[l] == 15:
                points+=(2/3)

for i in range(5):
    for j in range(5):
        for l in range(5):
            for k in range(5):
                if i!=j and j!=l and l!=k and hand[i]+hand[j]+hand[l]+hand[k] == 15:
                    points+=(2/4)


print(points)
