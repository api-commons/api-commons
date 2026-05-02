---
api_specs:
- filename: amazon-cloudfront-openapi.yml
  format: yaml
  label: Amazon CloudFront API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-cloudfront/refs/heads/main/openapi/amazon-cloudfront-openapi.yml
categories:
- get
- info
- microcks
- 'no'
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon CloudFront.
layout: rules
name: Amazon CloudFront API Rules
provider_name: Amazon CloudFront
provider_slug: amazon-cloudfront
rule_count: 19
rules:
- description: API title must start with "Amazon CloudFront"
  given: $.info.title
  name: info-title-prefix
  severity: error
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API must define at least one server
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: operationId must use PascalCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationId-pascal-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amazon CloudFront"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All response codes must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should document 500 internal server error
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-500-required
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have x-microcks-operation extension
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-present
  severity: info
rules_file: rules/amazon-cloudfront-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-cloudfront/refs/heads/main/rules/amazon-cloudfront-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 1
  warn: 6
slug: amazon-cloudfront-spectral-rules
source_filename: amazon-cloudfront-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-prefix:\n    description: API title must start with \"Amazon CloudFront\"\n    severity: error\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon CloudFront\"\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n  servers-required:\n    description: API must define at least one server\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\
  \n  operation-operationId-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-operationId-pascal-case:\n    description: operationId must use PascalCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]+$\"\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n  operation-summary-prefix:\n    description: Operation summaries must start with \"Amazon CloudFront\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon CloudFront\"\
  \n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n  response-description-required:\n    description: All response codes must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n  response-500-required:\n    description: Operations should document 500 internal\
  \ server error\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"500\"\n      function: truthy\n  schema-description-required:\n    description: Top-level schemas should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: \"$..description\"\n    then:\n      function: truthy\n  microcks-operation-present:\n    description: Operations should have x-microcks-operation\
  \ extension\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-cloudfront/refs/heads/main/rules/amazon-cloudfront-spectral-rules.yml
tags:
- CloudFront
- CDN
- Content Delivery
- Edge
- Spectral
- Linting
- API Governance
---
