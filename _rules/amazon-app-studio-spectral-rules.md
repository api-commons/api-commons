---
api_specs:
- filename: amazon-app-studio-openapi.yaml
  format: yaml
  label: Amazon App Studio API
  slug: app-studio-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-app-studio/refs/heads/main/openapi/amazon-app-studio-openapi.yaml
categories:
- amazon
description: Spectral linting rules defining API design standards and conventions for Amazon App Studio.
layout: rules
name: Amazon App Studio API Rules
provider_name: Amazon App Studio
provider_slug: amazon-app-studio
rule_count: 3
rules:
- description: API must have a title.
  given: $.info
  name: amazon-info-title
  severity: error
- description: Operations must have summaries.
  given: $.paths[*][get,post,put,patch,delete]
  name: amazon-operation-summary
  severity: error
- description: Operations must have operationIds.
  given: $.paths[*][get,post,put,patch,delete]
  name: amazon-operation-id
  severity: error
rules_file: rules/amazon-app-studio-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-app-studio/refs/heads/main/rules/amazon-app-studio-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 0
slug: amazon-app-studio-spectral-rules
source_filename: amazon-app-studio-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n- - spectral:oas\n  - all\nrules:\n  amazon-info-title:\n    description: API must have a title.\n    message: Info must include title.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  amazon-operation-summary:\n    description: Operations must have summaries.\n    message: Operation must include summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n  amazon-operation-id:\n    description: Operations must have operationIds.\n    message: Operation must include operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-app-studio/refs/heads/main/rules/amazon-app-studio-spectral-rules.yml
tags:
- Generative AI
- Internal Tools
- Low-Code
- No-Code
- Spectral
- Linting
- API Governance
---
