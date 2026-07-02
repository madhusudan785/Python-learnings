'''print("hello world")
x='Madhusudan Sahoo' #""
print(len(x))#length
print(x[:2])#slicing
print(x.lower())
print(x.upper())#like this more function are there find,count etc.
x=x.replace('Madhusudan','Milan')
print(x)
'''
greeting="hello"
name="milan"
# message=greeting+" "+name+". welcome"
# message='{},{} .welcome'.format(greeting,name)
message=f'{greeting}, {name.upper()} .welcome'
print(message)
print(dir(name))

#taking input from user
fname=input("user name is:")
print(f'{fname},welcome')