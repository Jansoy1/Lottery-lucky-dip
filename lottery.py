import random
import time


print("Do you think you can guess the lottery numbers?")
time.sleep(2)
print("You will have to choose five normal numbers between 1-50 and two star numbers between 1-12")
time.sleep(2)
print("Good Luck!\n")
aFive = []
aStar= []
five = []
star = []
star_match = []
five_match = []
def a():
    while len(aFive) < 5:
        lottery_ticket = int(input(("Please enter your lottery numbers: ")))
        if lottery_ticket < 1 or lottery_ticket > 50:
            print("Enter amount between 1 - 50")
            continue
        while lottery_ticket not in aFive:
            aFive.append(lottery_ticket)
            print(aFive)
            aFive.sort(reverse=False)
    
    while len(aStar) < 2:
        star_numbers = int(input(("Please enter your star numbers: ")))
        if star_numbers < 1 or star_numbers > 12:
            print("Enter amount between 1 - 12")
            continue
        while star_numbers not in aStar:
            aStar.append(star_numbers)
            print(aStar)
            aStar.sort(reverse=False)
    print("")
        
    
    time.sleep(2)
    print("""
prize break down:
Match 5 + 2 stars = £1,000,000
Match 4 + 2 stars  = £500,000
Match 4 + 1 star = £250,000
Match 4 = £100,00
Match 3 = £1,000
Match 2 = £500""")
    print("")
    start()
def start():
    while len(five) < 5:
        firstFive = random.randint(1,50)
        if firstFive not in five:
            five.append(firstFive)
            five.sort(reverse=False)
    while len(star) < 2:
        starNum = random.randint(1,12)
        if starNum not in star:
            star.append(starNum)
            star.sort(reverse=False)
            
    print("Your numbers:",*aFive, "  star numbers*=",*aStar)
    print("")
    print("Winning lottery numbers:",*five,"  star numbers*=",*star)
    print("")
    results()

def results():
    for line in star:
        if line in aStar:
            star_match.append("a")
    for fline in five:
        if fline in aFive:
            five_match.append("a")
            
    time.sleep(2)    
    print("Normal matches =",len(five_match))
    print("Star number matches =", len(star_match))
    time.sleep(2)
    if len(five_match) == 5 and len(star_match) == 2:
        print("You have won £1,000,000")
    elif len(five_match) == 4 and len(star_match) == 2:
        print("You have won £500,000")
    elif len(five_match) == 4 and len(star_match) == 1:
        print("You have won £250,000")
    elif len(five_match) == 4:
        print("You have won £100,000")
    elif len(five_match) == 3:
        print("You have won £1,000")
    elif len(five_match) == 2:
        print("You have won £500")
    else:
        print("no luck today")
    play()
        
def play():
    ply = input("would you like to try again: yes/no = ")
    if ply == "yes":
        aFive.clear()
        aStar.clear()
        five.clear()
        star.clear()
        star.clear()
        five.clear()
        a()
    elif ply == "no":
        quit()
    
a()
