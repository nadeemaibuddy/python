import random

ran=random.randint(1,100)

user=int(input("guess the number"))
n=1
guess=0
while(n==1):
    user=int(input("guess the number:"))
    guess+=1
    if user==ran:
        print(f"you guess is correct .the number was {ran}")
        print(f"you took {guess} attempts to guess the number")
        break
    elif user>ran:
        print("lower number please")
    elif user<ran:
        print("higher number please")

