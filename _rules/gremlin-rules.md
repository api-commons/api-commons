---
api_specs:
- filename: gremlin-openapi.yml
  format: yaml
  label: Gremlin API
  slug: gremlin-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gremlin/refs/heads/main/openapi/gremlin-openapi.yml
categories:
- gremlin
description: Spectral linting rules defining API design standards and conventions for Gremlin.
layout: rules
name: Gremlin API Rules
provider_name: Gremlin
provider_slug: gremlin
rule_count: 4
rules:
- description: Gremlin API spec must declare a contact.
  given: $.info
  name: gremlin-info-contact-required
  severity: warn
- description: All Gremlin servers must use HTTPS.
  given: $.servers[*].url
  name: gremlin-server-https-only
  severity: error
- description: Each Gremlin operation must declare at least one tag.
  given: $.paths[*][get,post,put,delete,patch]
  name: gremlin-operation-tag-required
  severity: warn
- description: Each operation should have a human-readable summary.
  given: $.paths[*][get,post,put,delete,patch]
  name: gremlin-operation-summary-required
  severity: warn
rules_file: rules/gremlin-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/gremlin/refs/heads/main/rules/gremlin-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 3
slug: gremlin-rules
source_filename: gremlin-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  gremlin-info-contact-required:\n    description: Gremlin API spec must declare a contact.\n    message: info.contact is required\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  gremlin-server-https-only:\n    description: All Gremlin servers must use HTTPS.\n    message: Server URL must use https://\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: ^https://\n  gremlin-operation-tag-required:\n    description: Each Gremlin operation must declare at least one tag.\n    given: $.paths[*][get,post,put,delete,patch]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n  gremlin-operation-summary-required:\n    description: Each operation should have a human-readable summary.\n    given: $.paths[*][get,post,put,delete,patch]\n    severity: warn\n    then:\n      field: summary\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/gremlin/refs/heads/main/rules/gremlin-rules.yml
tags:
- Chaos Engineering
- Fault Injection
- Infrastructure Testing
- Reliability
- Site Reliability Engineering
- Spectral
- Linting
- API Governance
---
