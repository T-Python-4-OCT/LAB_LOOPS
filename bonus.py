n = int(input("Enter a positive integer: "))
total = 0

for number in range(1, n + 1):
    if number % 2 == 0:
        total += number

print(f"The sum of even numbers between 1 and {n} is {total}.")