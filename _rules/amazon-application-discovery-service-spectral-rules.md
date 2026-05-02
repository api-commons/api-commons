---
api_specs:
- filename: amazon-application-discovery-service-openapi.yml
  format: yaml
  label: Amazon Application Discovery Service API
  slug: amazon-application-discovery-service-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-application-discovery-service/refs/heads/main/openapi/amazon-application-discovery-service-openapi.yml
categories:
- info
- openapi
- operation
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Application Discovery Service.
layout: rules
name: Amazon Application Discovery Service API Rules
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
rule_count: 21
rules:
- description: API title must start with "Amazon Application Discovery Service"
  given: $.info
  name: info-title-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API info must have a version field
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3x
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: error
- description: Path segments must use kebab-case or camelCase with /v1/ prefix
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amazon Application Discovery Service"
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: OperationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every operation must have a 200 success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should define a 500 error response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-500-defined
  severity: warn
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Global security must be defined
  given: $
  name: security-defined
  severity: error
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Operations should have x-microcks-operation for mock server compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
- description: POST operations should have request/response examples
  given: $.paths[*][post].requestBody.content.application/json
  name: operation-examples-encouraged
  severity: info
rules_file: rules/amazon-application-discovery-service-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-application-discovery-service/refs/heads/main/rules/amazon-application-discovery-service-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 2
  warn: 6
slug: amazon-application-discovery-service-spectral-rules
source_filename: amazon-application-discovery-service-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"Amazon Application Discovery Service\"\n    severity: warn\n    given: $.info\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: '^Amazon Application Discovery Service'\n\n  info-description-required:\n    description: API info must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must have a version field\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3x:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: '^3\\.'\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined\n    severity:\
  \ error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: $.servers[*]\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments must use kebab-case or camelCase with /v1/ prefix\n    severity: warn\n    given: $.paths\n    then:\n      field: '@key'\n      function: pattern\n      functionOptions:\n        match: '^/v1/'\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"Amazon Application Discovery Service\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n\
  \      field: summary\n      function: pattern\n      functionOptions:\n        match: '^Amazon Application Discovery Service'\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationId must use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]+$'\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n\
  \    then:\n      field: tags\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a 200 success response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '200'\n      function: truthy\n\n  response-500-defined:\n    description: Operations should define a 500 error response\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '500'\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  #\
  \ SECURITY\n  security-defined:\n    description: Global security must be defined\n    severity: error\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # QUALITY\n  operation-microcks-extension:\n    description: Operations should have x-microcks-operation for mock server compatibility\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  operation-examples-encouraged:\n    description: POST operations should have request/response examples\n    severity: info\n    given: $.paths[*][post].requestBody.content.application/json\n    then:\n      field: examples\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-application-discovery-service/refs/heads/main/rules/amazon-application-discovery-service-spectral-rules.yml
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- Spectral
- Linting
- API Governance
---
