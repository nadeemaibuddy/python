"""
functions
"""

def my_function(a,b):
    print("hello world")
    c=a+b
    print(f"sum is {c}")

my_function(10,20)

def my_name(name,nickname):
    print(f"my name is {name} {nickname}")

my_name("nadeem","arsalan")

def print_colour():
    colour ="blue"
    print(colour)

colour="green"
print(colour)
print_colour()

def number(high,low):
    print(high)
    print(low)

number(high=10,low=3)

"""def multiply(x,y):
    z=x*y
    print(f"product is {z}")

multiply(4,8)"""
def multiply(x,y):
    return x*y
product=multiply(4,8)
print(product)

def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)

number_list=[1,2,3,4,5]
print_list(number_list)

def cost(cost_of):
    return cost_of + tax(cost_of)
def tax(cost_of):
    rate=.03
    return cost_of * rate

finalcost=cost(50)
print(finalcost)