---
api_specs:
- filename: handwrite-io-openapi.yml
  format: yaml
  label: Handwrite IO API
  slug: handwrite-io
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/handwrite-io/refs/heads/main/openapi/handwrite-io-openapi.yml
categories: []
description: Spectral linting rules defining API design standards and conventions for Handwrite IO.
layout: rules
name: Handwrite IO API Rules
provider_name: Handwrite IO
provider_slug: handwrite-io
rule_count: 0
rules: []
rules_file: rules/handwrite-io-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/handwrite-io/refs/heads/main/rules/handwrite-io-rules.yml
severity_counts:
  error: 0
  hint: 0
  info: 0
  warn: 0
slug: handwrite-io-rules
source_filename: handwrite-io-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  operation-tags: warn\n  operation-description: warn\n  operation-operationId: error\n  info-contact: warn\n  info-description: error\n  no-$ref-siblings: error\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/handwrite-io/refs/heads/main/rules/handwrite-io-rules.yml
tags:
- Direct Mail
- Handwritten
- Marketing
- Notes
- Spectral
- Linting
- API Governance
---
