---
name: Postman Collections
description: A Postman Collection is a machine-readable collection of APIs for use in client, testing, and automation. Postman Collections provides a portable, machine-readable way of defining an API and making available for consumers via a Postman workspace or embedded via documentation and other websites. Collections bundle documentation, can be mocked, and work with the wider Postman platform ecosystem.
image: /images/postman.png
url: https://www.postman.com/collection/
machineReadable: true
source: platform
tags:
  - Machine-Readable
  - Client
  - Testing
  - Automation
aliases:
  - Postman Collection
  - PMC
  - Collection v2.1

standards:
  - name: Postman Collection Format v2.1.0
    url: https://schema.postman.com/json/collection/v2.1.0/collection.json
    kind: Postman (de facto)
  - name: Postman Collection Format v2.0.0
    url: https://schema.postman.com/json/collection/v2.0.0/collection.json
    kind: Postman (de facto)
  - name: Postman API
    url: https://learning.postman.com/docs/developer/postman-api/intro-api/
    kind: Postman (vendor)
  - name: OpenAPI 3.x (importable to/from collections)
    url: https://spec.openapis.org/oas/v3.1.0
    kind: OpenAPI Initiative
  - name: Bruno Collection Format (alternative, .bru files)
    url: https://docs.usebruno.com/bru-lang/overview
    kind: Bruno (de facto)
  - name: Insomnia Export Format (alternative)
    url: https://docs.insomnia.rest/insomnia/import-export-data
    kind: Kong / Insomnia (de facto)

media_types:
  - type: application/json
    note: Postman Collections are distributed as JSON conforming to the v2.1 schema.

openapi_expression:
  - field: n/a
    spec: Postman Collection
    description: Collections are not OpenAPI, but Postman can import/export between OpenAPI 3.x and Collection v2.1.

governance_rules:
  - id: collection-schema-valid
    source: Postman / Newman
    description: Collection must validate against the v2.1.0 JSON Schema.
  - id: collection-has-tests
    source: Convention
    description: Every request should include at least one test script.
  - id: collection-no-hardcoded-secrets
    source: Convention
    description: Use environment / vault variables instead of hardcoded tokens.
  - id: collection-uses-variables
    source: Convention
    description: Base URLs and IDs should be variables, not literals.

risk:
  owasp:
    - 'OWASP API Security Top 10: API8:2023 Security Misconfiguration — exported collections often contain secrets'
    - 'OWASP API Security Top 10: API2:2023 Broken Authentication — bearer tokens checked into shared collections'
  compliance:
    - SOC 2 CC6.1 — shared collections are an access-control surface
    - PCI DSS v4 Req. 3 — avoid storing cardholder data in example bodies
  security_implications: Collections are frequently shared via public workspaces and Git — scan exports for secrets, store credentials in Postman Vault or environments marked private, and rotate any token that lands in a committed collection. Treat public workspace publishing as a release event.

tools:
  - name: Postman
    url: https://www.postman.com/
    category: Client / platform
  - name: Newman
    url: https://github.com/postmanlabs/newman
    license: Apache-2.0
    category: CLI runner
  - name: Bruno
    url: https://www.usebruno.com/
    license: MIT
    category: Open-source client (alt format)
  - name: Insomnia
    url: https://insomnia.rest/
    license: MIT (core)
    category: Open-source client
  - name: portman
    url: https://github.com/apideck-libraries/portman
    license: MIT
    category: OpenAPI-to-collection generator
  - name: openapi-to-postmanv2
    url: https://github.com/postmanlabs/openapi-to-postman
    license: Apache-2.0
    category: OpenAPI-to-collection converter

metrics:
  - name: collection_test_coverage
    description: Share of requests in a collection that have test scripts.
  - name: newman_pass_rate
    description: Share of requests passing in a CI run.
  - name: collection_freshness_days
    description: Days since the collection was last updated.
  - name: collection_secret_leaks
    description: Count of secrets detected by scanning the exported JSON.

examples:
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Publishes official Postman Collections on the Postman API Network.
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Maintains a Stripe workspace with collections per product.
  - provider: Salesforce
    url: https://providers.apis.io/providers/salesforce/
    note: Publishes Salesforce Developers workspace with multiple collections.
  - provider: PayPal
    url: https://providers.apis.io/providers/paypal/
    note: Publishes Postman Collections via the API Network.

related_properties:
  - openapi
  - postman-workspace
  - json-schema
---
