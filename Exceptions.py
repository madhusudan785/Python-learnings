# try:
#     f=open("newFi_le.txt")
#     # if f.name=="newFile.txt":
#     #     raise Exception #we can use raise keyword for our custom exception

# except Exception as e:
#     print("error")
# else:
#     print(f.read())
#     f.close()
# finally:
    # print("no matter what it will execute ")

# with open("newFile.txt","r") as file:# as file.txt not exit and we are trying to open in read mode it will show us error
#         data=file.read()
#         print(data)
# try:
#     print("A")
#     x = 10 / 2
#     print("B")
# except:
#     print("C")
# finally:
#     print("D")
# try:
#     print("Start")
#     x = 10 / 0
#     print("Middle")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:
#     print("End")
# try:
#     print(name)
# except Exception as e:
#     print(e)
def divide(a, b):
    try:
        divide=a/b
        return divide
    except:
        print("You are dividing a value with 0")
    finally:
        print("Operation Finished")

print(divide(12,0))












