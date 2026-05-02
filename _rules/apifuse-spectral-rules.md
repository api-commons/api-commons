---
api_specs:
- filename: apifuse-api.yaml
  format: yaml
  label: Apifuse API
  slug: apifuse-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apifuse/refs/heads/main/openapi/apifuse-api.yaml
categories:
- info
- operation
- parameter
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Apifuse.
layout: rules
name: Apifuse API Rules
provider_name: Apifuse
provider_slug: apifuse
rule_count: 10
rules:
- description: API title must start with 'Apifuse'.
  given: $.info
  name: info-title-prefix
  severity: warn
- description: API must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https
  severity: error
- description: Operation summaries must start with 'Apifuse'.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: OperationId must use camelCase.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have a 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Schema properties must have a type defined.
  given: $.components.schemas[*].properties[*]
  name: schema-property-type-required
  severity: warn
rules_file: rules/apifuse-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apifuse/refs/heads/main/rules/apifuse-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 6
slug: apifuse-spectral-rules
source_filename: apifuse-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  info-title-prefix:\n    description: API title must start with 'Apifuse'.\n    severity: warn\n    given: '$.info'\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: '^Apifuse'\n\n  info-description-required:\n    description: API must have a description.\n    severity: error\n    given: '$.info'\n    then:\n      field: description\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: '$.servers[*]'\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  operation-summary-prefix:\n    description: Operation summaries must start with 'Apifuse'.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: '^Apifuse'\n\n  operation-id-required:\n    description: Every\
  \ operation must have an operationId.\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camelcase:\n    description: OperationId must use camelCase.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]*$'\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: tags\n      function: truthy\n\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: description\n      function: truthy\n\n  response-success-required:\n    description: Every operation must have a 2xx response.\n\
  \    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  schema-property-type-required:\n    description: Schema properties must have a type defined.\n    severity: warn\n    given: '$.components.schemas[*].properties[*]'\n    then:\n      field: type\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apifuse/refs/heads/main/rules/apifuse-spectral-rules.yml
tags:
- Embedded Integrations
- Integration Platform
- Integrations
- iPaaS
- Marketplace
- SaaS
- Workflow Automation
- Spectral
- Linting
- API Governance
---
