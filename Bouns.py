
i:int=int(input("Enter the number"))

sum=0
for f in range(1,i+1):
    if f % 2 ==0:
        sum+=f
        print(f)       
print("The sum of even numbers between 1 and", i, "is",sum)
    