questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the chemical symbol for water?": "H2O",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the largest planet in our solar system?": "Jupiter"
}

# Iterate over each question in the dictionary
for question, answer in questions.items():
    # Display the question to the user
    print(question)
    
    # Prompt the user to input their answer
    user_answer = input("Your answer: ")
    
    # Check if the user's answer matches the correct answer from the dictionary
    if user_answer.lower() == answer.lower():
        # Provide feedback to the user on a correct answer
        print("Correct!")
    else:
        # Provide feedback to the user on an incorrect answer
        print("Incorrect. The correct answer is:", answer)

# End of the program
print("Thank you for playing!")
