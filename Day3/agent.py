import os
import json
from dotenv import load_dotenv
from groq import Groq
from calculator_tool import calculator

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "openai/gpt-oss-120b"

calculator_tool = {
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "Calculates a mathematical expression.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The mathematical expression to calculate."
                }
            },
            "required": ["expression"]
        }
    }
}

questions = [
    "What is Python used for?",
    "What is the total fee if CS101 costs Rs. 12000 and AI202 costs Rs. 18000, with a 10% scholarship?",
    "If I have Rs. 50000 and spend Rs. 12500 on a course and Rs. 8500 on a laptop, how much money remains?"
]

for question in questions:

    print("\nQ:", question)

    messages = [
        {
            "role": "system",
            "content": "Answer normally when no calculation is needed. When a calculation is needed, use the calculator tool and use its result in your final answer."
        },
        {
            "role": "user",
            "content": question
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=[calculator_tool],
        tool_choice="auto",
        temperature=0
    )

    message = response.choices[0].message

    if message.tool_calls:

        for tool_call in message.tool_calls:

            print("Tool call:", tool_call.function.name)

            arguments = json.loads(tool_call.function.arguments)
            expression = arguments["expression"]

            print("Expression:", expression)

            result = calculator(expression)

            print("Tool result:", result)

            messages.append(message)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })

        final_response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0
        )

        print("A:", final_response.choices[0].message.content)

    else:
        print("Tool call: None")
        print("A:", message.content)