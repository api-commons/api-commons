---
name: GraphQL Schema
description: The GraphQL Schema is a machine readable collection of schema organized into a graph. The GraphQL Schema has emerged as a proven way to stitch together much of the API sprawl that has emerged behind the infrastructure, integrations, and applications that we depend on to do business today.
image: /images/graphql.png
url: https://graphql.org/learn/schema/
machineReadable: true
source: community
tags:
  - Machine-Readable
  - Schema
  - Graph
aliases:
  - GraphQL SDL
  - Schema Definition Language
  - GraphQL IDL

standards:
  - name: GraphQL Specification (October 2021)
    url: https://spec.graphql.org/October2021/
    kind: GraphQL Foundation (Linux Foundation)
  - name: GraphQL over HTTP
    url: https://graphql.github.io/graphql-over-http/draft/
    kind: GraphQL Foundation (draft)
  - name: GraphQL Federation v2
    url: https://www.apollographql.com/docs/federation/
    kind: Apollo (de facto)
  - name: Relay Cursor Connections Specification
    url: https://relay.dev/graphql/connections.htm
    kind: Meta (de facto)
  - name: GraphQL Scalars
    url: https://the-guild.dev/graphql/scalars
    kind: Community

media_types:
  - type: application/graphql-response+json
    spec: GraphQL over HTTP
    note: Response media type for GraphQL responses.
  - type: application/json
    note: Widely accepted request and response media type.
  - type: application/graphql
    note: De facto request media type for raw GraphQL query strings (not IANA-registered).

headers:
  - name: Content-Type
    direction: request
    spec: GraphQL over HTTP
    description: application/json for the JSON request form; application/graphql for raw query bodies.
  - name: Accept
    direction: request
    spec: GraphQL over HTTP
    description: Should include application/graphql-response+json to opt into the strict response semantics.

status_codes:
  - code: '200'
    name: OK
    spec: GraphQL over HTTP
    description: Default status — GraphQL surfaces field-level errors in the response body, not as HTTP errors, when using application/json.
  - code: '400'
    name: Bad Request
    spec: GraphQL over HTTP
    description: Returned for request-document errors under application/graphql-response+json.

openapi_expression:
  - field: n/a
    spec: GraphQL
    description: GraphQL does not use OpenAPI; the schema itself (SDL or introspection result) is the contract.

governance_rules:
  - id: graphql-eslint/naming-convention
    source: graphql-eslint
    description: Enforce naming conventions across types, fields, enums.
  - id: graphql-eslint/no-deprecated
    source: graphql-eslint
    description: Disallow use of deprecated fields/enums in operations.
  - id: graphql-eslint/require-description
    source: graphql-eslint
    description: Types and fields should carry descriptions.
  - id: graphql-inspector breaking-changes
    source: GraphQL Inspector
    description: Block PRs that introduce schema-breaking changes.

risk:
  owasp:
    - 'OWASP API Security Top 10: API4:2023 Unrestricted Resource Consumption — unbounded queries / depth / aliases'
    - 'OWASP API Security Top 10: API1:2023 Broken Object Level Authorization — resolver-level auth bugs'
    - 'OWASP API Security Top 10: API3:2023 Broken Object Property Level Authorization — over-fetching via field selection'
  compliance:
    - SOC 2 CC6.1 — per-field authorization decisions must be auditable
    - GDPR Art. 5(1)(c) — selection-based access enables data minimization when enforced
  security_implications: GraphQL collapses many endpoints into one — depth limits, complexity analysis, persisted queries, disabled introspection in production, and per-resolver authorization are required. Treat introspection as sensitive.

tools:
  - name: GraphiQL
    url: https://github.com/graphql/graphiql
    license: MIT
    category: IDE / Explorer
  - name: Apollo Studio / Rover
    url: https://www.apollographql.com/docs/rover/
    category: Schema registry / CLI
  - name: GraphQL Inspector
    url: https://the-guild.dev/graphql/inspector
    license: MIT
    category: Diff / governance
  - name: graphql-eslint
    url: https://the-guild.dev/graphql/eslint
    license: MIT
    category: Linter
  - name: GraphQL Code Generator
    url: https://the-guild.dev/graphql/codegen
    license: MIT
    category: Codegen
  - name: Hasura
    url: https://hasura.io/
    category: GraphQL engine

metrics:
  - name: graphql_query_depth_p95
    description: 95th-percentile depth of executed queries.
  - name: graphql_query_complexity_p95
    description: 95th-percentile complexity score of executed queries.
  - name: graphql_field_usage
    description: Per-field call counts; drives deprecation decisions.
  - name: graphql_error_rate
    description: Share of responses that include an errors array.
  - name: persisted_query_ratio
    description: Share of traffic served via persisted queries vs ad-hoc.

examples:
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Publishes a public GraphQL API alongside REST.
  - provider: Shopify
    url: https://providers.apis.io/providers/shopify/
    note: Admin API is GraphQL-first.
  - provider: Contentful
    url: https://providers.apis.io/providers/contentful/
    note: Content Delivery API offered via GraphQL.

related_properties:
  - openapi
  - json-schema
  - webhooks
---
