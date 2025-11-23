import random

# ------------------------------
# Quiz Questions
# ------------------------------
questions = [
    {
        "question": "Which language is used to write Python?",
        "options": ["A. C", "B. Java", "C. Python", "D. None"],
        "answer": "C"
    },
    {
        "question": "What is the output of 2**3?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 12"],
        "answer": "B"
    },
    
        "question": "Which of the following is a keyword in Python?",
        "options": ["A. while", "B. loop", "C. repeat", "D. switch"],
        "answer": "A"
    {
        "question": "What is used to define a block of code in Python?",
        "options": ["A. Brackets", "B. Indentation", "C. Semicolon", "D. None"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
        "answer": "C"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["A. input()", "B. scan()", "C. get()", "D. take()"],
        "answer": "A"
    },
    {
        "question": "What does 'len()' return?",
        "options": ["A. Height", "B. Length", "C. Width", "D. Size of screen"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "What is the index of the first element in a list?",
        "options": ["A. 1", "B. -1", "C. 0", "D. 2"],
        "answer": "C"
    },
    {
        "question": "Which module is used to generate random numbers?",
        "options": ["A. random", "B. math", "C. os", "D. time"],
        "answer": "A"
    }
]

# Shuffle questions for randomness
random.shuffle(questions)

# ------------------------------
# Quiz Game Start
# ------------------------------
print("\n==============================")
print("       PYTHON QUIZ GAME       ")
print("==============================\n")

score = 0
question_number = 1

for q in questions:
    print(f"Q{question_number}. {q['question']}")
    
    for option in q["options"]:
        print(option)
    
    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == q["answer"]:
        print("✔ Correct!\n")
        score += 1
    else:
        print(f"✘ Wrong! Correct answer is {q['answer']}\n")

    question_number += 1

# ------------------------------
# Final Score
# ------------------------------
print("==============================")
print("           RESULT             ")
print("==============================")
print(f"Your Score: {score} / {len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage == 100:
    print("Outstanding! You're a genius!")
elif percentage >= 80:
    print("Excellent work!")
#elif percentage >= 50:
    print("Good job, keep improving!")
else:
    print("Try again and you will do better next time!")