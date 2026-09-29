# Anatomy of a support agent prompt

Every prompt in this repo uses the same seven sections. Here's what each one does and what goes wrong when it's missing.

## 1. Identity

```text
You are the virtual assistant for {{BUSINESS_NAME}}, a dental clinic in Pune. You chat with visitors on {{WEBSITE}}.
```

One or two sentences. The business type and location change how the model interprets almost every question ("Do you take insurance?" means different things for a clinic in the US and one in India).

**Missing it:** generic answers that could come from any company.

## 2. What you can help with

A short list of jobs, written as actions. This is the agent's scope.

**Missing it:** the agent tries to help with everything, including things it shouldn't.

## 3. What you must never do

The industry's hard limits, stated plainly. A banking agent never asks for a PIN. A healthcare agent never diagnoses. A law firm agent never gives legal advice.

Write these as specific behaviours, not values. "Be responsible about medical questions" is too vague to follow. "Never interpret symptoms or suggest a condition" isn't.

**Missing it:** the risky answers that end up in screenshots.

## 4. Tone

Describe the voice in a sentence and add a length limit. Chat is read on phones; 80 words is a good default.

**Missing it:** walls of text with headings and bullet points in a chat bubble.

## 5. When to hand over

The specific triggers for passing the chat to a person, and what to say when it happens. See [human handoff patterns](../handoff/human-escalation.md).

**Missing it:** the agent loops on "I'm sorry, I can't help with that" while the visitor leaves.

## 6. Source of truth

```text
Answer only from the knowledge base provided. If the answer isn't there, say you don't have that information and offer to connect them with the team.
```

This is the single most important line. Without it, the model fills gaps from its training data, which is how agents end up quoting a competitor's return policy or inventing a discount.

## 7. Tests

Not part of the prompt itself, but every file in this repo ends with test questions. Each one checks a rule. Run them after every change to the prompt or knowledge base, the same way you'd run tests after changing code.

## Prompt versus knowledge base

Rules go in the prompt. Facts go in the knowledge base.

| Goes in the prompt | Goes in the knowledge base |
|---|---|
| Never quote a delivery date | Standard delivery takes 3 to 5 business days |
| Hand fraud reports to a person immediately | The card blocking hotline number |
| Keep replies under 80 words | Your returns policy |

Putting facts in the prompt means editing the prompt every time a price changes. Putting rules in the knowledge base means the model treats them as information it can weigh, not instructions it must follow.

## Further reading

- [The evolution of website chatbots](https://www.fwdslash.ai/blog/evolution-of-website-chatbots): how support chat moved from live chat and decision trees to AI agents
- [Industry prompts](../README.md#industry-prompts)
