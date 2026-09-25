questions = {
    "What is the capital of India? ": "delhi",
    "Which language are we learning? ": "python",
    "How many days did our Python basics challenge have? ": "30"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question).lower()

    if user_answer == answer:
        print("Correct! 🎉")
        score += 1
    else:
        print("Wrong!")

print("\nQuiz completed!")
print("Your score:", score, "/", len(questions))
