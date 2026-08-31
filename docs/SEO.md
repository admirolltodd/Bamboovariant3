# SEO Recommendations — Variant 3

This variant's HTML was **not modified** by this infrastructure pass, per
the project's non-destructive rules. Everything below is a recommendation
for a future, deliberate content change — not something already applied.

## Current state (as of this audit) — this variant is ahead of the others

- `index.html` has a unique `<title>`, a `<meta name="description">`, and
  an explicit `<meta name="robots" content="index,follow,max-image-preview:large">`.
- **JSON-LD `Restaurant` structured data is already present** in `<head>`
  for all three locations (name, cuisine, telephone, full postal address),
  and it validated as well-formed JSON during this audit. Left untouched,
  as instructed — it is not malformed.
- No `<link rel="canonical">`.
- No Open Graph (`og:*`) or Twitter Card (`twitter:*`) meta tags.
- `robots.txt` and `sitemap.xml` were added by this pass and are crawlable
  (new standalone infrastructure files, not existing page edits). Because
  this variant is a single page, the sitemap lists only `/`.

## Recommended (not applied) canonical tag

Add `<link rel="canonical" href="https://REPLACE-WITH-PRODUCTION-DOMAIN/">`
to `index.html` once a production domain is confirmed. Don't guess the
domain in the meantime.

## Recommended (not applied) Open Graph / Twitter Card tags

Using only facts already present in this repository:

```html
<meta property="og:type" content="restaurant">
<meta property="og:title" content="Bamboo Sushi Bar & Hibachi Express | Emerald Coast, FL">
<meta property="og:description" content="Family-owned sushi and hibachi on Florida's Emerald Coast since 2007. Browse Bamboo favorites and order direct from Crestview, Fort Walton Beach or Niceville.">
<meta property="og:url" content="https://REPLACE-WITH-PRODUCTION-DOMAIN/">
<meta property="og:image" content="https://REPLACE-WITH-PRODUCTION-DOMAIN/images/food/volcano-roll-hero-baked-krab-eel-sauce.webp">
<meta name="twitter:card" content="summary_large_image">
```

No dedicated 1200×630 social-share crop exists in this repo today (see
`docs/ASSETS.md`); the hero image above is a placeholder choice, not a
confirmed social-share asset.

## Recommended (not applied) addition to the existing structured data

The existing JSON-LD `Restaurant` entries do not currently encode opening
hours, even though the hours are already visible on the page (in each
`.loc`'s `.hours` grid) and are already used by the `isOpen()` JavaScript.
Since this is already-published, already-visible information (not a new
fact), an `openingHoursSpecification` array could be added per location,
for example for Crestview:

```json
"openingHoursSpecification": [
  { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Sunday"], "opens": "11:00", "closes": "20:30" },
  { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Friday","Saturday"], "opens": "11:00", "closes": "21:30" }
]
```

This was **not applied** because it means editing existing `<head>`
content in `index.html`, which is outside this pass's scope. If it is
added later, remember: the visible `.hours` HTML, this JSON-LD block, and
the `close` values inside the `isOpen()` function (see
`docs/CONTENT-GUIDE.md`) are three separate places encoding the same
hours — keep them in sync.

## Heading order note

The footer uses `<h4>` for "Explore"/"Call" column labels; there's no
`<h3>` immediately preceding them in that region of the DOM even though
`<h3>` is used extensively earlier on the page (duo section, menu cards,
location names). Not an SEO penalty by itself — see `docs/ACCESSIBILITY.md`.

## Sitemap / robots

Both were added as new standalone files in this pass (not existing-page
edits). The sitemap lists only `/` because this variant is genuinely a
single page today — do not add `#menu`/`#gallery`/`#locations`/`#story` as
separate sitemap entries; sitemaps list pages, not in-page anchors. Update
`REPLACE-WITH-PRODUCTION-DOMAIN` in both files together once a production
domain is confirmed.
