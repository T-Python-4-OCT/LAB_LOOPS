
n = int(input("Enter a positive integer: "))
even_sum = 0

for num in range(1, n + 1):
  if num % 2 == 0:  
    even_sum += num

print(f"The sum of even numbers between 1 and {n} is {even_sum}.")