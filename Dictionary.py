#key:value imp: we can't take list and tuple in place of key
#dictionary is mutable,unordered,don't allow duplicate keys

dict={
    "name":"Madhu",
    2:"Adu",
    3:"Sahoo",
    "marks":[12,34,55],
    # "marks":[12,34,55]
}
new_dict={"age":32}
# dict["name"]="milan"
# print(dict.get("name"))#no error simply return NOne
# print(dict["name"])#give us error if key is not present
dict.update(new_dict)
# print(dict)
# null_dict={}

# null_dict["name"]="madhu"
# print(null_dict)
#nested dictionary
nested_dict={
    "name":"Madhu",
    "class":12,
    "sub":"physics",
    "chap":{"chapter1":"motion",
            "chapter2":"vectors and scalers",
            "chapter3":"electromagnetic"
            }
}
# print(nested_dict["chap"]["chapter1"])
# print("output is in list format:",list(nested_dict.keys()))
# print("output is in list format:",list(nested_dict.values()))
# print(nested_dict.items())
#assignment

dictq={
    "table":["a piece of furniture","list of facts"],
    "cat":"a small animal"
}
# print(dictq)

# mark_dict={}
# mark1=input("enter your sub mark:")
# mark_dict.update({"phy":mark1})
# mark2=input("enter your sub mark:")
# mark_dict.update({"chm":mark2})
# mark3=input("enter your sub mark:")
# mark_dict.update({"math":mark3})
# print(mark_dict)

student = {
    "marks": [10, 20]
}

mark= student["marks"]

mark.append(30)

print(student)
