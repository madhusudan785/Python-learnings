# input output operation
file=open("demo.txt","r")
data=file.read() 
data1=file.readline()#read one line at a time
print(data)
print(type(data))
file.close()
with open("practice.txt","r") as file:
    data=file.read()
    print(data)

file1=open("practice.txt","r+")
#when we have to change things from starting we will use this r+
file1=open("practice.txt","w+")#it will truncate/wipe the data first then it will new data
file1.write("this")
print(file1.read())
file1.close()






