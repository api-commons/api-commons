---
api_specs:
- filename: air-quality-programmatic-apis-openapi.yml
  format: yaml
  label: AQICN Real-Time Air Quality API
  slug: air-quality-programmatic-apis
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/air-quality-programmatic-apis/refs/heads/main/openapi/air-quality-programmatic-apis-openapi.yml
- filename: aqicn-json-api-openapi.yaml
  format: yaml
  label: AQICN JSON Air Quality API
  slug: aqicn-json-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/air-quality-programmatic-apis/refs/heads/main/openapi/aqicn-json-api-openapi.yaml
categories:
- info
- operation
- parameter
- response
- servers
- token
description: Spectral linting rules defining API design standards and conventions for Air Quality Programmatic APIs.
layout: rules
name: Air Quality Programmatic APIs API Rules
provider_name: Air Quality Programmatic APIs
provider_slug: air-quality-programmatic-apis
rule_count: 10
rules:
- description: API title should start with "Air Quality" or "AQICN"
  given: $.info.title
  name: info-title-aqicn
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation should have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: API token query parameter should be documented on all operations
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.name == 'token')]
  name: token-parameter-required
  severity: warn
- description: Operations must define a 200 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-200-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: All parameters should have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: warn
rules_file: rules/aqicn-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/air-quality-programmatic-apis/refs/heads/main/rules/aqicn-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 0
  warn: 5
slug: aqicn-spectral-rules
source_filename: aqicn-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: \"spectral:oas\"\n\nrules:\n  info-title-aqicn:\n    description: API title should start with \"Air Quality\" or \"AQICN\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(Air Quality|AQICN)\"\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation should have tags\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  token-parameter-required:\n    description: API token\
  \ query parameter should be documented on all operations\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[?(@.name == 'token')]\"\n    then:\n      field: required\n      function: truthy\n\n  response-200-required:\n    description: Operations must define a 200 response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: [\"200\"]\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-description-required:\n    description: All parameters should have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  servers-defined:\n\
  \    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs should use HTTPS\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/air-quality-programmatic-apis/refs/heads/main/rules/aqicn-spectral-rules.yml
tags:
- Air Quality
- Environment
- EPA
- Open Data
- Public Health
- IoT
- Government Data
- Real-Time Data
- Spectral
- Linting
- API Governance
---
