numbers=[5,7,10,9,2]

def sum(num):
    sum=0
    for item in num:
        sum +=item
    return sum

def min(num):
    minm=num[0]
    for item in num:
        if item<minm:
            minm=item
            

    return minm
print(min(numbers))


numbers = [5, 7, 2, 9, 1]

print(sum(numbers))


# print(sum(numbers)) 











