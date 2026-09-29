# Add an AI chat agent to HubSpot CMS

How to put an AI support agent on a HubSpot CMS site: where the script goes, what plan you need, and how to fix the usual problems.

## Before you start

Applies to website pages and landing pages hosted on HubSpot. If your site isn't on HubSpot CMS, use the guide for the platform it's actually on.

You'll need the embed script from your chat tool. It usually looks like this:

```html
<script src="https://your-chat-provider.example/embed.js" data-agent-id="YOUR_AGENT_ID" defer></script>
```

If you're building the agent yourself on the Claude, OpenAI or Gemini API, **never paste an API key into HubSpot CMS**. Anything in custom code is visible in the page source. Put the key behind a small backend instead; see the [Claude API proxy example](../examples/claude-proxy/).

For the prompt itself, start from one of the [industry prompts](../README.md#industry-prompts).

## Steps

### 1. Open page settings

Click the settings icon, then go to Content > Pages.

### 2. Choose the domain

Select the domain you want the agent on, or apply to all domains.

### 3. Paste in the footer HTML

Under the Templates tab, paste the widget script into the Site footer HTML field and save.

### 4. Check HubSpot chat

If you use HubSpot's own chat flows on the same pages, decide which one stays so visitors don't see two bubbles.

## Common problems

**Missing on landing pages.** Landing pages can have their own settings. Check the landing pages settings for the same domain.

**Widget loads slowly or delays the page.** Make sure the script tag includes `defer` and is in the footer, not the head.

**It overlaps another floating button on mobile.** Cookie banners, WhatsApp buttons and back-to-top buttons often sit in the same corner. Move one of them in its settings.

## No-code route

If you'd rather not handle the model, hosting and widget yourself, a no-code AI agent builder like [FwdSlash](https://www.fwdslash.ai) trains an agent on your site and gives you the script above. The full walkthrough is in [How to add or embed Claude in any website](https://www.fwdslash.ai/blog/how-to-add-embed-claude-in-any-website) on the FwdSlash blog.

## Related

- [Human handoff patterns](../handoff/human-escalation.md)
- [Anatomy of a support agent prompt](../guides/prompt-anatomy.md)
