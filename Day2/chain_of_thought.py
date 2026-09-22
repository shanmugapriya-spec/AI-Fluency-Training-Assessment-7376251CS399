def chain_of_thought(question):
    """
    Chain-of-Thought demonstration:
    The problem is broken into logical steps before
    producing the final answer.
    """

    print("=== CHAIN-OF-THOUGHT ===")
    print("Question:", question)

    print("\nReasoning Summary:")
    print("1. The event starts at 10:00 AM.")
    print("2. We need to arrive 30 minutes early.")
    print("3. Required arrival time = 9:30 AM.")
    print("4. The journey takes 2 hours.")
    print("5. Leave time = 9:30 AM - 2 hours = 7:30 AM.")

    answer = "You should leave at 7:30 AM."

    print("\nFinal Answer:", answer)


if __name__ == "__main__":
    question = (
        "A college event in Coimbatore starts at 10:00 AM. "
        "The journey takes 2 hours and I want to arrive 30 minutes early. "
        "What time should I leave?"
    )

    chain_of_thought(question)