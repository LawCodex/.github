#!/usr/bin/env python3
"""Generate profile/README.md from countries.tsv and status.tsv."""
import csv
import datetime
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

LABELS = {
    "full": "✅ Full",
    "partial": "🟡 Partial",
    "minimal": "🟠 Minimal",
    "progress": "🔄 In progress",
    "todo": "⬜ Not started",
}


def read_tsv(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return [row for row in csv.reader(f, delimiter="\t") if row]


def existing_repos():
    out = subprocess.run(
        ["gh", "repo", "list", "LawCodex", "--limit", "1000", "--json", "name,pushedAt"],
        check=True, capture_output=True, text=True).stdout
    return {r["name"]: r["pushedAt"][:10] for r in json.loads(out)}


def main():
    repos = existing_repos()
    names = {r[0]: r[1] for r in read_tsv("countries.tsv")}
    status = {}
    for row in read_tsv("status.tsv"):
        row += [""] * (4 - len(row))
        status.setdefault(row[0], row[:4])

    rows = []
    for code, name in names.items():
        st, summary, source = status.get(code, [code, "todo", "", ""])[1:]
        rows.append((name, code, st, summary, source))
    rows.sort(key=lambda r: (r[1] != "eu", r[0]))

    counts = {k: sum(1 for r in rows if r[2] == k) for k in LABELS}
    out = []
    w = out.append
    w("# LawCodex\n")
    w("The legislation of every country, as plain Markdown in git — one repository per "
      "jurisdiction, named by its ISO 3166-1 alpha-2 code (`fr`, `de`, `jp`…), plus "
      "[`eu`](https://github.com/LawCodex/eu) for the European Union.\n")
    w("Each repository holds the constitution, codes and laws in force (and often "
      "regulations) taken from official sources wherever possible, one file per law with "
      "YAML front matter (title, official identifier, dates, status, source URL), organised "
      "the way that country's own legal system is. Every README states exactly what is "
      "covered, what is missing and why, the source licence, and how to regenerate the "
      "corpus with the scripts in `scripts/`.\n")
    w("Texts are reproduced faithfully but are **not** an official publication. Always "
      "check the official source cited in each file before relying on a text.\n")
    w("## Coverage\n")
    w(" · ".join(f"{LABELS[k]}: **{counts[k]}**" for k in LABELS) + "\n")
    w("- **✅ Full** — the in-force primary legislation the official source exposes, "
      "usually consolidated.")
    w("- **🟡 Partial** — substantial corpus with known gaps (unofficial or archived "
      "source, texts as enacted rather than consolidated, missing categories).")
    w("- **🟠 Minimal** — constitution and/or core codes only, usually because the source's "
      "terms forbid bulk download or the site blocks access.")
    w("- **🔄 In progress** / **⬜ Not started**.\n")
    w(f"_Table generated {datetime.date.today().isoformat()}. \"Updated\" is the date of the "
      "repository's last push._\n")
    w("| Jurisdiction | Repo | Status | Contents | Main source | Updated |")
    w("|---|---|---|---|---|---|")
    for name, code, st, summary, source in rows:
        repo = f"[`{code}`](https://github.com/LawCodex/{code})" if code in repos else f"`{code}`"
        updated = repos.get(code, "")
        w(f"| {name} | {repo} | {LABELS[st]} | {summary} | {source} | {updated} |")
    w("")
    w("## Help wanted: access to sources\n")
    w("Some corpora are incomplete only because the publisher requires permission, an API "
      "key or network access we don't have. If you can help obtain any of these, please "
      "open an issue in the relevant repository:\n")
    for line in ACCESS:
        w(f"- {line}")
    w("")
    w("## Conventions\n")
    w("See [CONVENTIONS.md](https://github.com/LawCodex/.github/blob/master/CONVENTIONS.md) "
      "for the file format, directory layout and sourcing rules all repositories follow.\n")
    with open(os.path.join(ROOT, "profile", "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))


ACCESS = [
    "**New Zealand** — an API key for the Parliamentary Counsel Office legislation API "
    "(contact@pco.govt.nz); the website is behind a bot challenge.",
    "**Cyprus** — written consent from ΚΙΝΟΠ (CyLaw) for bulk download (info@cylaw.org).",
    "**India** — API access to India Code from the Legislative Department.",
    "**Chile** — bulk export or higher API quota for Ley Chile from the Biblioteca del "
    "Congreso Nacional.",
    "**Colombia** — written permission from the Ministry of Justice to republish "
    "SUIN-Juriscol texts.",
    "**Singapore** — allow-listing or a bulk export from the Attorney-General's Chambers "
    "(Singapore Statutes Online).",
    "**Africa (AfricanLII / Laws.Africa network)** — bulk access to consolidated "
    "legislation for South Africa, Kenya, Zambia, Zimbabwe, Namibia, Malawi, Uganda, "
    "Tanzania, Sierra Leone, Lesotho, Ghana and Seychelles (support@lawlibrary.org.za).",
    "**Bahrain** — permission from the Legislation & Legal Opinion Commission (LLOC); "
    "**Kuwait** — written consent from the National Assembly Secretariat.",
    "**Andorra** — permission to reuse the consolidated texts of portaljuridicandorra.ad; "
    "**Vatican City** — permission from the Governatorato to publish the texts.",
    "**Lebanon** — permission from the Lebanese University Legal Informatics Center; "
    "**Palestine** — permission from Al-Muqtafi (Birzeit University).",
    "**Saint Kitts and Nevis** — written permission from the Law Commission to reproduce "
    "the Revised Laws (lawcommission.gov.kn).",
    "**Bolivia** — a licence to republish law texts (Ley de Imprenta, art. 69) from the "
    "Gaceta Oficial.",
    "**Vanuatu** — permission from Parliament to republish Acts; **Pacific (PacLII)** — "
    "allow-listing for consolidated legislation of PNG, Solomon Islands, Vanuatu, Samoa, Kiribati.",
    "**Mali, Benin, Congo** — written permission from the official journal / government "
    "secretariat sites to reproduce legislation.",
    "**Moldova, Lithuania, Romania, Serbia, Mexico, Israel, Belarus, Saudi Arabia, UAE, Kazakhstan, Kyrgyzstan, Malawi, Peru, Venezuela, Panama, Guatemala, Dominican Republic** — official sites "
    "unreachable or bot-protected from our network; a crawl from another network or an "
    "allow-listed crawler would allow complete, current corpora.",
]

if __name__ == "__main__":
    main()
