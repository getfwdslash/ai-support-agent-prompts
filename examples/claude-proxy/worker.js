// Minimal Cloudflare Worker that proxies chat messages to the Claude API.
// The API key stays on the server. The browser only ever talks to this Worker.

const MAX_MESSAGES = 20;
const MAX_CHARS = 4000;

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    const allowed = (env.ALLOWED_ORIGINS || "").split(",").map((s) => s.trim()).filter(Boolean);
    const originOk = allowed.includes(origin);

    const cors = {
      "Access-Control-Allow-Origin": originOk ? origin : "null",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
      "Vary": "Origin",
    };
    const json = (obj, status = 200) =>
      new Response(JSON.stringify(obj), { status, headers: { ...cors, "Content-Type": "application/json" } });

    if (request.method === "OPTIONS") return new Response(null, { headers: cors });
    if (request.method !== "POST") return json({ error: "method_not_allowed" }, 405);
    if (!originOk) return json({ error: "origin_not_allowed" }, 403);

    let body;
    try {
      body = await request.json();
    } catch {
      return json({ error: "invalid_json" }, 400);
    }

    // Keep only well-formed, recent messages, and make sure the list starts with a user turn.
    let messages = (Array.isArray(body.messages) ? body.messages : [])
      .filter((m) => (m.role === "user" || m.role === "assistant") && typeof m.content === "string")
      .map((m) => ({ role: m.role, content: m.content.slice(0, MAX_CHARS) }))
      .slice(-MAX_MESSAGES);
    while (messages.length && messages[0].role !== "user") messages.shift();
    if (!messages.length) return json({ error: "no_messages" }, 400);

    const upstream = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "x-api-key": env.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
      },
      body: JSON.stringify({
        model: env.MODEL,
        max_tokens: 600,
        system: env.SYSTEM_PROMPT,
        messages,
      }),
    });

    if (!upstream.ok) {
      console.log("Claude API error", upstream.status, await upstream.text());
      return json({ error: "upstream_error" }, 502);
    }

    const data = await upstream.json();
    const reply = (data.content || [])
      .filter((block) => block.type === "text")
      .map((block) => block.text)
      .join("\n");

    return json({ reply });
  },
};
