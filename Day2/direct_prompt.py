def direct_prompt(question):
    """
    Direct prompting:
    The model receives the question and gives an answer
    directly from its existing knowledge.
    """

    print("=== DIRECT PROMPTING ===")
    print("Question:", question)

    answer = (
        "For the college event, you should leave at 7:30 AM. "
        "The event starts at 10:00 AM, you want to arrive 30 minutes early, "
        "and the journey takes 2 hours."
    )

    print("Answer:", answer)


if __name__ == "__main__":
    question = (
        "A college event in Coimbatore starts at 10:00 AM. "
        "The journey takes 2 hours and I want to arrive 30 minutes early. "
        "What time should I leave?"
    )

    direct_prompt(question)