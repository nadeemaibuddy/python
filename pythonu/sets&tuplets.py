
"""sets are a type of unordered list which cannot contain duplicate data or repeated data"""
my_set={1,2,3,4,5,1,2}
print(my_set)
print(len(my_set))
"""to remove an element in a set"""
my_set.discard(2)
print(my_set)
"""to add one  elements"""
my_set.add(6)
print(my_set)
"""add more than one elements in set at a time"""
my_set.update([10,20])
print(my_set)
"""to remove all elements"""
my_set.clear()
print(my_set)
"""used when to remove duplication and arrange data"""
"""tuple is an ordered list which cannot be changed,cannot add any element"""
my_tuple=(1,2,3,4,5)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[1])
"""
numbers ={1,4,2,1,7,3,4,2}
print(numbers)
numbers.add(8)
print(numbers)
numbers.discard(2) #or remove
print(numbers)
numbers.update([3,9])
print(numbers)
numbers.clear()
print(numbers)
add,update,discard or remove,clear
"""
