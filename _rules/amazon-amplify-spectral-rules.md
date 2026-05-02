---
api_specs:
- filename: amazon-amplify-openapi.yaml
  format: yaml
  label: Amazon Amplify REST API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-amplify/refs/heads/main/openapi/amazon-amplify-openapi.yaml
categories:
- amazon
description: Spectral linting rules defining API design standards and conventions for Amazon Amplify.
layout: rules
name: Amazon Amplify API Rules
provider_name: Amazon Amplify
provider_slug: amazon-amplify
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
rules_file: rules/amazon-amplify-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-amplify/refs/heads/main/rules/amazon-amplify-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 0
slug: amazon-amplify-spectral-rules
source_filename: amazon-amplify-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n- - spectral:oas\n  - all\nrules:\n  amazon-info-title-required:\n    description: API must have a title.\n    message: Info must include title.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  amazon-operation-summary-required:\n    description: Operations must have summaries.\n    message: Operation must include summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n  amazon-operation-operationid-required:\n    description: Operations must have operationIds.\n    message: Operation must include operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  amazon-response-200-get:\n    description: GET operations must return 200.\n    message: GET must have 200 response.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: responses.200\n\
  \      function: truthy\n  amazon-schema-description:\n    description: Schemas should have descriptions.\n    message: Schema should include description.\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-amplify/refs/heads/main/rules/amazon-amplify-spectral-rules.yml
tags:
- Frontend
- Full Stack
- Hosting
- Mobile Development
- Web Applications
- Spectral
- Linting
- API Governance
---
