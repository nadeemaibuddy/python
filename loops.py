#loops
#execute block of code or statement the number of time we want
"""
print(1)
print(2)
print(3)
print(4)

#same task can be done by

for i in range(1,6):
    print(i)
"""

"""
#while loop
i=1
while(i<5):    #execut the block until the condition is true
    print(i)
    i +=1

ls=[1,2,3,4,5]
i=0
while(i<len(ls)):
    print(ls[i])
    i+=1


for i in range(0,100,2):  #start:end:increment
    print(i)

#for with list
l=[1,2,3,4,5,6]
for i in l:
    print(i)

#for with tuple
t=(3,5,1,7,3)
for i in t:
    print(i)

#for with strings
s="nadeem"
for i in s:
    print(i)

#for with else
ls=[1,2,3]
for i in ls:
    print(i)
else:
    print("loop completed")  #this is executed when loop is completed

#break
for i in range(100):
    if i==53:
        break    #exit the loop
    print(i)

#continue
for i in range(100):
    if i==53:
        continue   #skips this iteration
    print(i)

for i in range(645):
    pass     # to do nothing

i =0
while(i<345):
    pass    #to do nothing
"""

"""
#practice set

n=int(input("enter any number"))
for i in range(11):
    print(f" {n} x {i} = {n*i}")
"""

"""
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if "s" in name.lower():
        print(f"greetings {name}")

#if name.startwith("S"):
#print("hello {name}")
"""

"""
n=int(input("enter a number"))
i=0
while(i<11):
    print(f"{n} x {i} = {n*i}")
    i+=1
"""
"""
n=int(input("enter a number"))
i=1
p=0
while(i<n):
    if n%i==0:
        p+=1
    i+=1
if p<=2:
    print("prime")
else:
    print("not prime")
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
    else:
        print("prime")
"""
"""
n=int(input("enter a number "))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)
"""

"""
# 5!=1x2x3x4x5
n=int(input("enter a number"))
fac=1
for i in range(1,n+1):
    fac=fac*i
print(fac)
"""

"""
   *
  ***
 *****

n=int(input("entr a value"))
for i in range(1,n+1):
    print(" "*(n-i),"*"*((2*i)-1))            
"""
"""
*
**
***
n=int(input("entr a value"))
for i in range(1,n+1):
    print("*"*i)
"""
"""
* * *
*   *
* * *

n=int(input("entr a value"))
for i in range(1,n+1):
    if i%2!=0:
        print("*","*","*")
    else:
        print("*"," ","*")


n=int(input("entr a value"))
for i in range(1,n+1):
    if i==1 or i==n:
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*")

"""

"""
n=int(input("enter a number "))
for i in range(1,11):
    print(f"{n} x {11-i}={n*(11-i)}")
"""


"""
*****
****
***
**
*
n = 5
for i in range(n):
    print("*" * (n - i))

     *
    **
   ***
  ****
 *****
n=5
for i in range(1,n+1):
    print(" "*(n-i),"*"*i)
"""
