---
name: Naftiko Capability
description: "A NaftikoCapability property references a Naftiko capability YAML specification — a single declarative file that defines what APIs are consumed upstream, what surfaces are exposed (REST, MCP, Agent Skills), and what governance, identity, and telemetry rules apply. Capability specs are the deployable unit of the Naftiko platform: each one is validated by JSON Schema, committed to Git, and serves as both the implementation artifact and the governance contract. Publishing a capability spec makes it possible for AI agents, orchestration tools, and developer portals to discover and invoke governed API capabilities without direct knowledge of the underlying provider APIs."
image: /images/schema.png
url: #
tags:
  - Naftiko
  - Capability
  - AI
  - Governance
yaml_example: |
  - type: NaftikoCapability
    url: https://developers.example.com/naftiko/capability.yaml
    mediaType: application/yaml
---
