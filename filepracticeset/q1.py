"""f=open("poem.txt")
line=f.readline()
while line!="":
    if "twinkle" in line:
        print("yes the file contain the world twinkle")
        break
    line=f.readline()
f.close()
"""
f=open("poem.txt")
con=f.read()
if "twinkle" in con:
    print("yes")
else:
    print("not")
f.close()