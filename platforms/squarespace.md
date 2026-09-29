# Add an AI chat agent to Squarespace

How to put an AI support agent on a Squarespace site: where the script goes, what plan you need, and how to fix the usual problems.

## Before you start

Code Injection isn't available on Squarespace's entry-level plan. Check that your plan includes it before you start.

You'll need the embed script from your chat tool. It usually looks like this:

```html
<script src="https://your-chat-provider.example/embed.js" data-agent-id="YOUR_AGENT_ID" defer></script>
```

If you're building the agent yourself on the Claude, OpenAI or Gemini API, **never paste an API key into Squarespace**. Anything in custom code is visible in the page source. Put the key behind a small backend instead; see the [Claude API proxy example](../examples/claude-proxy/).

For the prompt itself, start from one of the [industry prompts](../README.md#industry-prompts).

## Steps

### 1. Open Code Injection

Go to Settings, then Developer Tools (Advanced on older dashboards), then Code Injection.

### 2. Paste in Footer

Paste the widget script into the Footer field.

### 3. Save and log out

Save, then view the site logged out or in a private window, since some scripts don't run for logged-in editors.

## Common problems

**Widget missing in the editor.** Code injection often doesn't render inside the editor. Check the live site.

**Widget loads slowly or delays the page.** Make sure the script tag includes `defer` and is in the footer, not the head.

**It overlaps another floating button on mobile.** Cookie banners, WhatsApp buttons and back-to-top buttons often sit in the same corner. Move one of them in its settings.

## No-code route

If you'd rather not handle the model, hosting and widget yourself, a no-code AI agent builder like [FwdSlash](https://www.fwdslash.ai) trains an agent on your site and gives you the script above. The full walkthrough is in [How to add or embed Claude in any website](https://www.fwdslash.ai/blog/how-to-add-embed-claude-in-any-website) on the FwdSlash blog.

## Related

- [Human handoff patterns](../handoff/human-escalation.md)
- [Anatomy of a support agent prompt](../guides/prompt-anatomy.md)
