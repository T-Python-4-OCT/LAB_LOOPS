n = int(input("Enter a positive integer: "))

total_sum = 0
i = 1

while i <= n:
    if i % 2== 0:
        total_sum = total_sum + i
    i = i +1

print("The sum of even numbers between 1 and", n, "is", total_sum, )
