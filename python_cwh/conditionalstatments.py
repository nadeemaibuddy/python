"""#condition  
#execut a block of code based on condition

a = int(input("enter your age"))

if a>=18:
    print("your eligible")
elif a<0:
    print("you are entering invalid age")
else:
    print("your not eligible")

print("end of program")


#relation & logical
==
>=
<=
and 
or
not

"""
"""
n1=int(input("enter a number"))
n2=int(input("enter a number"))
n3=int(input("enter a number"))
n4=int(input("enter a number"))
if n1>n2 and n1>n3 and n1>4:
    print("n1 is greater number")
elif n2>n1 and n2>n3 and n2>n4:
    print("n2 is greater number")
elif n3>n1 and n3>n2 and n3>n4:
    print("n3 is greater number")
else:
    print("n4 is greater number")
"""
"""
m1=int(input("enter your 1 shbject marks"))
m2=int(input("enter your 1 shbject marks"))
m3=int(input("enter your 1 shbject marks"))
t=m1+m2+m3
tp=(t/300)*100
if tp>=40 and (m1/100)*100 >=33 and (m2/100)*100 >=33 and (m3/100)*100 >=33:
    print("pass")
else:
    print("failed")
"""
"""
text =input("enter your comment")

s1="Make a lot of money"
s2="buy now"
s3="subscribe this"
s4="click this"

if s1 in text and s2 in text and s3 in text and s4 in text:
    print("spam")
else:
    print("normal comment")
"""
"""
user=input("enter name")
l=len(user)
if l < 10 :
    print("username contains less than 10 characters")
else:
    print("username dont contains less than 10 characters")
"""
"""
ls=["nadeem","owes","abdurrab"]
name=input("enter your name")
if name in ls:
    print("your name is in the list")
else:
    print("your name is not in the list")
"""
"""
marks =int(input("enter your marks"))
if 90<=marks<=100:
    print("EX grade")
elif 80<=marks<=90:
    print("A grade")
elif 70<=marks<=80:
    print("B grade")
elif 60<=marks<=70:
    print("C grade")
elif 50<=marks<=60:
    print("D grade")
else:
    print("F grade")
"""

post=input("enter your post")
if "harry" in post.lower():
    print("this post is talking about harry")
else:
    print("this post is not taking about harry")