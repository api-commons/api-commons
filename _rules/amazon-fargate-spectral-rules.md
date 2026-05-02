---
api_specs:
- filename: amazon-fargate-openapi.yml
  format: yaml
  label: Amazon Fargate API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-fargate/refs/heads/main/openapi/amazon-fargate-openapi.yml
categories:
- info
- 'no'
- openapi
- operation
- request
- response
- schema
- security
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Fargate.
layout: rules
name: Amazon Fargate API Rules
provider_name: Amazon Fargate
provider_slug: amazon-fargate
rule_count: 29
rules:
- description: API must have a title in info
  given: $.info
  name: info-title-required
  severity: error
- description: API title must start with Amazon Fargate
  given: $.info.title
  name: info-title-amazon-fargate-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.1.x
  given: $
  name: openapi-version-3-1
  severity: warn
- description: Must define at least one server
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-operationid-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summary must start with Amazon Fargate
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amazon-fargate-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: warn
- description: Global tags array must be defined
  given: $
  name: tags-defined
  severity: warn
- description: Each tag must have a description
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: Request bodies should use application/x-amz-json-1.1 or application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content-type
  severity: warn
- description: Every operation must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should have a 400 error response
  given: $.paths[*][post,put,patch].responses
  name: response-error-400
  severity: warn
- description: Operations should document 500 server errors
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-error-500
  severity: warn
- description: Component schemas must have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schema properties must define a type
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: Should use AWS Signature V4 authentication
  given: $.components.securitySchemes
  name: security-aws-sig-v4
  severity: info
- description: Amazon API operations should use application/x-amz-json-1.1 content type
  given: $.paths[*][post].requestBody.content
  name: operation-amz-json-content-type
  severity: info
- description: Operations should have x-microcks-operation extension for mock support
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/amazon-fargate-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-fargate/refs/heads/main/rules/amazon-fargate-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 4
  warn: 15
slug: amazon-fargate-spectral-rules
source_filename: amazon-fargate-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: API must have a title in info\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-title-amazon-fargate-prefix:\n    description: API title must start with Amazon Fargate\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Amazon Fargate\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  openapi-version-3-1:\n    description: Must use OpenAPI 3.1.x\n    severity: warn\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: ^3\\.1\\.\n  servers-required:\n    description:\
  \ Must define at least one server\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n  servers-https-only:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: ^https://\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: operationId\n      function: truthy\n  operation-operationid-camelcase:\n    description: operationId must use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: casing\n      functionOptions:\n        type: camel\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n  \
  \    field: summary\n      function: truthy\n  operation-summary-amazon-fargate-prefix:\n    description: Operation summary must start with Amazon Fargate\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Amazon Fargate\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: description\n      function: truthy\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: tags\n      function: truthy\n  tags-defined:\n    description: Global tags array must be defined\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n  tag-description-required:\n    description: Each tag\
  \ must have a description\n    severity: warn\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n  request-body-json-content-type:\n    description: Request bodies should use application/x-amz-json-1.1 or application/json\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n  response-success-required:\n    description: Every operation must have a 2xx success response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\
  \  response-error-400:\n    description: Operations should have a 400 error response\n    severity: warn\n    given: $.paths[*][post,put,patch].responses\n    then:\n      field: '400'\n      function: truthy\n  response-error-500:\n    description: Operations should document 500 server errors\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '500'\n      function: truthy\n  schema-description-required:\n    description: Component schemas must have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n  schema-property-description:\n    description: Schema properties should have descriptions\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: description\n      function: truthy\n  schema-type-defined:\n    description: Schema properties must define a type\n    severity: warn\n    given: $.components.schemas[*].properties[*]\n\
  \    then:\n      field: type\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n  security-global-defined:\n    description: Global security must be defined\n    severity: warn\n    given: $\n    then:\n      field: security\n      function: truthy\n  security-aws-sig-v4:\n    description: Should use AWS Signature V4 authentication\n    severity: info\n    given: $.components.securitySchemes\n    then:\n      field: aws_signature_v4\n      function: truthy\n  operation-amz-json-content-type:\n    description: Amazon API operations should use application/x-amz-json-1.1 content type\n    severity: info\n    given: $.paths[*][post].requestBody.content\n    then:\n      function: truthy\n  operation-microcks-extension:\n    description: Operations should have x-microcks-operation extension for mock support\n    severity:\
  \ info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: $..description\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-fargate/refs/heads/main/rules/amazon-fargate-spectral-rules.yml
tags:
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
- Spectral
- Linting
- API Governance
---
