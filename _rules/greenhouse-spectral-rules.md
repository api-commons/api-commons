---
api_specs:
- filename: greenhouse-harvest-openapi.yml
  format: yaml
  label: Greenhouse Harvest API
  slug: harvest
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/greenhouse/refs/heads/main/openapi/greenhouse-harvest-openapi.yml
- filename: greenhouse-job-board-openapi.yml
  format: yaml
  label: Greenhouse Job Board API
  slug: job-board
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/greenhouse/refs/heads/main/openapi/greenhouse-job-board-openapi.yml
- filename: greenhouse-ingestion-openapi.yml
  format: yaml
  label: Greenhouse Candidate Ingestion API
  slug: ingestion
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/greenhouse/refs/heads/main/openapi/greenhouse-ingestion-openapi.yml
- filename: greenhouse-onboarding-openapi.yml
  format: yaml
  label: Greenhouse Onboarding API
  slug: onboarding
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/greenhouse/refs/heads/main/openapi/greenhouse-onboarding-openapi.yml
categories:
- info
- openapi
- operation
- parameter
- paths
- response
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Greenhouse.
layout: rules
name: Greenhouse API Rules
provider_name: Greenhouse
provider_slug: greenhouse
rule_count: 13
rules:
- description: Info object must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: Info object must have a description.
  given: $.info
  name: info-description-required
  severity: warn
- description: Info object must have a version.
  given: $.info
  name: info-version-required
  severity: error
- description: OpenAPI version must be 3.x.
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: Servers must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Path segments should be kebab-case or templated.
  given: $.paths.*~
  name: paths-kebab-case
  severity: warn
- description: Paths should not end with a trailing slash.
  given: $.paths.*~
  name: paths-no-trailing-slash
  severity: warn
- description: Operations must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: warn
- description: Operations should have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Parameter names should be snake_case.
  given: $.paths[*][*].parameters[?(@.in == 'query')].name
  name: parameter-snake-case
  severity: info
- description: Operations must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Security schemes must be defined.
  given: $.components.securitySchemes
  name: security-defined
  severity: warn
rules_file: rules/greenhouse-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/greenhouse/refs/heads/main/rules/greenhouse-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 1
  warn: 7
slug: greenhouse-spectral-rules
source_filename: greenhouse-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: Info object must have a title.\n    given: $.info\n    severity: error\n    then:\n      field: title\n      function: truthy\n  info-description-required:\n    description: Info object must have a description.\n    given: $.info\n    severity: warn\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: Info object must have a version.\n    given: $.info\n    severity: error\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: OpenAPI version must be 3.x.\n    given: $.openapi\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined.\n    given: $\n    severity: error\n    then:\n      field: servers\n      function: truthy\n  servers-https:\n    description: Server\
  \ URLs must use HTTPS.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments should be kebab-case or templated.\n    given: $.paths.*~\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/([a-z0-9_\\\\-]+|\\\\{[a-zA-Z0-9_]+\\\\}))*/?$\"\n  paths-no-trailing-slash:\n    description: Paths should not end with a trailing slash.\n    given: $.paths.*~\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \".+/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Operations must have a summary.\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: warn\n    then:\n      field: summary\n      function: truthy\n  operation-tags-required:\n    description: Operations should have at least one tag.\n    given: $.paths[*][get,post,put,patch,delete]\n\
  \    severity: warn\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-snake-case:\n    description: Parameter names should be snake_case.\n    given: $.paths[*][*].parameters[?(@.in == 'query')].name\n    severity: info\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must define at least one 2xx response.\n    given: $.paths[*][get,post,put,patch,delete].responses\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          patternProperties:\n            \"^2[0-9][0-9]$\": {}\n          minProperties: 1\n\n  # SECURITY\n  security-defined:\n    description: Security schemes must be defined.\n    given: $.components.securitySchemes\n    severity: warn\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/greenhouse/refs/heads/main/rules/greenhouse-spectral-rules.yml
tags:
- ATS
- Recruiting
- Candidates
- Jobs
- Onboarding
- HR
- Spectral
- Linting
- API Governance
---
