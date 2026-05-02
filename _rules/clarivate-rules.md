---
categories:
- clarivate
description: Spectral linting rules defining API design standards and conventions for Clarivate.
layout: rules
name: Clarivate API Rules
provider_name: Clarivate
provider_slug: clarivate
rule_count: 6
rules:
- description: API info MUST contain a contact email or URL.
  given: $.info
  name: clarivate-info-contact
  severity: warn
- description: All Clarivate API servers MUST use HTTPS.
  given: $.servers[*].url
  name: clarivate-https-only
  severity: error
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: clarivate-operation-id
  severity: error
- description: Operations MUST be tagged for product domain grouping.
  given: $.paths[*][get,post,put,delete,patch].tags
  name: clarivate-tag-required
  severity: warn
- description: API MUST define API key security schemes.
  given: $.components.securitySchemes
  name: clarivate-security-required
  severity: error
- description: API MUST declare at least one server URL.
  given: $.servers
  name: clarivate-server-url
  severity: error
rules_file: rules/clarivate-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/clarivate/refs/heads/main/rules/clarivate-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 2
slug: clarivate-rules
source_filename: clarivate-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  clarivate-info-contact:\n    description: API info MUST contain a contact email or URL.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  clarivate-https-only:\n    description: All Clarivate API servers MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  clarivate-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  clarivate-tag-required:\n    description: Operations MUST be tagged for product domain grouping.\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n    then:\n      function: truthy\n  clarivate-security-required:\n    description: API MUST define API key security schemes.\n    severity: error\n    given:\
  \ $.components.securitySchemes\n    then:\n      function: truthy\n  clarivate-server-url:\n    description: API MUST declare at least one server URL.\n    severity: error\n    given: $.servers\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/clarivate/refs/heads/main/rules/clarivate-rules.yml
tags:
- Analytics
- Citations
- Data
- Drug Pipeline
- Insights
- Intellectual Property
- Life Sciences
- Patents
- Publications
- Research
- Spectral
- Linting
- API Governance
---
