# Add an AI chat agent to WordPress

How to put an AI support agent on a WordPress site: where the script goes, what plan you need, and how to fix the usual problems.

## Before you start

Self-hosted WordPress (WordPress.org) works on any host. On WordPress.com you need a plan that allows plugins or custom code, so check the current plan page before you start.

You'll need the embed script from your chat tool. It usually looks like this:

```html
<script src="https://your-chat-provider.example/embed.js" data-agent-id="YOUR_AGENT_ID" defer></script>
```

If you're building the agent yourself on the Claude, OpenAI or Gemini API, **never paste an API key into WordPress**. Anything in custom code is visible in the page source. Put the key behind a small backend instead; see the [Claude API proxy example](../examples/claude-proxy/).

For the prompt itself, start from one of the [industry prompts](../README.md#industry-prompts).

## Steps

### 1. Install a code snippets plugin

Plugins > Add New, search for a header and footer or code snippets plugin (WPCode is the most common), install and activate it. This is safer than editing theme files, because theme updates overwrite footer.php.

### 2. Add a footer snippet

Open the plugin, create a new snippet or go to its Header & Footer screen, and paste your widget script into the footer section.

### 3. Set it to run everywhere

Choose site-wide or all pages, then save and activate the snippet.

### 4. Clear your cache

If you use a caching plugin (WP Rocket, LiteSpeed, W3 Total Cache) or a CDN, purge the cache, then check the site in a private window.

## Common problems

**Widget doesn't appear.** Purge the cache first. Then check that a JavaScript optimisation setting (delay JS, combine JS) isn't holding the script back; exclude the widget's script URL from delay and combine.

**Theme editor route.** If you edit footer.php directly, do it in a child theme and paste the script just before the closing body tag. Otherwise the next theme update removes it.

**Widget loads slowly or delays the page.** Make sure the script tag includes `defer` and is in the footer, not the head.

**It overlaps another floating button on mobile.** Cookie banners, WhatsApp buttons and back-to-top buttons often sit in the same corner. Move one of them in its settings.

## No-code route

If you'd rather not handle the model, hosting and widget yourself, a no-code AI agent builder like [FwdSlash](https://www.fwdslash.ai) trains an agent on your site and gives you the script above. The full walkthrough is in [How to add or embed Claude in any website](https://www.fwdslash.ai/blog/how-to-add-embed-claude-in-any-website) on the FwdSlash blog.

## Related

- [Human handoff patterns](../handoff/human-escalation.md)
- [Anatomy of a support agent prompt](../guides/prompt-anatomy.md)
