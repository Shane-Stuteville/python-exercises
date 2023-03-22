'''
1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
    a. Write python 3 code to prompt the user for input and then run the is_vowel() function from the fuction_exercises.py module and repeat doing 
    so until user types q or quit. There are many other functions in the fuction_exercises.py module, so only run the is_vowel() function and not any
    others.
    b. Write python 3 code that will prompt the user for bill_total tip_percentage inputs and then pass those inputs into the calculate_tip() from 
    fuction_exercises.py. Repeat running this code until the user types q or quit.
    c. Create a jupyter notebook named import_exercises.ipynb. Write python 3 code that will prompt the user for a number_grade integer and then pass 
    that input into the get_letter_grade() from fuction_exercises.py. Repeat running the get_letter_grade() until the user types q or quit.
'''
# Import the is_vowel function from the function_exercises.py module
from function_exercises import is_vowel

# Start a while loop to repeatedly prompt the user for input
while True:
    # Prompt the user for input
    user_input = input("Enter a character, or 'q' to quit: ")
    # Check if the user entered 'q' or 'quit'
    if user_input == 'q' or user_input == 'quit':
        # If the user entered 'q' or 'quit', break out of the loop
        break
    # Call the is_vowel function and store the result in the 'result' variable
    result = is_vowel(user_input)
    # Print the result
    print("Result: ", result)



# Import the calculate_tip function from the function_exercises.py module
from function_exercises import calculate_tip

# Start a while loop to repeatedly prompt the user for input
while True:
    # Prompt the user for bill_total and tip_percentage
    bill_total = input("Enter bill total: ")
    tip_percentage = input("Enter tip percentage: ")
    # Check if the user entered 'q' or 'quit' for either input
    if bill_total == 'q' or bill_total == 'quit' or tip_percentage == 'q' or tip_percentage == 'quit':
        # If the user entered 'q' or 'quit' for either input, break out of the loop
        break
    # Call the calculate_tip function with bill_total and tip_percentage as arguments
    result = calculate_tip(float(bill_total), float(tip_percentage))
    # Print the result
    print("Result: ", result)


# Import the get_letter_grade function from the function_exercises.py module
from function_exercises import get_letter_grade

# Import the get_letter_grade function from the function_exercises.py module
from function_exercises import get_letter_grade

# Start a while loop to repeatedly prompt the user for input
while True:
    # Prompt the user for a number_grade
    number_grade = input("Enter a number grade: ")
    # Check if the user entered 'q' or 'quit'
    if number_grade == 'q' or number_grade == 'quit':
        # If the user entered 'q' or 'quit', break out of the loop
        break
    # Call the get_letter_grade function with number_grade as an argument
    result = get_letter_grade(int(number_grade))
    # Print the result
    print("Result: ", result)



'''
2. Read about and use the itertools module from the python standard library to help you solve the following problems (Hint: wrap the itertools results
in a list to see the results).
    Write python version 3 code that will calculate how different ways can you combine a single letter from "abc" with either 1, 2, or 3? 
    Show and count the different combinations.
    Write python version 3 code that will calculate how many different combinations are there of 2 letters from "abcd"? 
    Show and count the different combinations.
    Write python version 3 code that will calculate jow many different permutations are there of 2 letters from "abcd"?
    Show and count the different permutations.
'''
letters = "abc"
numbers = [1, 2, 3]
combinations = []

for letter in letters:
    for number in numbers:
        combination = letter + str(number)
        combinations.append(combination)

print("The different combinations are:")
for combination in combinations:
    print(combination)

print("\nNumber of combinations:", len(combinations))




letters = "abcd"
combinations = []

for i in range(len(letters)):
    for j in range(i + 1, len(letters)):
        combination = letters[i] + letters[j]
        combinations.append(combination)

print("The different combinations are:")
for combination in combinations:
    print(combination)

print("\nNumber of combinations:", len(combinations))


import itertools

letters = "abcd"
permutations = list(itertools.permutations(letters, 2))

print("The different permutations are:")
for permutation in permutations:
    print(permutation)

print("\nNumber of permutations:", len(permutations))




'''
3. Save this file as profiles.json inside of your exercises directory (right click -> save file as...).
Use the load function from the json module to open this file.
    import json
    json.load(open('profiles.json))

Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:

Write python version 3 code and include comments that will use data from the the profiles.json file calculate the following outputs:
    - Total number of users from the variable string "guid"
    - Number of active users from the boolean "isActive"
    - Number of inactive users boolean "isActive"
    - Grand total of balances for all users from the float "balance"
    - Average balance of all users
    - User with the lowest balance 
    - User with the highest balance 
    - Most common favorite fruit from the string "favoriteFruit"
    - Least most common favorite fruit string "favoriteFruit"
    - Total number of unread messages for all users "greeting". The number of messages are the numbers inside the string "greeting". This is an 
    example of the "greeting" string with a two digit number: "greeting": "Hello, Allison Wynn! You have 19 unread messages." This is an example of 
    the "greeting" string with one string variable: "greeting": "Hello, Herbert Estes! You have 4 unread messages."

    
'''

import json
from collections import Counter

# Load the profiles data from the json file
with open('profiles.json', 'r') as file:
    profiles = json.load(file)

# Initialize variables to keep track of the results
total_users = 0
active_users = 0
inactive_users = 0
grand_total_balance = 0
lowest_balance = None
lowest_balance_user = None
highest_balance = None
highest_balance_user = None
favorite_fruits = []
unread_messages = 0

# Loop through each profile
for profile in profiles:
    # Count the total number of users
    total_users += 1
    
    # Check if the user is active or inactive
    if profile['isActive']:
        active_users += 1
    else:
        inactive_users += 1
    
    # Convert the balance to a float and add it to the grand total
    balance = float(profile['balance'].replace('$', '').replace(',', ''))
    grand_total_balance += balance
    
    # Check if this is the lowest or highest balance so far
    if lowest_balance is None or balance < lowest_balance:
        lowest_balance = balance
        lowest_balance_user = profile['name']
    if highest_balance is None or balance > highest_balance:
        highest_balance = balance
        highest_balance_user = profile['name']
    
    # Add the favorite fruit to the list of all favorite fruits
    favorite_fruits.append(profile['favoriteFruit'])
    
    # Extract the number of unread messages from the greeting
    greeting = profile['greeting']
    start_index = greeting.index('You have ') + 9
    end_index = greeting.index(' unread messages')
    unread_messages += int(greeting[start_index:end_index])

# Calculate the average balance
average_balance = grand_total_balance / total_users

# Find the most and least common favorite fruits
fruit_counts = Counter(favorite_fruits)
most_common_fruit = fruit_counts.most_common(1)[0][0]
least_common_fruit = fruit_counts.most_common()[-1][0]

# Print the results
print(f'Total number of users: {total_users}')
print(f'Number of active users: {active_users}')
print(f'Number of inactive users: {inactive_users}')
print(f'Grand total of balances: ${grand_total_balance:.2f}')
print(f'Average balance: ${average_balance:.2f}')
print(f'User with lowest balance: {lowest_balance_user} (${lowest_balance:.2f})')
print(f'User with highest balance: {highest_balance_user} (${highest_balance:.2f})')
print(f'Most common favorite fruit: {most_common_fruit}')
print(f'Least common favorite fruit: {least_common_fruit}')
print(f'Total number of unread messages: {unread_messages}')
