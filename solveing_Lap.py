for num in range(45, 210):
    if num == 100:
        continue
    if num == 205:
        break
    print(num)


    
answer : str =  ""

while answer != "168":
    answer = input("What is the product of 7 * 24? ")

    if answer == "168":
        print("You answered this Question correctly")
    else:
        print("Your Answer is wrong try again..")
