#exception

# try:
#     a=int(input("enter number :"))
#     print(a)
# except ValueError as v:
#     print("heyyy")
#     print(v)
# except Exception as e:
#     print(e)

# print("hey")


# #raise exception

# a=int(input("enter a number"))
# b=int(input("enter second number"))
# if b==0:
#     raise ZeroDivisionError("hey we can divide a number by zero")
# else:
#     print(f"the division a/b is {a/b}")

# #try-else
# try:
#     a=int(input("enter number :"))
#     print(a)
# except Exception as e:
#     print(e)
# else:    #execute only if the try block execute
#     print("else")

# #try-finally
# def main():
#     try:
#         a=int(input("enter number :"))
#         print(a)
#         return
#     except Exception as e:
#         print(e)
#         return
#     finally:    
#         print("finallly")

# main()


#main

# from python.advancepy.module import myfun
# if __name__ =="__main__":
#     #if this code is directly exected by running the file its present in
#     print("we are directly running this code")