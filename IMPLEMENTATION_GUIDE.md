# Implementation Guide

## Architecture

This is a static multi-page site. Each public page is hand-authored HTML and shares one stylesheet:

```text
design-system.css
```

There is no active JavaScript bundle. Small page-specific scripts are inline only where needed:

- homepage image fallback from SVG to JPG
- contact form interest preselection from `?interest=`

## Active Page Set

Core funnel:

- `index.html`
- `roadmap.html`
- `toolkit.html`
- `coaching.html`
- `how-it-works.html`
- `about.html`
- `contact.html`
- `thank-you.html`

Trust and operations:

- `support.html`
- `terms.html`
- `privacy.html`
- `refunds.html`
- `acceptable-use.html`
- `license.html`

Utility:

- `icons.html`
- `_redirects`
- `robots.txt`
- `sitemap.xml`

## Design Direction

Foundry SMB should feel like an operator's command surface, not a generic AI agency.

Visual system:

- dark warm-black base
- molten orange and yellow accents
- cream typography
- serif display copy
- tight operational labels
- sharp panels
- structured grids
- treated photographic heroes
- light grain texture

Tone:

- direct
- operator-led
- practical
- premium but not precious
- AI-first without sounding like a tool demo

## CSS Structure

`design-system.css` contains:

- tokens
- reset
- base typography
- layout primitives
- header
- hero variants
- structured content grids
- tables
- forms
- footer
- legal/content blocks
- responsive rules

Keep new components in this same file unless the site becomes large enough to justify a build system.

## Navigation

Primary nav appears on all real pages:

```text
Sprint / Process / Toolkit / Coaching / About / Book
```

Footer nav includes:

```text
AI Revenue Sprint
Foundry Toolkit
Operator Coaching
How It Works
About
Contact
Support
```

Legal footer includes:

```text
Terms of Service
Privacy Policy
Refunds & Cancellation
Acceptable Use
Subscription License
```

When adding or renaming pages, update all repeated nav/footer blocks.

## Redirects

Old URLs are intentionally preserved. Keep the HTML redirect shims unless you are certain no inbound links exist.

Netlify also uses `_redirects`.

## Forms

`contact.html` contains the only active form.

It is Netlify-ready:

```html
<form name="access-request" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="thank-you.html">
```

Required:

- name
- email
- phone

Interest values:

- `roadmap`
- `toolkit`
- `coaching-1on1`
- `coaching-cohort`
- `general`

Links can preselect interest:

```text
contact.html?interest=toolkit
```

## Images

Local assets live in `images/`.

Current local assets:

- `images/foundry-pour.svg`
- `images/foundry-pour.jpg`
- `images/icons/*.svg`

Some page heroes still use remote Unsplash URLs. That is acceptable for preview, but final production-critical imagery should be downloaded into `images/` and referenced locally.

## SEO

Current SEO assets:

- per-page title and description
- semantic HTML
- `robots.txt`
- `sitemap.xml`
- legacy redirects

Recommended next SEO pass:

- add Open Graph tags to all primary pages
- add a 1200x630 social card image
- add structured data for Organization

## Adding A Page

1. Duplicate a similar page.
2. Update title and meta description.
3. Keep the shared header and footer.
4. Link `design-system.css`.
5. Add the page to `sitemap.xml` if it should be indexed.
6. Add footer/nav links only if the page is core.
7. Run local smoke test.

## Removing A Page

1. Replace it with a redirect shim if the URL may exist publicly.
2. Add a redirect in `_redirects`.
3. Remove it from `sitemap.xml`.
4. Check all internal links.

## Local Verification

```bash
cd "/Users/truckirwin/Desktop/Foundry SMB/foundrysmb-site"
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000
```
