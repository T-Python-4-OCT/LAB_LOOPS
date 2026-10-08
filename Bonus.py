num = int(input("Enter a positive integer: "))

total = 0

for number in range(1, num + 1):
    if number % 2 == 0:
        total += number

print("The sum of even numbers between 1 and", num, "is", total)