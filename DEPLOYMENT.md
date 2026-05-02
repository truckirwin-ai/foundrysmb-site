# Deployment Guide

Foundry SMB is a static website. There is no build command and no server-side app.

## Recommended Host

Use Netlify first.

Why:

- built-in static hosting
- built-in form handling for `contact.html`
- `_redirects` support
- automatic HTTPS
- deploy previews
- simple rollback

## Netlify Setup

1. Create or open the Netlify site.
2. Set the deploy root to this folder:

```text
/Users/truckirwin/Desktop/Foundry SMB/foundrysmb-site
```

3. Build command:

```text
none
```

4. Publish directory:

```text
.
```

5. Deploy.

6. In Netlify, open Forms and confirm `access-request` is detected after the first deploy.

7. Add notification routing for form submissions:

```text
hello@foundrysmb.com
```

## DNS

Point `foundrysmb.com` to the selected host.

For Netlify:

1. Add `foundrysmb.com` and `www.foundrysmb.com` in Domain settings.
2. Use Netlify DNS or update the registrar records as Netlify instructs.
3. Confirm HTTPS is issued.

## Redirects

The project includes `_redirects` for legacy URLs:

```text
/assessment.html /roadmap.html 301
/products.html /toolkit.html 301
/consulting.html /coaching.html 301
/bid-automation.html /toolkit.html 301
/context-vaults.html /toolkit.html 301
/permitting-navigator.html /toolkit.html 301
/autonomous-departments.html /toolkit.html 301
/industries.html /about.html 301
/case-studies.html /about.html 301
```

HTML redirect shims are also present for hosts that do not honor `_redirects`.

## Sitemap And Robots

The project includes:

- `sitemap.xml`
- `robots.txt`

Update `sitemap.xml` whenever public pages are added or removed.

## Pre-Launch Checklist

- Confirm homepage loads at `/`.
- Confirm all primary pages load.
- Confirm old URLs redirect.
- Submit the contact form in a deployed Netlify preview.
- Confirm Netlify captures the `access-request` form.
- Confirm email notifications are enabled.
- Confirm `foundrysmb.com` and `www.foundrysmb.com` both resolve.
- Confirm HTTPS.
- Run Lighthouse on desktop and mobile.
- Check the site on an actual phone.

## Local Smoke Test

```bash
cd "/Users/truckirwin/Desktop/Foundry SMB/foundrysmb-site"
python3 -m http.server 8000
```

Open:

```text
http://localhost:8000
```

## Alternate Hosts

Vercel:

- Build command: none
- Output directory: `.`
- Form handling requires a third-party service or serverless function

S3/CloudFront:

- Upload all files
- Configure `index.html` as index document
- Add redirects with CloudFront Functions or keep the HTML shims
- Use ACM for HTTPS

Traditional hosting:

- Upload all files to the web root
- Confirm `.html`, `.css`, `.xml`, and extensionless `_redirects` files are served if needed
- Use the HTML redirect shims if server-level redirects are unavailable

## Analytics

No analytics script is installed by default.

If adding analytics, keep it light:

- Plausible
- Fathom
- Google Analytics 4

Add scripts to every real page, not the redirect shims.

## Production Image Note

The site currently uses a mix of local foundry imagery and remote Unsplash imagery. For maximum durability, download production-critical hero images into `images/` and update the page URLs before final launch.
