#function
#group of statment performing a specific task

"""
a=12
b=45
c=56
average=(a+b+c)/3
print(average)
#function defination
def avg():
    a=int(input("enter your number"))
    b=int(input("enter your number"))
    c=int(input("enter your number"))
    average=(a+b+c)/3
    print(average)
#function call
avg()

def greet():
    name=input("enter your name")
    print(f"good day {name}")
greet()

#type
#built in 
#user define


#argument
def greet(name,end):       #parameter 
    print("good day "+ name)
    print(end)

greet("nadeem","thank")     #argument


#return
def greet(name,end):       
    print("good day "+ name)
    print(end)
    return  "done"

a=greet("nadeem","thank") 
print(a)



#default argument
def greet(name,end="thank you"):
    print(f"good day{name}")
    print(end)
greet("nadeem")
greet("nadeem","done")


#recurssion
def fact(n):
    if n==1 or n==0:   
        return 1
    else:                 #recursive condition
        return fact(n-1)*n
n=int(input("enter a number"))
f=fact(n)
print(f)



def great(a,b,c):
    if a>b and a>c:
        print(f"{a} is bigger number")
        return a
    elif b>a and b>c:
        print(f"{b} is bigger number")
        return b
    else:
        print(f"{c} is bigger number")
        return c
r=great(1,1,3)
print(f"{r} is bigger number")


#c/5=(f-32)/9
#c=5*(f-32)/9

def cel(f):
    return 5*(f-32)/9
n=float(input("enter a temperature in f"))
print(cel(round(n,2)))


print("hello ",end="")
print("world")


def sum(n):
    if n==1 or n==0:
        return 1
    else:
        return n+sum(n-1)
n=int(input("enter a number"))
print(sum(n))


def parten(n):
    if n==0:
        return 1
    print("*"*n)
    parten(n-1)
n=int(input("enter a number"))
parten(n)


#1 inch = 2.54 centimeters (cm)

def i_to_c(n):
    return n *2.54
n=float(input("enter a number"))
print(i_to_c(n))

def rem(l,word):
    n=[]
    for i in l:
        if not(i==word):
            n.append(i.strip(word))
    return n
l=["nadeem","owes","em"]
print(rem(l,"em"))
"""

def table(n):
    for i in range(1,11):
        print(f"{n} x {i} ={n*i}")
n=int(input("enter a number"))
table(n)