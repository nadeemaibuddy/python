with open("this.txt") as f:
    content=f.read()

with open("copyofthis.txt") as f:
    content2=f.read()

if content ==content2 or content in content2:
    print("this two files are identical")
else:
    print("this two files are not identical")