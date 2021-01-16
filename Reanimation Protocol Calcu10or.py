import random
import math


dead = input("How many models were slain?") 
wounds = input("How many wounds did each model have?") 

dice = int(dead) * int(wounds) 

y= 0 
yourlist = [0] * (int(dead) + 1)

while y <= 10000:
    a = 0

    for _ in range(dice):
       result = random.randint(1,6)
       if result >= 5: a += 1

    getup = math.floor( a / int(wounds) )
    yourlist[getup] += 1
    y += 1

print(yourlist)


dead2 = input("How many models were slain?") 

z= 0
yourlist1 = [0] * (int(dead2) + 1)

while z <= 10000:
    b = 0

    for _ in range(int(dead2)):
       result = random.randint(1,6)
       if result >= 5: b += 1

    yourlist1[b] += 1
    z += 1

print(yourlist1)