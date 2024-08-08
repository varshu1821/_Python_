a = int(input("enter a number: "))
b = int(input("enter a number: "))
even_count = 0
odd_count = 0

for i in range(a,b+1):
    if i%2 == 0:
        even_count+= 1
    elif i%2!= 0:
        odd_count+= 1
print("EVEN:", even_count)
print("ODD:", odd_count)
        
