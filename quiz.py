def display_question(question, options):
    print(question)
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")

def get_user_answer():
    while True:
        user_input = input("Enter your answer: ")
        if user_input.isdigit() and 1 <= int(user_input) <= 4:  # Assuming 4 options max
            return int(user_input)
        else:
            print("Invalid input. Please enter a number corresponding to your answer.")

def evaluate_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect. The correct answer is:", correct_answer)
        return 0

def run_quiz(questions):
    score = 0
    for question, options, correct_answer in questions:
        display_question(question, options)
        user_answer = get_user_answer()
        score += evaluate_answer(user_answer, correct_answer)
        print() 
    return score

def startQuiz():
    # Define quiz questions (question, options, correct_answer)
    questions = [
        ("What is the capital of France?", ["Paris", "Rome", "Berlin", "Madrid"], 1),
        ("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Venus", "Saturn"], 1),
        ("What is the powerhouse of the cell?", ["Nucleus", "Ribosome", "Mitochondria", "Chloroplast"], 3)
    ]

    print("Welcome to the Basic Quiz Game!")
    print("You will be asked a series of questions. Please input the number corresponding to your answer.")
    input("Press Enter to start the quiz...")

    score = run_quiz(questions)

    print("Quiz complete!")
    print("Your final score:", score)
startQuiz()