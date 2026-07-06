nums=[2,1,3,4,6,5,7,8,10]

is_even = lambda n :n%2==0 #lambda functions are those function that we are using as anonymous func which have only few things to do

evens=list(filter(is_even,nums))#filter accept a func and a iterable and pass one value at a time to the function

print(evens)

