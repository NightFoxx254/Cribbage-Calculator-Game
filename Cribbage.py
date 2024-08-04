import random
#Setting up the hand
hand = []
points = 0
for i in range(4):
    print("Please input a card from your hand.")
    hand.append(int(input(">")))
hand.append(random.randint(1,10))
print(hand)

# #checking for pairs
# for i in range(5):
#     points+= (hand.count(hand[i])-1)
# print(points)
#
# #checking for fifteens in two cards
# for i in range(5):
#     for j in range(5):
#         if i!=j and hand[i]+hand[j] == 15:
#             points+=(2/2)
# print(points)
#
#
# #checking for fifteens in three cards
# for i in range(5):
#     for j in range(5):
#         for l in range(5):
#             if i!=j and j!=l and hand[i]+hand[j]+hand[l] == 15:
#                 points+=(2/3)
# print(points)
#
# #checking for fifteens in four cards
# for i in range(5):
#     for j in range(5):
#         for l in range(5):
#             for k in range(5):
#                 if i!=j and j!=l and l!=k and hand[i]+hand[j]+hand[l]+hand[k] == 15:
#                     points+=(2/4)
# print(points)
#
# #checkiong for fifteens in all the cards
# if hand[0]+hand[1]+hand[2]+hand[3]+hand[4] == 15:
#     points+=2

#checking for runs of 3
newHand = []
smallNum = 11

for i in range(5):
    if hand[i] < smallNum:
        smallNum = hand[i]
        hand.pop(i)
newHand.append(smallNum)

smallNum = 11
for i in range(4):
    if hand[i] < smallNum:
        smallNum = hand[i]
        hand.pop(i)
newHand.append(smallNum)

smallNum = 11
for i in range(3):
    if hand[i] < smallNum:
        smallNum = hand[i]
        hand.pop(i)
newHand.append(smallNum)

smallNum = 11
for i in range(2):
    if hand[i] < smallNum:
        smallNum = hand[i]
        hand.pop(i)
newHand.append(smallNum)

newHand.append(hand[0])
hand.pop(0)


print(newHand)
