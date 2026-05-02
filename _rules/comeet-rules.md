---
api_specs:
- filename: comeet-careers-api-openapi.yml
  format: yaml
  label: Comeet Careers API
  slug: comeet-careers-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/comeet/refs/heads/main/openapi/comeet-careers-api-openapi.yml
categories:
- comeet
description: Spectral linting rules defining API design standards and conventions for Comeet.
layout: rules
name: Comeet API Rules
provider_name: Comeet
provider_slug: comeet
rule_count: 8
rules:
- description: API info must include a contact block.
  given: $.info
  name: comeet-info-contact
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: comeet-server-https
  severity: error
- description: Public server URL should point to comeet.co.
  given: $.servers[*].url
  name: comeet-server-host
  severity: warn
- description: Careers API server URL should include /careers-api/2.0.
  given: $.servers[*].url
  name: comeet-careers-base-path
  severity: info
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: comeet-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: comeet-operation-tags
  severity: warn
- description: Read endpoints must accept the public company `token` query parameter.
  given: $.paths[*].get.parameters
  name: comeet-token-query-param
  severity: warn
- description: Company-scoped endpoints must use a {company_uid} path parameter.
  given: $.paths[?(@property.indexOf('company') > -1)]
  name: comeet-company-uid-path
  severity: warn
rules_file: rules/comeet-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/comeet/refs/heads/main/rules/comeet-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 1
  warn: 4
slug: comeet-rules
source_filename: comeet-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for the Comeet (Spark Hire Recruit) Careers API.\n# Tuned to comeet.co careers-api conventions: tokenized GETs over HTTPS,\n# company UID path parameters, and embeddable widget data shapes.\nrules:\n  comeet-info-contact:\n    description: API info must include a contact block.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  comeet-server-https:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  comeet-server-host:\n    description: Public server URL should point to comeet.co.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"comeet.co\"\n\n  comeet-careers-base-path:\n    description: Careers API server URL should include /careers-api/2.0.\n\
  \    severity: info\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/careers-api/\"\n\n  comeet-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  comeet-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  comeet-token-query-param:\n    description: Read endpoints must accept the public company `token` query parameter.\n    severity: warn\n    given: \"$.paths[*].get.parameters\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type:\
  \ object\n            properties:\n              name:\n                const: token\n              in:\n                const: query\n\n  comeet-company-uid-path:\n    description: Company-scoped endpoints must use a {company_uid} path parameter.\n    severity: warn\n    given: \"$.paths[?(@property.indexOf('company') > -1)]\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"{company_uid}\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/comeet/refs/heads/main/rules/comeet-rules.yml
tags:
- ATS
- Candidates
- Careers
- Interviews
- Jobs
- Recruiting
- Talent Acquisition
- Spectral
- Linting
- API Governance
---
