grade=int(input("enter your marks out of hundred in maths "))
print("your grade according to your marks")
if grade>90 and grade<=100: #90< grade <=100
    print("A keep it up")
elif grade>80 and grade<=90: #80< grade <=90
    print("B almost there you can do it")
elif grade>70 and grade<=80: #70< grade <=80
    print("C try hard")
elif grade>60 and grade<=70: #60< grade <=70
    print("D try hard")
else:
    print("fail F")