n = int(input("Enter a positive integer: "))

total = 0
for number in range(2, n + 1, 2):
    total = total + number

print("The sum of even numbers between 1 and", n, "is", str(total) + ".")
