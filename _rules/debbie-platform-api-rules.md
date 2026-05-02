---
api_specs:
- filename: debbie-platform-api-openapi.yml
  format: yaml
  label: Debbie Platform API
  slug: debbie-platform-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/debbie-collect/refs/heads/main/openapi/debbie-platform-api-openapi.yml
- filename: debbie-client-api-openapi.yml
  format: yaml
  label: Debbie Client API
  slug: debbie-client-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/debbie-collect/refs/heads/main/openapi/debbie-client-api-openapi.yml
categories:
- debbie
description: Spectral linting rules defining API design standards and conventions for Debbie Collect.
layout: rules
name: Debbie Collect API Rules
provider_name: Debbie Collect
provider_slug: debbie-collect
rule_count: 5
rules:
- description: API info should include the Debbie API support contact.
  given: $.info
  name: debbie-info-contact
  severity: warn
- description: Servers should reference debbie.dk.
  given: $.servers[*].url
  name: debbie-base-url
  severity: warn
- description: API should declare bearer-token authentication.
  given: $.components.securitySchemes
  name: debbie-bearer-auth
  severity: error
- description: Operations should be tagged Cases, Creditors, Customers, Webhooks, etc.
  given: $.paths[*][*]
  name: debbie-operation-tags
  severity: warn
- description: API should expose /cases as a primary resource.
  given: $.paths
  name: debbie-case-resource-paths
  severity: warn
rules_file: rules/debbie-platform-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/debbie-collect/refs/heads/main/rules/debbie-platform-api-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 4
slug: debbie-platform-api-rules
source_filename: debbie-platform-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  debbie-info-contact:\n    description: API info should include the Debbie API support contact.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  debbie-base-url:\n    description: Servers should reference debbie.dk.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"debbie\\\\.dk\"\n  debbie-bearer-auth:\n    description: API should declare bearer-token authentication.\n    given: $.components.securitySchemes\n    severity: error\n    then:\n      field: bearerAuth\n      function: truthy\n  debbie-operation-tags:\n    description: Operations should be tagged Cases, Creditors, Customers, Webhooks, etc.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n  debbie-case-resource-paths:\n    description: API should expose /cases as a primary resource.\n    given: $.paths\n\
  \    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/cases\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/debbie-collect/refs/heads/main/rules/debbie-platform-api-rules.yml
tags:
- Accounts Receivable
- Collections
- Debt Collection
- FinTech
- Payments
- SaaS
- Spectral
- Linting
- API Governance
---
