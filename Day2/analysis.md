# Day 2 Analysis: Direct Prompting, Chain-of-Thought, Self-Consistency and ReAct

## 1. Introduction

This project compares different approaches used by AI systems to solve problems. The approaches demonstrated are Direct Prompting, Chain-of-Thought, Self-Consistency, and ReAct.

The selected scenario is a college event in Coimbatore. The scenario contains both reasoning-based questions and a question that requires current external information. This makes it useful for understanding the difference between reasoning and tool usage.

The project also demonstrates how Self-Consistency can use multiple answers to improve reliability and how a ReAct agent can interact with an external weather tool.

---

## 2. Scenario Used

The main reasoning question used in the demonstration is:

"A college event in Coimbatore starts at 10:00 AM. The journey takes 2 hours and I want to arrive 30 minutes early. What time should I leave?"

The calculation is:

* Event start time = 10:00 AM
* Required early arrival = 30 minutes
* Required arrival time = 9:30 AM
* Journey duration = 2 hours
* Required departure time = 7:30 AM

Therefore, the correct answer is 7:30 AM.

For demonstrating tool usage, the ReAct agent is given another question:

"What is the current weather in Coimbatore?"

This question requires current external information rather than only reasoning from the question.

---

## 3. Direct Prompting

### Explanation

Direct Prompting is the simplest approach. The user gives a question to the AI model and the model produces an answer directly.

The process is:

Question → Answer

There is no explicit multi-step reasoning process and no external tool call in this demonstration.

### Capabilities

Direct Prompting is useful for:

* Simple factual questions
* Straightforward calculations
* Short responses
* Tasks where the model already has the required information

It is simple and fast because there are no additional reasoning or tool-calling steps.

### Limitations

Direct Prompting can be less reliable for complex multi-step problems because the model may produce an answer without explicitly breaking the problem into smaller parts.

It also cannot automatically obtain live information from an external source when no tool is provided.

### Tool Usage

No external tool is used.

The program directly produces the answer:

"7:30 AM."

### Final Answer Process

The model receives the question and directly produces the final answer.

For the selected problem:

10:00 AM − 30 minutes − 2 hours = 7:30 AM.

### Scenario-Specific Limitation

Direct Prompting can solve the travel-time calculation, but it cannot independently check the current weather in Coimbatore because no weather tool is connected to it.

---

## 4. Chain-of-Thought

### Explanation

Chain-of-Thought is a reasoning approach where a complex problem is divided into smaller logical steps before producing the final answer.

In this project, a concise reasoning summary is displayed rather than private internal model reasoning.

The demonstrated process is:

Question → Break into steps → Calculate → Final Answer

### Capabilities

Chain-of-Thought can help with:

* Multi-step calculations
* Logical reasoning
* Problems that require several intermediate steps
* Reducing mistakes caused by skipping important steps

For the selected scenario, the problem is divided into smaller steps:

1. Identify the event start time.
2. Calculate the required early arrival time.
3. Subtract the journey duration.
4. Produce the departure time.

### Limitations

Chain-of-Thought does not automatically provide access to current external information.

For example, reasoning about the question "What is the current weather in Coimbatore?" does not provide the actual current weather unless the system has access to a weather tool or another external information source.

### Tool Usage

No external tool is used in this implementation.

### Final Answer Process

The reasoning summary calculates:

* Event = 10:00 AM
* Early arrival = 30 minutes
* Arrival = 9:30 AM
* Journey = 2 hours
* Departure = 7:30 AM

The final answer is therefore 7:30 AM.

### Scenario-Specific Limitation

CoT is useful for the travel-time calculation, but it cannot independently retrieve live weather information.

---

## 5. Self-Consistency

### Explanation

Self-Consistency is a technique in which the same reasoning problem is solved multiple times and the resulting answers are compared.

Instead of relying on only one generated answer, multiple attempts are considered and the most common answer can be selected.

The process is:

Question → Multiple attempts → Compare answers → Majority Answer

