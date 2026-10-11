PositiveInteger = int(input('Please Enter a Positive Integer: '))
EvenSum = 0

'''

1- Range function will start at 2 (first even numbers).
2- It will add 1 to the input entered from the user.
3- Move two steps

''' 
for Number in range(2, PositiveInteger + 1, 2):
  EvenSum += Number

print('The sum of even numbers between 1 and', Number, 'is', EvenSum)