---
api_specs:
- filename: amazon-data-pipeline-openapi.yml
  format: yaml
  label: AWS Data Pipeline API
  slug: aws-data-pipeline-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-data-pipeline/refs/heads/main/openapi/amazon-data-pipeline-openapi.yml
categories:
- action
- all
- info
- 'no'
- openapi
- operation
- pipeline
- request
- response
- schema
- security
- servers
- tags
- validation
description: Spectral linting rules defining API design standards and conventions for Amazon Data Pipeline.
layout: rules
name: Amazon Data Pipeline API Rules
provider_name: Amazon Data Pipeline
provider_slug: amazon-data-pipeline
rule_count: 22
rules:
- description: API title must start with "AWS Data Pipeline"
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
- description: AWS Data Pipeline uses Action-based path conventions with ?Action= query parameter
  given: $.paths[*]~
  name: action-based-paths
  severity: info
- description: AWS Data Pipeline uses POST for all operations
  given: $.paths[*][get,put,patch,delete]
  name: all-operations-use-post
  severity: info
- description: All operations must have a summary
  given: $.paths[*][post]
  name: operation-summary-required
  severity: error
- description: All operations must have a description
  given: $.paths[*][post]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][post]
  name: operation-id-required
  severity: error
- description: OperationId must use camelCase
  given: $.paths[*][post].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have tags
  given: $.paths[*][post]
  name: operation-tags-required
  severity: error
- description: All POST operations should support application/json
  given: $.paths[*].post.requestBody.content
  name: request-body-json-content
  severity: warn
- description: Tags array should be defined globally
  given: $
  name: tags-defined
  severity: warn
- description: All operations must have a 200 response
  given: $.paths[*][post].responses
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
- description: Pipeline operations should reference pipelineId in request body
  given: $.components.schemas[?(@ =~ /Request/)].properties
  name: pipeline-id-in-operations
  severity: info
- description: Validation operation responses should include errored field
  given: $.components.schemas.PutPipelineDefinitionOutput.properties
  name: validation-output-has-errored
  severity: info
rules_file: rules/amazon-data-pipeline-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-data-pipeline/refs/heads/main/rules/amazon-data-pipeline-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 4
  warn: 5
slug: amazon-data-pipeline-spectral-rules
source_filename: amazon-data-pipeline-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-prefix:\n    description: API title must start with \"AWS Data Pipeline\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AWS Data Pipeline\"\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  openapi-version-3x:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  servers-defined:\n    description: Servers array must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\
  \n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  action-based-paths:\n    description: AWS Data Pipeline uses Action-based path conventions with ?Action= query parameter\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/\\\\?Action=\"\n\n  all-operations-use-post:\n    description: AWS Data Pipeline uses POST for all operations\n    severity: info\n    given: \"$.paths[*][get,put,patch,delete]\"\n    then:\n      function: falsy\n\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][post]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: All operations must have a description\n    severity: error\n  \
  \  given: \"$.paths[*][post]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][post]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationId must use camelCase\n    severity: warn\n    given: \"$.paths[*][post].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: All operations must have tags\n    severity: error\n    given: \"$.paths[*][post]\"\n    then:\n      field: tags\n      function: truthy\n\n  request-body-json-content:\n    description: All POST operations should support application/json\n    severity: warn\n    given: \"$.paths[*].post.requestBody.content\"\n    then:\n      field: application/json\n      function: truthy\n\n  tags-defined:\n    description:\
  \ Tags array should be defined globally\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  response-success-required:\n    description: All operations must have a 200 response\n    severity: error\n    given: \"$.paths[*][post].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: [\"200\"]\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-description-required:\n    description: Top-level schemas should have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n\
  \      function: truthy\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  pipeline-id-in-operations:\n    description: Pipeline operations should reference pipelineId in request body\n    severity: info\n    given: \"$.components.schemas[?(@ =~ /Request/)].properties\"\n    then:\n      field: pipelineId\n      function: truthy\n\n  validation-output-has-errored:\n    description: Validation operation responses should include errored field\n    severity: info\n    given: \"$.components.schemas.PutPipelineDefinitionOutput.properties\"\n    then:\n      field: errored\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-data-pipeline/refs/heads/main/rules/amazon-data-pipeline-spectral-rules.yml
tags:
- Data Processing
- ETL
- Workflows
- Data Pipeline
- Automation
- Spectral
- Linting
- API Governance
---
