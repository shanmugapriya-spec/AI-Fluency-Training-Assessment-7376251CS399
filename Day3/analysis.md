# From Prompt to Action: Understanding LLMs, Tools, and Agents

## 1. Scenario

The scenario used in this project is a **Student Course Fee Calculator**.

The system receives questions related to courses, fees, scholarships, and available money.

Three questions were tested:

1. What is Python used for?
2. What is the total fee if CS101 costs Rs. 12000 and AI202 costs Rs. 18000, with a 10% scholarship?
3. If I have Rs. 50000 and spend Rs. 12500 on a course and Rs. 8500 on a laptop, how much money remains?

The first question can be answered using the language model's existing knowledge. The second and third questions involve numerical calculations.

---

## 2. What is an LLM?

A Large Language Model (LLM) is an AI model trained on a large amount of text. It can understand questions and generate natural-language responses.

In this project, the LLM is used to understand the user's question and generate an answer.

For example, the question:

> What is Python used for?

can be answered directly from the model's knowledge without using an external tool.

---

## 3. What is a Tool?

A tool is an external function that an AI model can use when it needs an operation that should be performed outside the model itself.

In this project, the tool is a **calculator**.

The calculator receives a mathematical expression and returns the calculated result.

Example:

```text
30000 * 0.9