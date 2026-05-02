---
api_specs:
- filename: amazon-global-accelerator-openapi.yml
  format: yaml
  label: Amazon Global Accelerator API
  slug: amazon-global-accelerator-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-global-accelerator/refs/heads/main/openapi/amazon-global-accelerator-openapi.yml
categories:
- info
- microcks
- 'no'
- operation
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Global Accelerator.
layout: rules
name: Amazon Global Accelerator API Rules
provider_name: Amazon Global Accelerator
provider_slug: amazon-global-accelerator
rule_count: 14
rules:
- description: API title must reference Amazon Global Accelerator
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with Amazon Global Accelerator
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-company-prefix
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Operations must have at least one success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Responses must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Security schemes should be defined in components
  given: $
  name: security-schemes-defined
  severity: warn
- description: Schema properties should have types
  given: $.components.schemas[*].properties[*]
  name: schema-properties-typed
  severity: info
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have x-microcks-operation
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/amazon-global-accelerator-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-global-accelerator/refs/heads/main/rules/amazon-global-accelerator-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 2
  warn: 5
slug: amazon-global-accelerator-spectral-rules
source_filename: amazon-global-accelerator-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-format:\n    description: API title must reference Amazon Global Accelerator\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Global Accelerator\"\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  servers-required:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\
  \n  operation-summary-company-prefix:\n    description: Operation summaries must start with Amazon Global Accelerator\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Global Accelerator\"\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  response-success-required:\n    description: Operations must have at least one success response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n\
  \        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: Responses must have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes should be defined in components\n    severity: warn\n    given: \"$\"\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  schema-properties-typed:\n    description: Schema properties should have types\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n\
  \        match: \".+\"\n\n  microcks-operation-extension:\n    description: Operations should have x-microcks-operation\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-global-accelerator/refs/heads/main/rules/amazon-global-accelerator-spectral-rules.yml
tags:
- Availability
- CDN
- Global
- Load Balancing
- Networking
- Performance
- Spectral
- Linting
- API Governance
---
