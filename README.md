# Bamboo Sushi Bar & Hibachi Express — Variant 3 (Premium Dark / Combined Concept)

This repository is one of three parallel design concepts for the Bamboo
Sushi Bar & Hibachi Express website. **Variant 3 is the premium dark
concept and is currently the most complete, combined/final-model design**:
a single richly-detailed page with a tabbed menu, a live open/closed
indicator per location, and existing SEO structured data.

This README documents this variant only. It does not describe Variant 1
(multi-page usability concept) or Variant 2 (bright black/white/red
concept) — those live in their own repositories.

## Design concept

- Dark, editorial palette: near-black background (`--ink:#0b0b0c`), warm
  paper tone for the menu section (`--paper:#f6f1e9`), red accent
  (`--red:#d8262a` / `--red2:#f2484c`) and a muted gold token
  (`--gold:#c9962f`).
- Serif display type (**Fraunces**) for headlines, **Inter** for body copy,
  **IBM Plex Mono** for labels/eyebrows — loaded from Google Fonts.
- Rounded-pill buttons and cards (`border-radius`), soft glass-morphism
  header (`backdrop-filter: blur`), and a persistent mobile order bar fixed
  to the bottom of the viewport on small screens.
- A tabbed, in-page menu (Sushi Rolls / Bamboo Signatures / Hibachi & More)
  switched entirely with vanilla JS — no page reload, no separate menu
  page.
- A **live open/closed status badge per location**, computed client-side
  in `America/Chicago` time against each location's known hours.

## Page structure

This variant currently has a **single HTML page**:

| Page | File | Purpose |
|---|---|---|
| Home (everything) | `index.html` | Hero, trust bar, "two kitchens" duo section, tabbed menu, gallery, locations with live status, story + catering callout, footer, sticky mobile order bar |
| 404 | `404.html` | Custom not-found page (added as part of this infrastructure pass) |

In-page anchors/sections: `#top` (hero), `#experience`, `#menu`,
`#gallery`, `#locations`, `#story`. There are no separate
`menu.html`/`locations.html` pages — everything lives on `index.html`.

## Running locally

No build step, no package manager. Serve the repository root with any
static file server, for example:

```
python3 -m http.server 8080
```

or

```
npx serve .
```

Then open `http://localhost:8080/`. The page depends on a live connection
to Google Fonts for its typography, and the location open/closed badges
depend on the browser's `Intl.DateTimeFormat` support (widely available in
modern browsers, no polyfill needed).

## Primary directories

```
/
├── index.html          # The entire site: inline <style>, inline JSON-LD, inline <script>
├── 404.html            # Custom not-found page (new)
├── images/
│   ├── awards/
│   ├── brand/
│   ├── food/
│   ├── gallery/
│   ├── menu/
│   └── press/
├── docs/                # Infrastructure & production documentation (this pass)
├── robots.txt
├── sitemap.xml
└── netlify.toml
```

Like Variant 2, this repository has **no `css/` or `js/` directory** —
every style rule, the JSON-LD block, and all interactive JavaScript live
inline inside `index.html`. This pass did not extract them into external
files, since doing so would mean editing `index.html` itself.

## Where content actually lives

- **Menu content** lives in three `<div class="menu-panel">` blocks inside
  `index.html` (`#rolls`, `#signatures`, `#hibachi`), switched by the
  `.menu-tab` buttons. It carries no prices — the page's own `.menu-note`
  copy says the live ordering menu is the source of truth for price and
  availability.
- **Location content** (address, phone, hours) lives in three
  `<article class="loc">` blocks inside `#locations`, and is **also**
  duplicated as JSON-LD `Restaurant` structured data in the page `<head>`
  (see `docs/SEO.md`). If you ever change an address, phone number, or
  hours, update **both** places so they stay in sync.
- **Order links** are direct links to each location's own ordering-system
  URL (`menu-6161.orderexperience.net/...`), one per location, opened in a
  new tab. The sticky mobile order bar (`.mobile-order`) at the bottom of
  small screens links to the in-page `#locations` section, not to a
  specific location — the visitor still picks a location once they get
  there.

## Important JavaScript behavior

All inline in `index.html`'s closing `<script>` block:

- **Menu tabs:** clicking a `.menu-tab` button shows the matching
  `.menu-panel` and hides the others, toggling `aria-selected` and the
  panel's `hidden` attribute.
- **Mobile nav:** toggles `.open` on `#mobileNav` and keeps
  `aria-expanded` on `#menuToggle` in sync.
- **Live open/closed status:** `centralNow()` reads the current time in
  `America/Chicago` via `Intl.DateTimeFormat`, and `isOpen()` compares it
  against the hours already printed on the page (11:00a–8:30p
  Mon–Thu/Sun, 11:00a–9:30p Fri–Sat) to toggle each location's `.status`
  badge between "Open now" and "Closed now". **If the restaurant's hours
  ever change, update both the visible `.hours` grid text for each
  location and the `close` values inside `isOpen()`** — they are two
  separate places that must be kept in sync.
- Sets the footer's `#year` span to the current year.

## Deployment

Deployed as a static site on Netlify. See `docs/DEPLOYMENT.md` for the full
checklist. Publish directory is the repository root, no build command.
`netlify.toml` now carries caching and security headers — see that file and
`docs/DEPLOYMENT.md` for why the CSP explicitly allows
`fonts.googleapis.com`/`fonts.gstatic.com`.

## Production checklist

- [ ] Click every anchor nav link (`#menu`, `#gallery`, `#locations`,
      `#story`) and confirm smooth-scroll lands on the right section.
- [ ] Click all three menu tabs and confirm the correct panel shows/hides.
- [ ] Click every "Order [Location]" link for all three locations.
- [ ] Confirm the open/closed badge is correct at a few different times of
      day (or temporarily adjust your system clock/timezone to test edge
      cases around opening/closing time).
- [ ] Confirm the JSON-LD block in `<head>` still validates (e.g. with
      Google's Rich Results Test) after any location-data edit.
- [ ] Test the mobile nav toggle and the sticky mobile order bar at a
      narrow viewport.
- [ ] Confirm `robots.txt` is served as plain text and `sitemap.xml` as
      XML.
- [ ] Confirm `404.html` renders for an unknown path and returns HTTP 404.

## Known limitations

- No Open Graph or Twitter Card meta tags, and no `<link rel="canonical">`
  yet (JSON-LD structured data, however, is already present and valid —
  see `docs/SEO.md`).
- Location hours are duplicated in three places if you count the visible
  `.hours` grid, the `isOpen()` JS logic, and the JSON-LD block (which
  currently does not encode hours — see `docs/SEO.md`) — keep the first two
  in sync manually.
- All CSS, structured data and JS are inline in `index.html`; `404.html`
  carries its own small, isolated copy of the shared design tokens (see
  `docs/PROJECT-STRUCTURE.md`).
- No automated tests or link checker; verification is manual (see checklist
  above and `docs/MAINTENANCE.md`).

## Related repositories

- Variant 1 (multi-page usability concept) — separate repository.
- Variant 2 (bright black/white/red concept) — separate repository.
- `828bamboosushi` — production-engineering reference repository used to
  inform the infrastructure and documentation patterns in this `docs/`
  folder. Its page content and visual design are not part of this variant.
