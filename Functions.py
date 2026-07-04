def add(*number):#Collect positional arguments as tuple
    print(number)

add(10,20,30)

def student(**details):#Collect keyword arguments as dictionary
    print(details)

student(name="Madhu",
    age=23,
    city="Cuttack")
