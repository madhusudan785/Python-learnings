list = [1,21,221,True,11,15.5,"milan"]#we can store any data in a single list
print(type(list),list)
#list is mutable unlike strings we can access and change the values
print(list[0])
list[0]="Milan"
print(list)
#list slicing is possible like strings
print(list[2:4])
list1=[10,20,12,13,24,11,21,22]
list1.insert(4,32)
print(list1)
# list1.append(1.2)
# print(list1.append(1.2))#these function with list
#return None when we are initializing for the first time
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
list1.reverse()
print(list1)
list2=[1]
print(list2)

movies=[]
# movies.extend(input("enter movies name:"))
# movies.append(input("enter movies name:"))
# print(movies)
# list.remove(1000)
print(list)
list.append(list1)
print(list)

