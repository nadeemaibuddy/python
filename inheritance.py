#inheritance
# class employee:
#     company="microsoft"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")

# class programmer:
#     company="google"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")

#     def showlan(self):
#         print(f"the name is {self.name} and he is good with {self.language} languagge")
# a=employee()
# b=programmer()
# print(a.company,b.company)

#insted of this

# class employee:   #base class (parent class)
#     company="microsoft"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")
# class programmer(employee):    #child class(derived class)
#     company="google"
#     def showlan(self):
#         print(f"the name is {self.name} and he is good with {self.language} languagge")
# a=employee()
# b=programmer()
# print(a.company,b.company)


# class employee:   
#     name="none"
#     company="microsoft"
#     def show(self):
#         print(f"the name is {self.name} and the company is {self.company}")

# class coder:
#     language ="python"
#     def printlan(self):
#         print(f"out of all the lang here is your language {self.language}")

# class programmer(employee,coder):    #multiple inheritance
#     company="google"
#     def showlan(self):
#         print(f"the name is {self.company} and he is good with {self.language} languagge")
# a=employee()
# b=programmer()
# print(a.company,b.company)
# b.show()
# b.printlan()
# b.showlan()

##mutilevel
# class employee:
#     a=1

# class programmer(employee):
#     b=1

# class manager(programmer):
#     c=3

# o=employee()
# print(o.a) #prints a
# # print(o.b) #gives error

# o1=manager()
# print(o1.a,o1.b,o1.c)

# #super method
# class employee:
#     def __init__(self):
#         print("employee constructer")
#     a=1

# class programmer(employee):
#     def __init__(self):
#         super().__init__()
#         print("programmer constructer")
#     b=1

# class manager(programmer):
#     def __init__(self):
#         super().__init__()
#         print("manager constructer")
#     c=3

# o=employee()


# o1=manager()
# print(o1.a,o1.b,o1.c)


# #class method
# class employee:
#     a=1
#     @classmethod     #shows class attribute  
#     def show(cls):
#         print(f"the class value of a is {cls.a}")

# e=employee()
# e.a=45

# e.show()


# #property decorator
# class employee:
#     a=1

#     @classmethod     #shows class attribute  
#     def show(cls):
#         print(f"the class value of a is {cls.a}")

#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
    
#     @name.setter
#     def name (self,value):
#         self.fname=value.split(" ")[0]
#         self.lname=value.split(" ")[1]
        
# e=employee()
# e.a=45
# e.name="nadeem uddin"
# print(e.name)
# print(e.fname,e.name)
# e.show()

# #dunder methods (operator overloading)
# class number:
#     def __init__(self,n):
#         self.n=n

#     def __add__(self,num):
#         return self.n+num.n
# n=number(1)
# m=number(2)

# print(n+m)


# class twodvector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def show(self):
#         print(f"vector is {self.i}i +{self.j}j")

# class threedvector(twodvector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def show(self):
#         print(f"vector is {self.i}i +{self.j}j +{self.k}k")
# a=twodvector(1,2)
# a.show()
# b=threedvector(1,2,3)
# b.show()

# class animals:
#     pass

# class pets(animals):
#     pass

# class dog(pets):
#     @staticmethod
#     def bark():
#         print("bhaww")
 
# obj=dog()
# obj.bark()

# class employee:
#     salary=1000
#     increment=50
#     @property
#     def salaryafterincrement(self):
#         return self.salary+self.salary*(self.increment/100)

#     @salaryafterincrement.setter
#     def salaryafterincrement(self,salary):
#         self.increment=((salary/self.salary)-1)*100
        
# e=employee()
# e.salaryafterincrement=1500
# print(e.increment)

# class complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i
        
#     def __add__(self, num):
#         return complex(self.r+num.r,self.i+num.i)
#     def __mul__(self, num):
#         real = self.r * num.r - self.i * num.i
#         imag = self.r * num.i + self.i * num.r
#         return complex(real, imag)

#     def __str__(self):
#         return f"{self.r}+{self.i}i"
# n=complex(1,2)
# m=complex(3,4)
# print(n+m)
# print(n*m)
