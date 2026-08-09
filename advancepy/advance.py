# #walrus operator
# #insted of writing 
# #n=len([1,2,3,4,5])
# #if n>3:
# #we use walrus operator 
# #it act as expression and vaiable at he same time
# if (n := len([1, 2, 3, 4, 5])) > 3:
#     print(f"List is too long ({n} elements, expected <= 3)")


# #type def 

# from typing import list,tuple,Union
# num :list[int] =[1,2,3,4,5]
# na :tuple[str,int]=("nadeem",1)

# n :int = 5

# name1 :str   #do declare variable like in c we write int a;
# name: str ="nadeem"  

# def sum(a:int,b :int) ->int:  #take integer value and returns integer value
#     return a+b


# #match case

# def status(status):
#     match status:
#         case 200:
#             return "ok"
#         case 404:
#             return "404 error"
#         case 500:
#             return "server issue"
#         case _:
#             return "unknown status"

# print(status(200))
# print(status(404))
# print(status(500))
# print(status(2001))


# #merge dic

# dic1 ={"a":1,"b":2}
# dic2 ={"b":3,"c":4}

# merge = dic1 | dic2
# print(merge)  #output {'a': 1, 'b': 3, 'c': 4}


# #with in file
# #we can open multiple files
# with (
#     open("file.txt") as f1,
#     open("file.txt") as f2,
# ):
#     pass



# #global keyword
# a=89   #global
# def fun():
#     global a        #it change the value of gobal variable
#     a=3
#     print(a)

# fun()
# print(a)


#enumerate

# l=[3,4,5,6]
# ind=0
# for i in l:
#     print(f"the item number {ind} is {i}")
#     ind+=1
# simlified
# l=[3,4,5,6]
# for index ,item in enumerate(l):
#     print(f"the item number at  index {index} is {item}")

#listcomprehensions

# l=[1,2,3,4,5]

# # squrelist=[]
# # for item in l:
# #     squrelist.append(item*item)
# squrelist=[i*i for i in l]

# print(squrelist)



# try:

#     with(
    
#     open("file.txt") as f1,
#     open("fileio.py") as f2,
#     open("file1.txt") as f3

#    ):
#         pass
# except FileNotFoundError as e:
#     print("file not found")
#     print(e)

# print("hi")


# l=[1,2,3,4,5,6,7,8]

# for ind,i in enumerate(l):
#     if ind==2 or ind==4 or ind==6:
#         print(i)


# n=int(input("enter a number"))

# table=[n*i for i in range(1,11)]
# print(table)

# a=1
# b=0
# try:
#     print(a/b)
# except ZeroDivisionError as e:
#     print("infinity")



def generate(n):
    table=[n*i for i in range(1,11)]
    with open("table111.txt","a") as f:
        f.write(str(table) +"\n")
    
for i in range(1,11):
    generate(i)