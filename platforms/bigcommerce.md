# Add an AI chat agent to BigCommerce

How to put an AI support agent on a BigCommerce site: where the script goes, what plan you need, and how to fix the usual problems.

## Before you start

Script Manager is available on all BigCommerce plans with a Stencil theme.

You'll need the embed script from your chat tool. It usually looks like this:

```html
<script src="https://your-chat-provider.example/embed.js" data-agent-id="YOUR_AGENT_ID" defer></script>
```

If you're building the agent yourself on the Claude, OpenAI or Gemini API, **never paste an API key into BigCommerce**. Anything in custom code is visible in the page source. Put the key behind a small backend instead; see the [Claude API proxy example](../examples/claude-proxy/).

For the prompt itself, start from one of the [industry prompts](../README.md#industry-prompts).

## Steps

### 1. Open Script Manager

Go to Storefront > Script Manager and click Create a Script.

### 2. Configure

Give it a name, set Location to Footer, Pages to All pages, and Script type to Script. Pick the consent category your cookie banner uses for functional scripts.

### 3. Paste and save

Paste your widget script into the contents box and save.

### 4. Check checkout pages

Decide whether you want the agent on checkout. Many stores exclude it there to keep checkout distraction-free.

## Common problems

**Widget hidden until cookie consent.** The script category is set to something visitors decline. Use the functional or essential category if your policy allows.

**Widget loads slowly or delays the page.** Make sure the script tag includes `defer` and is in the footer, not the head.

**It overlaps another floating button on mobile.** Cookie banners, WhatsApp buttons and back-to-top buttons often sit in the same corner. Move one of them in its settings.

## No-code route

If you'd rather not handle the model, hosting and widget yourself, a no-code AI agent builder like [FwdSlash](https://www.fwdslash.ai) trains an agent on your site and gives you the script above. The full walkthrough is in [How to integrate ChatGPT into BigCommerce](https://www.fwdslash.ai/blog/how-to-integrate-chatgpt-into-bigcommerce) on the FwdSlash blog.

## Related

- [Human handoff patterns](../handoff/human-escalation.md)
- [Anatomy of a support agent prompt](../guides/prompt-anatomy.md)
