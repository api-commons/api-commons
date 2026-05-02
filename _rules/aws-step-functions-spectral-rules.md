---
api_specs:
- filename: aws-step-functions-openapi.json
  format: json
  label: AWS Step Functions
  slug: aws-step-functions
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aws-step-functions/refs/heads/main/openapi/aws-step-functions-openapi.json
categories:
- sfn
description: Spectral linting rules defining API design standards and conventions for AWS Step Functions.
layout: rules
name: AWS Step Functions API Rules
provider_name: AWS Step Functions
provider_slug: aws-step-functions
rule_count: 8
rules:
- description: All operations must have a summary starting with "AWS Step Functions"
  given: $.paths[*][get,post,put,delete,patch]
  name: sfn-operation-summary
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: sfn-operation-id
  severity: error
- description: Info object must have a title
  given: $.info
  name: sfn-info-title
  severity: error
- description: Info object must have a version
  given: $.info
  name: sfn-info-version
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: sfn-response-description
  severity: error
- description: Operations should have x-microcks-operation annotation
  given: $.paths[*][get,post,put,delete,patch]
  name: sfn-microcks-annotation
  severity: info
- description: Schema components should have a type
  given: $.components.schemas[*]
  name: sfn-schema-type
  severity: warn
- description: API security schemes should be defined
  given: $
  name: sfn-security-defined
  severity: warn
rules_file: rules/aws-step-functions-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aws-step-functions/refs/heads/main/rules/aws-step-functions-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 3
slug: aws-step-functions-spectral-rules
source_filename: aws-step-functions-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  sfn-operation-summary:\n    description: All operations must have a summary starting with \"AWS Step Functions\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^AWS Step Functions\"\n  sfn-operation-id:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n  sfn-info-title:\n    description: Info object must have a title\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  sfn-info-version:\n    description: Info object must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n  sfn-response-description:\n    description: All responses must have a description\n    severity: error\n    given:\
  \ \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n  sfn-microcks-annotation:\n    description: Operations should have x-microcks-operation annotation\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n  sfn-schema-type:\n    description: Schema components should have a type\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n  sfn-security-defined:\n    description: API security schemes should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: components.securitySchemes\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/aws-step-functions/refs/heads/main/rules/aws-step-functions-spectral-rules.yml
tags:
- iPaaS
- Orchestration
- Serverless
- Spectral
- Linting
- API Governance
---
