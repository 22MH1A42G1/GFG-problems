#User function Template for python3

def fizzBuzz(number):
    # Write your code here.
    if (number%3==0 and number%5==0):
        print ("FizzBuzz")
    elif (number%3==0):
        print ("Fizz")
    elif (number%5==0):
        print ("Buzz")
    elif (number%3!=0 or number%5!=0):
        print(number)