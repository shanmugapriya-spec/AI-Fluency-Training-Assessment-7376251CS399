import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "openai/gpt-oss-120b"

questions = [
    "What is Python used for?",
    "What is the total fee if CS101 costs Rs. 12000 and AI202 costs Rs. 18000, with a 10% scholarship?",
    "If I have Rs. 50000 and spend Rs. 12500 on a course and Rs. 8500 on a laptop, how much money remains?"
]

for question in questions:
    print("\nQ:", question)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": question}
        ],
        temperature=0
    )

    print("A:", response.choices[0].message.content)

    