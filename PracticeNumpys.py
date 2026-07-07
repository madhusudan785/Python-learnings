import numpy as np

# a=np.array([1,2,3],dtype='int8')

# b=np.array([4,5,6])

# print(a.shape)

# print(a.ndim)

# print(a.size)

# print(a+b)
# print(a.itemsize)

# arr=np.arange(0,26,5)
# print(arr)
# result=np.full((3,4),7)
# print(result)
# print(np.identity(5))
p=np.array([
[10,20,30],
[40,50,60],
[70,80,90]
])
# print(p[1,1])
# print(p[:,1])
# print(p[2,:])
# print(p[:,-1])
q=np.array([
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
])
# print(q[0,1:])
# print(q[1,1:-1])
# print(q[:,2])
# print(q[:,0])


a = np.array([[1,2],
              [3,4]])

b = np.array([[5,6],
              [7,8]])

print(a * b)
#-----------------DOT Product --------------#
print(np.dot(a,b))