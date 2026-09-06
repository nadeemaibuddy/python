#class
#basic syntax
# class employee:
#     language ="py"      #class attribute
#     salary =16000000    #as it belong to class
# r1=employee()
# r1.name="nadeem"        #name is object attribute(instance attribute)
# print(r1.name,r1.salary,r1.language)
# r2=employee()
# r2.name="owes"
# print(r1.name,r2.salary,r2.language)



#4 pillers of oops
# Encapsulation - Keeps data safe by locking it inside a class and allowing access only through special methods.
# Abstraction   - hiding the work done
# Inheritance   - inheriting the propertys of other class
# Polymorphism  - Allows the exact same method name to perform different actions based on the object using it





#first object(instance) attribute is given preference
# class employee:
#     language ="py"      
#     salary =16000000    
# r1=employee()
# r1.language="java"           
# print(r1.salary,r1.language) #first checks  in object


# #self key word ad function in class
# class employee:
#     language ="py"      
#     salary =16000000    
#     def getinfo(self):
#         print(f" {self.language} {self.salary}")
    
#     def greet(self):
#         print("good morning")
# r1=employee()
# r1.name="nadeem"        
# r1.getinfo()    #->employee.getinfo(r1)
# r1.greet()


##static method
# class employee:
#     language ="py"      
#     salary =16000000    
#     def getinfo(self):
#         print(f" {self.language} {self.salary}")    
#     @staticmethod
#     def greet():
#         print("good morning")
# r1=employee()
# r1.name="nadeem"        
# r1.getinfo()   
# r1.greet()


# #constructor _init_
# class employee:
#     language ="py"      
#     salary =16000000   
#     def __init__(self,name,lang,sal):         #runs automatical(called when an object is created)   "dunder method"
#         print("i am creating an object")
#         self.name=name
#         self.language=lang
#         self.salary=sal 
#     def getinfo(self):
#         print(f" {self.language} {self.salary}")
    
#     def greet(self):
#         print("good morning")
# r1=employee("nadeem",16000000,"java")       
# r1.getinfo()    
# r1.greet()


# class programmer:
#     company="microsoft"
#     def __init__(self,name,language,salary):
#         self.name=name
#         self.language=language
#         self.salary=salary
#     def showdetails(self):
#         print(f"name :{self.name}\nlanguage: {self.language} \nsalary: {self.salary}")


# e1=programmer("nadeem","py",16000000)
# e2=programmer("arsalan","java",1600000000)
# e1.showdetails()
# e2.showdetails()

# class calculator:
#     def square(self,n):
#         print(f"square ={n**2}")
#     def cube(self,n2):
#         print(f"cube ={n2**3}")
#     def squareroot(self,n3):
#         print(f"squareroot ={n3**(1/2)}")
# obj=calculator()
# obj.square(10)
# obj.cube(10)
# obj.squareroot(16)

# class calculator:
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         print(f"square ={self.n**2}")
#     def cube(self):
#         print(f"cube ={self.n**3}")
#     def squareroot(self):
#         print(f"squareroot ={self.n**(1/2)}")

# obj=calculator(10)
# obj.square()
# obj.cube()
# obj.squareroot()

# class attribute:
#     n=10

# obj=attribute()
# print(obj.n)  #prints the class attrinute as instance attribute is not set
# obj.n=20 
# print(obj.n)  ##prints the instance attrinute as instance attribute is  set
# print(attribute.n)

# class calculator:
#     def __init__(self,n):
#         self.n=n
#     @staticmethod
#     def greet():
#         print("hello")
#     def square(self):
#         print(f"square ={self.n**2}")
#     def cube(self):
#         print(f"cube ={self.n**3}")
#     def squareroot(self):
#         print(f"squareroot ={self.n**(1/2)}")

# obj=calculator(10)
# obj.greet()
# obj.square()
# obj.cube()
# obj.squareroot()

# class train:
#     def __init__(self):
#         print("too book ticket enter your name and from and to address and tainno")
#         print("too know status enter train no")
#         print("to know the fair enter train no and from and to address")
#     def ticket(self,name,from1,to,trainno):
#         print(f"name :{name}\nfrom :{from1} to\n{to}")
#         print(f"your ticket is booked in tainno {trainno}")
#     def status(self,traino):
#         print(f"200 seats are left in tain no{traino}")
#     def fair(self,trainno,fro,to):
#         print(f"trian no {trainno} {fro} to {to} -75 ruppes")

# obj=train()
# obj.ticket("nadeem","nzb","kac",1234)
# obj.status(1234)
# obj.fair(1234,"nzb","kac")


# class demo:
#     def __init__(slf,name):
#         slf.name=name
#     def s(slf):
#         print(slf.name)    #changing self to slf or any other name does not effect the program
    
# obj=demo("nadeem")
# obj.s()
# obj.name="harry"
# obj.s()

