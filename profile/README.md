# LawCodex

The legislation of every country, as plain Markdown in git — one repository per jurisdiction, named by its ISO 3166-1 alpha-2 code (`fr`, `de`, `jp`…), plus [`eu`](https://github.com/LawCodex/eu) for the European Union.

Each repository holds the constitution, codes and laws in force (and often regulations) taken from official sources wherever possible, one file per law with YAML front matter (title, official identifier, dates, status, source URL), organised the way that country's own legal system is. Every README states exactly what is covered, what is missing and why, the source licence, and how to regenerate the corpus with the scripts in `scripts/`.

Texts are reproduced faithfully but are **not** an official publication. Always check the official source cited in each file before relying on a text.

## Coverage

✅ Full: **37** · 🟡 Partial: **25** · 🟠 Minimal: **7** · 🔄 In progress: **42** · ⬜ Not started: **87**

- **✅ Full** — the in-force primary legislation the official source exposes, usually consolidated.
- **🟡 Partial** — substantial corpus with known gaps (unofficial or archived source, texts as enacted rather than consolidated, missing categories).
- **🟠 Minimal** — constitution and/or core codes only, usually because the source's terms forbid bulk download or the site blocks access.
- **🔄 In progress** / **⬜ Not started**.

| Jurisdiction | Repo | Status | Contents | Main source |
|---|---|---|---|---|
| European Union | [`eu`](https://github.com/LawCodex/eu) | ✅ Full | 34,323 acts in force (treaties, regulations, directives, decisions), English, consolidated where available | EUR-Lex / Cellar |
| Afghanistan | [`af`](https://github.com/LawCodex/af) | 🟠 Minimal | 2004 Constitution + 2 laws (English), archived | Former official sites (archived) |
| Albania | [`al`](https://github.com/LawCodex/al) | ✅ Full | 2,668 laws in force (314 consolidated) | qbz.gov.al |
| Algeria | `dz` | 🔄 In progress |  |  |
| Andorra | `ad` | 🔄 In progress |  |  |
| Angola | `ao` | ⬜ Not started |  |  |
| Antigua and Barbuda | `ag` | ⬜ Not started |  |  |
| Argentina | [`ar`](https://github.com/LawCodex/ar) | 🟡 Partial | 11,052 national texts; many only as originally enacted | InfoLEG, SAIJ |
| Armenia | [`am`](https://github.com/LawCodex/am) | ✅ Full | 1,001 laws (Armenian) + 216 English translations, consolidated | ARLIS |
| Australia | [`au`](https://github.com/LawCodex/au) | ✅ Full | 29,287 texts: Constitution, Acts, legislative instruments (Commonwealth), consolidated | Federal Register of Legislation |
| Austria | [`at`](https://github.com/LawCodex/at) | ✅ Full | 19,099 texts: all federal and all nine Länder law in force, consolidated | RIS (OGD API) |
| Azerbaijan | [`az`](https://github.com/LawCodex/az) | ✅ Full | 2,640 laws in force (Constitution, codes, laws) | e-qanun |
| Bahamas | `bs` | ⬜ Not started |  |  |
| Bahrain | `bh` | 🔄 In progress |  |  |
| Bangladesh | [`bd`](https://github.com/LawCodex/bd) | 🟡 Partial | Constitution + 1,346 laws (English/Bangla) | bdlaws.minlaw.gov.bd |
| Barbados | `bb` | ⬜ Not started |  |  |
| Belarus | [`by`](https://github.com/LawCodex/by) | 🟡 Partial | Constitution, 25 codes, 125 laws | etalonline.by |
| Belgium | [`be`](https://github.com/LawCodex/be) | 🔄 In progress | Consolidated federal and regional legislation, French and Dutch | Justel |
| Belize | `bz` | ⬜ Not started |  |  |
| Benin | `bj` | ⬜ Not started |  |  |
| Bhutan | [`bt`](https://github.com/LawCodex/bt) | 🟡 Partial | Constitution + 165 Acts in English (archived copies) | National Assembly / OAG (archived) |
| Bolivia | `bo` | ⬜ Not started |  |  |
| Bosnia and Herzegovina | [`ba`](https://github.com/LawCodex/ba) | 🟡 Partial | State-level Constitution + ~230 laws in bs/hr/sr | parlament.ba |
| Botswana | `bw` | ⬜ Not started |  |  |
| Brazil | [`br`](https://github.com/LawCodex/br) | 🟡 Partial | 19,150 federal acts (compiled texts); some older laws not published by Planalto | Planalto |
| Brunei | [`bn`](https://github.com/LawCodex/bn) | 🔄 In progress |  |  |
| Bulgaria | [`bg`](https://github.com/LawCodex/bg) | 🟡 Partial | 2,559 consolidated texts (unofficial); no ordinances | legislation.apis.bg |
| Burkina Faso | `bf` | ⬜ Not started |  |  |
| Burundi | `bi` | ⬜ Not started |  |  |
| Cabo Verde | `cv` | ⬜ Not started |  |  |
| Cambodia | `kh` | 🔄 In progress |  |  |
| Cameroon | `cm` | ⬜ Not started |  |  |
| Canada | [`ca`](https://github.com/LawCodex/ca) | ✅ Full | 11,732 files: Constitution, Acts and regulations in English and French, consolidated | Justice Laws (XML) |
| Central African Republic | `cf` | ⬜ Not started |  |  |
| Chad | `td` | ⬜ Not started |  |  |
| Chile | [`cl`](https://github.com/LawCodex/cl) | 🟠 Minimal | Constitution and 15 codes only (bulk download prohibited by terms) | Ley Chile (BCN) |
| China | [`cn`](https://github.com/LawCodex/cn) | 🟡 Partial | Constitution, 286/302 laws, 606 administrative regulations, 199 judicial interpretations | NPC, MOFCOM, State Council |
| Colombia | [`co`](https://github.com/LawCodex/co) | 🟠 Minimal | Constitution, 28 codes, index of all laws (republication requires permission) | SUIN-Juriscol |
| Comoros | `km` | ⬜ Not started |  |  |
| Congo | `cg` | ⬜ Not started |  |  |
| Congo (Democratic Republic) | `cd` | ⬜ Not started |  |  |
| Costa Rica | `cr` | ⬜ Not started |  |  |
| Croatia | [`hr`](https://github.com/LawCodex/hr) | 🟡 Partial | Constitution, 977 laws, 1,108 decrees; mostly original text + amendments; in-force status inferred | Narodne novine |
| Cuba | `cu` | ⬜ Not started |  |  |
| Cyprus | [`cy`](https://github.com/LawCodex/cy) | 🟠 Minimal | Constitution only (bulk download requires CyLaw consent) | CyLaw |
| Czechia | [`cz`](https://github.com/LawCodex/cz) | ✅ Full | 8,935 acts in force, consolidated | e-Sbírka |
| Côte d'Ivoire | `ci` | ⬜ Not started |  |  |
| Denmark | [`dk`](https://github.com/LawCodex/dk) | ✅ Full | 11,134 documents in force | Retsinformation |
| Djibouti | `dj` | ⬜ Not started |  |  |
| Dominica | `dm` | ⬜ Not started |  |  |
| Dominican Republic | `do` | ⬜ Not started |  |  |
| Ecuador | `ec` | ⬜ Not started |  |  |
| Egypt | `eg` | 🔄 In progress |  |  |
| El Salvador | `sv` | ⬜ Not started |  |  |
| Equatorial Guinea | `gq` | ⬜ Not started |  |  |
| Eritrea | `er` | ⬜ Not started |  |  |
| Estonia | [`ee`](https://github.com/LawCodex/ee) | ✅ Full | 4,753 acts in force (Estonian) + 404 English translations, consolidated | Riigi Teataja |
| Eswatini | `sz` | ⬜ Not started |  |  |
| Ethiopia | `et` | ⬜ Not started |  |  |
| Fiji | `fj` | ⬜ Not started |  |  |
| Finland | [`fi`](https://github.com/LawCodex/fi) | ✅ Full | 10,541 consolidated statutes in Finnish and Swedish (only part of the statute book is consolidated) | Finlex open data |
| France | [`fr`](https://github.com/LawCodex/fr) | ✅ Full | 48,889 texts in force: Constitution, 76 codes, lois, ordonnances, décrets (no arrêtés) | DILA LEGI |
| Gabon | `ga` | ⬜ Not started |  |  |
| Gambia | `gm` | ⬜ Not started |  |  |
| Georgia | [`ge`](https://github.com/LawCodex/ge) | ✅ Full | 507 acts in force (Georgian) + 299 English translations; no secondary legislation | Matsne |
| Germany | [`de`](https://github.com/LawCodex/de) | ✅ Full | 6,139 federal laws and ordinances in force, consolidated | gesetze-im-internet.de |
| Ghana | `gh` | ⬜ Not started |  |  |
| Greece | [`gr`](https://github.com/LawCodex/gr) | 🔄 In progress | Constitution, codes and laws |  |
| Grenada | `gd` | ⬜ Not started |  |  |
| Guatemala | `gt` | ⬜ Not started |  |  |
| Guinea | `gn` | ⬜ Not started |  |  |
| Guinea-Bissau | `gw` | ⬜ Not started |  |  |
| Guyana | `gy` | ⬜ Not started |  |  |
| Haiti | `ht` | ⬜ Not started |  |  |
| Honduras | `hn` | ⬜ Not started |  |  |
| Hungary | [`hu`](https://github.com/LawCodex/hu) | ✅ Full | 8,215 laws in force, consolidated | Nemzeti Jogszabálytár |
| Iceland | [`is`](https://github.com/LawCodex/is) | 🟡 Partial | Constitution and all 916 laws; 2,916 of 6,949 regulations | Althingi, island.is |
| India | [`in`](https://github.com/LawCodex/in) | 🟠 Minimal | Constitution + 3 criminal codes (India Code prohibits bulk download) | legislative.gov.in |
| Indonesia | [`id`](https://github.com/LawCodex/id) | 🔄 In progress | UUD 1945, UU, Perppu, PP | JDIH BPK |
| Iran | `ir` | 🔄 In progress |  |  |
| Iraq | `iq` | 🔄 In progress |  |  |
| Ireland | [`ie`](https://github.com/LawCodex/ie) | ✅ Full | 5,450 files: Constitution, Acts (577 revised, rest as enacted), pre-1922 statutes | Law Reform Commission, Irish Statute Book |
| Israel | [`il`](https://github.com/LawCodex/il) | 🟡 Partial | 6,169 texts, unofficial consolidations; official Knesset sources geo-blocked | Hebrew Wikisource (Open Law Book) |
| Italy | [`it`](https://github.com/LawCodex/it) | ✅ Full | 76,894 acts in force (vigente), incl. all DPRs and royal decrees | Normattiva open data |
| Jamaica | `jm` | ⬜ Not started |  |  |
| Japan | [`jp`](https://github.com/LawCodex/jp) | ✅ Full | 9,017 laws in force (法律, 政令, 府省令, 規則) | e-Gov 法令検索 |
| Jordan | `jo` | 🔄 In progress |  |  |
| Kazakhstan | [`kz`](https://github.com/LawCodex/kz) | 🔄 In progress |  |  |
| Kenya | `ke` | ⬜ Not started |  |  |
| Kiribati | `ki` | ⬜ Not started |  |  |
| Korea (North) | `kp` | ⬜ Not started |  |  |
| Korea (South) | [`kr`](https://github.com/LawCodex/kr) | ✅ Full | 5,628 current laws, decrees and ordinances | law.go.kr Open API |
| Kosovo | [`xk`](https://github.com/LawCodex/xk) | ✅ Full | ~615 laws in Albanian, Serbian and English | Official Gazette |
| Kuwait | `kw` | 🔄 In progress |  |  |
| Kyrgyzstan | [`kg`](https://github.com/LawCodex/kg) | 🔄 In progress |  |  |
| Laos | `la` | 🔄 In progress |  |  |
| Latvia | [`lv`](https://github.com/LawCodex/lv) | ✅ Full | 6,410 consolidated laws and Cabinet regulations + 1,680 English translations | Likumi.lv |
| Lebanon | `lb` | 🔄 In progress |  |  |
| Lesotho | `ls` | ⬜ Not started |  |  |
| Liberia | `lr` | ⬜ Not started |  |  |
| Libya | `ly` | 🔄 In progress |  |  |
| Liechtenstein | `li` | 🔄 In progress |  |  |
| Lithuania | [`lt`](https://github.com/LawCodex/lt) | 🟡 Partial | 12,229 files, mostly from unofficial mirrors (~March 2026); official sources blocked | e-seimas, open-data mirrors |
| Luxembourg | [`lu`](https://github.com/LawCodex/lu) | ✅ Full | 16,781 texts in force (6% consolidated, rest as published) | Legilux |
| Madagascar | `mg` | ⬜ Not started |  |  |
| Malawi | `mw` | ⬜ Not started |  |  |
| Malaysia | [`my`](https://github.com/LawCodex/my) | 🔄 In progress |  |  |
| Maldives | [`mv`](https://github.com/LawCodex/mv) | 🟡 Partial | Constitution + 241 laws and regulations in Dhivehi | MVLaw (AGO) |
| Mali | `ml` | ⬜ Not started |  |  |
| Malta | [`mt`](https://github.com/LawCodex/mt) | 🟡 Partial | 5,076 laws in English and Maltese, converted from PDF | legislation.mt |
| Marshall Islands | `mh` | ⬜ Not started |  |  |
| Mauritania | `mr` | 🔄 In progress |  |  |
| Mauritius | `mu` | ⬜ Not started |  |  |
| Mexico | [`mx`](https://github.com/LawCodex/mx) | 🟡 Partial | 454 federal texts; site unreachable, Internet Archive copies, some outdated | Cámara de Diputados (archived) |
| Micronesia | `fm` | ⬜ Not started |  |  |
| Moldova | [`md`](https://github.com/LawCodex/md) | 🟠 Minimal | Constitution only (official sites behind bot protection) | presedinte.md |
| Monaco | `mc` | 🔄 In progress |  |  |
| Mongolia | [`mn`](https://github.com/LawCodex/mn) | 🔄 In progress |  |  |
| Montenegro | [`me`](https://github.com/LawCodex/me) | 🟡 Partial | Constitution + 297 laws (unofficial texts) + register index | sluzbenilist.me, gov.me |
| Morocco | `ma` | 🔄 In progress |  |  |
| Mozambique | `mz` | ⬜ Not started |  |  |
| Myanmar | `mm` | 🔄 In progress |  |  |
| Namibia | `na` | ⬜ Not started |  |  |
| Nauru | `nr` | ⬜ Not started |  |  |
| Nepal | [`np`](https://github.com/LawCodex/np) | 🟡 Partial | Constitution + 361 Acts, English translations from archived copies | Nepal Law Commission (archived) |
| Netherlands | [`nl`](https://github.com/LawCodex/nl) | ✅ Full | 12,955 regelingen in force | wetten.overheid.nl (BWB) |
| New Zealand | [`nz`](https://github.com/LawCodex/nz) | 🟡 Partial | 3,201 Acts from Internet Archive copies; official API needs a key | legislation.govt.nz (archived) |
| Nicaragua | `ni` | ⬜ Not started |  |  |
| Niger | `ne` | ⬜ Not started |  |  |
| Nigeria | `ng` | ⬜ Not started |  |  |
| North Macedonia | [`mk`](https://github.com/LawCodex/mk) | 🟡 Partial | 4,776 files: base laws and amending laws separately | LDBIS |
| Norway | [`no`](https://github.com/LawCodex/no) | ✅ Full | 5,881 laws and central regulations in force | Lovdata public data |
| Oman | `om` | 🔄 In progress |  |  |
| Pakistan | [`pk`](https://github.com/LawCodex/pk) | 🟡 Partial | Constitution + 981 federal laws; Urdu and scans missing | Pakistan Code |
| Palau | `pw` | ⬜ Not started |  |  |
| Palestine | `ps` | 🔄 In progress |  |  |
| Panama | `pa` | ⬜ Not started |  |  |
| Papua New Guinea | `pg` | ⬜ Not started |  |  |
| Paraguay | `py` | ⬜ Not started |  |  |
| Peru | `pe` | ⬜ Not started |  |  |
| Philippines | [`ph`](https://github.com/LawCodex/ph) | ✅ Full | 25,250 texts as enacted (RAs, PDs, EOs, Acts, codes) | LawPhil (CC BY-NC) |
| Poland | [`pl`](https://github.com/LawCodex/pl) | ✅ Full | 21,273 acts in force (2,640 consolidated, 3,611 unverified OCR) | Sejm ELI API |
| Portugal | [`pt`](https://github.com/LawCodex/pt) | ✅ Full | 4,840 consolidated diplomas in force | Diário da República Eletrónico |
| Qatar | `qa` | 🔄 In progress |  |  |
| Romania | [`ro`](https://github.com/LawCodex/ro) | 🟡 Partial | 18,057 acts as published (not consolidated), in-force status unknown | legislatie.just.ro web service |
| Russia | [`ru`](https://github.com/LawCodex/ru) | ✅ Full | 11,770 federal acts in force incl. all 25 codes, consolidated | pravo.gov.ru |
| Rwanda | `rw` | ⬜ Not started |  |  |
| Saint Kitts and Nevis | `kn` | ⬜ Not started |  |  |
| Saint Lucia | `lc` | ⬜ Not started |  |  |
| Saint Vincent and the Grenadines | `vc` | ⬜ Not started |  |  |
| Samoa | `ws` | ⬜ Not started |  |  |
| San Marino | `sm` | 🔄 In progress |  |  |
| Sao Tome and Principe | `st` | ⬜ Not started |  |  |
| Saudi Arabia | [`sa`](https://github.com/LawCodex/sa) | 🔄 In progress |  |  |
| Senegal | `sn` | ⬜ Not started |  |  |
| Serbia | [`rs`](https://github.com/LawCodex/rs) | 🟡 Partial | 1,039 consolidated acts from Internet Archive copies (~425 laws) | pravno-informacioni-sistem.rs (archived) |
| Seychelles | `sc` | ⬜ Not started |  |  |
| Sierra Leone | `sl` | ⬜ Not started |  |  |
| Singapore | [`sg`](https://github.com/LawCodex/sg) | 🟠 Minimal | 57 texts (official site blocks access) | SSO via ELD, WIPO Lex |
| Slovakia | [`sk`](https://github.com/LawCodex/sk) | ✅ Full | 9,699 acts in force, consolidated | Slov-Lex |
| Slovenia | [`si`](https://github.com/LawCodex/si) | ✅ Full | 7,145 acts in force (1,861 consolidated) | PIS |
| Solomon Islands | `sb` | ⬜ Not started |  |  |
| Somalia | `so` | ⬜ Not started |  |  |
| South Africa | [`za`](https://github.com/LawCodex/za) | 🟡 Partial | Constitution + 2,804 Acts as enacted, 64% OCR; consolidated sources prohibit bulk download | gov.za |
| South Sudan | `ss` | ⬜ Not started |  |  |
| Spain | [`es`](https://github.com/LawCodex/es) | ✅ Full | 10,003 consolidated state and regional norms in force | BOE |
| Sri Lanka | [`lk`](https://github.com/LawCodex/lk) | 🟡 Partial | Constitution + 816 Acts as passed (1999+) | parliament.lk |
| Sudan | `sd` | 🔄 In progress |  |  |
| Suriname | `sr` | ⬜ Not started |  |  |
| Sweden | [`se`](https://github.com/LawCodex/se) | ✅ Full | 5,338 consolidated SFS texts in force | Riksdagen open data |
| Switzerland | [`ch`](https://github.com/LawCodex/ch) | ✅ Full | 5,072 texts in force in DE/FR/IT (+RM), internal and international law, consolidated | Fedlex |
| Syria | `sy` | 🔄 In progress |  |  |
| Taiwan | [`tw`](https://github.com/LawCodex/tw) | ✅ Full | 8,279 texts in force (Chinese) + 2,888 English translations | 全國法規資料庫 open data |
| Tajikistan | [`tj`](https://github.com/LawCodex/tj) | 🔄 In progress |  |  |
| Tanzania | `tz` | ⬜ Not started |  |  |
| Thailand | [`th`](https://github.com/LawCodex/th) | 🔄 In progress |  |  |
| Timor-Leste | `tl` | 🔄 In progress |  |  |
| Togo | `tg` | ⬜ Not started |  |  |
| Tonga | `to` | ⬜ Not started |  |  |
| Trinidad and Tobago | `tt` | ⬜ Not started |  |  |
| Tunisia | `tn` | 🔄 In progress |  |  |
| Turkmenistan | [`tm`](https://github.com/LawCodex/tm) | 🔄 In progress |  |  |
| Tuvalu | `tv` | ⬜ Not started |  |  |
| Türkiye | [`tr`](https://github.com/LawCodex/tr) | ✅ Full | 14,607 consolidated texts incl. regulations and tebliğler | Mevzuat Bilgi Sistemi |
| Uganda | `ug` | ⬜ Not started |  |  |
| Ukraine | [`ua`](https://github.com/LawCodex/ua) | 🔄 In progress | Constitution, 23 codes, laws (fetch ongoing under API rate limits) | data.rada.gov.ua |
| United Arab Emirates | `ae` | 🔄 In progress |  |  |
| United Kingdom | [`gb`](https://github.com/LawCodex/gb) | ✅ Full | 6,720 Acts (UK, Scotland, Wales, NI, pre-Union), revised; no statutory instruments; pre-1980s scans missing | legislation.gov.uk |
| United States | [`us`](https://github.com/LawCodex/us) | ✅ Full | US Code (all titles), Constitution, eCFR | OLRC (via Internet Archive), GovInfo |
| Uruguay | `uy` | ⬜ Not started |  |  |
| Uzbekistan | [`uz`](https://github.com/LawCodex/uz) | 🔄 In progress |  |  |
| Vanuatu | `vu` | ⬜ Not started |  |  |
| Vatican City | `va` | 🔄 In progress |  |  |
| Venezuela | `ve` | ⬜ Not started |  |  |
| Viet Nam | [`vn`](https://github.com/LawCodex/vn) | 🟡 Partial | 2,487 documents in force; 1,043 more without obtainable text | vbpl.vn, Công báo |
| Yemen | `ye` | 🔄 In progress |  |  |
| Zambia | `zm` | ⬜ Not started |  |  |
| Zimbabwe | `zw` | ⬜ Not started |  |  |

## Help wanted: access to sources

Some corpora are incomplete only because the publisher requires permission, an API key or network access we don't have. If you can help obtain any of these, please open an issue in the relevant repository:

- **New Zealand** — an API key for the Parliamentary Counsel Office legislation API (contact@pco.govt.nz); the website is behind a bot challenge.
- **Cyprus** — written consent from ΚΙΝΟΠ (CyLaw) for bulk download (info@cylaw.org).
- **India** — API access to India Code from the Legislative Department.
- **Chile** — bulk export or higher API quota for Ley Chile from the Biblioteca del Congreso Nacional.
- **Colombia** — written permission from the Ministry of Justice to republish SUIN-Juriscol texts.
- **Singapore** — allow-listing or a bulk export from the Attorney-General's Chambers (Singapore Statutes Online).
- **Africa (AfricanLII / Laws.Africa network)** — bulk access to consolidated legislation for South Africa, Kenya, Zambia, Zimbabwe, Namibia, Malawi, Uganda, Tanzania, Sierra Leone, Lesotho, Ghana and Seychelles (support@lawlibrary.org.za).
- **Moldova, Lithuania, Romania, Serbia, Mexico, Israel, Belarus** — official sites unreachable or bot-protected from our network; a crawl from another network or an allow-listed crawler would allow complete, current corpora.

## Conventions

See [CONVENTIONS.md](https://github.com/LawCodex/.github/blob/master/CONVENTIONS.md) for the file format, directory layout and sourcing rules all repositories follow.
