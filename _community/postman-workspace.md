---
name: Postman Workspaces
description: A Postman Workspace is a cloud space where you can store collections, OpenAPI, tests, and other elements. Think of a Postman Workspace as a GitHub repository, but specifically for APIs, providing a place you can organize collections, OpenAPIs, monitors, tests, and other ways to automate API operations and integrations. Workspaces can be public, private, or partner access only, helping you organize your APIs into individual spaces that are isolated for different audiences.
image: /images/postman.png
url: https://www.postman.com/product/workspaces/
machineReadable: false
source: platform
tags:
  - Workspaces
aliases:
  - Postman Workspace
  - Public Workspace
  - Team Workspace
  - Partner Workspace

standards:
  - name: Postman Workspaces (product documentation)
    url: https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/creating-workspaces/
    kind: Postman (vendor)
  - name: Postman API — Workspaces
    url: https://www.postman.com/postman/postman-public-workspace/documentation/i2uqzpp/postman-api
    kind: Postman (vendor)
  - name: Postman API Network
    url: https://www.postman.com/explore
    kind: Postman (vendor)
  - name: Postman Collection Format v2.1.0 (artifact stored in workspaces)
    url: https://schema.postman.com/json/collection/v2.1.0/collection.json
    kind: Postman (de facto)
  - name: OpenAPI 3.x (artifact stored in workspaces)
    url: https://spec.openapis.org/oas/v3.1.0
    kind: OpenAPI Initiative

governance_rules:
  - id: workspace-visibility-reviewed
    source: Convention
    description: Public-workspace visibility changes should be reviewed before publication.
  - id: workspace-no-private-environments-public
    source: Convention
    description: Environments containing secrets must not be published to a public workspace.
  - id: workspace-ownership-assigned
    source: Convention
    description: Every workspace should have a named owner / team.
  - id: workspace-publishing-checklist
    source: Convention
    description: Use a release checklist before flipping a workspace from private to public.

risk:
  owasp:
    - 'OWASP API Security Top 10: API8:2023 Security Misconfiguration — public workspaces have leaked tokens, internal URLs, and PII'
    - 'OWASP API Security Top 10: API9:2023 Improper Inventory Management — shadow workspaces drift from canonical APIs'
  compliance:
    - SOC 2 CC6.1 — workspace ACLs are an access-control surface
    - GDPR — example bodies in public workspaces have historically exposed personal data
  security_implications: Workspaces are a publishing surface. Treat going public as a release; scan all collections, environments, and example responses for secrets and PII; review who has edit rights; and prefer Partner workspaces over Public when sharing with named third parties.

tools:
  - name: Postman
    url: https://www.postman.com/
    category: Platform
  - name: Postman API
    url: https://learning.postman.com/docs/developer/postman-api/intro-api/
    category: Management API
  - name: Postman CLI
    url: https://learning.postman.com/docs/postman-cli/postman-cli-overview/
    category: CLI
  - name: Newman
    url: https://github.com/postmanlabs/newman
    license: Apache-2.0
    category: Collection runner (consumes workspace artifacts)

metrics:
  - name: workspace_visibility
    description: Whether a workspace is private, team, partner, or public.
  - name: workspace_collection_count
    description: Number of collections in the workspace.
  - name: workspace_view_count
    description: Public-workspace view count, exposed via Postman analytics.
  - name: workspace_fork_count
    description: Number of times collections in the workspace have been forked.
  - name: workspace_last_activity_days
    description: Days since any artifact in the workspace was updated.

examples:
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Maintains a public Twilio workspace on the Postman API Network.
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Stripe Developers public workspace.
  - provider: Salesforce
    url: https://providers.apis.io/providers/salesforce/
    note: Salesforce Developers workspace.
  - provider: PayPal
    url: https://providers.apis.io/providers/paypal/
    note: PayPal public workspace on the Postman API Network.

related_properties:
  - postman-collection
  - openapi
---
