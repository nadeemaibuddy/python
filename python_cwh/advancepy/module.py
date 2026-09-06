def myfun():
    print("hello world")

myfun()
print(__name__) #__name__ show the name main if wwe are running it in the file which it is written 
                #it show file name if the file is imported and executed

if __name__ =="__main__":
    #if this code is directly exected by running the file its present in
    print("we are directly running this code")
    myfun()
    print(__name__)