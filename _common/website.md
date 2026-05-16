---
name: Website
description: The primary public website for the company or product behind an API — distinct from the developer portal. The website is where the broader audience (buyers, partners, press, candidates) lands; it usually links downstream into the developer portal, documentation, signup, and pricing. Standardizing a pointer to the website lets discovery tools tie an API back to its parent organization without scraping.
image: /images/website.png
url: '#'
machineReadable: false
source: commons
tags:
  - Discovery
  - Organization
  - Landing Pages
aliases:
  - Home Page
  - Company Website
  - Corporate Website
  - Marketing Site
yaml_example: |
  - type: Website
    url: https://example.com/

standards:
  - name: schema.org WebSite
    url: https://schema.org/WebSite
    kind: Schema.org
  - name: schema.org Organization
    url: https://schema.org/Organization
    kind: Schema.org
  - name: RFC 8288 — Web Linking
    url: https://www.rfc-editor.org/rfc/rfc8288
    kind: IETF
  - name: Open Graph Protocol
    url: https://ogp.me/
    kind: De facto

link_relations:
  - rel: canonical
    spec: HTML Living Standard
    description: Identifies the canonical URL of the company or product home.
  - rel: home
    spec: IANA Link Relations
    description: Link to the start page of an application or site.

openapi_expression:
  - field: info.contact.url
    spec: OpenAPI 3.x
    description: Often points to the company website when no separate portal exists.

risk:
  security_implications: The marketing site is typically a separate CMS from the developer portal but often shares brand assets and analytics tags. Treat redirects from the marketing site into authenticated developer surfaces as trust boundaries; phishing pages routinely impersonate the marketing site to harvest credentials.

metrics:
  - name: website_to_portal_referrals
    description: Visits that originate on the marketing site and land in the developer portal.
  - name: api_page_views
    description: Visits to API/product pages on the marketing site — a top-of-funnel indicator.

examples:
  - provider: Stripe
    url: https://stripe.com/
    note: Marketing site at stripe.com is distinct from the developer surface at stripe.com/docs.
  - provider: Twilio
    url: https://www.twilio.com/
    note: www.twilio.com markets the platform; developers move to twilio.com/docs.
  - provider: GitHub
    url: https://github.com/
    note: github.com hosts both the product and developer-facing surfaces under one domain.

related_properties:
  - portal
  - about
  - contact
  - signup
---
