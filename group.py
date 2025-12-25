# Simple Quiz Application in Python (Username & Student ID Input)

# Taking Username and Student ID from user
username = input("Enter your username: ")
student_id = input("Enter your Student ID: ")

print(f"\n===== Welcome {username}! =====")
print(f"Student ID: {student_id}")
print("===== Welcome to the Quiz Application =====\n")

# Quiz data: questions, options, and correct answers
quiz = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "2. Which language is used for web apps?",
        "options": ["A. Python", "B. Java", "C. JavaScript", "D. C++"],
        "answer": "C"
    },
    {
        "question": "3. Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. James Gosling", "D. Bjarne Stroustrup"],
        "answer": "B"
    },
    {
        "question": "4. What is the capital of India?",
        "options": ["A. Mumbai","B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "5. What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "6. Which planet is known as the 'Red Planet'?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "7. What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "8. What is the chemical symbol for water?",
        "options": ["A. O2", "B. H2O", "C. CO2", "D. NaCl"],
        "answer": "B"
    },
    {
        "question": "9. Who painted the Mona Lisa?",
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
        "answer": "C"
    }
]

score = 0

# Asking questions
for q in quiz:
    print(q["question"])
    for option in q["options"]:
        print(option)
    
    user_answer = input("\nEnter your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("✔ Correct!\n")
        score += 1
    else:
        print(f"✘ Wrong! Correct answer is {q['answer']}\n")

# Final result
print("===== Quiz Completed =====")
print(f"Student: {username}")
print(f"Student ID: {student_id}")
print(f"Your Score: {score} out of {len(quiz)}")

if score == len(quiz):
    print("Excellent! Full marks!")
elif score >= len(quiz) // 2:
    print("Good job!")
else:
    print("Better luck next time!")
