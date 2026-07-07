# lst=[12,43,24,3,64,3,5,75,24]
# my_list=[] this is the usual scenario of coping data to another list
# for i in lst:
#     my_list.append(i)
#---------------- list Comprehensions-----------#
# the statement is i want n from list of nth index
# my_list=[n for n in lst]
# my_sqr_list=[n*n for n in lst]
# even_list=[n%2==0 for n in lst] here this don't work because we are conditioning and we know the output is in True/False
# so we use filter and lambda for our Comprehension
# even_list1=list(filter(lambda n: n%2==0 ,lst))#so here lambda is anynimous function who execute only one piece of line so we have
# take output as n after put the condition we just filter which one to add in even_list or which one to ignore from list(lst) 
# even_list=[n  for n in lst if n%2==0]
# print(even_list)
# print (even_list1)
# print(my_list)
# print(my_sqr_list)
#--------------Tuple Comprehensions --------------#
# my_list=[]
# i want a (letter,num) tuple pair which contains 'abcd' and '0,1,2,3'
# so usual way 
# for char in 'abcd':
#     for i in range(4):
#         my_list.append((char,i))
# print(my_list)
# but in Comprehension we do something like this
# my_list_comp=list((letter, num) for letter in "abcd" for num in range(4))
# print(my_list_comp)
#-----------------Dictionary Comprehension----------------#
# names=["milan","anil","bruce","Dyne"]
# surname=["sahoo","jena","banner","ryle"]

# my_dict=list(zip(names,surname))[('milan', 'sahoo'), ('anil', 'jena'), ('bruce', 'banner'), ('Dyne', 'ryle')]
# print(my_dict)
# my_dict={}
# for name,surname in zip(names,surname):
#     my_dict[name]=surname
# print(my_dict)#{'milan': 'sahoo', 'anil': 'jena', 'bruce': 'banner', 'Dyne': 'ryle'}

# my_dict={names:surname for names,surname in zip(names,surname)}
# print(my_dict){'milan': 'sahoo', 'anil': 'jena', 'bruce': 'banner', 'Dyne': 'ryle'}
#-------------SET Comprehensions ------------------#
list=[1,2,1,2,4,3,5,3,1,2,3,1,3,4]
# for i in list:
#     my_set.add(i)
# print(my_set)

my_set={num for num in list} # for dictionary and set use {} 
# print(my_set)
#----------generators Comprehensions----------------#

lst=[12,43,24,3,64,3,5,75,24]

my_generator=(n*n for n in lst)# pretty much similar to list Comprehension

# for i in my_generator:
#     print(i)

