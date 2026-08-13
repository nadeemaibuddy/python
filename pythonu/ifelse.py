""" you have to give 4 space before writing any statement in  the if or else
you can use only one if and else but many elif statements
"""
x=input("enter number")
if x==6:
    print("you entered 6")
else:
    print("you enter ",x)
"""
 ^
 |
like above
"""
age=int(input("enter age"))
if age>=18 and age<=90:
    print("your eligible to vote")
elif age==17:
    print("you can get  eligible by next year")
else:
    print("your are not eligible to vote")