# Part 1 Using range()


numbers = range(45, 211)

for num in numbers:
    if num == 100:
        continue      # skip 100 by using continue
    if num == 205:
        break         # stop the loop at 205 by using break
    print(num)


# Part 2 Using a while loop and input

while True:
    answer = input("what is the product of 7 * 24 ? ")

    if answer == "168":
        print("You answered this Question correctly ")
        break
    else:
        print("Your Answer is wrong try again.. ")


        #outout
# what is the product of 7 * 24 ? 167
# Your Answer is wrong try again..
# what is the product of 7 * 24 ? 166
# Your Answer is wrong try again..
# what is the product of 7 * 24 ? 100
# Your Answer is wrong try again..
# what is the product of 7 * 24 ? 168
# You answered this Question correctly