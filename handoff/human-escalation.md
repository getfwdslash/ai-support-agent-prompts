# Human handoff patterns for AI support agents

An AI support agent is judged by what happens when it can't help. This page covers when to hand a conversation to a person, how to word it, and what the person on the other end needs.

## The four triggers

Every prompt in this repo hands over on some version of these:

1. **Safety or urgency.** Fraud, a medical emergency, a legal deadline, someone in danger. The agent gives the urgent contact in its first sentence, then offers a handover.
2. **Action on an account or order.** Anything that changes a booking, order, policy, membership or account. The agent can explain; only a person (or a trusted system) can act.
3. **Judgment calls.** Coverage decisions, admissions chances, whether someone has a case, which product is right for their finances. These need a qualified human.
4. **Frustration.** The visitor asks for a person, repeats the same question, or uses words like "useless" or "ridiculous". Don't argue with the signal.

## Add this block to any prompt

```text
## Handing over
When a handover trigger applies:
1. Tell the visitor in one sentence that you're connecting them with the team.
2. Write a summary for the team in this format:
   Need: <one line>
   Details given: <order number, dates, product, anything relevant>
   Already tried: <what you explained or suggested>
   Urgency: <normal | high>
3. If the team is offline ({{SUPPORT_HOURS}}), say when they'll reply and ask for an email address.
Never make the visitor repeat what they've already told you.
```

## Wording that works

| Situation | Say | Avoid |
|---|---|---|
| Normal handover | "I'll connect you with our team so they can sort this out. I've passed on what you told me." | "I'm just an AI and can't help with that." |
| Team offline | "The team is back at 9am tomorrow. Can I take your email so they can reply first thing?" | "No one is available." |
| Urgent | "Please call 1800-XXX-XXXX now to block your card. I'm also flagging this to our team." | Asking clarifying questions first. |
| Frustrated visitor | "Sorry this has been frustrating. Let me get a person to help." | Explaining why the answer was correct. |

## Where the handover goes

The summary is only useful if it lands where your team already works. Common routes:

- **Team chat.** The conversation is forwarded to a Slack channel and a teammate replies from there. [FwdSlash](https://www.fwdslash.ai) works this way: when a visitor asks for a human, the chat is transferred to your team in Slack.
- **Helpdesk ticket.** The summary becomes a ticket in Zendesk, Freshdesk, Intercom or HubSpot.
- **Email.** Fine for small teams, but set an auto-reply with a response time.

Whatever the route, measure two things: how often chats are handed over, and how long visitors wait for a person. A handover rate that keeps rising usually means the knowledge base is missing something, not that the agent is broken.

## Related

- [Anatomy of a support agent prompt](../guides/prompt-anatomy.md)
- [Industry prompts](../README.md#industry-prompts)
