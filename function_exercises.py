'''
1. Write python version 3 funciton named is_two. It should accept one input and return True if the passed input is either the number or 
the string 2, False if otherwise. Prompt the user for input and then run the function and repeat doing so until user types q or quit.
Include comments with the code.
'''
def is_two(input_value):
    return input_value == 2 or input_value == "2"

while True:
    user_input = input("Enter a value or 'q' to quit: ")
    if user_input == 'q' or user_input == 'quit':
        break
    result = is_two(user_input)
    print("Result: ", result)


'''
2. Write python version 3 funciton named is_vowel. It should return True if the passed string is a vowel, False otherwise. Prompt the user for 
input and then run the function and repeat doing so until user types q or quit. Include comments with the code.
'''
# Define the is_vowel function
def is_vowel(input_value):
    # Define a string of vowels
    vowels = "aeiouAEIOU"
    # Return True if the input value is in the vowels string, False otherwise
    return input_value in vowels

# Start a while loop to repeatedly prompt the user for input
while True:
    # Prompt the user for input
    user_input = input("Enter a letter or 'q' to quit: ")
    # Check if the user entered 'q' or 'quit'
    if user_input == 'q' or user_input == 'quit':
        # If the user entered 'q' or 'quit', break out of the loop
        break
    # Call the is_vowel function and store the result in the 'result' variable
    result = is_vowel(user_input)
    # Print the result
    print("Result: ", result)


'''
3. Write python version 3 funciton named is_consonant. It should return True if the passed string is a consonant, False otherwise. Prompt the user for 
input and then run the function and repeat doing so until user types q or quit. Include comments with the code.
'''
# Define the is_consonant function
def is_consonant(input_value):
    # Define a string of vowels
    vowels = "aeiouAEIOU"
    # Return True if the input value is not in the vowels string, False otherwise
    return input_value not in vowels

# Start a while loop to repeatedly prompt the user for input
while True:
    # Prompt the user for input
    user_input = input("Enter a letter or 'q' to quit: ")
    # Check if the user entered 'q' or 'quit'
    if user_input == 'q' or user_input == 'quit':
        # If the user entered 'q' or 'quit', break out of the loop
        break
    # Call the is_consonant function and store the result in the 'result' variable
    result = is_consonant(user_input)
    # Print the result
    print("Result: ", result)



'''
4. Write python version 3 funciton that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts 
with a consonant. Prompt the user to input a word and then run the function and repeat doing so until user types q or quit. Include comments with the 
code.
'''
# Define the capitalize_first_letter function
def capitalize_first_letter(input_value):
    # Define a string of vowels
    vowels = "aeiouAEIOU"
    # Check if the first letter of the input value is a consonant
    if input_value[0] not in vowels:
        # If the first letter of the input value is a consonant, capitalize it
        return input_value.capitalize()
    # If the first letter of the input value is not a consonant, return the input value as-is
    return input_value

# Start a while loop to repeatedly prompt the user for input
while True:
    # Prompt the user for input
    user_input = input("Enter a word or 'q' to quit: ")
    # Check if the user entered 'q' or 'quit'
    if user_input == 'q' or user_input == 'quit':
        # If the user entered 'q' or 'quit', break out of the loop
        break
    # Call the capitalize_first_letter function and store the result in the 'result' variable
    result = capitalize_first_letter(user_input)
    # Print the result
    print("Result: ", result)



'''
5. Write python version 3 funciton named calculate_tip. It should accept a tip percentage and the bill total, and return the amount to tip. 
Prompt the user to enter a bill amount and tip percentage and then run the function and repeat doing so until user types q or quit. Include comments 
with the code.
'''
# Define the calculate_tip function
def calculate_tip(bill_total, tip_percentage):
    # Calculate the tip amount by multiplying the bill total by the tip percentage
    tip_amount = bill_total * (tip_percentage / 100)
    # Return the tip amount
    return tip_amount

