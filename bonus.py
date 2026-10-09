number = int(input("Enter a positive number:"))
total =0

for i in range(0,number+1,2) :
    total = total +i
    
print (f"the sum of even numbers between 1 and {number} = {total}")