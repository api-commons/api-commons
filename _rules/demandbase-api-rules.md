---
api_specs:
- filename: demandbase-api-openapi.yml
  format: yaml
  label: Demandbase API
  slug: demandbase-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/openapi/demandbase-api-openapi.yml
- filename: demandbase-real-time-identification-openapi.yml
  format: yaml
  label: Demandbase Real-Time Identification API
  slug: demandbase-real-time-identification-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/openapi/demandbase-real-time-identification-openapi.yml
- filename: demandbase-advertising-openapi.yml
  format: yaml
  label: Demandbase Advertising API
  slug: demandbase-advertising-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/openapi/demandbase-advertising-openapi.yml
- filename: demandbase-engagement-openapi.yml
  format: yaml
  label: Demandbase Engagement API
  slug: demandbase-engagement-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/openapi/demandbase-engagement-openapi.yml
- filename: demandbase-account-list-openapi.yml
  format: yaml
  label: Demandbase Account List API
  slug: demandbase-account-list-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/openapi/demandbase-account-list-openapi.yml
- filename: demandbase-b2b-data-openapi.yml
  format: yaml
  label: Demandbase B2B Data API
  slug: demandbase-b2b-data-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/openapi/demandbase-b2b-data-openapi.yml
- filename: demandbase-ip-openapi.yml
  format: yaml
  label: Demandbase IP API
  slug: demandbase-ip-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/openapi/demandbase-ip-openapi.yml
- filename: demandbase-admin-openapi.yml
  format: yaml
  label: Demandbase Admin API
  slug: demandbase-admin-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/openapi/demandbase-admin-openapi.yml
- filename: demandbase-data-export-openapi.yml
  format: yaml
  label: Demandbase Data Export API
  slug: demandbase-data-export-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/openapi/demandbase-data-export-openapi.yml
- filename: demandbase-data-import-openapi.yml
  format: yaml
  label: Demandbase Data Import API
  slug: demandbase-data-import-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/openapi/demandbase-data-import-openapi.yml
categories:
- demandbase
description: Spectral linting rules defining API design standards and conventions for Demandbase.
layout: rules
name: Demandbase API Rules
provider_name: Demandbase
provider_slug: demandbase
rule_count: 5
rules:
- description: API info should include Demandbase support contact.
  given: $.info
  name: demandbase-info-contact
  severity: warn
- description: Servers should reference api.demandbase.com.
  given: $.servers[*].url
  name: demandbase-base-url
  severity: warn
- description: API should declare apiKey authentication.
  given: $.components.securitySchemes
  name: demandbase-apikey-auth
  severity: error
- description: Operations should be tagged Accounts, Enrichment, Firmographics, etc.
  given: $.paths[*][*]
  name: demandbase-operation-tags
  severity: warn
- description: API should expose /accounts as a primary resource.
  given: $.paths
  name: demandbase-accounts-resource
  severity: warn
rules_file: rules/demandbase-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/rules/demandbase-api-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 4
slug: demandbase-api-rules
source_filename: demandbase-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  demandbase-info-contact:\n    description: API info should include Demandbase support contact.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  demandbase-base-url:\n    description: Servers should reference api.demandbase.com.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"demandbase\\\\.com\"\n  demandbase-apikey-auth:\n    description: API should declare apiKey authentication.\n    given: $.components.securitySchemes\n    severity: error\n    then:\n      field: apiKeyAuth\n      function: truthy\n  demandbase-operation-tags:\n    description: Operations should be tagged Accounts, Enrichment, Firmographics, etc.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n  demandbase-accounts-resource:\n    description: API should expose /accounts as a primary resource.\n\
  \    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/accounts\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/rules/demandbase-api-rules.yml
tags:
- Account-Based Marketing
- Advertising
- AI Agents
- B2B Marketing
- Data Enrichment
- Intent Data
- Personalization
- Sales Intelligence
- Spectral
- Linting
- API Governance
---
