n=int(input("Enter positive integer:"))
total=0
for i in range(1,n+1):
    if i %2==0:
        total+=i
print("The sum of even Num between 1 and ",n, "is",total)