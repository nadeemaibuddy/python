"""
#list and tuple are data strcutre in python which store multiple values of different type
#a=[1,2.5,False,"name"]
#list are mutable
num=["apple",2.5,3,4,5] 
print(num[3])

num[3]=6
print(num[3])

print(num[0:4:2])  #staring:ending:increment

#function or method
num1=[5,1,8,3,9]
num1.append(6)        #add an element at the end of string
print(num1) 

num1.sort()           #sort the list in asending(small-big)
num1.reverse()        #sort the list in decinding(big-small)
print(num1)

num1.insert(4,14)     #insert or add an element at the required index
print(num1)

print(num1.pop(3))           #delete an element at particular index 

num1.remove(3)        #remove the specific element
print(num1)


#tuple is immutable

a=(1,)  #for one element in tuple
print(type(a))
a=(1,2.5,45,45)

print(a)

#function or method

print(a.count(45))  #tell the count of a value in the tuple

print(a.index(45))    #return index

"""

"""
fruits=[]

f1=input("enter any fruit name")
fruits.append(f1)
f2=input("enter any fruit name")
fruits.append(f2)
f3=input("enter any fruit name")
fruits.append(f3)
f4=input("enter any fruit name")
fruits.append(f4)
f5=input("enter any fruit name")
fruits.append(f5)
f6=input("enter any fruit name")
fruits.append(f6)
f7=input("enter any fruit name")
fruits.append(f7)

print(fruits)"""

"""
marks=[]
m1=int(input("enter marks of std 1"))
marks.append(m1)
m2=int(input("enter marks of std 2"))
marks.append(m2)
m3=int(input("enter marks of std 3"))
marks.append(m3)
m4=int(input("enter marks of std 4"))
marks.append(m4)
m5=int(input("enter marks of std 5"))
marks.append(m5)
m6=int(input("enter marks of std 6"))
marks.append(m6)
marks.sort()
print(marks)
"""

"""
num=[2,3,4,5]
sum=0
sum+=num[0]
sum+=num[1]
sum+=num[2]
sum+=num[3]
print(sum)
print(sum(num))
"""

"""
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
"""