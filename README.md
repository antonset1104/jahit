# Jahit Terukur | Vijeron

An original, bilingual sewing-measurement and fabric-planning site for `jahit.vijeron.com`.

## Contents

- Eight original guides in Indonesian and English, each with a worked example, a pitfall and relevant source links.
- Two browser-only calculators: a repeated rectangular-panel fabric planner and a rectangular edging-tape estimator.
- Users supply usable width, cut dimensions and their own extra length. The tools do not rotate patterns, match prints, assume a universal waste rate or claim fabric stock.
- Static HTML with per-page canonicals, ID/EN `hreflang`, Article or WebPage JSON-LD, sitemap, robots.txt and ads.txt.
- GA4 `G-79X7K7H4MJ` and AdSense `ca-pub-6180580801533680` on content pages. Consent defaults denied and Funding Choices is present. Ad serving depends on account approval and applicable consent.

## Build and check

Requires Python 3.10+ and no third-party packages:

```powershell
python build.py
python check.py
node --check assets/calculator.js
```

Commit generated `dist/` with the source. In Cloudflare Pages, connect `main`, leave the build command blank and set output directory to `dist`. Attach `jahit.vijeron.com` through the Pages custom-domain workflow.

## Editorial boundaries

`content.py` contains original copy. Sources verify concepts; source prose, illustrations and projects are not republished. The fabric-art diagram and icon are original code-native graphics. Update the publication date only after material editorial changes. Inputs and results stay in the browser; GA4 tool events include only tool name and page language. This is a planning aid, not a garment pattern, product test, fabric recommendation, or sewing certification.
