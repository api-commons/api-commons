---
api_specs:
- filename: amazon-app-runner-openapi.yaml
  format: yaml
  label: Amazon App Runner API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-app-runner/refs/heads/main/openapi/amazon-app-runner-openapi.yaml
categories:
- amazon
description: Spectral linting rules defining API design standards and conventions for Amazon App Runner.
layout: rules
name: Amazon App Runner API Rules
provider_name: Amazon App Runner
provider_slug: amazon-app-runner
rule_count: 3
rules:
- description: API must have a title.
  given: $.info
  name: amazon-app-runner-info-title
  severity: error
- description: Operations must have summaries.
  given: $.paths[*][get,post,put,patch,delete]
  name: amazon-app-runner-operation-summary
  severity: error
- description: Operations must have operationIds.
  given: $.paths[*][get,post,put,patch,delete]
  name: amazon-app-runner-operation-id
  severity: error
rules_file: rules/amazon-app-runner-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-app-runner/refs/heads/main/rules/amazon-app-runner-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 0
slug: amazon-app-runner-spectral-rules
source_filename: amazon-app-runner-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n- - spectral:oas\n  - all\nrules:\n  amazon-app-runner-info-title:\n    description: API must have a title.\n    message: Info must include title.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  amazon-app-runner-operation-summary:\n    description: Operations must have summaries.\n    message: Operation must include summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n  amazon-app-runner-operation-id:\n    description: Operations must have operationIds.\n    message: Operation must include operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-app-runner/refs/heads/main/rules/amazon-app-runner-spectral-rules.yml
tags:
- CI/CD
- Containers
- Deployment
- Managed Service
- Serverless
- Web Applications
- Spectral
- Linting
- API Governance
---
