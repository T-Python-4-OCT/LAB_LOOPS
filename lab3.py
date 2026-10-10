
for i in range(45, 210):
    if i == 100:
        continue
    if i == 205:
        break
    print(i)

answer = int(input("What is the product of 7 * 24? "))

while answer != 168:
    print("Your Answer is wrong try again..")
    answer = int(input("What is the product of 7 * 24? "))

print("You answered this Question correctly")
