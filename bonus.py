#

positive = int(input("Enter a positive integer:"))


sum:int = 0

for number in range(1, positive +1):
    if number % 2 == 0:
        sum += number

print(f"The sum of even numbers between 1 and {positive} is {sum}")