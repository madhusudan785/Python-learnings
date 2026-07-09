import numpy as np

#---------Broadcasting-----------#

#it says when we are performing some arithmetic operation with higher higher dimensions array in lower dimensions 
# it will automatically reshape without chaining the entire array
egg=np.array([1,2,3,4])
dig=np.array([5])
print(egg+dig)



#--------Reshape the array------#

before=np.array([[1,2,3,4],[8,9,10,11]])

print(before)

print()

after=before.reshape((2,2,2))
print("reshaped:",after)
print()
before=after.flatten()
print("flatten:",before)
#----------------Vertically stacking---------#

c=np.array([1,2,3,4])
d=np.array([4,5,6,4])
print(c==d)#comparing each element
print(np.array_equal(c,d))#compares the array entirely 
# print(np.vstack([c,d,d]))

# print(np.hstack([c,d]))

# with open("practice.txt","w+")as file:
#         # write the random numbers as a string
#         data=file.write(','.join(map(str, np.random.randint(1,100,(4,10)))))

#---------load data from a file-------#
# filedata=np.genfromtxt('practice.txt',delimiter=',')
# print(filedata)
# filedata=filedata.astype('int32')
# print(filedata)
#-----------Boolean Masking and Adv. indexing----------------#
# print(filedata[filedata>=50])

nums=np.array([1,2,3,4,5,6,7,8,9])

# print(nums[[1,2,8]])#indexing using list


















