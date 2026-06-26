---
name: Spectral Rules
description: A Spectral ruleset that governs how an API's OpenAPI or AsyncAPI definition is linted — publishing it makes the provider's design and governance standards discoverable and lets consumers see the quality bar the API is held to.
image: /images/rulesets.png
url: '#'
machineReadable: true
source: rules
tags:
  - Spectral
  - Governance
  - Linting
aliases:
  - Spectral Rules
  - SpectralRuleset
  - Spectral Ruleset
yaml_example: |
  - type: SpectralRules
    url: https://developers.example.com/.spectral.yaml
    mediaType: application/yaml
---
