---
name: Unified Intent Mediator
description: A reference to a provider's Unified Intent Mediator (UIM) surface — an early-stage protocol proposal for standardizing how AI agents discover, negotiate, and execute intents against web services, rather than driving raw endpoints. UIM's contribution is that it treats the intent as the unit of interaction and pairs it with a policy layer covering permissions and compensation. It is a proposal, not an adopted standard — the specification is published openly under Apache-2.0 but has no ratifying body and no known production adopters, so record it as an experiment alongside Model Context Protocol rather than as a peer of it.
image: /images/intents.png
url: '#'
machineReadable: false
source: ai
tags:
  - UIM
  - AI
  - Agents
  - Intents
  - Proposal
aliases:
  - UIM
  - UIM Protocol
  - Unified Intent Mediator Protocol
yaml_example: |
  - type: UnifiedIntentMediator
    url: https://developers.example.com/uim

standards:
  - name: UIM Protocol specification
    url: https://synaptiai.github.io/uim-protocol/
    kind: Open proposal (Apache-2.0, no standards body)
  - name: UIM Protocol repository
    url: https://github.com/synaptiai/uim-protocol
    kind: Open proposal (source of record)
  - name: Model Context Protocol
    url: https://modelcontextprotocol.io/
    kind: Anthropic / open specification
  - name: Agent2Agent (A2A) Protocol
    url: https://a2a-protocol.org/
    kind: Linux Foundation
  - name: llms.txt
    url: https://llmstxt.org/
    kind: Community convention
  - name: AGENTS.md
    url: https://agents.md/
    kind: Community convention
  - name: OpenAPI Specification
    url: https://spec.openapis.org/oas/latest.html
    kind: OpenAPI Initiative

openapi_expression:
  - field: operationId
    spec: OpenAPI 3.x
    description: Stable operationIds are what any intent layer binds to; unstable ones break the mapping silently.
  - field: tags
    spec: OpenAPI 3.x
    description: Tag groupings are the usual starting point for deriving candidate intents from an existing API.
  - field: components.securitySchemes
    spec: OpenAPI 3.x
    description: The permission layer an intent protocol has to delegate to rather than replace.

risk:
  security_implications: >-
    Any intent-mediation layer moves authorization decisions away from the endpoint and toward a broker, which widens
    the blast radius of a misconfigured policy — an over-broad intent can compose several individually-safe operations
    into one unsafe action. UIM specifically proposes a policy and compensation layer, which means it also carries
    machine-negotiated commercial terms; treat those as an untrusted input path. Because the protocol is pre-adoption
    with no conformance suite, do not depend on it for access control. Keep enforcement at the API, scope agent
    credentials narrowly, and log intent execution against the underlying operations it resolved to.

metrics:
  - name: intents_declared
    description: Count of intents a provider publishes.
  - name: intent_to_operation_coverage
    description: Share of API operations reachable through a declared intent.
  - name: intent_resolution_success_rate
    description: Fraction of agent intent requests that resolve to an executable operation.

related_properties:
  - model-context-protocol
  - agent-skills
  - agent-prompt
  - llms-txt
  - openapi
  - authentication
---
