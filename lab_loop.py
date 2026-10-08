for number in range(45, 210):       
    if number == 100:
        continue
    if number == 205:
        break     
    print(number)
while True: 
    answer = input("what is the product of 7 * 24 ?")
    if answer != "168":
        print("Incorrect, try again.")
    if answer == "168":
        print("Correct!")
        break