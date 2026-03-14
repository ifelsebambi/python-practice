
for number in range(101):
  #skips 0 in the range or can probably do the multiple parameters in the range(start, stop, step)
  if number == 0:   
    continue
  else:
    #if the number is a factor of 3 and 5 then print FizzBuzz
    if number % 3 == 0 and number % 5 == 0: 
      print('FizzBuzz')
    #if the number is a factor of 3 only then print Fizz
    elif number % 3 == 0: 
      print('Fizz')
    #if the number is a factor of 5 only then print Buzz
    elif number % 5 == 0: 
      print('Buzz')
    #otherwise just print the number
    else:
      print(number)
