# Add an AI chat agent to Webflow

How to put an AI support agent on a Webflow site: where the script goes, what plan you need, and how to fix the usual problems.

## Before you start

Site-wide footer code needs a paid Site plan. On the free plan, you can still add the widget to a single page with a Code Embed element.

You'll need the embed script from your chat tool. It usually looks like this:

```html
<script src="https://your-chat-provider.example/embed.js" data-agent-id="YOUR_AGENT_ID" defer></script>
```

If you're building the agent yourself on the Claude, OpenAI or Gemini API, **never paste an API key into Webflow**. Anything in custom code is visible in the page source. Put the key behind a small backend instead; see the [Claude API proxy example](../examples/claude-proxy/).

For the prompt itself, start from one of the [industry prompts](../README.md#industry-prompts).

## Steps

### 1. Site-wide (paid plan)

Open Site settings, go to Custom code, and paste the script into the Footer code field.

### 2. Single page (any plan)

Drag a Code Embed element onto the page and paste the script inside it.

### 3. Add defer

Make sure the script tag has the defer attribute so it loads after the page renders.

### 4. Publish

Custom code doesn't run in the Designer. Publish and check the live site.

## Common problems

**Works on one page only.** The script is in a page's own settings. Move it to Site settings footer code.

**Widget flashes or blocks the page.** Add defer to the script tag.

**Widget loads slowly or delays the page.** Make sure the script tag includes `defer` and is in the footer, not the head.

**It overlaps another floating button on mobile.** Cookie banners, WhatsApp buttons and back-to-top buttons often sit in the same corner. Move one of them in its settings.

## No-code route

If you'd rather not handle the model, hosting and widget yourself, a no-code AI agent builder like [FwdSlash](https://www.fwdslash.ai) trains an agent on your site and gives you the script above. The full walkthrough is in [How to integrate Claude into Webflow](https://www.fwdslash.ai/blog/how-to-integrate-claude-into-webflow) on the FwdSlash blog.

## Related

- [Human handoff patterns](../handoff/human-escalation.md)
- [Anatomy of a support agent prompt](../guides/prompt-anatomy.md)
