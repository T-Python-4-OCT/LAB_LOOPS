#using range function with for loop
for  i in  range(45,211):
    if i ==100:
        continue

    if i ==205:
        break
    print(i)    


#using while loop    

while True:
    answer = int(input("what is the product of 5*5?"))
    if answer == 25:
        print("Correct!")
        break
    else:
        print("Try again!")