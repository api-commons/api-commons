---
api_specs:
- filename: cycloid-api-openapi.yml
  format: yaml
  label: Cycloid HTTP API
  slug: http-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cycloid/refs/heads/main/openapi/cycloid-api-openapi.yml
categories:
- cycloid
description: Spectral linting rules defining API design standards and conventions for Cycloid.
layout: rules
name: Cycloid API Rules
provider_name: Cycloid
provider_slug: cycloid
rule_count: 6
rules:
- description: Cycloid API spec must declare a contact.
  given: $.info
  name: cycloid-info-contact
  severity: warn
- description: Cycloid server URLs must use HTTPS.
  given: $.servers[*].url
  name: cycloid-server-https
  severity: error
- description: Cycloid base URL must be http-api.cycloid.io.
  given: $.servers[*].url
  name: cycloid-base-url
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cycloid-tags-required
  severity: warn
- description: Every operation must declare an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cycloid-operation-id-required
  severity: error
- description: Resource paths must be scoped under /organizations/{organization_canonical}.
  given: $.paths
  name: cycloid-organization-scoped
  severity: warn
rules_file: rules/cycloid-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cycloid/refs/heads/main/rules/cycloid-api-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 3
slug: cycloid-api-rules
source_filename: cycloid-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  cycloid-info-contact:\n    description: Cycloid API spec must declare a contact.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  cycloid-server-https:\n    description: Cycloid server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  cycloid-base-url:\n    description: Cycloid base URL must be http-api.cycloid.io.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://http-api\\.cycloid\\.io'\n  cycloid-tags-required:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  cycloid-operation-id-required:\n    description: Every operation must declare an operationId.\n \
  \   severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  cycloid-organization-scoped:\n    description: Resource paths must be scoped under /organizations/{organization_canonical}.\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        match: 'organizations/\\{organization_canonical\\}'\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cycloid/refs/heads/main/rules/cycloid-api-rules.yml
tags:
- Asset Inventory
- CI/CD
- Cloud Cost Management
- Cloud Management
- Developer Experience
- DevOps
- FinOps
- GitOps
- GreenOps
- Infrastructure as Code
- Internal Developer Platform
- Internal Developer Portal
- Multi-Cloud
- Platform Engineering
- RBAC
- Self-Service
- Service Catalog
- StackForms
- Terraform
- Spectral
- Linting
- API Governance
---
