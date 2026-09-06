"""#string is data type
#imutable

a ='nadeem'
b="nadeem"
c=""nadeem""

name=a[0:4]   #stating :ending:increment(back word start from  -1)
print(name)
print(len(a))
print(a[-5:-1])
print(a[1:]) #same as a[1:6]
print(a[:4]) #same as a[0:4]

print(a[1:6:2])


print("hi\n i am nadeem") #\n new line
#\t tab
# \"\" 


#function or method
print(len(a))
print(a.endswith("eem"))
print(b.startswith("na"))
print(c.capitalize()) #only captilize only first letter
print(a.lower())
print(b.upper())
print(a.count("e"))
print(a.find("a"))
print(a.replace("nadeem","NADEEM"))



name1=input("enter your name")
print(f"good afternoon {name1}")

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>",name1).replace("<|Date|>","16-06-2026"))

text="hello world  hi world"
print(text.find("  "))
print(text.replace("  "," "))

letter1 = "Dear Harry,\nthis python course is nice.\nThanks!"
print(letter1)

"""