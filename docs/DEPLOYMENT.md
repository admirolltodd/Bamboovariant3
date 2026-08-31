# Deployment — Variant 3

## Hosting assumptions

Static site hosted on Netlify. No backend, no database, no server-rendered
content, no build tooling.

## Build

- **Build command:** none.
- **Publish directory:** repository root (`.`), as set in `netlify.toml`.

Only public-facing website material should be committed at the repository
root — the `docs/*.md` files and `README.md` are explicitly blocked from
being served by the redirects in `netlify.toml`, but keep that in mind
before adding new root-level files.

## Headers

`netlify.toml` sets:

- A one-year cache on `/images/*` (safe because image filenames change
  when the photo changes — see `docs/ASSETS.md`).
- A no-cache / must-revalidate policy on HTML so edits show up immediately.
- Security headers on every response, including a
  `Content-Security-Policy` that explicitly allows
  `https://fonts.googleapis.com` (stylesheets) and
  `https://fonts.gstatic.com` (font files) because `index.html` loads
  Fraunces, Inter and IBM Plex Mono from Google Fonts — **removing those
  two origins from the CSP will break the site's typography.**
  `script-src`/`style-src` also allow `'unsafe-inline'` because this
  variant's entire CSS, JSON-LD block and JS live inline in `index.html`
  with no build step to hash or externalize them.

**If you ever add a new third-party resource** (analytics, a map embed, a
different font host, a reservations widget), you must widen the relevant
CSP directive in `netlify.toml` first, or it will silently fail to load.

## Redirects / custom domain

No redirects currently exist beyond the two that 404 stray Markdown/config
files (`README.md`, `netlify.toml`) so they aren't servable as public
pages. There is no confirmed production custom domain yet —
`robots.txt` and `sitemap.xml` both use a `REPLACE-WITH-PRODUCTION-DOMAIN`
placeholder that must be swapped for the real domain once one is assigned.

## 404 behavior

`404.html` is a static file at the repository root. Netlify serves it
automatically for any unmatched path (Netlify's default behavior for a
file literally named `404.html` at the publish root) — no extra
`[[redirects]]` rule is required.

## Deployment verification checklist

- [ ] `index.html` returns HTTP 200.
- [ ] An unknown path (e.g. `/does-not-exist`) returns HTTP 404 and renders
      `404.html`.
- [ ] `robots.txt` is served as `text/plain`, not as an HTML fallback.
- [ ] `sitemap.xml` is served as XML, not as an HTML fallback.
- [ ] Google Fonts still load — check that `Fraunces`/`Inter`/`IBM Plex
      Mono` render, not a system-font fallback.
- [ ] The JSON-LD `Restaurant` block in `<head>` still validates (e.g. with
      Google's Rich Results Test).
- [ ] The live open/closed status badge shows the correct state for the
      current time in `America/Chicago`.
- [ ] Response headers include the security headers from `netlify.toml`
      (check with browser dev tools or `curl -I`).
- [ ] Every menu tab switches panels correctly, and every "Order
      [Location]" link works.
- [ ] Mobile nav toggle and the sticky mobile order bar both work on a
      small viewport.
