# Accessibility Notes — Variant 3

Observations only. No layout or content changes were made to `index.html`
as part of this pass.

## Already in good shape

- `lang="en"` set on the page.
- A working skip-to-content link (`.skip`, targets `#main`), visible on
  focus, plus a **global `:focus-visible` outline**
  (`outline:2px solid var(--red2)`) applied to every focusable element —
  this variant already does more here than Variant 1 or Variant 2.
- Heading structure is a single `<h1>` with `<h2>`/`<h3>`/`<h4>` used in a
  largely sensible order (one gap noted below).
- The menu tabs use proper ARIA tab pattern markup: `role="tablist"`,
  `role="tab"`, `aria-selected`, and `hidden` on inactive panels.
- The mobile nav toggle has `aria-expanded`/`aria-controls` kept in sync by
  the inline script.
- `@media (prefers-reduced-motion: reduce)` disables `scroll-behavior` and
  transitions site-wide.
- No forms exist on this page, so form labeling is not applicable.

## Observations for future, deliberate fixes

- **Heading level gap.** The footer's `<h4>` labels ("Explore", "Call")
  have no `<h3>` immediately preceding them in that part of the document,
  even though `<h3>` is used extensively earlier (duo section, menu-card
  titles, location names). A screen-reader heading-list view will show a
  level jump into the footer. Low-risk if revisited later, but not
  attempted in this pass since it edits existing HTML.
- **Live status region.** The open/closed badge (`.status`) updates its
  text via JavaScript on page load but is not marked as an ARIA live
  region. Since it only changes once (on load), this is unlikely to
  confuse most assistive tech, but if the badge is ever made to update
  periodically without a page reload, consider `aria-live="polite"` on the
  `.status` element.
- **Color contrast.** White text on `--red: #d8262a` / `--red2: #f2484c`
  (used on `.btn-red`, the "Order" buttons, the eyebrow badges) should be
  checked with a contrast tool for the smallest text sizes used in those
  areas. The muted gray tokens (`--muted: #aaa19b`) used for hours/labels
  on the dark background are also worth spot-checking for small mono-font
  text specifically.
- **Decorative glyphs.** The large background "寿"/"火" characters in
  `.duo .glyph` are rendered as plain text content rather than `aria-hidden`
  elements. They're very low-contrast/decorative by design
  (`color:rgba(255,255,255,.025)`), but a screen reader will still
  announce them since they aren't marked `aria-hidden="true"`. A low-risk
  future fix would add that attribute; not applied here since it edits
  existing HTML.

## Applied (near-zero-risk only)

No content or layout changes were made to `index.html`. The observations
above were left as documented recommendations rather than applied, since
editing existing HTML in `index.html` falls outside this pass's scope of
"infrastructure and documentation only."
