a = int(input("enter a number: "))
b = int(input("enter a number: "))
count = 0

for i in range(a,b+1):
    if i%2!=0:
        count+= 1
print(count)