# Start a while loop to repeatedly prompt the user for input
while True:
    # Prompt the user for the bill total
    bill_total = input("Enter the bill total or 'q' to quit: ")
    # Check if the user entered 'q' or 'quit'
    if bill_total == 'q' or bill_total == 'quit':
        # If the user entered 'q' or 'quit', break out of the loop
        break
    # Convert the bill total to a float
    bill_total = float(bill_total)
    # Prompt the user for the tip percentage
    tip_percentage = input("Enter the tip percentage: ")
    # Convert the tip percentage to a float
    tip_percentage = float(tip_percentage)
    # Call the calculate_tip function and store the result in the 'result' variable
    result = calculate_tip(bill_total, tip_percentage)
    # Print the result
    print("Tip amount: $%.2f" % result)


'''
6. Write python version 3 funciton named apply_discount. It should accept a original price, and a discount percentage, and return the price after 
the discount is applied. Prompt the user to input a original price and discount percentage then run the function  to calculate the discount price
and repeat doing so until user types q or quit. Include comments with the code.
'''
# Define the apply_discount function
def apply_discount(original_price, discount_percentage):
    # Calculate the discount amount by multiplying the original price by the discount percentage
    discount_amount = original_price * (discount_percentage / 100)
    # Calculate the discounted price by subtracting the discount amount from the original price
    discounted_price = original_price - discount_amount
    # Return the discounted price
    return discounted_price

# Start a while loop to repeatedly prompt the user for input
while True:
    # Prompt the user for the original price
    original_price = input("Enter the original price or 'q' to quit: ")
    # Check if the user entered 'q' or 'quit'
    if original_price == 'q' or original_price == 'quit':
        # If the user entered 'q' or 'quit', break out of the loop
        break
    # Convert the original price to a float
    original_price = float(original_price)
    # Prompt the user for the discount percentage
    discount_percentage = input("Enter the discount percentage: ")
    # Convert the discount percentage to a float
    discount_percentage = float(discount_percentage)
    # Call the apply_discount function and store the result in the 'result' variable
    result = apply_discount(original_price, discount_percentage)
    # Print the result
    print("Discounted price: $%.2f" % result)




'''
7. Write python version 3 funciton named handle_commas. It should accept a string that is a number that contains commas in it as input, and return 
a number as output. Prompt the user to enter a string number and then run the function and repeat doing so until user types q or quit. Include 
comments with the code.
'''
# Define the handle_commas function
def handle_commas(input_value):
    # Remove the commas from the input value
    input_value = input_value.replace(',', '')
    # Convert the input value to a float
    input_value = float(input_value)
    # Return the input value as a float
    return input_value

# Start a while loop to repeatedly prompt the user for input
while True:
    # Prompt the user for input
    user_input = input("Enter a number with commas or 'q' to quit: ")
    # Check if the user entered 'q' or 'quit'
    if user_input == 'q' or user_input == 'quit':
        # If the user entered 'q' or 'quit', break out of the loop
        break
    # Call the handle_commas function and store the result in the 'result' variable
    result = handle_commas(user_input)
    # Print the result
    print("Result: ", result)


'''
8. Write python version 3 funciton named get_letter_grade. It should accept a number (4,3,2,1,0) and return the letter grade associated with that 
number (A,B,C,D,F). Prompt the user to enter a number and then run the function and repeat doing so until user types q or quit. Include comments 
with the code.
'''
# Define the get_letter_grade function
def get_letter_grade(number_grade):
    # Use an if/elif/else statement to determine the letter grade based on the number grade
    if number_grade == 4:
        return 'A'
    elif number_grade == 3:
        return 'B'
    elif number_grade == 2:
        return 'C'
    elif number_grade == 1:
        return 'D'
    elif number_grade == 0:
        return 'F'
    else:
        return 'Invalid input'

