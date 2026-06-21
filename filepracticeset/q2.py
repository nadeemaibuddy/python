import random

def game():
    print("your palying game")
    score=random.randint(1,100)
    print(f"your score = {score}")
    with open("score.txt") as f:
        highscore=f.read()
        if highscore=="":
            highscore=0
        else:
            highscore=int(highscore)
    with open("score.txt","w") as f:
        if score>highscore:
            f.write(str(score))
        
game()