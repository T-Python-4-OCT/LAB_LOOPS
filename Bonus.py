n = int(input("Enter a positive number: "))
total = 0

while n <= 0:
    n = int(input("please Enter a positive number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        total += i

print("The sum of even numbers from 1 to", n, "is:", total)