# Start a while loop to repeatedly prompt the user for input
while True:
    # Prompt the user for input
    user_input = input("Enter a number grade (4, 3, 2, 1, 0) or 'q' to quit: ")
    # Check if the user entered 'q' or 'quit'
    if user_input == 'q' or user_input == 'quit':
        # If the user entered 'q' or 'quit', break out of the loop
        break
    # Convert the user input to an integer
    number_grade = int(user_input)
    # Call the get_letter_grade function and store the result in the 'result' variable
    result = get_letter_grade(number_grade)
    # Print the result
    print("Letter grade: ", result)


'''
9. Write python version 3 funciton named remove_vowels that accepts a string and returns a string with all the vowels removed. Prompt the user 
to enter a string and then run the function and repeat doing so until user types q or quit. Include comments with the code.
'''
# Define the remove_vowels function
def remove_vowels(input_string):
    # Define a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Initialize an empty string for the result
    result = ''
    # Loop through each character in the input string
    for char in input_string:
        # Check if the character is not a vowel
        if char.lower() not in vowels:
            # If the character is not a vowel, add it to the result string
            result += char
    # Return the result string
    return result

# Start a while loop to repeatedly prompt the user for input
while True:
    # Prompt the user for input
    user_input = input("Enter a string or 'q' to quit: ")
    # Check if the user entered 'q' or 'quit'
    if user_input == 'q' or user_input == 'quit':
        # If the user entered 'q' or 'quit', break out of the loop
        break
    # Call the remove_vowels function and store the result in the 'result' variable
    result = remove_vowels(user_input)
    # Print the result
    print("Result: ", result)


'''
10. Write python version 3 funciton named normalize_name. It should accept a string and return a valid python identifier, that is:
    anything that is not a valid python identifier should be removed, leading and trailing whitespace should be removed, everything 
    should be lowercase, andspaces should be replaced with underscores.
    For example: Name will become name, First Name will become first_name, % Completed will become completed. Include comments 
    with the code.
'''
import re

# Define the normalize_name function
def normalize_name(input_string):
    # Remove anything that is not a valid python identifier using the re library
    input_string = re.sub(r'[^\w\s]', '', input_string)
    # Remove leading and trailing whitespace
    input_string = input_string.strip()
    # Replace spaces with underscores
    input_string = input_string.replace(' ', '_')
    # Make everything lowercase
    input_string = input_string.lower()
    # Return the result
    return input_string

# Start a while loop to repeatedly prompt the user for input
while True:
    # Prompt the user for input
    user_input = input("Enter a string or 'q' to quit: ")
    # Check if the user entered 'q' or 'quit'
    if user_input == 'q' or user_input == 'quit':
        # If the user entered 'q' or 'quit', break out of the loop
        break
    # Call the normalize_name function and store the result in the 'result' variable
    result = normalize_name(user_input)
    # Print the result
    print("Result: ", result)


'''
11. Write python version 3 funciton named cumulative_sum that accepts a list of numbers and returns a list that is the total of the numbers in the list.
    Prompt the user to enter a number and then run the function and repeat doing so until user types q or quit. Include comments with the code.
'''
# Define the cumulative_sum function
def cumulative_sum(numbers):
    # Initialize a variable to keep track of the running sum
    running_sum = 0
    # Loop through each number in the input list
    for num in numbers:
        # Add the current number to the running sum
        running_sum += num
    # Return the running sum
    return running_sum

# Start a while loop to repeatedly prompt the user for input
while True:
    # Prompt the user for input
    user_input = input("Enter a list of numbers separated by commas, or 'q' to quit: ")
    # Check if the user entered 'q' or 'quit'
    if user_input == 'q' or user_input == 'quit':
        # If the user entered 'q' or 'quit', break out of the loop
        break
    # Convert the user input string into a list of numbers
    numbers = [int(num.strip()) for num in user_input.split(',')]
    # Call the cumulative_sum function and store the result in the 'result' variable
    result = cumulative_sum(numbers)
    # Print the result
    print("Result: ", result)


