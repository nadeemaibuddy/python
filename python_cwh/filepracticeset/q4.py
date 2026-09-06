word ="Donkey"
with open("do.txt") as f:
    content=f.read()

contentnew=content.replace(word,"#####")
with open("do.txt","w") as f:
    f.write(contentnew)

