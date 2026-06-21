word=["Donkey","bad","cheater"]
with open("do.txt") as f:
    content=f.read()
for i in word:
    content=content.replace(i,"#"*len(i))
with open("do.txt","w") as f:
        f.write(content)