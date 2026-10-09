number=int(input("Enter a Positive number: "))

sum_numbers=0

for num in range(1,number+1):
    if num % 2 == 0:
        sum_numbers += num
    
print(f"the sum of all even numbers from 1 to {number} is: {sum_numbers}")
    
            