

class Animal:
     
     def sound(self):
          print("Animal")
class Dog(Animal):
     
     def sound(self):
          print("bark")
class Cat(Animal):
     
     def sound(self):
          print("Mewo")
animals = [
    Dog(),
    Cat()
]

for animal in animals:
    animal.sound()
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     def showDetails(self):
#         return self.name,self.salary

# employee1=Employee("MAdhusudan",200000)
# employee2=Employee("Rajesh",300000)

# print(employee1.showDetails())
# print(employee2.showDetails())

# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def add(self):
#         sum=self.num1+self.num2
#         return sum
#     def sub(self):
#         sum=self.num1-self.num2
#         return sum
#     def multiply(self):
#         sum=self.num1*self.num2
#         return sum

# c = Calculator(10, 5)

# result=c.add()
# print(result)



# class Student:

#     def greet(me):
#         print("Hello")

# s = Student()

# s.greet()
# class Student:

#     def __init__(self, name):
#         self.name = name

# s1 = Student("Madhu")
# s2 = Student("Milan")

# s1.name = "Krishna"

# print(s2.name)
# class Student:

#     college = "ABC"

# s1 = Student()

# s2 = Student()

# #It creates a new instance variable called college only for s1, which shadows the class variable.
# s1.college = "XYZ"

# print(s2.college)