---
name: Use Case
description: . A use case corresponds to a set of resources and capabilities that API should perform in interaction with its consumers, and which produces an observable result that contributes with the goals of each individual API operation. Use cases define the business requirements which can be regularly aligned with the operational technical requirements defined as an OpenAPI.
image: /images/use-case.png
url: '#'
machineReadable: false
source: concept
tags:
  - Use Case
  - Business
  - Requirements
aliases:
  - Scenario
  - Job to be Done
  - JTBD
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
    description: Group operations by use case for navigation and discovery.
  - field: x-use-case
    spec: Vendor extension
    description: Links an operation or tag to a documented use case.
  - field: components.examples
    spec: OpenAPI 3.x
    description: Concrete request/response examples that illustrate a use case end-to-end.

governance_rules:
  - id: operation-description
    source: Spectral built-in (spectral:oas)
    description: Each operation needs a description, which is where use-case context belongs.
  - id: oas-tag-description
    source: Spectral built-in
    description: Tags representing use cases must include a description.

risk:
  governance: Without documented use cases the API surface is hard to prioritize, deprecate, or version; product and engineering optimize different targets.

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
  - name: Stoplight Studio
    url: https://stoplight.io/studio
    category: Use-case-driven API design

metrics:
  - name: use_cases_documented
    description: Count of use cases linked to operations in the description.
  - name: operations_without_use_case
    description: Operations not associated with any documented use case.
  - name: example_coverage_percent
    description: Share of operations that include at least one request/response example.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Use-case-led documentation (accept a payment, save a card, run a subscription).
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Quickstarts and tutorials organized around communication use cases.
  - provider: Postman
    url: https://providers.apis.io/providers/postman/
    note: Collections represent named, runnable use cases against an API.

related_properties:
  - use-cases
  - openapi
  - examples
  - tests
  - personas
---
