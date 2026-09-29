# AI Support Agent Prompts

Copy-paste system prompts, guardrails and deployment guides for customer support AI agents, organised by industry and by website platform.

Every prompt here is model-agnostic. It works with Claude, GPT, Gemini or any LLM that accepts a system prompt, whether you build the agent yourself on an API or in a no-code AI agent builder like [FwdSlash](https://www.fwdslash.ai).

**Browse the site:** https://getfwdslash.github.io/ai-support-agent-prompts/

## What's inside

### Industry prompts

Each file has a ready-to-use system prompt, the guardrails that matter in that industry and why, a knowledge base checklist, escalation rules, and test questions to run before launch.

| Industry | What the agent handles | File |
|---|---|---|
| Banking | Account FAQs, card issues, branch info, fraud routing | [industries/banking.md](industries/banking.md) |
| E-commerce | Product questions, orders, returns, shipping | [industries/ecommerce.md](industries/ecommerce.md) |
| Education | Admissions, courses, fees, student support | [industries/education.md](industries/education.md) |
| Fitness | Memberships, class schedules, trainers, freezes | [industries/fitness.md](industries/fitness.md) |
| Healthcare | Appointments, clinic info, insurance accepted, triage routing | [industries/healthcare.md](industries/healthcare.md) |
| Hospitality | Rooms, bookings, amenities, local info | [industries/hospitality.md](industries/hospitality.md) |
| HR | Candidate questions and internal policy FAQs | [industries/hr.md](industries/hr.md) |
| Insurance | Policy questions, claims process, quotes routing | [industries/insurance.md](industries/insurance.md) |
| Law firms | Practice areas, consultation booking, client intake | [industries/law-firms.md](industries/law-firms.md) |
| Supply chain | Order and shipment status, supplier questions | [industries/supply-chain.md](industries/supply-chain.md) |

### Platform guides

Where to paste an AI chat widget on each website builder, plan requirements, and the problems people hit most often.

| Platform | File |
|---|---|
| WordPress | [platforms/wordpress.md](platforms/wordpress.md) |
| Shopify | [platforms/shopify.md](platforms/shopify.md) |
| Wix | [platforms/wix.md](platforms/wix.md) |
| Webflow | [platforms/webflow.md](platforms/webflow.md) |
| BigCommerce | [platforms/bigcommerce.md](platforms/bigcommerce.md) |
| HubSpot CMS | [platforms/hubspot.md](platforms/hubspot.md) |
| Squarespace | [platforms/squarespace.md](platforms/squarespace.md) |
| Framer | [platforms/framer.md](platforms/framer.md) |

### Guides and patterns

- [Anatomy of a support agent prompt](guides/prompt-anatomy.md): the seven sections every prompt in this repo uses, and why.
- [Human handoff patterns](handoff/human-escalation.md): when an AI agent should pass a chat to a person, and how to word it.
- [Claude API proxy example](examples/claude-proxy/): a minimal Cloudflare Worker for developers who want to call Claude from a website without exposing the API key.

## How to use a prompt

1. Open the industry file closest to your business.
2. Copy the block under **The system prompt**.
3. Replace every `{{PLACEHOLDER}}` with your details.
4. Load your knowledge base (the checklist in each file tells you what to include).
5. Run the test questions at the bottom of the file. Fix anything the agent gets wrong before you go live.

If you don't want to manage the model, hosting and widget yourself, [FwdSlash](https://www.fwdslash.ai) lets you paste one of these prompts into a no-code agent, train it on your site, pick the model, and embed it with one script tag.

## Principles behind these prompts

- **Answer from the knowledge base, not from memory.** A support agent that guesses is worse than no agent.
- **Say "I don't know" and route to a person.** Every prompt defines exactly when to hand over.
- **Industry rules beat general helpfulness.** A banking agent never asks for a PIN. A healthcare agent never diagnoses. These are written into each prompt, not left to the model.
- **Short answers.** Visitors read chat on phones.

## Contributing

New industries, platforms and fixes are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. Use the prompts in commercial projects, change them, ship them. See [LICENSE](LICENSE).

---

Maintained by [FwdSlash](https://www.fwdslash.ai), the no-code AI agent builder.
