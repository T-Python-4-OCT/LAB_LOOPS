
num=int ( input("Enter a positive integer: "))

total=0

for n in range(1,num+1) :
     if n % 2 == 0:
        total +=n
print(f"The sum of even numbers between 1 and {num} is {total} ")