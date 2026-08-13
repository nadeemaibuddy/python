user_dictionary={
    "name":"nadeem",
    'age':'17'
}
#add elements
user_dictionary['married']=False
#print whole dictionary
print(user_dictionary)
#copy1
user_dictionary2=user_dictionary
user_dictionary2.pop("name")
print(user_dictionary2)
#copy2
"""
user_dictionary2=user_dictionary.copy()
user_dictionary2.pop("name")
print(user_dictionary2)
"""
#print dictionary using for loop
for x,y in user_dictionary.items():
    print(x,y)
#print indivitual element
print(user_dictionary.get('name'))
#lent of dictionary
print(len(user_dictionary))
#remove an element from dictionary
user_dictionary.pop("age")
#clear whole dictionary
user_dictionary.clear()
print(user_dictionary)
#delete whole dictionary
del user_dictionary


"""
data ={
    "gojo" :"infinite void",
    "sukuna" : "malevolent shrine",
}
data1=data
print(data1)
print(data.get("gojo"))
print(data)
data["yuji"]="black flash"
print(data)
data["gojo"] = "stronger than sukuna"
print(data)
data.pop("yuji")
print(data)
print(type(data))
print(len(data))
data.clear();
print(data)
del data
# clear,pop,get,del
"""