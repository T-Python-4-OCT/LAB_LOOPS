# 1) Using range and for loop
for number in range(45, 211):
    if number == 100:
        continue
    if number == 205:
        break
    print(number)

# 2) Using a while loop
while True:
    answer = input("What is the product of 7 * 24? ")
    if answer == "168":
        print("You answered this Question correctly")
        break
    print("Your Answer is wrong try again..")