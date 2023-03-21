''' 
Write python version 3 code that will prompt the user for the day of the week, print out whether it is Monday or not and whether it is a 
weekday or weekend
'''

'''
1. Conditional Basics
    a. Prompt the user for a day of the week, print out whether the day is Monday or not
    b. Prompt the user for a day of the week, print out whether the day is a weekday or a weekend
'''

def main():
    day_of_week = input("Please enter the day of the week: ").lower()

    if day_of_week == "monday":
        print("Today is Monday.")
    else:
        print("Today is not Monday.")

    if day_of_week in ["saturday", "sunday"]:
        print("Today is a weekend.")
    elif day_of_week in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
        print("Today is a weekday.")
    else:
        print("Invalid day entered. Please enter a valid day of the week.")

if __name__ == "__main__":
    main()

'''
    c. Calculate a weekly paycheck, accounting for overtime pay. Create variables and make up values for:

            The number of hours worked in one week
            The hourly rate
        For calculating pay:
            For working 40 hours or less, each hour is paid at the hourly rate
            For working more than 40 hours
                the first 40 hours are paid at the hourly rate
                each hour after 40 is paid at time and a half (hourly rate * 1.5)

    Write python version 3 code that will create a random integer between 1-80 called number_of_hours_worked integer variable and a random float
    to two decimal places between 10.00-100.00 called hourly_rate. The number_of_hours_worked up to 40 and hourly_rate will then be multiplied
    by each other for the regular_pay. If the number_of_hours_worked is over 40, then the remainder will be multiplied by 1.5 * hourly_rate
    and that will be the overtime_pay. Then the regular_pay and overtime_pay will be added together to be the total_pay. Print 
    the number_of_hours_worked, hourly_rate, regular_pay, overtime_pay, and total_pay. Then ask the user if they want to start again or quit.
'''

import random

def calculate_pay():
    # Generate random number of hours worked between 1-80
    number_of_hours_worked = random.randint(1, 80)
    # Generate random hourly rate between 10.00-100.00
    hourly_rate = round(random.uniform(10.00, 100.00), 2)
    # Calculate regular pay
    if number_of_hours_worked <= 40:
        regular_pay = number_of_hours_worked * hourly_rate
        overtime_pay = 0
    else:
        regular_pay = 40 * hourly_rate
        overtime_pay = (number_of_hours_worked - 40) * 1.5 * hourly_rate
    # Calculate total pay
    total_pay = regular_pay + overtime_pay
    # Print results
    print("Number of hours worked: ", number_of_hours_worked)
    print("Hourly rate: $", hourly_rate)
    print("Regular pay: $", regular_pay)
    print("Overtime pay: $", overtime_pay)
    print("Total pay: $", total_pay)

# Ask user if they want to start again or quit
while True:
    calculate_pay()
    user_input = input("Would you like to start again or quit (start/quit)? ")
    if user_input == "quit":
        break


'''
2. Loop Basics
    a. While
        i. Create an integer variable i with a value of 5. Create a while loop that runs so long as i is less than or equal to 15. Each loop iteration,
        output the current value of i, then increment i by one.
'''
i = 5
while i <= 15:
    print(i)
    i += 1
'''
        ii. Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
'''
i = 0
while i <= 100:
    print(i)
    i += 2

'''
        iii. Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.
'''
i = 2
while i < 1000000:
    print(i**2)
    i += 1


'''
        iv. Write a while loop that that starts at 100 and subtracks 5 each time until 5 is reached and stop. Print output on each line starting at 
        100 showing each subtraction until the end.
'''
i = 100
while i >= 5:
    print(i)
    i -= 5


'''
    b. For Loops
        i.  Write some code using a for loop that prompts the user for a number, then shows a multiplication table up through 10 for that number.
'''
number = int(input("Enter a number: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")


'''
        ii.  Create a for loop that prints itself by its value upto and includeing 9. For example, line one is 1, line two is 22, line three is 333,
        and so on through nine 9's on line nine.
'''
for i in range(1, 10):
    print(str(i) * i)

'''
    c. break and continue
        i.  Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user 
        entered down to 1.
'''
number = int(input("Enter a positive integer: "))

while number >= 1:
    print(number)
    number -= 1


'''
        ii. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a postive number
        and write a loop that counts from 0 to that number. 
'''
number = int(input("Enter a positive number: "))

for i in range(number + 1):
    print(i)


'''
        iii. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter
        invalid input. Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered. 
'''
while True:
    number = int(input("Enter an odd number between 1 and 50: "))
    if number >= 1 and number <= 50 and number % 2 == 1:
        break
    print("Invalid input. Please try again.")

for i in range(1, 51, 2):
    if i == number:
        continue
    print(i)


'''
3. Fizzbuzz

    One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed 
    to test basic looping and conditional logic skills.

        Write a program that prints the numbers from 1 to 100.
        For multiples of three print "Fizz" instead of the number
        For the multiples of five print "Buzz".
        For numbers which are multiples of both three and five print "FizzBuzz".

        Write the python code for the fizzbuzz test that prints a random number from 1-100 each second. For every number generated that is a 
        multiple of three print 'Fizz' in addition to the number. For every number generated that is a multiple of five print 'Buzz' in addition to
        the number. For every number generated that is a multiple of both three and five print'FizzBuzz'.
'''
import random
import time

while True:
    # Generate a random number from 1-100
    number = random.randint(1, 100)
    # Check if the number is a multiple of both three and five
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # Check if the number is a multiple of three
    elif number % 3 == 0:
        print("Fizz")
    # Check if the number is a multiple of five
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    # Wait for one second before printing the next number
    time.sleep(1)


'''
4. Display a table of powers.

    Prompt the user to enter an integer
    Display a table of squares and cubes from 1 to the value entered
    Ask if the user wants to continue
    Assume that the user will enter valid data
    Only continue if the user agrees to 

    Write python version 3 code that asks the user for an integer user_integer. Take the user_integer and place it in the first column called 'number'. 
    Take the user_integer and square it for squared_integer and place it in the second column called 'squared'. Then, take the user_integer and cube it 
    for cubed_integer and place it in the third column called 'cubed'. Finally, ask the user to enter a another integer and repeat the process until the 
    user enters q or quit.
'''
while True:
    user_input = input("Enter an integer or 'q' to quit: ")
    if user_input == 'q' or user_input == 'quit':
        break
    user_integer = int(user_input)
    squared_integer = user_integer ** 2
    cubed_integer = user_integer ** 3
    print("number: ", user_integer)
    print("squared: ", squared_integer)
    print("cubed: ", cubed_integer)
