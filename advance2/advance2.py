#lambda  function
# def square(n):
#     return n*n
# square =lambda x:x*x  #function in expression form

# sum=lambda a,b,c:a+b+c
# print(sum(1,2,3))
# print(square(5))


# #join
# l=["nadeem","uddin","mohammad"]
# final="_".join(l)
# print(final)



# #formate
# a="{} ia a good {}".format("nadeem","boy")
# print(a)


# #map
# #to run one function for multiple elements
# l=[1,2,3,4]
# square =lambda x:x*x
# sq=map(square,l)
# print(list(sq))

# #filter
# l=[1,2,3,4]
# def even(n):
#     if n%2==0:
#         return True
#     return False

# onlyeven=filter(even,l)
# print(list(onlyeven))

# #reduce
# from functools import reduce
# l=[1,2,3,4]
# def sum(a,b):
#     return a+b

# print(reduce(sum,l))


# name=input("enter your name")
# marks=int(input("enter your marks"))
# number=int(input("enter your number"))

# s="the name of the student is {},his marks are {},and phone number{}".format(name,marks,number)
# print(s)


# l=[str(7*i for i in range(1,11))]

# s="\n".join(l)
# print(s)

# def divisible5(n):
#     if(n%5==0):
#         return 5
    
# l=[1,5,2,7,10,15,17]
# s=filter(divisible5,l)
# print(list(s))

# from functools import reduce
# l=[1,36,5,2,54,7,10,15,17]
# def greater(a,b):
#     if a>b:
#         return a
#     return b

# print(reduce(greater,l))

