# Foundry SMB Website

Static production website for Foundry SMB.

The current site is the cash-first Revenue Sprint funnel:

- AI Revenue Sprint, $1,500, 5 business days
- AI System Install, $5K-$15K follow-on implementation
- Foundry Toolkit digital products
- Operator Coaching as an add-on
- Netlify-ready sprint application form

No framework. No build step. No package install. Serve the folder and deploy the folder.

## Canonical Files

```text
foundrysmb-site/
├── index.html
├── roadmap.html
├── toolkit.html
├── coaching.html
├── how-it-works.html
├── about.html
├── contact.html
├── thank-you.html
├── support.html
├── terms.html
├── privacy.html
├── refunds.html
├── acceptable-use.html
├── license.html
├── design-system.css
├── sales-assets/
├── digital-products/
├── outbound/
├── agent-ops/
├── content/
├── pod/
├── _redirects
├── robots.txt
├── sitemap.xml
└── images/
```

Redirect compatibility pages are kept for old URLs:

- `assessment.html` -> `roadmap.html`
- `products.html` -> `toolkit.html`
- `consulting.html` -> `coaching.html`
- `bid-automation.html` -> `toolkit.html`
- `context-vaults.html` -> `toolkit.html`
- `permitting-navigator.html` -> `toolkit.html`
- `autonomous-departments.html` -> `toolkit.html`
- `industries.html` -> `about.html`
- `case-studies.html` -> `about.html`

## Local Preview

```bash
cd "/Users/truckirwin/Desktop/Foundry SMB/foundrysmb-site"
python3 -m http.server 8000
```

Open:

```text
http://localhost:8000
```

## Deployment

This folder can deploy as-is to Netlify, Vercel, S3/CloudFront, GitHub Pages, or any static host.

Netlify is the preferred host because `contact.html` already uses a Netlify form:

```html
<form name="revenue-sprint-application" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="thank-you.html">
```

Deploy root: this directory.

Build command: none.

Publish directory: this directory.

## Design System

The active stylesheet is `design-system.css`.

The visual direction is dark foundry-floor editorial:

- Source Serif 4 for display copy
- Inter Tight for body and UI copy
- JetBrains Mono for labels and operational detail
- warm black, cream, molten orange, yellow, and plum accents
- sharp panels, structured grids, image-led proof, and restrained texture

## Current Content Model

Top-level funnel:

1. Homepage sells the $1,500 AI Revenue Sprint.
2. Sprint page explains the five-day workflow diagnosis and prototype.
3. Process page explains sprint to install to productize.
4. Toolkit sells narrow digital products that support the service funnel.
5. Coaching sells direct operator support as an add-on.
6. Contact captures qualified sprint applications.

The Revenue Sprint is the primary CTA across the site.

## Form Handling

The contact form requires:

- name
- email
- phone
- company
- website
- industry
- team size
- painful workflow
- current tools
- desired outcome
- urgency
- budget confirmation

It posts to `thank-you.html`. On Netlify, submissions will appear under Forms after deployment.

For local testing, the browser will navigate to `thank-you.html` after submit, but no submission is stored.

## Maintenance Rules

- Update shared navigation and footer links consistently across all real pages.
- Keep `design-system.css` as the only active stylesheet.
- Keep redirect shims for old inbound URLs unless analytics proves they are unused.
- Add new pages as plain `.html` files in this folder.
- Prefer local images under `images/` for durable assets.
- External hero images are acceptable for preview, but production-critical images should be local.

## Verification

Run a local server and check:

- `/`
- `/roadmap.html`
- `/toolkit.html`
- `/coaching.html`
- `/how-it-works.html`
- `/about.html`
- `/contact.html`
- `/support.html`
- `/terms.html`
- `/privacy.html`
- `/refunds.html`
- `/acceptable-use.html`
- `/license.html`
- old redirect URLs listed above

See `LOCAL_TESTING.md` for a fuller checklist.
