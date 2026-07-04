class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass # here __ is used to keep the variable private
    def reset_pass(self,reset_passwd):
        self.__reset_passwd=reset_passwd
        self.__acc_pass=self.__reset_passwd
        print(self.__acc_pass)

acc=Account(12345,"Madhu@34")
# print(acc.acc_no)
# acc.reset_pass("Madhu@12")

#how to change the class 
class Student:
    def __init__(self,phy,chm,math):
        self.phy=phy
        self.chm=chm
        self.math=math
    @property # this is used when we have a property which can change when other attr changes
    def percentage(self):
        return str((self.phy+self.chm+self.math)/3) +"%"


s=Student(99,56,76)
print(s.percentage)
s.chm=78
print(s.percentage)


#  name="unknown"
    # def __init__(self,name):
    #     self.name=name #this will change the instance att
    #     self.__class__.name=name # this will change the class attr
    #     Student.name="madhu"
    # @classmethod # this decorator will also change the class attr
    # def change_name(cls,name):
    #     cls.name=name