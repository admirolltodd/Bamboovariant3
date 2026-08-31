# Bamboo Sushi Bar & Hibachi Express — Variant 3

Variant 3 is a static, customer-facing concept site for Bamboo Sushi Bar & Hibachi Express on Florida's Emerald Coast.

## Design direction

This variant keeps the dark charcoal/red restaurant identity, strong food photography, a warm light menu section, and a direct customer journey from discovery to ordering.

## Site goals

- Explain Bamboo's sushi and hibachi offering quickly.
- Let customers browse representative menu items and ingredients without duplicating live prices.
- Route customers to the correct location-specific ordering system.
- Give Crestview, Fort Walton Beach, and Niceville dedicated local landing pages.
- Keep the gallery descriptive without guessing specific dish names from photographs.

## Structure

- `index.html` — primary landing page
- `menu/index.html` — expanded shared menu landing page
- `locations/index.html` — location directory
- `locations/crestview/index.html` — Crestview location
- `locations/fort-walton-beach/index.html` — Fort Walton Beach location
- `locations/niceville/index.html` — Niceville location
- `404.html` — branded error page
- `robots.txt` — crawler guidance
- `sitemap.xml` — crawlable page inventory
- `images/` — existing asset library
- `netlify.toml` — Netlify static deployment configuration

## Ordering

The website intentionally does not publish prices. Current pricing, availability, modifications, and checkout remain in the location-specific OrderExperience menus.

## Maintenance rule

Do not invent menu ingredients, photo identities, awards, press claims, hours, or restaurant history. Verify business information before changing public-facing copy.

## Deployment

This project has no build step. Netlify publishes the repository root directly.