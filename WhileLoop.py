'''

Using a while loop and input , do the following :
Ask the the user : "what is the product of 7 * 24 ?"
check if the answer is right then exit the loop and print "You answered this Question correctly"
if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.

'''

Product = int(input('What is the result of 7 Multiply by 24 ? : '))
while Product != 168 :
  print('Your Answer is wrong, Try Again!')
  Product = int(input('What is the result of 7 Multiply by 24 ? : '))

print('You Answer the question correctly!')
