"""
import random
computer=random.randint(1,3)
print("1 FOR SNAKE \n2 FOR WATER \n3 FOR GUN")
user=int(input("enter your choice"))
if user in [1,2,3]: 
    if user==computer:
        print("DRAW")
    elif user==1 and computer==2:
        print("user win")
    elif user==2 and computer==3:
        print("user win")
    elif user==3 and computer==1:
        print("user win")
    elif computer==1 and user==2:
        print("you lose")
    elif computer==2 and user==3:
        print("you lose")
    elif computer==3 and user==1:
        print("you lose")
else:
    print("invalid choice")
"""

import random
computer = random.choice([1,2,3])
yous=input("ENTER s FOR SNAKE\nENTER w FOR WATER\nENTER g FOR GUN\n")
choice={"s":1,"w":2,"g":3}
rchoice={1:"snake",2:"water",3:"gun"}
you=choice[yous]
print(f"you choose :{rchoice[you]}\ncomputer choosen :{rchoice[computer]}")
if you==computer:
    print("Draw")
else:
    if you==1 and computer==2:
        print("YOU WIN")
    elif you==2 and computer==3:
        print("YOU WIN")
    elif you==3 and computer==1:
        print("YOU WIN")
    elif computer==1 and you==2:
        print("YOU LOSE")
    elif computer==2 and you==3:
        print("YOU LOSE")
    elif computer==3 and you==1:
        print("YOU LOSE")
    else:
        print("somthing went wrong")
    