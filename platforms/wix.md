# Add an AI chat agent to Wix

How to put an AI support agent on a Wix site: where the script goes, what plan you need, and how to fix the usual problems.

## Before you start

Custom code on Wix needs a Premium plan with a connected domain. On a free Wix site the Custom Code panel isn't available, so plan for the upgrade before you build the agent.

You'll need the embed script from your chat tool. It usually looks like this:

```html
<script src="https://your-chat-provider.example/embed.js" data-agent-id="YOUR_AGENT_ID" defer></script>
```

If you're building the agent yourself on the Claude, OpenAI or Gemini API, **never paste an API key into Wix**. Anything in custom code is visible in the page source. Put the key behind a small backend instead; see the [Claude API proxy example](../examples/claude-proxy/).

For the prompt itself, start from one of the [industry prompts](../README.md#industry-prompts).

## Steps

### 1. Open Custom Code

In your site's dashboard, go to Settings, then Custom Code (under Advanced).

### 2. Add the script

Click Add Custom Code and paste your widget script.

### 3. Choose placement

Set it to load on all pages, load code once, and place it at the end of the body.

### 4. Publish

Apply, then publish the site. Custom code doesn't run in the editor preview.

## Common problems

**Nothing in the preview.** Expected. Custom code only runs on the published site.

**Widget covers the Wix chat or a mobile action bar.** Turn off Wix Chat if you're replacing it, and check the widget's position settings for mobile.

**Widget loads slowly or delays the page.** Make sure the script tag includes `defer` and is in the footer, not the head.

**It overlaps another floating button on mobile.** Cookie banners, WhatsApp buttons and back-to-top buttons often sit in the same corner. Move one of them in its settings.

## No-code route

If you'd rather not handle the model, hosting and widget yourself, a no-code AI agent builder like [FwdSlash](https://www.fwdslash.ai) trains an agent on your site and gives you the script above. The full walkthrough is in [How to add or embed Claude in any website](https://www.fwdslash.ai/blog/how-to-add-embed-claude-in-any-website) on the FwdSlash blog.

## Related

- [Human handoff patterns](../handoff/human-escalation.md)
- [Anatomy of a support agent prompt](../guides/prompt-anatomy.md)
