#iterables are something that can looped over e.g:-list
# nums=[12,3,2,4]
# it = iter(nums)

# print(next(it))

# print(next(it))
# print()
# for x in it:
#     print(x)

# print()
# numbers = [x*x for x in range(1000000)]
# numbers1 = (x*x for x in range(1000000))


# i_nums=iter(nums)
# while True:
#     try:
#         item=next(i_nums)
#         print(item)
#     except StopIteration:
#         break
# for i in i_nums:
#     item=i
#     print(i)


# print(dir(i_nums))
# for i in nums:
#     print(i)
#__iter__ is a object with a state which can remember its current position.
#hence list is not a iterator so it don't know what is next value
# print(next(nums))#it will show error of list' object is not an iterator
# next() is internally calling __next__ dunder function


#custom class to make that iterable

class MyRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        current = self.start
        self.start += self.step
        return current

#generators instead of iterables
def my_range(start,end,step=1):
    current=start
    while current<end:
        yield current #yield internally remember the state and return the value as well it raise the StopIteration
        current +=step

def even_numbers(n):
    current=1
    while current<=n:
        if current%2==0:
            yield current
        current +=1

nums=even_numbers(20)
for num in nums:
    print(num)
# nums = my_range(1, 10)
# for num in nums:
#     print(num)


print()

nums = my_range(1, 5)

print(next(nums))

print(next(nums))
print()
for i in nums:
    print(i)




