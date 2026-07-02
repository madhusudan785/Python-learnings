list=[1,2,4,16,24,30,35]
index=0
target=16
for i in list:
    if i==target:
        print("target found at :",index)
        
    index +=1

for i in range(len(list),2):
    print(list[i])
n=5
sum=0
fact=1
for i in range(1,n+1):
    sum +=i
    fact *=i
  
print(sum)
print(fact)
while index < len(list):
    if list[index]==target:
        print("found at index :",index)
        break
    index +=1



count=1
while count <=10:
    print(3*count)
    count +=1

count=1
while count<=5:
    print("HNHN")
    count+=1

count=5
while count>=1:
    print(count)
    count -=1
