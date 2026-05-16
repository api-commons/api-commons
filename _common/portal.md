---
name: Portal
description: Providing references to the relevant portal to an APIs operation, providing access to the landing page for the wider company, operations, as well as just for individual APIs when it makes sense--helping connect the wider ecosystem surrounding each API being delivered.
image: /images/portals.png
url: '#'
machineReadable: true
source: commons
tags:
  - Portals
  - Landing Pages
aliases:
  - Developer Portal
  - DevHub
  - API Hub
yaml_example: |
  - type: Portal
    url: https://portal.example.com/

standards:
  - name: RFC 8631 — Link Relation Types for Web Services
    url: https://www.rfc-editor.org/rfc/rfc8631
    kind: IETF
  - name: RFC 8288 — Web Linking
    url: https://www.rfc-editor.org/rfc/rfc8288
    kind: IETF
  - name: schema.org WebSite
    url: https://schema.org/WebSite
    kind: schema.org
  - name: Backstage Software Catalog
    url: https://backstage.io/docs/features/software-catalog/
    kind: CNCF

link_relations:
  - rel: service-desc
    spec: RFC 8631
    description: Link to a machine-readable service description (e.g., OpenAPI) discoverable from the portal.
  - rel: service-doc
    spec: RFC 8631
    description: Link to human-readable service documentation hosted in the portal.
  - rel: service-meta
    spec: RFC 8631
    description: Link to metadata describing the service.
  - rel: status
    spec: IANA
    description: Often linked from portal headers/footers to a status page.

openapi_expression:
  - field: info.contact.url
    spec: OpenAPI 3.x
    description: Frequently set to the developer portal landing page.
  - field: externalDocs.url
    spec: OpenAPI 3.x
    description: Points to portal-hosted long-form documentation.

governance_rules:
  - id: oas-info-contact
    source: Spectral built-in
    description: Portal URL is a common value for info.contact.url.
  - id: oas-external-docs
    source: Spectral built-in
    description: externalDocs should reference the portal's docs section.

risk:
  security_implications: Developer portals often combine marketing pages with authenticated key management. Treat the authenticated app/keys area with the same care as a console — MFA, session management, audit logs — and isolate it from the public marketing CMS.

tools:
  - name: Backstage
    url: https://backstage.io/
    license: Apache-2.0
    category: Internal developer portal
  - name: Tyk Developer Portal
    url: https://tyk.io/docs/tyk-developer-portal/
    category: API gateway portal
  - name: Kong Developer Portal
    url: https://docs.konghq.com/gateway/latest/developer-portal/
    category: API gateway portal
  - name: Apigee Developer Portal
    url: https://cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal
    category: API management portal
  - name: Azure API Management Developer Portal
    url: https://learn.microsoft.com/azure/api-management/api-management-howto-developer-portal
    category: API management portal
  - name: Readme.com
    url: https://readme.com/
    category: Hosted developer hub

metrics:
  - name: portal_signups
    description: New developer accounts created in the portal per period.
  - name: time_to_first_call_p50
    description: Median time from signup to first successful API call originated from a portal-issued key.
  - name: docs_search_no_results_rate
    description: Share of portal-search queries that return zero results — a content-gap signal.
  - name: key_rotation_rate
    description: Portion of active keys rotated within policy interval.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Dashboard + docs portal at stripe.com/docs with workbench tooling.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Console + docs portal with project-scoped credentials.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: docs.github.com plus the developer settings area for tokens and apps.
  - provider: Google
    url: https://providers.apis.io/providers/google/
    note: Google Cloud Console as the portal for API enablement and credentials.

related_properties:
  - portals
  - documentation
  - sign-up
  - login
  - sdks
---
