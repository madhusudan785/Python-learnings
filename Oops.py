# class Student:
#     college_name="Madhusudan college" #this one is same for all students so this is class attribute and store once in mem
#     name="milansd"#class attr < obj attr (while value is same)
#     def __init__(self,name,marks):
#         self.name=name # this variables are diff for all student obj so this is student obj attribute
#         self.marks=marks 
#         print("Add these parameters to database....")


# s=Student("milan",97)
# print(s.name)
# print(Student.college_name)

# class Student1:
#     def greet(self,name):
#         return "hello", name
# s = Student1()
# print(s.greet("Milan"))

#     # def __init__(self):
#     #     print("Hello this is printing because init method initiated when the object creation happen")

class Student:

    @staticmethod  #this decorator is used when there is no need of obj instance in a method
                   #it takes function as i/p and extend it's behavior and give func as o/p
    def college_name():
        print("Mno institute of tech")

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg_marks(self):
        sum=0
        for val in self.marks:
            sum +=val
        
        return "name is:",self.name,"avg marks:",sum/3


s=Student("madhu",[63,24,45])
x=s.get_avg_marks()
s.college_name()
print(x)

