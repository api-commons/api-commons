---
api_specs:
- filename: API_Operations.html
  format: yaml
  label: Amazon API Gateway REST API
  slug: rest-api
  spec_type: OpenAPI
  url: https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html
- filename: amazon-api-gateway-websocket-asyncapi.yml
  format: yaml
  label: Amazon API Gateway WebSocket API
  slug: websocket-api
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-api-gateway/refs/heads/main/asyncapi/amazon-api-gateway-websocket-asyncapi.yml
categories:
- amazon
description: Spectral linting rules defining API design standards and conventions for Amazon API Gateway.
layout: rules
name: Amazon API Gateway API Rules
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
rule_count: 5
rules:
- description: API must have a title.
  given: $.info
  name: amazon-info-title-required
  severity: error
- description: Operations must have summaries.
  given: $.paths[*][get,post,put,patch,delete]
  name: amazon-operation-summary-required
  severity: error
- description: Operations must have operationIds.
  given: $.paths[*][get,post,put,patch,delete]
  name: amazon-operation-operationid-required
  severity: error
- description: GET operations must return 200.
  given: $.paths[*].get
  name: amazon-response-200-get
  severity: error
- description: Schemas should have descriptions.
  given: $.components.schemas[*]
  name: amazon-schema-description
  severity: info
rules_file: rules/amazon-api-gateway-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-api-gateway/refs/heads/main/rules/amazon-api-gateway-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 0
slug: amazon-api-gateway-spectral-rules
source_filename: amazon-api-gateway-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n- - spectral:oas\n  - all\nrules:\n  amazon-info-title-required:\n    description: API must have a title.\n    message: Info must include title.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  amazon-operation-summary-required:\n    description: Operations must have summaries.\n    message: Operation must include summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n  amazon-operation-operationid-required:\n    description: Operations must have operationIds.\n    message: Operation must include operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  amazon-response-200-get:\n    description: GET operations must return 200.\n    message: GET must have 200 response.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: responses.200\n\
  \      function: truthy\n  amazon-schema-description:\n    description: Schemas should have descriptions.\n    message: Schema should include description.\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-api-gateway/refs/heads/main/rules/amazon-api-gateway-spectral-rules.yml
tags:
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
- Spectral
- Linting
- API Governance
---
