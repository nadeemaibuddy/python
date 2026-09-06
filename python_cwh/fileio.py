#file i/o
"""
f=open("file.txt")  #open("file name","mode") default open("filename","r")
data=f.read()
print(data)
f.close()
"""


"""
#writing in file
#it remove the current data from the file and add the given data(text)
text="i am nadeem .i am doing good"
f=open("myfile.txt","w")
f.write(text)
f.close()
"""


"""
#it add the text or data at the end of the file with out earising old data(text)
text="hello world"
f=open("myfile.txt","a")
f.write(text)
f.close()
"""
"""
f=open("file.txt")

#return lines in the form of list
#lines = f.readlines()
#print(lines,type(lines))

#read line by line
line=f.readline()
print(line)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)
f.close()

f=open("file.txt")
line=f.readline()
while line !="":
    print(line)
    line=f.readline()
f.close()
"""

#with statment
f=open("file.txt")
print(f.read())
f.close()
#same can be written in 
with open("file.txt") as f:
    f.read()