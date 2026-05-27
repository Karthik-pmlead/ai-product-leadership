# Prompt Engineering — Templates & Evaluation Framework

This document contains production-grade prompt templates and a complete evaluation framework for GenAI systems.

It is designed for:
- LLM applications
- RAG systems
- AI copilots
- agent-based systems
- decision intelligence platforms

---

# 🎯 Design Principles

- deterministic structure where possible
- explicit instructions
- constrained outputs
- evaluation-friendly formatting
- minimal ambiguity

---

# 🧠 PART 1 — PROMPT TEMPLATES

---

## 1. System Instruction Template

```text
You are a {role}.

Your task is to {goal}.

Constraints:
- {constraint_1}
- {constraint_2}

Output format:
{format_spec}

If information is missing, respond with "INSUFFICIENT DATA".
```

2. RAG Answering Template
```
You are a retrieval-augmented assistant.

Use ONLY the provided context to answer.

Context:
{context}

Question:
{question}

Rules:
- Do not hallucinate
- If answer is not in context, say "Not found in provided data"

Answer:
```

3. Summarization Template
```
Summarize the following content.

Requirements:
- max {n} bullet points
- preserve key facts
- remove redundancy

Content:
{text}

Summary:
```
4. Decision Support Template
```
You are a decision intelligence assistant.

Task:
Help evaluate options and recommend the best choice.

Options:
{options}

Evaluation criteria:
{criteria}

Output:
- comparison table
- recommendation
- reasoning
```

5. Classification Template

```
Classify the following input into one of:
{labels}

Input:
{text}

Return ONLY the label.
```

6. Agent Reasoning Template
```
You are an AI agent.

Goal:
{goal}

Available tools:
{tools}

Steps:
1. Understand input
2. Plan approach
3. Execute reasoning
4. Provide final output

Return structured response.
```

7. Structured JSON Output Template

```
Return output in valid JSON only.

Schema:
{schema}

Input:
{input}
```

8. Explanation Template

```
Explain the output in simple terms.

Constraints:
- no jargon
- max 5 bullets
- include example

Output:
{result}
```
