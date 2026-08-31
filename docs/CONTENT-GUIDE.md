# Content Guide — Variant 3

Practical rules for editing this variant's content without breaking its
single-page design or its live behaviors.

## Menu content

- Menu items live in three `<div class="menu-panel">` blocks in
  `index.html`: `#rolls` (Sushi Rolls), `#signatures` (Bamboo Signatures)
  and `#hibachi` (Hibachi & More), switched by the `.menu-tab` buttons
  above them.
- Do not add prices — the page's own `.menu-note` copy already tells
  visitors the live ordering menu is the source of truth for price and
  availability.
- If you add a new tab/panel, you must add both: a new `<button
  class="menu-tab" role="tab" data-panel="...">` and a matching `<div
  class="menu-panel" id="...">` with the same id as `data-panel` — the tab
  JS matches them by that id.
- Existing dish names (California Roll, Volcano Roll, Godzilla Roll, Mt.
  Fuji Roll, Sasquatch Roll, TNT Roll, King Kong, etc.) are already
  confirmed by the page's own content. Only add a new dish name you can
  confirm elsewhere (a menu board photo, another variant's verified menu
  copy, or the ordering platform) — don't invent one.

## Location content — keep three sources in sync

Location facts appear in **three** places in this variant:

1. The visible `<article class="loc">` blocks in `#locations`
   (address, phone, hours).
2. The JSON-LD `Restaurant` structured data in `<head>` (name, phone,
   address — currently does not encode hours).
3. The `isOpen()` JavaScript function's hardcoded close times (`20.5` /
   `21.5`, i.e. 8:30pm / 9:30pm), used to compute the live "Open now" /
   "Closed now" badge.

**If hours or an address change, update all three.** Missing one means the
live status badge, the structured data search engines read, and what the
page visibly says will disagree with each other.

Each location's "Order" button links directly to that location's own
ordering-system URL. Never point a location's Order button at another
location's URL or a generic/shared ordering page.

## Gallery / photography

- Do not invent a dish name for a gallery photo. This variant's own gallery
  copy says it deliberately avoids "guessing at dish names" — keep using
  generic, descriptive alt text (e.g. "Prepared seafood dish at Bamboo")
  unless the dish is already confirmed by existing copy.

## Voice and tone

Existing copy pairs a short declarative fragment with a colored emphasis
word (e.g. "Two kitchens. *One table.*", "Sushi. Hibachi. *Bamboo.*").
Section intros are one to two sentences. New copy should match that
brevity — the layout relies on large serif display type and generous
whitespace, and long paragraphs will overflow the fixed-height duo/location
cards.
