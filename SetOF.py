#set contains unique,unordered,immutable elements values inside it
#concept:we can't store list and dictionary in set
collection={1,2,"hello",3,4,"world"}
collection2={"milan",43,1,"world",4,6,9}
collection2.add("9.0")
coll={("float",9.0),("int",9)}
print(coll)
print(collection2)
a = {1, 2, 3}
b = {3, 4, 5}

print(a-b)#difference-elements that are in a but not in b. and vice verse(b-a)
print(a&b)#intersection
print(a|b)#union
# print(collection.union(collection2))
# print(collection.intersection(collection2))


# collection.add("na")#set it self is mutable
# print(collection)
# collection.remove("na")
# print(collection)
# print(collection.pop())#remove a random value
# collection.clear()
# print(collection)
# empty_set=set()#empty set declaration