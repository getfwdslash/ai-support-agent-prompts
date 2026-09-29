# Add an AI chat agent to Shopify

How to put an AI support agent on a Shopify site: where the script goes, what plan you need, and how to fix the usual problems.

## Before you start

Works on every Shopify plan. If your chat tool has a Shopify app, installing the app (a theme app embed) is often easier than editing code.

You'll need the embed script from your chat tool. It usually looks like this:

```html
<script src="https://your-chat-provider.example/embed.js" data-agent-id="YOUR_AGENT_ID" defer></script>
```

If you're building the agent yourself on the Claude, OpenAI or Gemini API, **never paste an API key into Shopify**. Anything in custom code is visible in the page source. Put the key behind a small backend instead; see the [Claude API proxy example](../examples/claude-proxy/).

For the prompt itself, start from one of the [industry prompts](../README.md#industry-prompts).

## Steps

### 1. Duplicate your theme

Online Store > Themes, then Actions > Duplicate on your live theme. This gives you a backup.

### 2. Open the code editor

On the live theme, choose Edit code and open layout/theme.liquid.

### 3. Paste before the closing body tag

Find the closing body tag near the end of the file and paste your widget script directly above it.

### 4. Save and check

Save, then open your store in a private window and check a product page, the cart and checkout-adjacent pages.

## Common problems

**Two chat bubbles.** You installed the tool's Shopify app and also pasted the script. Remove one.

**Theme update removed the widget.** Switching or updating to a new theme version replaces theme.liquid. Re-add the script, or use the app embed, which survives theme changes.

**Widget loads slowly or delays the page.** Make sure the script tag includes `defer` and is in the footer, not the head.

**It overlaps another floating button on mobile.** Cookie banners, WhatsApp buttons and back-to-top buttons often sit in the same corner. Move one of them in its settings.

## No-code route

If you'd rather not handle the model, hosting and widget yourself, a no-code AI agent builder like [FwdSlash](https://www.fwdslash.ai) trains an agent on your site and gives you the script above. The full walkthrough is in [How to add or embed Claude in any website](https://www.fwdslash.ai/blog/how-to-add-embed-claude-in-any-website) on the FwdSlash blog.

## Related

- [Human handoff patterns](../handoff/human-escalation.md)
- [Anatomy of a support agent prompt](../guides/prompt-anatomy.md)
