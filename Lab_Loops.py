#using range
for i in range (45 , 211):
    if i == 100:
        continue      
    if i ==205:
        break
    print(i)

print("-"*30)

#Using a while loop and input
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    answer = int(input("what is the product of 7 * 24 ? "))
    attempts += 1

    if answer == 7 * 24:
        print("You answered this Question correctly")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print("Your Answer is wrong try again..")
            print("Attempts remaining:", remaining)
        else:
            print("Sorry, you have used all your attempts.")
