# Contributing

Thanks for helping make support agents better. New industries, platforms and fixes are all welcome.

## Adding an industry prompt

Copy an existing file in `industries/` and keep the same sections, in the same order:

1. Intro and "Good for"
2. The system prompt (with `{{PLACEHOLDERS}}` for anything business-specific)
3. Why these guardrails
4. What to put in the knowledge base
5. Test it before you go live (at least four questions, including one the agent should refuse or hand over)
6. Related

Guardrails should describe specific behaviour ("Never ask for a PIN"), not values ("Be careful with security"). If a guardrail comes from a regulation, name the regulation.

## Adding a platform guide

Copy a file in `platforms/`. Include the plan requirement, the exact menu path, and at least one problem you've actually seen.

## Style

- Plain English, short sentences.
- No em dashes.
- Test your prompt on at least one model before opening a pull request, and say which one in the PR description.

## Rebuilding the site

The site in `docs/` is generated from the Markdown files. After editing, run:

```bash
pip install markdown
python scripts/build_site.py
```

Commit the updated `docs/` folder with your change.
