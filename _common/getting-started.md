---
name: Getting Started
description: Providing the basic steps of how an API consumer can get started using an API with as few steps as possible is essential for any API. Like other common properties, a getting started isn't just for API consumers to understand how to onboard, and it is about pushing API producers to simply and reduce friction when it comes to onboarding.
image: /images/getting-started.png
machineReadable: true
source: commons
url: '#'
tags:
  - Onboarding
  - Authentication
  - Documentation
aliases:
  - Quickstart
  - Quick Start
  - Onboarding
  - First Call
yaml_example: |
  - type: GettingStarted
    url: https://developers.example.com/getting-started

standards:
  - name: OpenAPI Specification 3.1
    url: https://spec.openapis.org/oas/v3.1.0
    kind: OpenAPI Initiative
  - name: Schema.org HowTo
    url: https://schema.org/HowTo
    kind: Schema.org
  - name: Postman Collection Format v2.1
    url: https://schema.postman.com/json/collection/v2.1.0/collection.json
    kind: Postman
  - name: CommonMark 0.31
    url: https://spec.commonmark.org/0.31.2/
    kind: CommonMark
  - name: cURL
    url: https://curl.se/docs/manpage.html
    kind: De facto
  - name: HTTPie
    url: https://httpie.io/docs/cli
    kind: De facto

openapi_expression:
  - field: servers
    spec: OpenAPI 3.x
    description: Base URLs used in the first-call example.
  - field: components.securitySchemes
    spec: OpenAPI 3.x
    description: Auth mechanism the quickstart walks through.
  - field: components.examples
    spec: OpenAPI 3.x
  - field: paths.*.*.requestBody.content.*.example
    spec: OpenAPI 3.x
    description: Inline request example used in walkthroughs.
  - field: paths.*.*.responses.*.content.*.example
    spec: OpenAPI 3.x
  - field: x-codeSamples
    spec: Redoc / Redocly vendor extension
    description: Per-operation curl/SDK samples rendered alongside the reference.

governance_rules:
  - id: operation-success-response
    source: Spectral built-in
    description: Operations must define a successful response so quickstarts can show a meaningful body.
  - id: oas3-valid-media-example
    source: Spectral built-in
    description: Inline examples must validate against their schema.
  - id: oas3-server-not-example.com
    source: Spectral built-in
    description: Quickstarts need a real, callable base URL.
  - id: info-contact
    source: Spectral built-in
    description: Quickstart pages typically link to `info.contact` for help.

risk:
  security_implications: Quickstarts frequently leak credentials when contributors paste live tokens into examples; prefer placeholders and key-redaction tooling. "Curl in 30 seconds" flows that skip TLS verification or hard-code admin scopes train consumers into insecure habits.
  compliance:
    - Accessibility (WCAG 2.2) — onboarding flows are a first-impression surface
    - Terms-of-Service acceptance must be explicit before issuing keys

tools:
  - name: Postman
    url: https://www.postman.com/
    category: Collections and Run-in-Postman
  - name: Insomnia
    url: https://insomnia.rest/
    category: API client
  - name: Hoppscotch
    url: https://hoppscotch.io/
    license: MIT
    category: API client
  - name: HTTPie
    url: https://httpie.io/
    license: BSD-3-Clause
    category: CLI client
  - name: curl
    url: https://curl.se/
    license: curl
    category: CLI client
  - name: Bruno
    url: https://www.usebruno.com/
    license: MIT
    category: API client

metrics:
  - name: time_to_first_hello_world
    description: Median time from signup to first successful 2xx response (TTFHW).
  - name: signup_to_first_call_funnel
    description: Stepwise conversion across signup, key creation, and first authenticated call.
  - name: quickstart_completion_rate
    description: Fraction of new accounts that finish the documented quickstart steps.
  - name: copy_button_click_rate
    description: Engagement with copyable curl / SDK snippets on the quickstart page.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Test-mode keys preloaded into curl/SDK samples so a first charge works without signup friction.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Send-an-SMS-in-five-minutes quickstart across multiple language tabs.
  - provider: OpenAI
    url: https://providers.apis.io/providers/openai/
    note: API key creation, environment variable, first completion in three steps.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Personal access token plus curl call to /user as a canonical first request.

related_properties:
  - authentication
  - documentation
  - signup
  - software-development-kits
  - code-samples
---
