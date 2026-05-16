---
name: Naftiko Capability
description: "A NaftikoCapability property references a Naftiko capability YAML specification — a single declarative file that defines what APIs are consumed upstream, what surfaces are exposed (REST, MCP, Agent Skills), and what governance, identity, and telemetry rules apply. Capability specs are the deployable unit of the Naftiko platform: each one is validated by JSON Schema, committed to Git, and serves as both the implementation artifact and the governance contract. Publishing a capability spec makes it possible for AI agents, orchestration tools, and developer portals to discover and invoke governed API capabilities without direct knowledge of the underlying provider APIs."
image: /images/schema.png
url: '#'
tags:
  - Naftiko
  - Capability
  - AI
  - Governance
aliases:
  - Capability Spec
  - Naftiko Capability YAML
yaml_example: |
  - type: NaftikoCapability
    url: https://developers.example.com/naftiko/capability.yaml
    mediaType: application/yaml

standards:
  - name: Naftiko Framework
    url: https://github.com/naftiko/framework
    kind: apis.io project (community)
  - name: Naftiko Sandbox
    url: https://github.com/naftiko
    kind: apis.io project (community)
  - name: JSON Schema 2020-12
    url: https://json-schema.org/specification
    kind: IETF (draft) / JSON Schema Org
  - name: OpenAPI Specification 3.x
    url: https://spec.openapis.org/oas/v3.1.0
    kind: OpenAPI Initiative / Linux Foundation
  - name: Model Context Protocol (MCP)
    url: https://modelcontextprotocol.io/
    kind: Anthropic / community
  - name: AsyncAPI 3.x
    url: https://www.asyncapi.com/docs/reference
    kind: AsyncAPI Initiative / Linux Foundation

media_types:
  - type: application/yaml
    note: Canonical Naftiko capability serialization.
  - type: application/json
    note: Equivalent JSON form for tooling and validation.

governance_rules:
  - id: capability-schema-valid
    source: Naftiko JSON Schema
    description: Capability YAML must validate against the published Naftiko schema.
  - id: capability-upstream-declared
    source: Naftiko Framework
    description: Upstream APIs consumed must be enumerated with identity and scope.
  - id: capability-surfaces-declared
    source: Naftiko Framework
    description: Exposed surfaces (REST, MCP, Agent Skills) must be declared explicitly.
  - id: capability-identity-bound
    source: Naftiko Framework
    description: An identity or credential reference must be bound to each upstream call.

risk:
  security_implications: Capability specs concentrate routing, identity, and policy in one artifact — treat them as production configuration. Store secrets via references (vault, env, OIDC federation), never inline. Review schema-validated diffs in PRs and require approvals before deploy. Provenance of the framework is the Naftiko project itself (a community apis.io-adjacent effort), not an industry standards body — adopt with that maturity in mind.

tools:
  - name: Naftiko Framework
    url: https://github.com/naftiko/framework
    category: Capability runtime
  - name: Naftiko Sandbox
    url: https://github.com/naftiko
    category: Local development / examples
  - name: JSON Schema validators (ajv, jsonschema)
    url: https://json-schema.org/implementations
    category: Spec validation
  - name: Spectral
    url: https://stoplight.io/open-source/spectral
    license: Apache-2.0
    category: Linting OpenAPI references inside capabilities
  - name: MCP SDKs
    url: https://modelcontextprotocol.io/
    category: Surface bridging
  - name: Git
    url: https://git-scm.com/
    license: GPL-2.0
    category: Capability source of truth

metrics:
  - name: capability_count
    description: Capability YAML files under management.
  - name: schema_validation_failures
    description: Validation errors caught in CI before merge.
  - name: upstream_apis_per_capability
    description: Distribution of upstream dependencies per capability.
  - name: surface_invocations_total
    description: Calls served per exposed surface (REST / MCP / Agent Skill).

examples:
  - provider: Naftiko
    url: https://github.com/naftiko/framework
    note: Canonical framework, schema, and example capabilities.

related_properties:
  - openapi
  - asyncapi
  - schema
  - mcp
  - agent-skills
---
