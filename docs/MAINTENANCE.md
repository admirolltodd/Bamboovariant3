# Maintenance Guide — Variant 3

Practical instructions for common future edits. No build tools, package
managers, or frameworks are involved anywhere in this workflow — everything
lives inline in `index.html`.

## Updating menu descriptions

1. Edit the relevant `<article class="menu-card">` inside the matching
   `<div class="menu-panel">` (`#rolls`, `#signatures`, or `#hibachi`) in
   `index.html`.
2. Do not add prices — the page's own `.menu-note` copy already tells
   visitors the live ordering menu is the source of truth for price and
   availability.
3. Only use a dish name you can confirm (existing menu copy, a menu board
   photo, or the ordering platform) — don't invent one.
4. If you add a whole new tab/category, add both a `.menu-tab` button and
   a matching `.menu-panel` with the same id (see `docs/CONTENT-GUIDE.md`).

## Updating location information — three places, every time

Location facts appear in three places in this variant. **All three must be
updated together** whenever hours, an address, or a phone number changes:

1. The visible `<article class="loc">` block for that location.
2. The JSON-LD `Restaurant` entry for that location in `<head>`.
3. The `close` values inside the `isOpen()` JavaScript function, if the
   closing time itself changes.

See `docs/CONTENT-GUIDE.md` for exactly where each of these lives.

## Replacing hero photos

Replace the file referenced by `.hero-bg img` in `index.html` with a new
file in `images/food/` (see `docs/ASSETS.md` for naming convention). Give
the new file a new, descriptive filename rather than overwriting the old
one — `netlify.toml` caches everything under `/images/*` for a year, so
reusing a filename means returning visitors keep seeing the old photo until
their cache expires. **Also update the `<link rel="preload" as="image"
href="...">` tag in `<head>`** to reference the same new filename — it is
a separate reference from the `<img src>` and both must point at the same
file (see `docs/ASSETS.md`).

## Adding gallery images

Add the new file to the matching `images/` subfolder and reference it from
`.gallery-grid`. Do not caption it with a specific dish name unless that
name is already confirmed elsewhere (see `docs/CONTENT-GUIDE.md`) — this
variant's own copy says its gallery deliberately avoids "guessing at dish
names."

## Updating ordering links

Each location's "Order [Location]" button in `#locations` points directly
to that location's own URL on the ordering platform
(`menu-6161.orderexperience.net/...`). If a location's URL changes, update
it only in that location's `<article class="loc">` block — do not
consolidate multiple locations onto one shared ordering URL. The sticky
mobile order bar (`.mobile-order`) links to `#locations`, not to a specific
location, so it needs no change when an individual location's URL changes.

## Testing mobile layouts

Resize the browser below 980px and then below 620px (the two breakpoints in
`index.html`'s inline `<style>`) and confirm:

- `.menu-toggle` appears and `#mobileNav` opens/closes correctly.
- The sticky `.mobile-order` bar appears at the bottom of the viewport
  below 620px and both its buttons work.
- The hero, duo section, menu grid, gallery grid, locations grid and
  story/footer all collapse to the expected layout at each breakpoint.

## Validating sitemap changes

If this variant ever grows beyond a single page:

1. Add the corresponding `<url>` entry to `sitemap.xml`.
2. Validate the file is well-formed XML (e.g. `python3 -c "import
   xml.dom.minidom as m; m.parse('sitemap.xml')"`).
3. Confirm every URL in the sitemap actually resolves to a real page.

Until then, `sitemap.xml` should keep listing only `/` — do not add
in-page anchors like `#menu` as separate sitemap entries.

## Testing 404 routing

Visit an unknown path (e.g. `/does-not-exist`) on the deployed site and
confirm `404.html` renders and the response status is 404 (check with
`curl -I` or browser dev tools). If the shared design tokens in
`index.html`'s `<style>` block change (colors, fonts), update the isolated
copy at the top of `404.html`'s `<style>` block to match — see the comment
there for why the two can't simply share one stylesheet today.

## Deployment checks

See `docs/DEPLOYMENT.md` for the full pre-deploy checklist.
