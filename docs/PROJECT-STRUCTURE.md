# Project Structure — Variant 3

This reflects the actual repository layout. It is documentation only; no
files were moved or renamed to produce this listing.

```
/
├── index.html            # The entire site: one page, inline <style>, inline JSON-LD, inline <script>
├── 404.html              # Custom not-found page (new — has its own small isolated <style>)
├── robots.txt
├── sitemap.xml
├── netlify.toml
├── README.md
├── images/
│   ├── awards/            # Community's Choice / Best of Florida award graphics
│   ├── brand/              # Logo files
│   ├── food/                # Dish photography, including the homepage hero
│   ├── gallery/             # Storefront and dining-room photography
│   ├── menu/                 # Menu board photographs
│   └── press/                # Press clippings
└── docs/                  # This documentation set
    ├── PROJECT-STRUCTURE.md
    ├── ASSETS.md
    ├── CONTENT-GUIDE.md
    ├── DEPLOYMENT.md
    ├── SEO.md
    ├── ACCESSIBILITY.md
    └── MAINTENANCE.md
```

## Notes

- **There is no `css/` or `js/` directory.** All styling, the JSON-LD
  structured-data block, and all interactivity (menu tabs, mobile nav,
  live open/closed status) live inline in `index.html`. This is a
  deliberate characteristic of this variant, not an omission, and this
  infrastructure pass did not restructure it.
- `404.html` cannot `<link>` to a shared stylesheet because none exists. It
  carries its own small, isolated `<style>` block with just the design
  tokens and header/footer chrome needed to look consistent with
  `index.html` — see the comment at the top of `404.html` for why.
- There are no separate `menu.html` / `locations.html` / `story.html`
  pages; those topics are sections within `index.html` reached via
  in-page anchors (`#menu`, `#gallery`, `#locations`, `#story`).
- This variant is the only one of the three that already ships JSON-LD
  `Restaurant` structured data in `<head>` — see `docs/SEO.md`.
