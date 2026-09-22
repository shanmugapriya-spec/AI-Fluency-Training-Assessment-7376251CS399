from collections import Counter


def solve_question():
    """
    Simulates multiple reasoning attempts for the same question.
    """

    question = (
        "A student has ₹500. They spend ₹180 on transportation "
        "and ₹120 on food. How much money is left?"
    )

    print("=== SELF-CONSISTENCY ===")
    print("Question:", question)

    # Answers produced by multiple reasoning attempts
    answers = [200, 200, 200, 200, 200]

    print("\nAnswers from multiple attempts:")

    for i, answer in enumerate(answers, start=1):
        print(f"Attempt {i}: ₹{answer}")

    # Find the most common answer
    majority_answer = Counter(answers).most_common(1)[0][0]

    print("\nMajority Answer:", f"₹{majority_answer}")

    # Verify the answer
    correct_answer = 500 - 180 - 120

    if majority_answer == correct_answer:
        print("Result: Correct")
    else:
        print("Result: Incorrect")


if __name__ == "__main__":
    solve_question()
    