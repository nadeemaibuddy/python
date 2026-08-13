from classimport import *

def battle(e1:enemy,e2:enemy):
    e1.get()
    e2.get()
    while e1.hp>0 and e2.hp>0:
        print("------")
        e1.special_att()
        e2.special_att()
        e1.get()
        print(f"{e1.hp} hp is left")
        e2.get()
        print(f"{e2.hp} hp is left")
        a=e1.att()
        e2.hp-=a
        b=e2.att()
        e1.hp-=b
        print("------")
        if e1.hp>0:
            print(f"zombie has won")
        else:
            print(f"ogre has won")


def battle(e1:hero,e2:enemy):
    while e1.hp>0 and e2.hp>0:
        print("------")
        e2.special_att()
       
        print(f"{e1.hp} hp is left of hero")
        e2.get()
        print(f"{e2.hp} hp is left")
        
        e2.hp-=e1.attack
        b=e2.att()
        e1.hp-=b
        print("------")
        if e1.hp>0:
            print(f"hero has won")
        else:
            print(f"ogre has won")



Zombie=zombie(100,10)
Ogre=ogre(100,10)

Hero=hero(102,15)
battle(Hero,Zombie)
"""
from classimport import *

obj1=enemystats("gojo",2000,10000)
print(obj1.get())
obj1.talk()
obj1.attck()
obj1.domain()
"""





"""
print(f"{obj1.name} {obj1.att} {obj1.hp}") 
print(f"{obj2.name} {obj2.att} {obj2.hp}") 
obj1=enemystats()
obj1.name="gojo"
obj1.hp=2000
obj1.att=1000000"""