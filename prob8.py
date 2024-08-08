num = int(input("Enter number:"))
sum = 0
print("The first", num, "natural numbers are:")

for i in range(1,num+1):
    print(i)
    sum += i
print("SUM:" ,sum)
