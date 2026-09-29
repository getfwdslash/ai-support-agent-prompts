"""Build the GitHub Pages site in /docs from the Markdown files in this repo.

Usage:
    pip install markdown
    python scripts/build_site.py

Change SITE_URL and REPO_URL below if the repo lives under a different
GitHub account or name.
"""
import html
import os
import re
import shutil
from datetime import date

import markdown

SITE_URL = "https://fwdslash-ai-agent-builder.github.io/ai-support-agent-prompts/"
REPO_URL = "https://github.com/fwdslash-ai-agent-builder/ai-support-agent-prompts"
SITE_NAME = "AI Support Agent Prompts"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")

SECTIONS = [
    ("Industries", "industries"),
    ("Platforms", "platforms"),
]
EXTRA_PAGES = [
    ("guides/prompt-anatomy.md", "Prompt anatomy"),
    ("handoff/human-escalation.md", "Human handoff"),
    ("examples/claude-proxy/README.md", "Claude API proxy"),
    ("CONTRIBUTING.md", "Contributing"),
]
GUIDE_DESCRIPTIONS = {
    "guides/prompt-anatomy.md": "The seven sections every prompt here uses, and what breaks without each one.",
    "handoff/human-escalation.md": "When an agent should pass a chat to a person, and how to word it.",
    "examples/claude-proxy/README.md": "Call Claude from a website without exposing your API key.",
    "CONTRIBUTING.md": "Add an industry, a platform or a fix.",
}


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def title_and_intro(md_text):
    title = re.search(r"^# (.+)$", md_text, re.M).group(1).strip()
    body = md_text.split("\n", 1)[1]
    for block in body.strip().split("\n\n"):
        block = block.strip()
        if block and not block.startswith(("#", "|", "```", "-", "**")):
            intro = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", block)
            return title, intro.replace("\n", " ")
    return title, ""


def out_path(md_path):
    """Map a repo Markdown path to its path inside /docs."""
    if md_path == "README.md":
        return "index.html"
    if md_path.endswith("README.md"):
        return md_path[: -len("README.md")] + "index.html"
    return md_path[:-3] + ".html"


def rewrite_links(html_text, md_path):
    def fix(m):
        href = m.group(1)
        if href.startswith(("http", "#", "mailto:")):
            return m.group(0)
        path, _, frag = href.partition("#")
        if path.endswith("README.md"):
            path = path[: -len("README.md")] + "index.html"
        elif path.endswith(".md"):
            path = path[:-3] + ".html"
        elif path in ("LICENSE", "../LICENSE"):
            return f'href="{REPO_URL}/blob/main/LICENSE"'
        return 'href="' + path + ("#" + frag if frag else "") + '"'

    return re.sub(r'href="([^"]+)"', fix, html_text)


def md_to_html(md_text, md_path, drop_title=True):
    if drop_title:
        md_text = re.sub(r"^# .+\n", "", md_text, count=1)
    out = markdown.markdown(md_text, extensions=["fenced_code", "tables", "toc"])
    return rewrite_links(out, md_path)


def rel_root(page_out):
    depth = page_out.count("/")
    return "../" * depth


def nav_html(page_out, entries):
    root = rel_root(page_out)
    parts = []
    for label, items in entries:
        links = []
        for item_out, slug, _t in items:
            cur = ' aria-current="page"' if item_out == page_out else ""
            links.append(f'<li><a href="{root}{item_out}"{cur}><span class="sl">/</span>{html.escape(slug)}</a></li>')
        parts.append(f'<p class="nav-group">{label}</p><ul>{"".join(links)}</ul>')
    return "".join(parts)


