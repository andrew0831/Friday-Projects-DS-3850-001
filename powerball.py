print("Welcome to the PowerBall number generator!")

# Asking the user if they want PowerBall numbers
response = input("Would you like some PowerBall numbers? (yes/no): ")

if response.lower() == "yes":
    # Generating the numbers
    white_ball_1 = random.randint(1, 69)
    white_ball_2 = random.randint(1, 69)
    white_ball_3 = random.randint(1, 69)
    white_ball_4 = random.randint(1, 69)
    white_ball_5 = random.randint(1, 69)
    red_ball = random.randint(1, 26)
    
    # Printing the numbers with appropriate spacing
    print("Your PowerBall numbers are:")
    print(white_ball_1, "  ", white_ball_2, "  ", white_ball_3, "  ", white_ball_4, "  ", white_ball_5, "    ", red_ball)
    
    # Farewell message
    print("Good luck with your PowerBall ticket!")
else:
    print("Okay, maybe next time! Have a great day!")
