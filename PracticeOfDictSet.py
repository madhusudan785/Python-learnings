
words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "grapes"
]

seen = set()
result = []

for item in words:
    if item not in seen:
        seen.add(item)
        result.append(item)

print(result)    

print(seen)


numbers = [1, 2, 3]

a = numbers
b = numbers.copy()

a.append(4)

print(numbers)
print(a)
print(b)
list1 = {1,2,3,4,5,6}
list2 = {4,5,6,7,8,9}
print(set(list1) & set(list2))
print(list1 & list2)


sentence = "python is fun and python is powerful"
word_list=sentence.split()
word_dictionary={}
for words in word_list:
    if words in word_dictionary:
        word_dictionary[words] +=1
    else:
        word_dictionary[words]=1
print(word_dictionary)


student = {
    "name": "Madhusudan",
    "age": 23,
    "city": "Cuttack"
}
new_update={"course":"math",
            "age": 24
            }
student.pop("city")
student.update(new_update)
print(student)

numbers = [1, 2, 3, 2, 4, 5, 1, 6]
collect=set()
collect.update(numbers)
print(collect)
student = {
    "name": "Madhusudan",
    "age": 23,
    "city": "Mumbai"
}
print(student.keys())
student.update({"course": "Python"})
print(student)
# question - 3
names = [
    "Rahul",
    "Aman",
    "Rahul",
    "Ravi",
    "Aman",
    "Kiran"
]

seen = set()
duplicates = set()

for name in names:
    if name in seen:
        duplicates.add(name)
    else:
        seen.add(name)

# Question-5
fruits = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple"
]
fruit_count = {}

for fruit in fruits:
    if fruit in fruit_count:
        fruit_count[fruit] = fruit_count[fruit] + 1
    else:
        fruit_count[fruit] = 1

print(fruit_count)

# IMP: The dictionary is storing the variable for you.

# Question-6
student = {
    "name": "Madhusudan",
    "age": 23,
    "city": "Mumbai"
}

print(list(student.keys()),list(student.values()))
word = "programming"
word_dic={}
for char in word:
    if char in word_dic:
        word_dic[char]+=1
    else:
        word_dic[char]=1
print(word_dic)
for char in word_dic:
    if word_dic[char]==1:# >=2 if first repeating charecter asked
        print(char)
        break

a = {1, 2, 3}
b = {3, 4, 5}

print(a-b)#difference
