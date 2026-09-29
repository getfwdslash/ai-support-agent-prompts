# Claude API proxy for website chat

A minimal Cloudflare Worker that lets a website chat widget talk to Claude without exposing your Anthropic API key.

Anything you put in a website's custom code is visible in the page source. If an API key ends up there, anyone can copy it and spend your credits. This Worker keeps the key server-side: the browser sends messages to the Worker, the Worker adds the key and your system prompt, calls Claude, and returns only the reply text.

## Files

| File | What it does |
|---|---|
| `worker.js` | The proxy: origin check, input limits, Claude API call |
| `wrangler.toml` | Config: model ID, allowed sites, system prompt |
| `demo.html` | A bare-bones chat page to test the Worker |

## Deploy

1. Install Wrangler and log in: `npm install -g wrangler` then `wrangler login`.
2. Edit `wrangler.toml`: set `MODEL` to a current model ID from Anthropic's models overview, set `ALLOWED_ORIGINS` to your site, and paste your system prompt from one of the [industry prompts](../../README.md#industry-prompts).
3. Add your API key as a secret: `npx wrangler secret put ANTHROPIC_API_KEY`.
4. Deploy: `npx wrangler deploy`.
5. Put the Worker URL into `demo.html` and open it from an allowed origin to test.

## What this doesn't do

This is a starting point, not a product. Before putting it in front of real visitors you'll want:

- **Rate limiting** per IP or session, so one visitor can't run up your bill. Cloudflare's rate limiting rules work well here.
- **Knowledge base retrieval.** The Worker sends only the system prompt and the chat. To answer from your content, you need to retrieve relevant pages and add them to the request.
- **Streaming**, so replies appear word by word.
- **Human handoff** to your team. See [human handoff patterns](../../handoff/human-escalation.md).
- **Logging and analytics** to see what visitors ask and where the agent fails.

If you'd rather not build those, a no-code AI agent builder like [FwdSlash](https://www.fwdslash.ai) handles retrieval, handoff to Slack, lead capture and analytics, and lets you choose Claude as the model. The trade-offs between both routes are covered in [How to add or embed Claude in any website](https://www.fwdslash.ai/blog/how-to-add-embed-claude-in-any-website).
