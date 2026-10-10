for number in range(45, 211):
    if number == 100:
        continue
    if number == 205:
        break
    print(number)

while True:
    answer = input("what is the product of 7 * 24 ? ")
    
    if answer == "168":
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")