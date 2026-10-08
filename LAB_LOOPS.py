#      *The core program*
#Range:
print("*Welcome to the loop program*")
for number in range(45, 210):
    if number == 100:
        continue
    if number == 206:
        break
    print(number)

#While:
while True:
    answer = input("what is the product of 7*24 ? ")
    if answer == "168":
        print("You answered this question correctly")
        break
    print("Your Answer is wrong try again..")

#      *The bonus program*
bonus = int(input("Enter a positive integer: "))
while bonus <= 0:
    bonus = int(input("Please enter a positive integer: "))

even_sum = 0
for number in range(2, bonus + 1, 2):
    even_sum += number

print(f"The sum of even numbers between 1 and {bonus} is {even_sum}.")
print("Thank you for using the program")