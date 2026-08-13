my_list=[1,2,3,4,5]
""" 
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
"""
sum=0
for iterartor in my_list:
    sum+=iterartor 
    print(iterartor)
print("sum=",sum)
# for i in range(3,6):
#   print(i)
days=["monday","tuesday","wednesday","thursday","friday"]
for i in days:
    print(f"today is {i}")

#while
x=0
while x <=6:
    x+=1
    if x==3:
        continue # go at the starting of the loop
    if x==6:
        break    # stop the loop

    print(x)