### Question Used

"A student has ₹500. They spend ₹180 on transportation and ₹120 on food. How much money is left?"

Correct calculation:

₹500 − ₹180 − ₹120 = ₹200

### Demonstration

Five attempts were recorded:

| Attempt | Answer |
| ------- | -----: |
| 1       |   ₹200 |
| 2       |   ₹200 |
| 3       |   ₹200 |
| 4       |   ₹200 |
| 5       |   ₹200 |

The majority answer is ₹200.

The answer is then checked against the actual calculation:

₹500 − ₹180 − ₹120 = ₹200

Therefore, the majority answer is correct.

### Reliability

Self-Consistency can improve reliability when different reasoning attempts sometimes produce different answers. If several independent attempts reach the same answer, the majority result provides additional evidence for that answer.

However, majority voting does not guarantee correctness. If the model repeatedly produces the same incorrect answer, the majority answer can still be wrong.

### Temperature

Self-Consistency is normally useful when the model generates different reasoning paths. A non-zero temperature can introduce variation between model responses.

At temperature 0, model responses are generally more deterministic, so repeated attempts are more likely to produce the same result. This reduces the diversity that Self-Consistency relies on.

### Tool Usage

The demonstration does not use an external tool.

### Scenario-Specific Limitation

Self-Consistency can help with reasoning problems, but it does not automatically provide current external information. A separate tool would still be required for questions such as current weather.

---

## 6. ReAct Agent

### Explanation

ReAct stands for Reasoning and Acting.

A ReAct agent combines reasoning with actions such as calling external tools. The agent can decide that it needs additional information, call a tool, observe the returned information, and then produce an answer.

The basic process is:

Thought → Action → Observation → Final Answer

### Tool Used

The project uses a weather tool called:

`get_weather()`

The tool contacts the Open-Meteo weather service and retrieves current weather information for Coimbatore.

### Demonstration

The agent receives:

"What is the current weather in Coimbatore?"

The agent first identifies that current weather information is required.

**Thought:**

"I need current weather information, so I should use a weather tool."

**Action:**

The agent calls:

`get_weather("Coimbatore")`

**Observation:**

The tool returns current weather information, including temperature and humidity.

**Final Answer:**

The agent uses the observed information to produce the final response.

### Capabilities

ReAct is useful when a problem requires external information or actions.

It can:

* Reason about what information is needed
* Select an appropriate tool
* Call the tool
* Use the returned observation
* Produce a final answer based on the observation

### Limitations

ReAct systems are more complex than direct prompting because they require tool definitions and additional processing.

They can also fail if:

* A tool is unavailable
* The external service is unavailable
* The tool returns incorrect or incomplete information
* The agent selects an inappropriate tool
* Network access is unavailable

### Scenario-Specific Advantage

For the selected scenario, ReAct can handle the current-weather question because it has access to an external weather tool.

This is something that Direct Prompting and basic Chain-of-Thought cannot do by themselves.

---

## 7. Comparison of Approaches

| Feature                | Direct Prompting             | Chain-of-Thought                     | Self-Consistency                           | ReAct                                                       |
| ---------------------- | ---------------------------- | ------------------------------------ | ------------------------------------------ | ----------------------------------------------------------- |
| Reasoning depth        | Low                          | Higher for multi-step problems       | Multiple reasoning attempts                | Reasoning combined with actions                             |
| Tool usage             | No                           | No                                   | No in this demonstration                   | Yes                                                         |
| Multi-step reliability | Suitable for simple problems | Can improve multi-step reasoning     | Can improve reliability through agreement  | Useful when reasoning and external information are required |
| Transparency           | Shows final answer           | Shows reasoning summary              | Shows multiple answers and majority result | Shows Thought, Action and Observation                       |
| Speed                  | Fast                         | Usually slower than direct prompting | Slower because of multiple attempts        | Can be slower because of tool calls                         |
| Cost                   | Low                          | Potentially higher                   | Higher because of multiple generations     | Higher because of reasoning and tool calls                  |
| Consistency            | Usually one answer           | Depends on model generation          | Uses majority voting                       | Depends on reasoning and tool reliability                   |

