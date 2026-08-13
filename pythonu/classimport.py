import random
class enemy:
    def __init__(self,name,hp,attack):
        self.__name=name 
        self.hp=hp 
        self.attack=attack 

    def get(self):
        print( self.__name)

    def att(self):
        print("boom")

    def special_att(self):
        print("no special attack")

class zombie(enemy):
    def __init__(self,hp,attack):
        super().__init__(name="zombie",hp=hp,attack=attack)

    def att(self):
        return self.attack

    def special_att(self):
        work=random.random()<0.50
        if work:
            self.hp+=4
            print("zombie gained 2 hp")

class ogre(enemy):
    def __init__(self,hp,attack):
        super().__init__(name="ogre",hp=hp,attack=attack)

    def att(self):
       return self.attack

    def special_att(self):
        work=random.random()<0.20
        if work:
            self.attack+=4
            print("ogre gets stronger")

class weapon:
    def __init__(self,weapon,attack):
        self.weapon=weapon
        self.attack=15

class hero(weapon):

    def __init__(self,hp,attack):
        self.hp=hp
        self.attack=attack
        self.weapon_equipped=False
        self.weapon: weapon=None

    def weaponequip(self,wepon,attack):
        if self.weapon is not None and not self.weapon_equipped:
            self.attack=self.weapon.attack
            self.weapon_equipped=True




"""
class enemystats:

    name : str
    hp:int 
    att:int

    def __init__(self,a,b,c):                             # parametrisized constructur
        self.__name=a                                     # make a variable private using  "__" int the ront of a variable
        self.hp=b
        self.att=c
    def talk(self):                                       # abstraction     
        print(f"i am {self.__name}")
    def attck(self):
        print("hollow purpul 200%")

    def domain(self):
        print("domain expansion infinite void")
     
    def get(self):                                        # to access or see the value in the variable
        return  self.__name

"""









"""
    default constructur
    def __init__(self):
        pass
"""



"""
    no argument constructure
    def __init__(self):
        print("hello")
"""



""" 
    name : str
    hp:int 
    att:int
    def __init__(self,a,b,c):  #parametrisized constructur
        self.name=a
        self.hp=b
        self.att=c
"""