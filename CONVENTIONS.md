# LawCodex conventions

LawCodex publishes the legislation of every country as plain Markdown in git: one public
repository per jurisdiction.

## Repositories

- Name: ISO 3166-1 alpha-2 code, lowercase (`fr`, `de`, `jp`, `us`, `gb`...). Supranational: `eu`.
- Default branch: `master`.
- Each repository contains:
  - `README.md` — what is covered (counts per category), what is **not** covered and why,
    sources with URLs, structure, retrieval date, licence / copyright status of the source
    texts, and how to regenerate.
  - `scripts/` — the fetch and convert code (Python 3) with `requirements.txt`; re-runnable to
    refresh the corpus.
  - `.gitattributes` (`* text=auto eol=lf`) and `.gitignore`.
- No raw downloads, images or other binaries are committed — text only; images are linked to
  their official URL.

## What is collected

"Laws" means primary legislation, in its current consolidated (in-force) version where the
source offers it:

1. Constitution / basic laws.
2. Codes.
3. Acts / statutes passed by the legislature — all of those the source exposes.
4. Subordinate legislation (decrees, regulations) when the volume is reasonable; mass-volume
   secondary legislation may be skipped, and the README says so.

Sources are preferred in this order: official open-data dumps / APIs > official websites >
official PDFs > reputable non-official sources or Internet Archive copies of official pages
(always stated clearly, per file and in the README). Texts are kept in their official
language(s), one directory per language where there are several. Official translations may be
added and are marked as translations.

## File format

One Markdown file per law (very large codes may be split into one file per book/part). UTF-8,
LF line endings.

```markdown
---
title: "Code civil"
identifier: "LEGITEXT000006070721"   # official ID / number / ELI
type: code                            # constitution | code | act | decree | regulation | treaty ...
jurisdiction: fr
language: fr
date: 1804-03-21                      # enactment / promulgation date
last_amended: 2026-09-30              # or consolidation date
status: in_force                      # in_force | repealed | unknown
source: "https://www.legifrance.gouv.fr/codes/id/LEGITEXT000006070721"
retrieved: 2026-10-11
---

# Code civil

## Livre Ier — Des personnes
...
```

- The law's internal hierarchy (book/part/title/chapter/section/article) maps to heading levels;
  below `######`, article labels are **bold**.
- Text is reproduced faithfully: no summarising, translating or editorialising.
- Tables become Markdown tables when simple, HTML otherwise.
- File and directory names are stable lowercase ASCII slugs (official identifiers are used when
  titles are long or in non-Latin scripts; the native title stays in the front matter and H1).
- No directory holds more than 1,000 entries (GitHub's listing limit) — shard by year, letter or
  number range. No file exceeds 50 MB.

## Sourcing rules

- Identify honestly: a descriptive `LawCodex/1.0 (+https://github.com/LawCodex)` User-Agent (or
  an access token the publisher's API documentation requires), never a fake browser identity.
- Respect robots.txt and Crawl-delay, rate limits and terms of use. If a publisher's terms
  prohibit bulk or automated download, only what is permitted is published, and the README
  explains what consent would be needed.
- Never circumvent bot challenges, WAFs, logins or geo-blocks.
- Low concurrency (≤ 4), retries with backoff, local caching so re-runs don't re-download.
