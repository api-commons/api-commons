---
api_specs:
- filename: clockodo-openapi.yml
  format: yaml
  label: Clockodo API
  slug: clockodo-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/clockodo/refs/heads/main/openapi/clockodo-openapi.yml
categories:
- clockodo
description: Spectral linting rules defining API design standards and conventions for Clockodo.
layout: rules
name: Clockodo API Rules
provider_name: Clockodo
provider_slug: clockodo
rule_count: 6
rules:
- description: API info MUST contain a contact email or URL.
  given: $.info
  name: clockodo-info-contact
  severity: warn
- description: All Clockodo API servers MUST use HTTPS.
  given: $.servers[*].url
  name: clockodo-https-only
  severity: error
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: clockodo-operation-id
  severity: error
- description: Operations MUST be tagged for resource grouping (Entries, Customers, Projects, Services, Users, Absences, LumpSumServices, HolidaysQuota, Clock).
  given: $.paths[*][get,post,put,delete,patch].tags
  name: clockodo-tag-required
  severity: warn
- description: API MUST define API-key and/or basic-auth security since Clockodo authenticates with X-ClockodoApiUser/X-ClockodoApiKey headers or HTTP Basic.
  given: $.components.securitySchemes
  name: clockodo-auth-required
  severity: error
- description: API MUST declare at least one server URL pointing at my.clockodo.com.
  given: $.servers
  name: clockodo-server-url
  severity: error
rules_file: rules/clockodo-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/clockodo/refs/heads/main/rules/clockodo-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 2
slug: clockodo-rules
source_filename: clockodo-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  clockodo-info-contact:\n    description: API info MUST contain a contact email or URL.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  clockodo-https-only:\n    description: All Clockodo API servers MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  clockodo-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  clockodo-tag-required:\n    description: Operations MUST be tagged for resource grouping (Entries, Customers, Projects, Services, Users, Absences, LumpSumServices, HolidaysQuota, Clock).\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n    then:\n      function: truthy\n  clockodo-auth-required:\n    description:\
  \ API MUST define API-key and/or basic-auth security since Clockodo authenticates with X-ClockodoApiUser/X-ClockodoApiKey headers or HTTP Basic.\n    severity: error\n    given: $.components.securitySchemes\n    then:\n      function: truthy\n  clockodo-server-url:\n    description: API MUST declare at least one server URL pointing at my.clockodo.com.\n    severity: error\n    given: $.servers\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/clockodo/refs/heads/main/rules/clockodo-rules.yml
tags:
- Absence Management
- Billing
- Project Management
- Stop Clock
- Time Tracking
- Timesheets
- Spectral
- Linting
- API Governance
---
