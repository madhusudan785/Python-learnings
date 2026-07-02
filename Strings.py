
shopping_bag = [ "apples",
    "madam",
    "bread",
    "level",
    "milk",
    "racecar", "coffee beans", "tomatoes"]
for item in shopping_bag:
      if item[::-1] == item:
         print(item)

shopping_bag = ["live", "evil", "god", "dog", "apple"]
copy_shopping_bag=shopping_bag.copy()

for item in shopping_bag:
    for j in copy_shopping_bag:
      if item[::-1] == j:
         print(j)

for item in shopping_bag:
    print(f"Word: {item}")
    print(f"First: {item[0]}, Last: {item[-1]}")
    print(f"Without first: {item[1:]}")
    print(f"Reversed: {item[::-1]}")#[start : stop : step]
    print("-" * 20)

word="apples"
print(word[0])
print(word[0:1])
print(type(word[0]))
print(type(word[0:1]))



for item in shopping_bag:
  if len(item)>5:
    print(item)
  
for item in shopping_bag:
  if item.startswith("t"):#item[0] == "t":
    print(item)


  ''' 0 → if the letter is found at the first position
1, 2, 3, ... → if found later
-1 → if not found '''
for item in shopping_bag:
  if "e" in item: #item.find("e"):this is at some point wrong reason above
    print(item)

for item in shopping_bag:
  if item.endswith("s"):
    print(item[:-1])
  else:
    print(item)

# reverse a string 
str="madhu"
print(str[1:3])#string slicing
print(str.replace("m","b"))#replace a word
print(str[::-1])

