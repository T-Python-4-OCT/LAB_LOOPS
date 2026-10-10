# Lab


range_numbers = range(45, 210)

for number in range_numbers:
    if number == 100:
        continue
    if number == 205:
        break
    print(number)



question = "what is the product of 7 * 24 ?"

while input(question) != "168":
    print("Your Answer is wrong try again..") 
else:
    print("You answered this Question correctly")
       