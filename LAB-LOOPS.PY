for number in range(45, 211):
    if number == 100:
        continue
    if number == 205:
        break
    print(number)


answer = input("what is the product of 7 * 24 ? ")
while answer != "168":
    print("Your Answer is wrong try again..")
    answer = input("what is the product of 7 * 24 ? ")
print("You answered this Question correctly")
