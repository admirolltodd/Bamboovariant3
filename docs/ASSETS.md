# Asset Guide — Variant 3

Documents where image assets live and how they're used. This does not
rename or move any existing file.

## Directories

| Directory | Contents |
|---|---|
| `images/brand/` | `bamboo-sushi-hibachi-logo.png` (used as favicon and in header/footer brand mark) and `bamboo-sushi-hibachi-logo-full.png` (currently unused by `index.html`) |
| `images/food/` | Dish photography, including the homepage hero (`volcano-roll-hero-baked-krab-eel-sauce.webp`, preloaded with `fetchpriority="high"`) and the two "two kitchens"/gallery images |
| `images/gallery/` | Storefront, signage and dining-room photography, used in the gallery grid and the "Our Story" section |
| `images/menu/` | Photographs of physical menu boards (not currently placed on the single page) |
| `images/awards/` | Community's Choice and Best of Florida award graphics (not currently placed on the single page) |
| `images/press/` | Press clipping images (not currently placed on the single page) |

## The hero image is preloaded by filename

`<head>` contains `<link rel="preload" as="image"
href="images/food/volcano-roll-hero-baked-krab-eel-sauce.webp"
fetchpriority="high">`, and the hero `<img>` tag in `.hero-bg` references
the same file. **If the hero photo is ever replaced, update both
references together** — the preload tag and the `<img src>` — or the
browser will preload an image the page doesn't actually display.

## Naming conventions already in use

Filenames are descriptive kebab-case. Some files in `images/food/` carry a
`-800w` suffix (a pre-sized responsive variant) and some don't
(`sunset.webp`, `volcano.webp`, `volcano-roll-hero-baked-krab-eel-sauce.webp`
are single files) — this variant does not use `srcset`/`sizes`, so each
`<img>` references one specific file directly. Do not rename existing
files; follow whichever convention the folder you're adding to already
uses.

## Assets that should not be renamed

Every file currently referenced by an `<img src="...">` , `<link
rel="icon">`, or `<link rel="preload">` in `index.html` or `404.html`.
Renaming any of them requires updating every place that references that
filename — including the preload tag noted above.

## Content safety

Do not caption or rename an image with a specific dish name (e.g. "Volcano
Roll", "Spicy Tuna") unless the existing alt text or page copy already
names it. The tabbed menu panels in `index.html` do name specific dishes
(California Roll, Spicy Tuna Roll, Volcano Roll, Godzilla Roll, etc.) —
those names come from the page's own existing copy and are already
verified by it. The gallery images, however, use deliberately generic alt
text ("Prepared sushi platter at Bamboo", "Prepared seafood dish at
Bamboo") — keep that pattern for gallery/ambiance photography rather than
assigning it a specific menu-item name.

## Where future optimized images should go

Add new photography into the existing category folder that matches its
subject (`images/food/`, `images/gallery/`, etc.) rather than creating new
top-level image directories.
