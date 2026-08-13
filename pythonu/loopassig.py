days=["monday","tuesday","wednesday","thursday","friday"]
i=0
while i<3:
    i+=1
    for x in days:
        print("---------")
        if x=="monday":
            continue
        print(x)
    if i<3:
        continue
    else:
        break;