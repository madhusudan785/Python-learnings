n=5

def factorial(n):
        if(n==0 or n==1):
            return n
        else:
          return n*factorial(n-1)
     
print(factorial(n))




# def length(lst):
#     count=0;
#     for i in lst:
#         count +=1
#     return count


# numbers=[1,2,4,5,2,4,1]

# print(length(numbers))




# def sum(a,b):
#   s=a+b
#   return s

# a=5
# b=6
# # print(sum(a,b))
# def avg_of_nos(a,b,c):
#   return (a+b+c)/3

# print(avg_of_nos(1,2,3))


# def calculator():
#     a = int(input("First number: "))
#     b = int(input("Second number: "))
#     operation = input("Choose (+, -, *, /): ")

#     if operation == "+":
#         print("Result:", a + b)
#     elif operation == "-":
#         print("Result:", a - b)
#     elif operation == "*":
#         print("Result:", a * b)
#     elif operation == "/":
#         print("Result:", a / b)
#     else:
#         print("Invalid operation")

# calculator()
