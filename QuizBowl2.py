import sqlite3

connection = sqlite3.connect('FridayProj5.db')
cursor = connection.cursor()
questions = cursor.execute("SELECT * FROM QuestAns;").fetchall()

total_questions = len(questions)
correct_answers = 0

for question in questions:
    correct_answer = question[2]
    print(f"{question[0]}. {question[1]}")
    user_answer = input("Your answer: ")
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
        correct_answers += 1
    else:
        print(f"That was incorrect. The correct answer is {correct_answer}.")

print(f"End of the quiz. You got {correct_answers}/{total_questions} correct.")

connection.close()
