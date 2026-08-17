---
name: Integrations
description: Providing ready to go integrations with other APIs has become commonplace as part of Software as a Service (SaaS) solutions, and help demonstrate the value an API provides. Demonstrating how an API can be used with the existing platforms that API consumers are already using help make your APIs more useful and sticky for developers.
image: /images/integrations.png
url: '#'
machineReadable: true
source: concept
tags:
  - Integrations
  - Interoperability 
aliases:
  - Connectors
  - Integration Catalog
  - Partner Integrations
yaml_example: |
  - name: Connectors
    type: Integrations
    url: https://example.com/connectors/
    source_date: '2026-08-17'
    count: 412
    data:
      - name: Salesforce
        url: https://example.com/connectors/salesforce/
        partner_domain: salesforce.com
        category: CRM
        kind: connector
        direction: bidirectional
        built_by: first-party
        status: ga
        auth: oauth2

standards:
  - name: API Commons Integrations schema
    url: https://github.com/api-commons/integrations
    kind: API Commons (Apache-2.0)
  - name: OpenAPI Specification 3.1
    url: https://spec.openapis.org/oas/v3.1.0
    kind: OpenAPI Initiative
  - name: AsyncAPI Specification
    url: https://www.asyncapi.com/docs/reference/specification/latest
    kind: AsyncAPI Initiative
  - name: RFC 6749 — OAuth 2.0 (scopes for partner access)
    url: https://www.rfc-editor.org/rfc/rfc6749
    kind: IETF
  - name: Standard Webhooks
    url: https://www.standardwebhooks.com/
    kind: Community standard
  - name: CloudEvents 1.0
    url: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md
    kind: CNCF
  - name: Arazzo Specification
    url: https://spec.openapis.org/arazzo/latest.html
    kind: OpenAPI Initiative

media_types:
  - type: application/json
    note: Catalog metadata and integration manifests.
  - type: application/yaml
    note: OpenAPI, AsyncAPI, and Arazzo descriptions backing integrations.
  - type: application/cloudevents+json
    note: CloudEvents structured-mode payloads for event-driven integrations.

openapi_expression:
  - field: servers
    spec: OpenAPI 3.x
    description: Distinct base URLs per integration environment (sandbox, partner, prod).
  - field: components.securitySchemes
    spec: OpenAPI 3.x
    description: OAuth 2.0 and API-key schemes consumed by integration platforms.
  - field: webhooks
    spec: OpenAPI 3.1
    description: Outbound webhook contracts exposed to integration partners.

governance_rules:
  - id: operation-operationId
    source: Spectral built-in
    description: Stable operationIds are required for generated connectors and iPaaS bindings.
  - id: oas-security-defined
    source: Spectral built-in
    description: Every operation must declare a security scheme partners can wire up.

risk:
  security_implications: Partner integrations multiply the attack surface; require least-privilege OAuth scopes, per-partner secrets, signed webhooks (Standard Webhooks), and revocable credentials. Document data-handling expectations for downstream platforms.
  governance: Unversioned integration manifests cause silent breakage across iPaaS catalogs. Treat connector metadata as a versioned artifact alongside the API description.

tools:
  - name: API Commons Integrations schema + validator
    url: https://github.com/api-commons/integrations
    license: Apache-2.0
    category: Machine-readable schema
  - name: Zapier developer platform
    url: https://platform.zapier.com/
    category: iPaaS
  - name: Make
    url: https://www.make.com/
    category: iPaaS
  - name: Pipedream
    url: https://pipedream.com/
    category: iPaaS / workflow
  - name: n8n
    url: https://n8n.io/
    license: Sustainable Use License
    category: Self-hostable workflow automation
  - name: OpenAPI Generator
    url: https://openapi-generator.tech/
    license: Apache-2.0
    category: Client / connector generation
  - name: Workato
    url: https://www.workato.com/
    category: Enterprise iPaaS

metrics:
  - name: active_integrations
    description: Count of active partner integrations in the catalog.
  - name: integration_install_count
    description: Number of times each integration is enabled by an end user.
  - name: webhook_delivery_success_rate
    description: Share of outbound webhook attempts acknowledged with 2xx.
  - name: partner_token_refresh_failures
    description: Failed OAuth refresh attempts per partner; indicates rotation problems.

examples:
  - provider: Zapier
    url: https://providers.apis.io/providers/zapier/
    note: Developer platform for building published Zapier integrations.
  - provider: Slack
    url: https://providers.apis.io/providers/slack/
    note: OAuth scopes and Events API webhooks consumed by integration platforms.
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Connect, webhooks, and the Stripe App platform power third-party integrations.
  - provider: HubSpot
    url: https://providers.apis.io/providers/hubspot/
    note: Marketplace apps and OAuth-scoped partner integrations.

related_properties:
  - openapi
  - asyncapi
  - webhooks
  - authentication
  - partners
  - sdks
---
