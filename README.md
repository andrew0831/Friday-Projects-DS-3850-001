README.md

# Madlib

The program prompts the user to input words for various parts of the story.
It stores each input in a corresponding variable.
It then prints the story with the user-provided words inserted into the appropriate places using string concatenation.
Each line of the story is printed using the print() function.

# Powerball

1. Import the `random` module to generate random numbers.
2. Print a greeting message to welcome the user.
3. Prompt the user to input whether they want PowerBall numbers or not, and store the user's response in the variable `response`.
4. Check if the user's response (converted to lowercase) is "yes".
   - If yes, proceed to generate PowerBall numbers.
   - If no, print a farewell message and exit the program.
5. Generate 5 random numbers for the white balls (1-69) using the `randint` function and store them in a list comprehension.
6. Generate a random number for the red ball (1-26) using the `randint` function.
7. Concatenate the white ball numbers into a single string with two space characters between each number, followed by four space characters and the red ball number.
8. Print the generated PowerBall numbers.
9. Print a message wishing the user good luck with their PowerBall ticket.
10. If the user did not respond with "yes" to the prompt asking if they want PowerBall numbers, print a farewell message.



