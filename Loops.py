numbers=range(45,211)

for num in numbers:
   
    if num ==100:
        continue
    
    if num == 205:
        
        break
    
    print(num)
else:
    print("Loop completed without break.")




question="Qustion for you : what is the product of 7 * 24?"

while input(question) != "168":
    print("Incorrect answer. Please try again.")
    
else:
    print("Correct answer! The product of 7 * 24 is indeed 168.")
