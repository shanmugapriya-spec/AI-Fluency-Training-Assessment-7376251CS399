import json
from datetime import date
from groq import Groq


# ==========================================
# TOOL 1: Read private student task data
# ==========================================

def get_student_tasks():
    with open("../data/student_tasks.json", "r") as file:
        data = json.load(file)

    return data


# ==========================================
# TOOL 2: Get today's date
# ==========================================

def get_today_date():
    return str(date.today())


# ==========================================
# Create Groq client
# ==========================================

client = Groq()


# ==========================================
# Define tools
# ==========================================

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_student_tasks",
            "description": "Reads the student's private task data.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_today_date",
            "description": "Returns today's date.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]


# ==========================================
# Get user's question
# ==========================================

print("=== AI AGENT ===")

user_question = input(
    "Ask the AI agent about your tasks: "
)


# ==========================================
# System instructions
# ==========================================

system_message = """
You are a student task management AI agent.

You have tools that can access private student data.

When the user asks about their actual tasks,
deadlines, or priorities, use the available tools.

Follow this process:

1. Understand the user's request.
2. Decide which tool is needed.
3. Use the tool.
4. Observe the tool result.
5. Continue if another tool is needed.
6. Give a clear final answer.

Never invent private task information.
"""


messages = [
    {
        "role": "system",
        "content": system_message
    },
    {
        "role": "user",
        "content": user_question
    }
]


# ==========================================
# AGENT LOOP
# ==========================================

for step in range(5):

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    messages.append(message)


    # ======================================
    # Check whether the agent requested tools
    # ======================================

    if not message.tool_calls:

        print("\nAgent final response:")
        print(message.content)

        break


    # ======================================
    # Execute requested tools
    # ======================================

    for tool_call in message.tool_calls:

        tool_name = tool_call.function.name

        print(f"\nAgent used tool: {tool_name}")


        if tool_name == "get_student_tasks":

            result = get_student_tasks()

        elif tool_name == "get_today_date":

            result = get_today_date()

        else:

            result = "Unknown tool"


        # ==================================
        # Send tool result back to the agent
        # ==================================

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            }
        )

else:

    print(
        "\nAgent stopped after reaching "
        "the maximum number of steps."
    )
    