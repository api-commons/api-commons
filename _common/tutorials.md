---
name: Tutorials
description: Step-by-step learning content that walks a consumer from zero to a working integration around a specific use case. Tutorials sit between the bare quickstart (one-call hello world) and the full reference (everything you could call); their job is to teach how the pieces compose. A healthy tutorials surface covers the canonical workflows for the API and is the second-most-visited area of a portal after the reference.
image: /images/tutorials.png
url: '#'
machineReadable: false
source: commons
tags:
  - Onboarding
  - Documentation
  - Learning
aliases:
  - Tutorial
  - Guides
  - Learning
  - Walkthroughs
  - How-To
yaml_example: |
  - type: Tutorials
    url: https://developers.example.com/tutorials

standards:
  - name: schema.org HowTo
    url: https://schema.org/HowTo
    kind: Schema.org
  - name: schema.org LearningResource
    url: https://schema.org/LearningResource
    kind: Schema.org
  - name: schema.org Course
    url: https://schema.org/Course
    kind: Schema.org
  - name: CommonMark 0.31
    url: https://spec.commonmark.org/0.31.2/
    kind: CommonMark
  - name: Arazzo Specification 1.0.1
    url: https://spec.openapis.org/arazzo/v1.0.1
    kind: OpenAPI Initiative

openapi_expression:
  - field: x-codeSamples
    spec: Redoc / Redocly vendor extension
    description: Per-operation code samples are often lifted directly from tutorial content.
  - field: tags[].externalDocs
    spec: OpenAPI 3.x
    description: Tutorial sets are commonly linked from per-tag external docs.

risk:
  security_implications: Tutorials are read and copied far more than reference docs; an insecure pattern in a tutorial (skipped TLS verification, hardcoded admin tokens, weak input handling) propagates into production code at scale. Treat tutorials as production-quality code and lint them with the same governance rules as samples.

tools:
  - name: MDX
    url: https://mdxjs.com/
    license: MIT
    category: Markdown with interactive components for tutorials
  - name: Docusaurus
    url: https://docusaurus.io/
    license: MIT
    category: Docs site with tutorial layouts
  - name: Jupyter Book
    url: https://jupyterbook.org/
    license: BSD-3-Clause
    category: Executable-notebook tutorials
  - name: Arazzo
    url: https://spec.openapis.org/arazzo/v1.0.1
    category: Machine-readable workflow descriptions that pair with tutorials

metrics:
  - name: tutorial_completion_rate
    description: Share of readers who reach the final step of a tutorial.
  - name: tutorial_to_first_call
    description: Time from opening a tutorial to making the first real API call.
  - name: tutorial_freshness_days
    description: Days since each tutorial was last validated against the live API.
  - name: copy_button_click_rate
    description: Engagement with copyable snippets — a proxy for tutorial usefulness.

examples:
  - provider: Twilio
    url: https://www.twilio.com/docs/tutorials
    note: Long-running tutorial library covering messaging, voice, and video flows.
  - provider: Stripe
    url: https://stripe.com/docs/payments/quickstart
    note: Use-case tutorials per payment method and integration pattern.
  - provider: GitHub
    url: https://docs.github.com/en/get-started/quickstart
    note: Multi-step guides covering common platform workflows.

related_properties:
  - documentation
  - getting-started
  - code-samples
  - software-development-kits
---
