def calculater(homework_arg):
    sum=0
    for i in homework_arg.values():
        sum+=i
    final=round(sum/len(homework_arg),2)
    print(final)
