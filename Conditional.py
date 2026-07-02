eat=input("What to eat:")
if eat=="rice":
    print("ok")
elif eat=="dal":
    print("eat with rice")
else:
    print("don't eat")

print("ok") if eat=="rice" or eat=="dal" else print("don't eat")

salary=float(input("your salary"))
tax=salary*(0.5,0.10)[salary>=3000]
print(tax)
