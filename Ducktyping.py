
# What is Duck Typing?
# Duck typing is a feature of Python where an object's suitability is determined
#  by the methods or attributes it provides rather than its actual type.
# If an object supports the required behavior, it can be used regardless of its class.
class Duck:
    def quack(self):
        print("sounds quack")
    def fly(self):
        print("I can fly by myself")
class Person:
    def quack(self):
        print("I can pretend sounds like duck")
    def fly(self):
        print("I can fly duck")
def quack_and_fly(thing):
    thing.quack()
    thing.fly()
    # if isinstance(thing,Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print("I am not a Duck")

d=Duck()
quack_and_fly(d)
p=Person()
quack_and_fly(p)

