---
api_specs:
- filename: amazon-fis-openapi.yml
  format: yaml
  label: AWS Fault Injection Simulator API
  slug: aws-fis-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-fault-injection-simulator/refs/heads/main/openapi/amazon-fis-openapi.yml
categories:
- client
- info
- 'no'
- operation
- path
- paths
- response
- schema
- security
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Fault Injection Simulator.
layout: rules
name: Amazon Fault Injection Simulator API Rules
provider_name: Amazon Fault Injection Simulator
provider_slug: amazon-fault-injection-simulator
rule_count: 28
rules:
- description: API must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Title must start with AWS Fault Injection Simulator
  given: $.info.title
  name: info-title-aws-fis-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API must define servers
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Operations must have summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Summaries must start with AWS Fault Injection Simulator
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-aws-fis-prefix
  severity: warn
- description: Operations must have description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operations should have x-microcks-operation
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Operations must have a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Mutating operations should document 400
  given: $.paths[*][post,put,patch].responses
  name: response-error-400
  severity: warn
- description: Operations on specific resources should document 404
  given: $.paths[*][get,patch,delete].responses
  name: response-error-404
  severity: warn
- description: Operations should document 500
  given: $.paths[*][*].responses
  name: response-error-500
  severity: warn
- description: Component schemas must have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should define type
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: Path parameters should have descriptions
  given: $.paths[*][*].parameters[*][?(@.in=="path")]
  name: path-parameters-described
  severity: warn
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Global tags must be defined
  given: $
  name: tags-defined
  severity: warn
- description: Each tag must have a description
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: Create operations should include clientToken for idempotency
  given: $.paths[*][post].requestBody.content
  name: client-token-in-create
  severity: info
rules_file: rules/amazon-fis-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-fault-injection-simulator/refs/heads/main/rules/amazon-fis-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 2
  warn: 16
slug: amazon-fis-spectral-rules
source_filename: amazon-fis-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: API must have a title\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-title-aws-fis-prefix:\n    description: Title must start with AWS Fault Injection Simulator\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: ^AWS Fault Injection Simulator\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  servers-required:\n    description: API must define servers\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity:\
  \ error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: ^https://\n  operation-operationid-required:\n    description: Operations must have operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  operation-operationid-camelcase:\n    description: operationId must use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: casing\n      functionOptions:\n        type: camel\n  operation-summary-required:\n    description: Operations must have summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n  operation-summary-aws-fis-prefix:\n    description: Summaries must start with AWS Fault Injection Simulator\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n    \
  \  function: pattern\n      functionOptions:\n        match: ^AWS Fault Injection Simulator\n  operation-description-required:\n    description: Operations must have description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n  operation-tags-required:\n    description: Operations must have tags\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  operation-microcks-extension:\n    description: Operations should have x-microcks-operation\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: $.paths\n    then:\n      function: truthy\n  response-success-required:\n    description: Operations must have a success response\n    severity: error\n\
  \    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: truthy\n  response-description-required:\n    description: Responses must have descriptions\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n  response-error-400:\n    description: Mutating operations should document 400\n    severity: warn\n    given: $.paths[*][post,put,patch].responses\n    then:\n      field: '400'\n      function: truthy\n  response-error-404:\n    description: Operations on specific resources should document 404\n    severity: warn\n    given: $.paths[*][get,patch,delete].responses\n    then:\n      field: '404'\n      function: truthy\n  response-error-500:\n    description: Operations should document 500\n    severity: warn\n    given: $.paths[*][*].responses\n    then:\n      field: '500'\n      function: truthy\n  schema-description-required:\n    description: Component schemas must have descriptions\n\
  \    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n  schema-type-defined:\n    description: Schema properties should define type\n    severity: warn\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: type\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n  security-global-defined:\n    description: Global security must be defined\n    severity: warn\n    given: $\n    then:\n      field: security\n      function: truthy\n  path-parameters-described:\n    description: Path parameters should have descriptions\n    severity: warn\n    given: $.paths[*][*].parameters[*][?(@.in==\"path\")]\n    then:\n      field: description\n      function: truthy\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity:\
  \ warn\n    given: $..description\n    then:\n      function: truthy\n  tags-defined:\n    description: Global tags must be defined\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n  tag-description-required:\n    description: Each tag must have a description\n    severity: warn\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n  client-token-in-create:\n    description: Create operations should include clientToken for idempotency\n    severity: info\n    given: $.paths[*][post].requestBody.content\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-fault-injection-simulator/refs/heads/main/rules/amazon-fis-spectral-rules.yml
tags:
- Chaos Engineering
- DevOps
- Fault Injection
- Resilience Testing
- Spectral
- Linting
- API Governance
---
