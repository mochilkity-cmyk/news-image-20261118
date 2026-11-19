# news-image-20261118 — build log

## Stories chosen (Wednesday 18 November 2026)

All verified from multiple independent reports (search, 19 Nov 2026).
Each story is a distinct 18 Nov development, not a carry-over of 17 Nov
news (the 17 Nov US strike on Qeshm Island appears only as the context
for the new 18 Nov Iranian strikes; the Kerch Bridge strike of 17 Nov
was left out and replaced by the overnight 18 Nov refinery strikes).

1. **Iran strikes Kuwait and Bahrain** (Middle East) — Iran hit US bases
   in Kuwait (Ali Al Salem) and Bahrain early on 18 Nov, after US jets
   struck a missile site on Qeshm Island on 17 Nov. Sources: Reuters
   (via KTWB, 18 Nov), Just Security Early Edition 18 Nov, AP (via
   OilPrice / The Labor Econ).
2. **Trump lands in Shenzhen for summit** (Asia-Pacific) — Xi greeted
   Trump at the airport and met Putin for over two hours; the first-ever
   Trump–Xi–Putin talks are set for Thursday, on the APEC sidelines.
   Sources: AP/NPR (via KENW, 18 Nov), FirstFeed News (18 Nov),
   Statement.com (18 Nov).
3. **Peltola wins Alaska Senate seat** (Americas) — Democrat Mary Peltola
   beat Dan Sullivan with 50.1% of the vote, giving Democrats a 56-44
   Senate majority; the last 2026 midterm race to be called. Sources:
   AP (via The Sen Times, 18 Nov), Open Chronicle global brief 18 Nov,
   Reuters (via NewsCentralTV, 18 Nov).
4. **Ukraine hits two Russian refineries** (Europe) — drones struck the
   Ilsky and Afipsky refineries overnight on 18 Nov; Reuters reported
   Russian refining output down about 45% since late October (industry
   sources' estimate, not official data). Sources: h.ua / Ukraine
   General Staff (18 Nov), Europa Journal News (18 Nov), Reuters via
   The Library Estate (18 Nov).
5. **Nvidia posts record $115.8bn quarter** (Technology) — revenue more
   than doubled year on year to $115.8bn in its first report since
   Jensen Huang resigned on 12 Nov; the board said it does not intend
   to reinstate him as CEO. Sources: Motley Fool earnings-call
   transcript (18 Nov), Wealth Professional / CNBC / Reuters (18 Nov),
   AJU Press (18 Nov).
6. **Ebola in DR Congo tops 11,000 cases** (Health) — WHO said cases
   have more than doubled in three months, with 400–500 new cases a
   week; on 18 Nov WHO kept the outbreak a public health emergency of
   international concern. Sources: UN News (via European Sting, 18 Nov),
   Reuters (via Zark News / NewsCentralTV, 18 Nov), CDC situation
   update published 18 Nov.

Left out for space (real, but lower priority): the Russian An-12 military
plane crash in Siberia (all 19 aboard killed), the Quad leaders' meeting
in Manila and Trump's claimed Philippines trade deal (Manila said nothing
was signed), Israel's Knesset electing Matan Kahana speaker, and the
Board of Peace report faulting Israel and Hamas over the Gaza ceasefire.

## How the image was made

`render.py` (in this repo) draws a 1024×1024 infographic with Python PIL
and DejaVu Sans: a navy header with the date in 52pt bold, six cards
(2 cols × 3 rows) each with a region kicker, a bold headline (≤2 lines)
and a 2–3 line detail, and a footer naming the sources. No starter image
was copied — the kit starter's entry.png is a placeholder globe and was
not used. The final image was viewed twice and checked: no overlaps, no
garbled text; three details were shortened during layout so they fit
three lines, and the Ebola detail was revised after viewing to restore
"more than doubled", which the first shortening had dropped.

## Validation

- `main.ts` run twice (MAKEFUN_OUTPUT_DIR=/tmp/ni18-a and /tmp/ni18-b):
  byte-identical outputs, both equal to entry.png — DETERMINISM PASS.
- Image: 1024×1024, 128,652 bytes — within the 1 MiB and 1024×1024 caps.
- Secret scan: no private key, API key or credential in any entry file.
- Kit check / bundling / submission: not done here — the parent handles
  repo creation, bundling and submission.

## Caveats

- The news picture comes from wire reporting (Reuters, AP, AFP) as
  carried by secondary outlets and roundups, plus UN/WHO and company
  sources; each story was corroborated across at least two independent
  results, but casualty and case figures are as reported on the day and
  may be revised (the 45% refining-output figure is an industry-source
  estimate cited by Reuters, not official Russian data).
- The Peltola result was called by AP late on 17 Nov US time and widely
  reported on 18 Nov; it is included as the day's settled US-politics
  news, with the count still unofficial pending certification.
- No local judge grade exists for this bounty — the server grades every
  entry, so no rank is promised.
