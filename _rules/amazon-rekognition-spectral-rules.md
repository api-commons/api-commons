---
api_specs:
- filename: amazon-rekognition-openapi.yml
  format: yaml
  label: Amazon Rekognition
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-rekognition/refs/heads/main/openapi/amazon-rekognition-openapi.yml
categories:
- info
- operation
- post
- response
- schema
- security
- servers
- tag
description: Spectral linting rules defining API design standards and conventions for Amazon Rekognition.
layout: rules
name: Amazon Rekognition API Rules
provider_name: Amazon Rekognition
provider_slug: amazon-rekognition
rule_count: 18
rules:
- description: Info title must start with Amazon Rekognition
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: All operations must have a summary
  given: $.paths[*][*]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with Amazon Rekognition
  given: $.paths[*][*].summary
  name: operation-summary-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][*]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][*]
  name: operation-operationid-required
  severity: error
- description: OperationIds must use camelCase
  given: $.paths[*][*].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][*]
  name: operation-tags-required
  severity: warn
- description: All operations should specify security
  given: $.paths[*][*]
  name: operation-security-required
  severity: warn
- description: Operations must have a 2xx success response
  given: $.paths[*][*].responses
  name: response-success-required
  severity: error
- description: Operations should have a 400 error response
  given: $.paths[*][*].responses
  name: response-400-recommended
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Security schemes must be defined in components
  given: $
  name: security-schemes-defined
  severity: warn
- description: POST operations should use AWS JSON content type
  given: $.paths[*].post.requestBody.content
  name: post-must-use-amz-json
  severity: info
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tag-descriptions-required
  severity: info
rules_file: rules/amazon-rekognition-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-rekognition/refs/heads/main/rules/amazon-rekognition-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 2
  warn: 8
slug: amazon-rekognition-spectral-rules
source_filename: amazon-rekognition-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-prefix:\n    description: Info title must start with Amazon Rekognition\n    message: Info title should start with \"Amazon Rekognition\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Amazon Rekognition\n  info-description-required:\n    description: Info must have a description\n    message: Info object must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: Info must have a version\n    message: API version is required\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  servers-required:\n    description: At least one server must be defined\n    message: Servers array must be defined and non-empty\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n  servers-https:\n    description:\
  \ Server URLs must use HTTPS\n    message: Server URL must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: ^https://\n  operation-summary-required:\n    description: All operations must have a summary\n    message: Operation must have a summary\n    severity: error\n    given: $.paths[*][*]\n    then:\n      field: summary\n      function: truthy\n  operation-summary-prefix:\n    description: Operation summaries must start with Amazon Rekognition\n    message: Operation summary should start with \"Amazon Rekognition\"\n    severity: warn\n    given: $.paths[*][*].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Amazon Rekognition\n  operation-description-required:\n    description: All operations must have a description\n    message: Operation must have a description\n    severity: error\n    given: $.paths[*][*]\n    then:\n      field: description\n      function:\
  \ truthy\n  operation-operationid-required:\n    description: All operations must have an operationId\n    message: Operation must have an operationId\n    severity: error\n    given: $.paths[*][*]\n    then:\n      field: operationId\n      function: truthy\n  operation-operationid-camelcase:\n    description: OperationIds must use camelCase\n    message: OperationId must use camelCase\n    severity: warn\n    given: $.paths[*][*].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: ^[a-z][a-zA-Z0-9]*$\n  operation-tags-required:\n    description: All operations must have at least one tag\n    message: Operation must have at least one tag\n    severity: warn\n    given: $.paths[*][*]\n    then:\n      field: tags\n      function: truthy\n  operation-security-required:\n    description: All operations should specify security\n    message: Operation should define security requirements\n    severity: warn\n    given: $.paths[*][*]\n    then:\n      field:\
  \ security\n      function: truthy\n  response-success-required:\n    description: Operations must have a 2xx success response\n    message: Operation must define at least one 2xx success response\n    severity: error\n    given: $.paths[*][*].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n          - required:\n            - '200'\n          - required:\n            - '201'\n          - required:\n            - '202'\n          - required:\n            - '204'\n  response-400-recommended:\n    description: Operations should have a 400 error response\n    message: Operation should define a 400 Bad Request response\n    severity: warn\n    given: $.paths[*][*].responses\n    then:\n      field: '400'\n      function: truthy\n  schema-description-required:\n    description: Top-level schemas should have descriptions\n    message: Schema must have a description\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n  \
  \    field: description\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    message: Security schemes should be defined in components/securitySchemes\n    severity: warn\n    given: $\n    then:\n      field: components.securitySchemes\n      function: truthy\n  post-must-use-amz-json:\n    description: POST operations should use AWS JSON content type\n    message: POST operations should use application/x-amz-json-1.1 content type\n    severity: info\n    given: $.paths[*].post.requestBody.content\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required:\n          - application/x-amz-json-1.1\n  tag-descriptions-required:\n    description: Global tags should have descriptions\n    message: Tag must have a description\n    severity: info\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-rekognition/refs/heads/main/rules/amazon-rekognition-spectral-rules.yml
tags:
- Celebrity Recognition
- Computer Vision
- Content Moderation
- Custom Labels
- Deep Learning
- Face Liveness
- Facial Recognition
- Image Analysis
- Machine Learning
- Object Detection
- Text Detection
- Video Analysis
- Spectral
- Linting
- API Governance
---
