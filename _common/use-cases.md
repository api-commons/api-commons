---
name: Use Cases
description: Providing the who, what, how, and why of an API, establishing details about who the intended consumer is, while also linking use cases to specific operations to help align the business and technical details of an API.
image: /images/use-cases.png
url: '#'
machineReadable: false
source: concept
tags:
  - Use Cases 
  - Business
  - Alignment
aliases:
  - Scenarios
  - Recipes
  - Tutorials
yaml_example: |
  - type: UseCases
    url: https://developers.example.com/use-cases

standards:
  - name: OpenAPI Specification 3.1
    url: https://spec.openapis.org/oas/v3.1.0
    kind: OpenAPI Initiative
  - name: Arazzo Specification (workflow descriptions)
    url: https://spec.openapis.org/arazzo/latest.html
    kind: OpenAPI Initiative
  - name: AsyncAPI Specification
    url: https://www.asyncapi.com/docs/reference/specification/latest
    kind: AsyncAPI Initiative
  - name: schema.org HowTo
    url: https://schema.org/HowTo
    kind: schema.org
  - name: Postman Collection v2.1
    url: https://schema.postman.com/collection/json/v2.1.0/draft-07/collection.json
    kind: Postman
  - name: Bruno Collections
    url: https://docs.usebruno.com/
    kind: Bruno

media_types:
  - type: application/json
    note: Postman, Bruno, and Arazzo workflow documents.
  - type: application/yaml
    note: OpenAPI and Arazzo workflow authoring format.

openapi_expression:
  - field: tags
    spec: OpenAPI 3.x
    description: Group operations by audience or use case so documentation reflects intent.
  - field: x-use-cases
    spec: Vendor extension
    description: Catalog of use cases each referencing one or more operations.
  - field: components.examples
    spec: OpenAPI 3.x
    description: Worked examples illustrate end-to-end use cases.

governance_rules:
  - id: operation-description
    source: Spectral built-in (spectral:oas)
    description: Every operation requires a description anchoring it to a use case.
  - id: oas-tag-description
    source: Spectral built-in
    description: Tags that represent use cases must include descriptions.
  - id: operation-tag-defined
    source: Spectral built-in
    description: Use-case tags must be declared in the global tags array.

risk:
  governance: Operations not linked to a use case are candidates for deprecation but also for surprise breakage; align lifecycle decisions to the use-case catalog.

tools:
  - name: Postman
    url: https://www.postman.com/
    category: Collections and runnable scenarios
  - name: Bruno
    url: https://www.usebruno.com/
    license: MIT
    category: Git-friendly API collections
  - name: Arazzo Specification project
    url: https://github.com/OAI/Arazzo-Specification
    license: Apache-2.0
    category: Workflow modeling
  - name: Redocly
    url: https://redocly.com/
    category: Use-case-grouped reference docs (x-tagGroups)
  - name: Stoplight Elements
    url: https://stoplight.io/open-source/elements
    license: Apache-2.0
    category: Use-case-driven documentation rendering

metrics:
  - name: use_case_coverage_percent
    description: Share of operations linked to at least one documented use case.
  - name: top_use_case_traffic_share
    description: Share of total API traffic explained by the top N use cases.
  - name: tutorial_completion_rate
    description: Share of developers who finish a use-case tutorial after starting it.
  - name: time_to_first_use_case
    description: Median time from signup to a developer completing the first canonical use case.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Recipes and workflow guides organized by commerce use case.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Use Cases section frames products around customer scenarios.
  - provider: Slack
    url: https://providers.apis.io/providers/slack/
    note: Tutorials and sample apps organized by integration use case.
  - provider: Postman
    url: https://providers.apis.io/providers/postman/
    note: Public collections represent shareable, runnable use cases.

related_properties:
  - use-case
  - openapi
  - examples
  - tests
  - personas
  - integrations
---