---

## 8. Reasoning Depth

Direct Prompting provides the shortest path from question to answer.

Chain-of-Thought provides a structured reasoning process for multi-step problems.

Self-Consistency extends this by generating multiple possible solutions and comparing their final answers.

ReAct combines reasoning with actions. Its reasoning is not limited to information already available to the model because it can interact with external tools.

Therefore, the approaches represent increasing levels of processing complexity, from direct answering to reasoning with external interaction.

---

## 9. Tool Usage

Direct Prompting does not use a tool in this project.

Chain-of-Thought also does not use a tool.

Self-Consistency does not use a tool in the demonstrated implementation.

ReAct uses the `get_weather()` function to retrieve current weather information.

This demonstrates an important difference between reasoning and information retrieval. Reasoning can process available information, while a tool can provide new information from an external source.

---

## 10. Reliability on Multi-Step Questions

Direct Prompting can solve simple multi-step questions, but it does not explicitly break the problem into intermediate steps.

Chain-of-Thought can make multi-step reasoning more structured by separating the problem into smaller calculations.

Self-Consistency can provide additional reliability by comparing several answers and selecting the majority answer.

ReAct can be useful when a multi-step problem also requires external information or an action.

No approach guarantees a correct answer in every situation. Reliability depends on the model, prompt, quality of information, and any tools being used.

---

## 11. Transparency

Direct Prompting provides the final answer with minimal process information.

Chain-of-Thought can provide a reasoning summary that explains how the answer was reached.

Self-Consistency provides multiple results and shows the majority answer.

ReAct provides a visible sequence of:

Thought → Action → Observation → Final Answer.

In this project, the displayed CoT is a concise reasoning summary rather than private internal chain-of-thought.

---

## 12. Speed and Cost

Direct Prompting generally requires the least processing.

Chain-of-Thought may require additional processing because the problem is handled through multiple reasoning steps.

Self-Consistency can require several model generations, so it can increase both processing time and cost.

ReAct can also require additional time because the agent may need to call external tools and wait for their responses.

Therefore, more advanced approaches can provide additional capabilities but may require more computation or external resources.

---

## 13. Suitability Analysis

### Direct Prompting

Suitable for:

* Simple questions
* Short answers
* Straightforward calculations
* Situations where external information is not required

### Chain-of-Thought

Suitable for:

* Multi-step mathematical problems
* Logical problems
* Problems where intermediate reasoning is useful

### Self-Consistency

Suitable for:

* Difficult reasoning problems
* Problems where multiple possible reasoning paths can be generated
* Situations where agreement between multiple answers can improve confidence

### ReAct

Suitable for:

* Tasks requiring external information
* Tasks requiring tools
* Real-world applications where the AI must interact with external systems

For the selected college travel scenario, ReAct is particularly useful for the current-weather question because it can obtain information from an external weather service.

---

## 14. General Conclusion

The four approaches demonstrate different ways an AI system can process a problem.

Direct Prompting provides a simple and fast question-to-answer process.

Chain-of-Thought introduces structured reasoning for multi-step problems.

Self-Consistency improves the reasoning process by comparing multiple generated answers and selecting the majority answer.

ReAct extends reasoning by allowing an AI agent to interact with external tools. In this project, the ReAct agent uses a weather tool to retrieve current information about Coimbatore.

The main lesson from the experiment is that reasoning and tool usage solve different problems. Better reasoning can help an AI process complex information, while tools allow an AI system to obtain information that is not available in the original prompt.

Therefore, the appropriate approach depends on the requirements of the task. Simple questions may need only Direct Prompting, complex reasoning problems can benefit from Chain-of-Thought or Self-Consistency, and tasks requiring external information or actions can use a ReAct-style agent.

