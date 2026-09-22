# Day 1 Analysis: Plain Chatbot vs Rule-Based Workflow vs AI Agent

## 1. Scenario

The chosen scenario is a Student Personal Task and Assignment Assistant.

The student has private task information stored in a local JSON file.

The system should answer:

> What tasks do I have due soon, and which one should I work on first?

The private data contains:

- Student information
- Assignment names
- Subjects
- Due dates
- Priority
- Task status

---

# 2. Plain Chatbot

## How it works

The plain chatbot uses an LLM to understand and respond to the user's question.

It does not access the student's private JSON file.

Therefore, when the user asks about actual tasks, the chatbot explains that it cannot access the student's private task information.

## Data Access

The chatbot has no access to:

```text
student_tasks.json