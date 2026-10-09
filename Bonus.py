n :int =int(input('enter your number'))

total = 0

for number in range(1, n+1):
    if number % 2 == 0:
      total= total+number
      
print("The sum of even numbers between 1 and", n, "is", total)
    
      