CSS = """
:root{--paper:#ffffff;--ink:#000000;--text:#2f3a4c;--muted:#5f6b80;--blue:#2150f5;--blue-deep:#1235b8;--wash:#eef2ff;--rule:#dbe1ec;--code:#f5f7fc}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--text);font:17px/1.65 "Schibsted Grotesk",system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:var(--blue);text-underline-offset:3px;text-decoration-thickness:1px}
a:hover{color:var(--blue-deep);text-decoration-thickness:2px}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:3px solid var(--blue);outline-offset:2px;border-radius:2px}
.shell{display:grid;grid-template-columns:250px minmax(0,1fr);max-width:1180px;margin:0 auto}
.side{position:sticky;top:0;align-self:start;height:100vh;overflow-y:auto;padding:32px 24px 40px;border-right:1px solid var(--rule)}
.brand{display:block;color:var(--ink);text-decoration:none;font-weight:800;font-size:18px;line-height:1.25;margin-bottom:28px}
.brand .sl{color:var(--blue);font-size:30px;line-height:0;margin-right:2px;vertical-align:-3px}
.nav-group{margin:22px 0 6px;font-size:13px;font-weight:700;color:var(--ink)}
.side ul{list-style:none;margin:0;padding:0}
.side li a{display:block;padding:3px 0;color:var(--muted);text-decoration:none;font-size:15px}
.side li a .sl{color:var(--rule);margin-right:1px;font-weight:700}
.side li a:hover{color:var(--ink)}
.side li a:hover .sl,.side li a[aria-current] .sl{color:var(--blue)}
.side li a[aria-current]{color:var(--ink);font-weight:700}
.mobile-nav{display:none}
main{padding:56px 56px 80px;min-width:0}
.content{max-width:72ch}
.path{font-weight:800;color:var(--ink);font-size:clamp(44px,7vw,76px);line-height:1;letter-spacing:-.03em;margin:0 0 14px;word-break:break-word}
.path .sl{color:var(--blue)}
h1{font-size:28px;line-height:1.2;color:var(--ink);font-weight:700;margin:0 0 18px;letter-spacing:-.01em}
h2{font-size:24px;line-height:1.25;color:var(--ink);font-weight:800;margin:52px 0 12px;letter-spacing:-.01em}
h3{font-size:18px;color:var(--ink);margin:30px 0 6px}
p,li{max-width:72ch}
strong{color:var(--ink)}
code{font-family:"JetBrains Mono",ui-monospace,Menlo,monospace;font-size:.86em;background:var(--code);padding:.1em .35em;border-radius:4px}
pre{position:relative;background:var(--wash);border:1px solid #d3dcfb;border-radius:10px;padding:52px 20px 20px;overflow-x:auto;margin:18px 0 24px}
pre code{background:none;padding:0;font-size:13.5px;line-height:1.6;color:#15213a;white-space:pre-wrap;word-break:break-word}
.copy{position:absolute;top:10px;right:10px;font:600 13px/1 "Schibsted Grotesk",system-ui,sans-serif;background:var(--paper);color:var(--blue);border:1px solid #c5d1fa;border-radius:6px;padding:7px 11px;cursor:pointer}
.copy:hover{background:var(--blue);color:#fff;border-color:var(--blue)}
.table-wrap{overflow-x:auto;margin:18px 0 24px}
table{border-collapse:collapse;width:100%;font-size:15px}
th,td{text-align:left;vertical-align:top;padding:10px 14px 10px 0;border-bottom:1px solid var(--rule)}
th{color:var(--ink);font-weight:700;border-bottom:2px solid var(--ink)}
hr{border:0;border-top:1px solid var(--rule);margin:40px 0}
.lede{font-size:20px;line-height:1.55;color:var(--text);max-width:60ch;margin:0 0 8px}
.hero{padding-bottom:34px;border-bottom:1px solid var(--rule);margin-bottom:10px}
.hero h1{font-size:clamp(34px,5vw,54px);line-height:1.06;letter-spacing:-.03em;font-weight:800;max-width:17ch;margin-bottom:20px}
.dir{list-style:none;padding:0;margin:8px 0 0;border-top:2px solid var(--ink)}
.dir li{max-width:none;border-bottom:1px solid var(--rule)}
.dir a{display:grid;grid-template-columns:minmax(150px,220px) 1fr;gap:4px 24px;padding:14px 0;text-decoration:none;color:var(--text)}
.dir .slug{font-weight:800;font-size:20px;color:var(--ink);letter-spacing:-.01em}
.dir .slug .sl{color:var(--blue)}
.dir .desc{font-size:15px;color:var(--muted);align-self:center}
.dir a:hover .slug{color:var(--blue)}
.dir a:hover .desc{color:var(--text)}
.meta{margin-top:56px;padding-top:20px;border-top:1px solid var(--rule);font-size:14px;color:var(--muted)}
.meta p{margin:4px 0}
@media (max-width:860px){
 .shell{display:block}
 .side{display:none}
 .mobile-nav{display:block;border-bottom:1px solid var(--rule);padding:14px 20px;position:sticky;top:0;background:var(--paper);z-index:5}
 .mobile-nav summary{cursor:pointer;font-weight:800;color:var(--ink);list-style:none}
 .mobile-nav summary .sl{color:var(--blue)}
 .mobile-nav ul{list-style:none;padding:0;margin:0}
 .mobile-nav li a{display:block;padding:5px 0;color:var(--text);text-decoration:none}
 .mobile-nav li a .sl{color:var(--blue)}
 .mobile-nav .nav-group{margin-top:16px}
 main{padding:32px 20px 64px}
 .dir a{grid-template-columns:1fr}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

JS = """
document.querySelectorAll('pre').forEach(function(pre){
  var b=document.createElement('button');b.className='copy';b.type='button';b.textContent='Copy';
  b.addEventListener('click',function(){
    var t=pre.querySelector('code').innerText;
    navigator.clipboard.writeText(t).then(function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy'},1600)});
  });
  pre.appendChild(b);
});
document.querySelectorAll('.content table').forEach(function(t){
  var w=document.createElement('div');w.className='table-wrap';t.parentNode.insertBefore(w,t);w.appendChild(t);
});
"""


def page(page_out, title, description, body, entries, source_md=None, is_home=False):
    root = rel_root(page_out)
    canonical = SITE_URL + ("" if page_out == "index.html" else page_out)
    full_title = SITE_NAME if is_home else f"{title} | {SITE_NAME}"
    nav = nav_html(page_out, entries)
    source = (
        f'<p><a href="{REPO_URL}/blob/main/{source_md}">View or edit this page on GitHub</a></p>' if source_md else ""
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(description[:300])}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(description[:300])}">
<meta property="og:url" content="{canonical}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Schibsted+Grotesk:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/site.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='%232150f5'/><path d='M20 6 12 26' stroke='white' stroke-width='4' stroke-linecap='round'/></svg>">
</head>
<body>
<details class="mobile-nav"><summary><span class="sl">/</span> Menu</summary><a class="brand" href="{root}index.html">{SITE_NAME}</a>{nav}</details>
<div class="shell">
<aside class="side"><a class="brand" href="{root}index.html"><span class="sl">/</span>{SITE_NAME}</a>{nav}</aside>
<main><div class="content">
{body}
<div class="meta">
{source}
<p>Open source under the MIT license. Maintained by <a href="https://www.fwdslash.ai">FwdSlash</a>, the no-code AI agent builder.</p>
</div>
</div></main>
</div>
<script src="{root}assets/site.js"></script>
</body>
</html>
"""


def collect():
    entries = []
    pages = []  # (md_path, out, slug, title, intro)
    for label, folder in SECTIONS:
        items = []
        for fn in sorted(os.listdir(os.path.join(ROOT, folder))):
            if not fn.endswith(".md"):
                continue
            md_path = f"{folder}/{fn}"
            t, intro = title_and_intro(read(md_path))
            slug = fn[:-3]
            o = out_path(md_path)
            items.append((o, slug, t))
            pages.append((md_path, o, slug, t, intro))
        entries.append((label, items))
    guide_items = []
    for md_path, short in EXTRA_PAGES:
        t, intro = title_and_intro(read(md_path))
        slug = short.lower().replace(" ", "-")
        o = out_path(md_path)
        guide_items.append((o, slug, t))
        pages.append((md_path, o, slug, t, intro))
    entries.append(("Guides", guide_items))
    return entries, pages


def short_desc(o, pages):
    """One-line description for the home page directory."""
    md_path = next(p[0] for p in pages if p[1] == o)
    text = read(md_path)
    if md_path.startswith("industries/"):
        # Use the "What the agent handles" column from the README table.
        m = re.search(r"\]\(" + re.escape(md_path) + r"\)", read("README.md"))
        row = read("README.md")[: m.start()].rsplit("\n", 1)[-1]
        return row.split("|")[2].strip() + "."
    if md_path.startswith("platforms/"):
        m = re.search(r"## Before you start\n\n(.+?)\n", text)
        return m.group(1).split(". ")[0].rstrip(".") + "."
    if md_path in GUIDE_DESCRIPTIONS:
        return GUIDE_DESCRIPTIONS[md_path]
    desc = next(p[4] for p in pages if p[1] == o)
    return desc.split(". ")[0].rstrip(".") + "."


def build_home(entries, pages):
    readme = read("README.md")
    intro = title_and_intro(readme)[1]
    keep = []
    for chunk in re.split(r"(?m)^## ", readme)[1:]:
        heading = chunk.split("\n", 1)[0].strip()
        if heading in ("How to use a prompt", "Principles behind these prompts"):
            keep.append("## " + chunk)
    extra_html = md_to_html("\n".join(keep), "README.md", drop_title=False)

    def directory(label, anchor):
        items = next(i for l, i in entries if l == label)
        rows = []
        for o, slug, t in items:
            short = short_desc(o, pages)
            rows.append(
                f'<li><a href="{o}"><span class="slug"><span class="sl">/</span>{html.escape(slug)}</span>'
                f'<span class="desc">{html.escape(short)}</span></a></li>'
            )
        return f'<h2 id="{anchor}">{label}</h2><ul class="dir">{"".join(rows)}</ul>'

    body = f"""
<section class="hero">
<h1>Support agent prompts you can paste, test and ship.</h1>
<p class="lede">{html.escape(intro)} Every prompt works with Claude, GPT, Gemini or any model that takes a system prompt, and each one comes with the guardrails and test questions for its industry.</p>
</section>
{directory("Industries", "industry-prompts")}
{directory("Platforms", "platform-guides")}
{directory("Guides", "guides")}
{extra_html}
"""
    return page("index.html", SITE_NAME, intro, body, entries, "README.md", is_home=True)


def build():
    if os.path.isdir(DOCS):
        shutil.rmtree(DOCS)
    os.makedirs(os.path.join(DOCS, "assets"))
    with open(os.path.join(DOCS, "assets", "site.css"), "w") as f:
        f.write(CSS.strip() + "\n")
    with open(os.path.join(DOCS, "assets", "site.js"), "w") as f:
        f.write(JS.strip() + "\n")
    open(os.path.join(DOCS, ".nojekyll"), "w").close()

    entries, pages = collect()
    with open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_home(entries, pages))

    for md_path, o, slug, t, intro in pages:
        md_text = read(md_path)
        body = f'<p class="path" aria-hidden="true"><span class="sl">/</span>{html.escape(slug)}</p><h1>{html.escape(t)}</h1>' + md_to_html(md_text, md_path)
        dest = os.path.join(DOCS, o)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(page(o, t, intro, body, entries, md_path))

    today = date.today().isoformat()
    urls = [SITE_URL] + [SITE_URL + o.replace("index.html", "") for _, o, *_ in pages]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>" for u in urls]
    sm.append("</urlset>")
    with open(os.path.join(DOCS, "sitemap.xml"), "w") as f:
        f.write("\n".join(sm) + "\n")
    print(f"Built {len(pages) + 1} pages into docs/")


if __name__ == "__main__":
    build()
