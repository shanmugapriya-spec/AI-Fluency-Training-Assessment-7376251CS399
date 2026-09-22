import json
from datetime import date


def load_tasks():
    with open("../data/student_tasks.json", "r") as file:
        data = json.load(file)

    return data


def find_upcoming_tasks(tasks):
    today = date.today()
    upcoming = []

    for task in tasks:
        due_date = date.fromisoformat(task["due_date"])
        days_left = (due_date - today).days

        if 0 <= days_left <= 7:
            upcoming.append((task, days_left))

    return upcoming


print("=== RULE-BASED WORKFLOW ===")

data = load_tasks()

upcoming_tasks = find_upcoming_tasks(data["tasks"])

if upcoming_tasks:
    print("\nUpcoming tasks:")

    for task, days_left in upcoming_tasks:
        print(
            f"- {task['title']} | "
            f"Due: {task['due_date']} | "
            f"Days left: {days_left} | "
            f"Priority: {task['priority']}"
        )
else:
    print("No upcoming tasks found.")


print("\nRule-based decision:")

if upcoming_tasks:
    first_task = min(
        upcoming_tasks,
        key=lambda item: (
            item[1],
            {"High": 1, "Medium": 2, "Low": 3}[item[0]["priority"]]
        )
    )

    task = first_task[0]

    print(f"Work on '{task['title']}' first.")
else:
    print("No task requires immediate attention.")