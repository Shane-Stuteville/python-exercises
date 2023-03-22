'''
1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
    a. Write python 3 code and import the function is_vowel from the fuction_exercises.py module. Prompt the user for 
    input and then run the is_vowel function from the fuction_exercises.py module and repeat doing so until user types q or quit.
    b. Create a file named import_exercises.py. Within this file, use from to import the calculate_tip function directly. Call this function with values
    you choose and print the results.
    c. Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. Test this function
    in your notebook.
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



'''
2. Read about and use the itertools module from the python standard library to help you solve the following problems (Hint: wrap the itertools results
in a list to see the results).
    How many different ways can you combine a single letter from "abc" with either 1, 2, or 3?
    How many different combinations are there of 2 letters from "abcd"?
    How many defferent permutations are there of 2 letters from "abcd"?
'''

'''
3. Save this file as profiles.json inside of your exercises directory (right click -> save file as...).
Use the load function from the json module to open this file.
    import json
    json.load(open('profiles.json))

Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
    - Total number of users
    - Number of active users
    - Number of inactive users
    - Grand total of balances for all users
    - Average balance per user
    - User with the lowest balance
    - User with the highest balance
    - Most common favorite fruit
    - Least most common favorite fruit
    - Total number of unread messages for all users
'''