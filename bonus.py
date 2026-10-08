n = input("Enter a positive integer: ")
total = 0
for i in range(1, int(n) + 1):
    if i % 2 == 0:
        total += i
print(f"The sum of even numbers from 1 to {n} is: {total}")