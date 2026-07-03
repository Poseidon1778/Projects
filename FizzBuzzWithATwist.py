# A simple implementation of the FizzBuzz game with a twist. This version includes an additional rule where if a number contains the digit '3', it outputs "Almost Fizz" instead of the number itself.
'''
FizzBuzz is a simple and classic programming game often used to teach basic logic and control flow. The game involves iterating through numbers from 1 up to a specified limit. For each number:

If the number is divisible by 3, the program outputs "Fizz."
If the number is divisible by 7, it outputs "Buzz."
If the number is divisible by both 3 and 7, it outputs "FizzBuzz."
Otherwise, it simply outputs the number.
This game is an excellent way to practice using loops, conditionals, and modular arithmetic.
'''

print("Welcome to FizzBuzz!")

def fizzbuzz(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 7 == 0:
        result += "Buzz"
    if result == "":
        if "3" in str(number):
            result = "Almost Fizz"
        else:
            result = str(number)
    return result

limit = int(input("Enter The Limit to start: "))

# Play FizzBuzz
for i in range(1, limit + 1):
    print(fizzbuzz(i))
