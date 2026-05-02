---
api_specs:
- filename: aws-x-ray-openapi.yml
  format: yaml
  label: AWS X-Ray
  slug: aws-x-ray
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aws-x-ray/refs/heads/main/openapi/aws-x-ray-openapi.yml
categories:
- xray
description: Spectral linting rules defining API design standards and conventions for AWS X-Ray.
layout: rules
name: AWS X-Ray API Rules
provider_name: AWS X-Ray
provider_slug: aws-x-ray
rule_count: 5
rules:
- description: All operations must have a summary starting with "AWS X-Ray"
  given: $.paths[*][get,post,put,delete,patch]
  name: xray-operation-summary
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: xray-operation-id
  severity: error
- description: Info object must have a title
  given: $.info
  name: xray-info-title
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: xray-response-description
  severity: error
- description: Operations should have x-microcks-operation annotation
  given: $.paths[*][get,post,put,delete,patch]
  name: xray-microcks-annotation
  severity: info
rules_file: rules/aws-x-ray-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aws-x-ray/refs/heads/main/rules/aws-x-ray-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 1
  warn: 1
slug: aws-x-ray-spectral-rules
source_filename: aws-x-ray-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  xray-operation-summary:\n    description: All operations must have a summary starting with \"AWS X-Ray\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^AWS X-Ray\"\n  xray-operation-id:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n  xray-info-title:\n    description: Info object must have a title\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  xray-response-description:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n  xray-microcks-annotation:\n    description: Operations should have x-microcks-operation annotation\n\
  \    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/aws-x-ray/refs/heads/main/rules/aws-x-ray-spectral-rules.yml
tags:
- Debugging
- Distributed Tracing
- Microservices
- Observability
- Spectral
- Linting
- API Governance
---
