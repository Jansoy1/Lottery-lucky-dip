import random
#1-50 #1-12
normalfive = open("onetofithty.txt")
powerball = open("onetotwelve.txt")

five = []
two = []
lottery = []
afive = 0
atwo = 5

for a in normalfive:
        a = a.strip()
        five.append(a)
for b in powerball:
        b = b.strip()
        two.append(b)
        
while afive < 5:
        randfive = random.choice(five)
        lottery.append(randfive)
        afive += 1
        if randfive in lottery:
                pass
        else:
                continue

        
while atwo < 7:
        randtwo = random.choice(two)
        lottery.append(randtwo)
        atwo += 1


print(*lottery)
