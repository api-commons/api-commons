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
rule_count: 3
rules:
- description: Servers should reference api.demandbase.com or company-target.com.
  given: $.servers[*].url
  name: demandbase-ip-base-url
  severity: warn
- description: IP API should declare apiKey authentication.
  given: $.components.securitySchemes
  name: demandbase-ip-apikey-auth
  severity: error
- description: IP API should expose /api/v3/ip.json.
  given: $.paths
  name: demandbase-ip-resource
  severity: warn
rules_file: rules/demandbase-ip-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/rules/demandbase-ip-api-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 2
slug: demandbase-ip-api-rules
source_filename: demandbase-ip-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  demandbase-ip-base-url:\n    description: Servers should reference api.demandbase.com or company-target.com.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(demandbase|company-target)\\\\.com\"\n  demandbase-ip-apikey-auth:\n    description: IP API should declare apiKey authentication.\n    given: $.components.securitySchemes\n    severity: error\n    then:\n      field: apiKeyAuth\n      function: truthy\n  demandbase-ip-resource:\n    description: IP API should expose /api/v3/ip.json.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/api/v3/ip\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/rules/demandbase-ip-api-rules.yml
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
