"""
#dictonary are the collection of key value pair
#it is mutable
#cant contain duplicates

#d={} for empty dic
marks ={
    "nadeem":100,
    "nadee":99,
    "nade":98
}
print(marks,type(marks))

print(marks["nadeem"]) #cant use normal index like list and tuple insted of it use key to get value

#function or method

print(marks.items())  #return all items
print(marks.keys())   #return keys
print(marks.values()) #return values
marks.update({"nadeem":99})  #update values
print(marks)
print(marks.get("nadeem"))  #return required value
print(marks.get("someone")) #return none if the value is not in dic
#print(marks["someone"]) return error
"""

"""
#set is collection of values it does not contain duplicate

s={1,2,2,32,"name"}
print(s)
#e=set() to create mpty set
#it is unorder
#cant access  using index
#function or method
s.add(5)
print(s)
print(len(s))

s.remove(2)  #remove any element
print(s)

s.pop() #remove random elements
s.clear #empty our set

#union
#return all values from both sets with out duplicate
s1={1,2,3,4,5}
s2={6,7,8,1,9}
print(s1.union(s2))
#intersection
print(s1.intersection(s2))

"""
"""
hindi={
    "chawal":"rice",
    "aam":"mango",
    "jaam":"guava"
}
print(hindi)
word=input("enter the word which meaning you wantyou want")
print(hindi[word])
"""
"""
s=set()
s1=int(input("enter a number :"))
s.add(s1)
s2=int(input("enter a number :"))
s.add(s2)
s3=int(input("enter a number :"))
s.add(s3)
s4=int(input("enter a number :"))
s.add(s4)
s5=int(input("enter a number :"))
s.add(s5)
s6=int(input("enter a number :"))
s.add(s6)
s7=int(input("enter a number :"))
s.add(s7)
s8=int(input("enter a number :"))
s.add(s8)
print(s)
"""
"""
s={18,'18'}
print(s,type(s))
"""
"""
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))
"""
"""
s = {}
print(type(s))
"""
"""
name={}
nf1=input("enter your name")
f1=input("enter your language")
name.update({nf1:f1})
nf2=input("enter your name")
f2=input("enter your language")
name.update({nf2:f2})
nf3=input("enter your name")
f3=input("enter your language")
name.update({nf3:f3})
nf4=input("enter your name")
f4=input("enter your language")
name.update({nf4:f4})
print(name)
"""
"""
s = {8, 7, 12, "Harry", [1,2]}
s.update({[1,2],[3,4]})
print(s)
cant do
"""