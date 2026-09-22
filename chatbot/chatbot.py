from groq import Groq

client = Groq()

print("=== PLAIN CHATBOT ===")

user_question = input("Ask your question: ")

prompt = f"""
You are a simple chatbot.

The user asked:
{user_question}

You do NOT have access to the student's private task data.

Answer the question honestly.
Do not invent the student's actual tasks.

If the question requires private student information,
explain that you cannot access it.
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nChatbot response:")
print(response.choices[0].message.content)
