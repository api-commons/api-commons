---
api_specs:
- filename: apigee-api-management-openapi.yml
  format: yaml
  label: Apigee API Management
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/openapi/apigee-api-management-openapi.yml
- filename: apigee-api-hub-openapi.yml
  format: yaml
  label: Apigee API Hub API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/openapi/apigee-api-hub-openapi.yml
- filename: apigee-integrations-openapi.yml
  format: yaml
  label: Apigee Integrations API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/openapi/apigee-integrations-openapi.yml
- filename: apigee-apim-openapi.yml
  format: yaml
  label: Apigee API Management API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/openapi/apigee-apim-openapi.yml
- filename: apigee-registry-openapi.yml
  format: yaml
  label: Apigee Registry API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/openapi/apigee-registry-openapi.yml
categories:
- delete
- info
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Apigee.
layout: rules
name: Apigee API Rules
provider_name: Apigee
provider_slug: apigee
rule_count: 14
rules:
- description: API title must start with 'Apigee'.
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
- description: Apigee API servers should be on *.googleapis.com.
  given: $.servers[*]
  name: servers-googleapis
  severity: info
- description: Operation summaries must be in Title Case.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-title-case
  severity: warn
- description: Operation summaries must start with 'Apigee'.
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
- description: DELETE operations should return 200 or 204.
  given: $.paths[*].delete.responses
  name: delete-returns-200-or-204
  severity: warn
- description: Schema properties should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Apigee APIs must define OAuth2 security.
  given: $.components.securitySchemes
  name: security-oauth2-required
  severity: error
rules_file: rules/apigee-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/rules/apigee-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 2
  warn: 7
slug: apigee-spectral-rules
source_filename: apigee-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  info-title-prefix:\n    description: API title must start with 'Apigee'.\n    severity: warn\n    given: '$.info'\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: '^Apigee'\n\n  info-description-required:\n    description: API must have a description.\n    severity: error\n    given: '$.info'\n    then:\n      field: description\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: '$.servers[*]'\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  servers-googleapis:\n    description: Apigee API servers should be on *.googleapis.com.\n    severity: info\n    given: '$.servers[*]'\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: '\\.googleapis\\.com'\n\n  operation-summary-title-case:\n    description: Operation summaries\
  \ must be in Title Case.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: '^[A-Z]'\n\n  operation-summary-prefix:\n    description: Operation summaries must start with 'Apigee'.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: '^Apigee'\n\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camelcase:\n    description: OperationId must use camelCase.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]*$'\n\n  operation-tags-required:\n\
  \    description: Every operation must have at least one tag.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: tags\n      function: truthy\n\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: description\n      function: truthy\n\n  response-success-required:\n    description: Every operation must have a 2xx response.\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  delete-returns-200-or-204:\n    description: DELETE operations should return 200 or 204.\n    severity: warn\n    given: '$.paths[*].delete.responses'\n    then:\n      function: schema\n      functionOptions:\n\
  \        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['204']\n\n  schema-property-description:\n    description: Schema properties should have descriptions.\n    severity: info\n    given: '$.components.schemas[*].properties[*]'\n    then:\n      field: description\n      function: truthy\n\n  security-oauth2-required:\n    description: Apigee APIs must define OAuth2 security.\n    severity: error\n    given: '$.components.securitySchemes'\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/rules/apigee-spectral-rules.yml
tags:
- Analytics
- API Gateway
- API Governance
- API Hub
- API Management
- Developer Portal
- Enterprise
- Hybrid
- Integrations
- Microservices
- Monetization
- Spectral
- Linting
- API Governance
---
