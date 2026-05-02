---
api_specs:
- filename: amtrust-financial-services-commercial-lines-api.yaml
  format: yaml
  label: AmTrust Commercial Lines API
  slug: commercial-lines-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/openapi/amtrust-financial-services-commercial-lines-api.yaml
categories:
- info
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for AmTrust Financial Services.
layout: rules
name: AmTrust Financial Services API Rules
provider_name: AmTrust Financial Services
provider_slug: amtrust-financial-services
rule_count: 10
rules:
- description: API title must include AmTrust Financial Services
  given: $.info.title
  name: info-title-amtrust
  severity: warn
- description: Info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: All servers must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: All operations must have summaries
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: All operations must have operationIds
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: All parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All operations must have success responses
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Schema properties should have explicit types
  given: $.components.schemas[*].properties[*]
  name: schema-properties-typed
  severity: warn
rules_file: rules/amtrust-financial-services-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/rules/amtrust-financial-services-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 3
slug: amtrust-financial-services-spectral-rules
source_filename: amtrust-financial-services-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: \"spectral:oas\"\nrules:\n  info-title-amtrust:\n    description: API title must include AmTrust Financial Services\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AmTrust\"\n\n  info-description-required:\n    description: Info must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  servers-https-only:\n    description: All servers must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  operation-summary-required:\n    description: All operations must have summaries\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-operationid-required:\n    description: All operations must have operationIds\n    severity: error\n\
  \    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: All operations must have tags\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-success-required:\n    description: All operations must have success responses\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity:\
  \ error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  schema-properties-typed:\n    description: Schema properties should have explicit types\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/rules/amtrust-financial-services-spectral-rules.yml
tags:
- Commercial Insurance
- Insurance
- Property And Casualty
- Small Business
- Workers Compensation
- Spectral
- Linting
- API Governance
---
