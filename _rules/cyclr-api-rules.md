---
api_specs:
- filename: cyclr-cyclr-openapi.yml
  format: yaml
  label: Cyclr API
  slug: api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cyclr/refs/heads/main/openapi/cyclr-cyclr-openapi.yml
categories:
- cyclr
description: Spectral linting rules defining API design standards and conventions for Cyclr.
layout: rules
name: Cyclr API Rules
provider_name: Cyclr
provider_slug: cyclr
rule_count: 6
rules:
- description: Cyclr API spec must declare a contact.
  given: $.info
  name: cyclr-info-contact
  severity: warn
- description: Cyclr server URLs must use HTTPS.
  given: $.servers[*].url
  name: cyclr-server-https
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cyclr-tags-required
  severity: warn
- description: Every operation must declare an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cyclr-operation-id-required
  severity: error
- description: Cyclr uses bearer-token authentication.
  given: $.components.securitySchemes
  name: cyclr-bearer-auth
  severity: warn
- description: Cyclr base URL must include a version segment (/v1.0).
  given: $.servers[*].url
  name: cyclr-versioned-base-url
  severity: error
rules_file: rules/cyclr-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cyclr/refs/heads/main/rules/cyclr-api-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 3
slug: cyclr-api-rules
source_filename: cyclr-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  cyclr-info-contact:\n    description: Cyclr API spec must declare a contact.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  cyclr-server-https:\n    description: Cyclr server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  cyclr-tags-required:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  cyclr-operation-id-required:\n    description: Every operation must declare an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  cyclr-bearer-auth:\n    description: Cyclr uses bearer-token authentication.\n    severity: warn\n    given: $.components.securitySchemes\n\
  \    then:\n      field: bearerAuth\n      function: truthy\n  cyclr-versioned-base-url:\n    description: Cyclr base URL must include a version segment (/v1.0).\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '/v[0-9]+(\\.[0-9]+)?'\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cyclr/refs/heads/main/rules/cyclr-api-rules.yml
tags:
- Connectors
- Custom Connectors
- Data Synchronization
- Embedded iPaaS
- Embedded SaaS Integration
- Embedded UI
- Integration Platform
- Integrations
- Marketplace
- OAuth 2.0
- REST API
- SaaS
- Templates
- Webhooks
- White Label
- Workflows
- Spectral
- Linting
- API Governance
---
