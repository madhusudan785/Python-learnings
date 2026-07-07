import numpy as np

a=np.array([1,2,3,4],dtype='int32')#1D array
b=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])#2D array

#get a specific[start_index,stop_index,step_size]
print(b[0,1:6:3])

c=np.array([[[1,2],[3,4],[4,5],[6,7]]])

# print(c)
# print(c[0,3,0])
# print(c.ndim)

        #row,column
# print(b[1,2])
# print(b[0,:])#1st row or 0th index row in b
# print(b[:,2])#get a specific column
# print(a.ndim)#no of dimensions
# print(b.ndim)

# print(a.shape)#no of rows and columns
# print(b.shape)

# print(a.dtype)#actual type the data stored we can also specify at beginning
# print(b.dtype)

# print(a.itemsize)#get item size
# print(b.itemsize)

# print("#get size")
# print(a.size)#get size
# print(b.size)


#initialization of empty array same goes for ones()
d=np.zeros((3,4)) # mention the dimensions
# print(d)
#any other value
# e=np.full((5,5),1,dtype="float32")
# print(e)
#passing random numbers
# print(np.random.rand(2,4))
# print(np.random.random_sample(e.shape))
# print(np.random.randint(100,size=e.shape))#why this line shows error it need a size and am passing a shape directly e.shape

# print(np.identity(3))

#----------repeat an array
# arr=np.array([[1,2,3]])
# r=np.repeat(arr,3, axis=0)
# print(r)
            
arr=np.ones((5,5))
z=np.zeros((3,3))
z[1,1]=9
arr[1:-1,1:4]=z
print(arr)
print(z)
student_marks = np.array([
[90,80],
[85,92],
[78,81]
])
print(student_marks.shape)
