#arrays, strings, loops, functions, dictionaries, and basic algorithms



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