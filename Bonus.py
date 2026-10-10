n = int(input("Enter a positive integer: "))
total_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total_sum += i

print(f"The sum of even numbers between 1 and {n} is {total_sum}.")