class Animal:

    def eat(self):
        print("Eating")

class Dog(Animal):

    def bark(self):
        print("Bark")

a=Animal()
d=Dog()
d.eat()


# class Car():
#     def __init__(self,type):
#         self.type=type
#     @staticmethod # static method can use or change the class state and generally use for utility
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("car stopped")
#     @staticmethod
#     def engine():
#         print("engine started")

# class BMW(Car):
#     # def __init__(self) -> None:
#     #     super().__init__()# bydefault it is calling super
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name

# car1=BMW("X5","Petrol")
# car2=BMW("X7","electric")
# print(car1.name,car1.type)
# print(car1.start())

#Multi-level inheritance
# class X5(Car):
#     def __init__(self,type):
#         self.type=type

# car3=X5("petrol")
# car3.start()
# #multiple inheritance

# # class x7(BMW,X5):
# #     color="white"

# #     def __init__(self, name, type):
# #         BMW.__init__(self, name)# we have to implement the methods that have in those classes
# #         X5.__init__(self, type)

# # x7_car = x7("BMW","petrol")
# # x7_car.start()



