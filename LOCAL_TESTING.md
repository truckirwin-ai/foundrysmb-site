# Local Testing

## Start The Site

```bash
cd "/Users/truckirwin/Desktop/Foundry SMB/foundrysmb-site"
python3 -m http.server 8000
```

Open:

```text
http://localhost:8000
```

If port 8000 is busy:

```bash
python3 -m http.server 8010
```

## Primary Page Checklist

Check these pages:

- `http://localhost:8000/`
- `http://localhost:8000/roadmap.html`
- `http://localhost:8000/toolkit.html`
- `http://localhost:8000/coaching.html`
- `http://localhost:8000/how-it-works.html`
- `http://localhost:8000/about.html`
- `http://localhost:8000/contact.html`
- `http://localhost:8000/support.html`
- `http://localhost:8000/terms.html`
- `http://localhost:8000/privacy.html`
- `http://localhost:8000/refunds.html`
- `http://localhost:8000/acceptable-use.html`
- `http://localhost:8000/license.html`

## Legacy URL Checklist

These should move to current pages:

- `/assessment.html` -> `/roadmap.html`
- `/products.html` -> `/toolkit.html`
- `/consulting.html` -> `/coaching.html`
- `/bid-automation.html` -> `/toolkit.html`
- `/context-vaults.html` -> `/toolkit.html`
- `/permitting-navigator.html` -> `/toolkit.html`
- `/autonomous-departments.html` -> `/toolkit.html`
- `/industries.html` -> `/about.html`
- `/case-studies.html` -> `/about.html`

## Visual Checks

Desktop:

- Hero image appears on homepage.
- Header links are visible.
- Body text does not overlap imagery.
- Content grids align cleanly.
- CTA buttons are readable.
- Footer columns are readable.

Mobile:

- No horizontal scrolling.
- Header wraps without overlapping.
- Hero text fits without clipping.
- Cards stack cleanly.
- Form fields are full-width and readable.
- CTA text stays inside buttons.

## Form Check

On `contact.html`:

1. Confirm the Revenue Sprint application fields are required:
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
   - $1,500 budget confirmation
2. Confirm interest can be preselected from URL params:

```text
http://localhost:8000/contact.html?interest=revenue-sprint
http://localhost:8000/contact.html?interest=toolkit
```

3. Submit locally to confirm the browser lands on `thank-you.html`.

Local submit does not store anything. Deployed Netlify submit should appear in Netlify Forms.

## Browser Console

Open DevTools and confirm:

- no missing local CSS
- no missing local images
- no JavaScript errors
- no 404s for internal pages

Remote Unsplash images may be blocked offline. That should not break layout.

## Accessibility

Check:

- Tab reaches navigation and CTAs in order.
- Skip link appears on focus.
- Form fields have labels.
- Hero background images are decorative and do not carry required content.
- Link text is meaningful.

## Deployment Readiness

Before launch:

- run the local smoke test
- run a deployed preview
- test Netlify form capture
- run Lighthouse on mobile and desktop
- verify `robots.txt`
- verify `sitemap.xml`
