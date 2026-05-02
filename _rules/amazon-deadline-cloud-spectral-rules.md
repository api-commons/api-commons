---
api_specs:
- filename: amazon-deadline-cloud-openapi.yml
  format: yaml
  label: Amazon Deadline Cloud API
  slug: amazon-deadline-cloud-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-deadline-cloud/refs/heads/main/openapi/amazon-deadline-cloud-openapi.yml
categories:
- info
- list
- 'no'
- openapi
- operation
- paths
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Deadline Cloud.
layout: rules
name: Amazon Deadline Cloud API Rules
provider_name: Amazon Deadline Cloud
provider_slug: amazon-deadline-cloud
rule_count: 20
rules:
- description: API title must reference "Deadline Cloud"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3x
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Deadline Cloud API paths should include API version date prefix
  given: $.paths[*]~
  name: paths-versioned
  severity: warn
- description: Most Deadline Cloud resources are scoped under a farm
  given: $.paths[*]~
  name: paths-farm-scoped
  severity: info
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: OperationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Tags array should be defined globally
  given: $
  name: tags-defined
  severity: warn
- description: All operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: List operations should return nextToken for pagination
  given: $.paths[*][get].responses.200.content.application/json.schema.properties
  name: list-has-pagination
  severity: info
rules_file: rules/amazon-deadline-cloud-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-deadline-cloud/refs/heads/main/rules/amazon-deadline-cloud-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 2
  warn: 5
slug: amazon-deadline-cloud-spectral-rules
source_filename: amazon-deadline-cloud-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-prefix:\n    description: API title must reference \"Deadline Cloud\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"Deadline Cloud\"\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  openapi-version-3x:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  servers-defined:\n    description: Servers array must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n\
  \  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  paths-versioned:\n    description: Deadline Cloud API paths should include API version date prefix\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/2023-10-12/\"\n\n  paths-farm-scoped:\n    description: Most Deadline Cloud resources are scoped under a farm\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/2023-10-12/farms\"\n\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: All operations must have\
  \ a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationId must use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: All operations must have tags\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  tags-defined:\n    description: Tags array should be defined globally\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function:\
  \ truthy\n\n  response-success-required:\n    description: All operations must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-description-required:\n    description: Top-level schemas should have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n\
  \      function: truthy\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  list-has-pagination:\n    description: List operations should return nextToken for pagination\n    severity: info\n    given: \"$.paths[*][get].responses.200.content.application/json.schema.properties\"\n    then:\n      field: nextToken\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-deadline-cloud/refs/heads/main/rules/amazon-deadline-cloud-spectral-rules.yml
tags:
- Compute
- Media
- Rendering
- Visual Effects
- Spectral
- Linting
- API Governance
---
