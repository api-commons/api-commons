---
api_specs:
- filename: amazon-comprehend-openapi.yml
  format: yaml
  label: Amazon Comprehend API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-comprehend/refs/heads/main/openapi/amazon-comprehend-openapi.yml
categories:
- comprehend
- get
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- request
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Comprehend.
layout: rules
name: Amazon Comprehend API Rules
provider_name: Amazon Comprehend
provider_slug: amazon-comprehend
rule_count: 23
rules:
- description: OpenAPI info must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: OpenAPI info must have a description.
  given: $.info
  name: info-description-required
  severity: warn
- description: OpenAPI info must have a version field.
  given: $.info
  name: info-version-required
  severity: error
- description: Specs must use OpenAPI 3.0.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-required
  severity: error
- description: Server URLs should use HTTPS.
  given: $.servers[*]
  name: servers-https-required
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with Amazon Comprehend.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amazon-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: OperationIds should use PascalCase as per AWS convention.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-pascal-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Request bodies should use application/json.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
- description: Schema objects should have a type.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations should not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Language code parameters should be documented with valid ISO 639-1 codes.
  given: $.components.schemas.LanguageCode
  name: comprehend-language-code-documented
  severity: info
- description: Confidence score properties should have minimum and maximum defined.
  given: $.components.schemas[*].properties.Score
  name: comprehend-confidence-score-range
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should have x-microcks-operation for mock server compatibility.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/amazon-comprehend-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-comprehend/refs/heads/main/rules/amazon-comprehend-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 4
  warn: 11
slug: amazon-comprehend-spectral-rules
source_filename: amazon-comprehend-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: OpenAPI info must have a title.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: OpenAPI info must have a description.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: OpenAPI info must have a version field.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Specs must use OpenAPI 3.0.x.\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: At least one server must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n\
  \      function: truthy\n\n  servers-https-required:\n    description: Server URLs should use HTTPS.\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-amazon-prefix:\n    description: Operation summaries should start with Amazon Comprehend.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Comprehend\"\n\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n   \
  \   function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-pascal-case:\n    description: OperationIds should use PascalCase as per AWS convention.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n   \
  \   function: truthy\n\n  # REQUEST BODIES\n  request-body-json-content:\n    description: Request bodies should use application/json.\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n  response-description-required:\n    description: Every response must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-recommended:\n    description: Top-level schemas should have a description.\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    description: Schema objects should have a type.\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n\
  \    description: Security schemes must be defined.\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP CONVENTIONS\n  get-no-request-body:\n    description: GET operations should not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # COMPREHEND-SPECIFIC\n  comprehend-language-code-documented:\n    description: Language code parameters should be documented with valid ISO 639-1 codes.\n    severity: info\n    given: \"$.components.schemas.LanguageCode\"\n    then:\n      field: enum\n      function: truthy\n\n  comprehend-confidence-score-range:\n    description: Confidence score properties should have minimum and maximum defined.\n    severity: info\n    given: \"$.components.schemas[*].properties.Score\"\n    then:\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not\
  \ be empty strings.\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: truthy\n\n  microcks-operation-extension:\n    description: Operations should have x-microcks-operation for mock server compatibility.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-comprehend/refs/heads/main/rules/amazon-comprehend-spectral-rules.yml
tags:
- Machine Learning
- Natural Language Processing
- NLP
- Text Analysis
- Spectral
- Linting
- API Governance
---
