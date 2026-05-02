---
api_specs:
- filename: amazon-swf-openapi-original.yml
  format: yaml
  label: Amazon Simple Workflow Service API
  slug: amazon-swf-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-swf/refs/heads/main/openapi/amazon-swf-openapi-original.yml
categories:
- info
- operation
- parameter
- response
- security
description: Spectral linting rules defining API design standards and conventions for Amazon Simple Workflow Service.
layout: rules
name: Amazon Simple Workflow Service API Rules
provider_name: Amazon Simple Workflow Service
provider_slug: amazon-swf
rule_count: 9
rules:
- description: Info title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present.
  given: $.info
  name: info-description-required
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][*]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with 'Amazon SWF'.
  given: $.paths[*][*].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][*]
  name: operation-operationId-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][*]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have at least one 2xx response.
  given: $.paths[*][*].responses
  name: response-success-required
  severity: error
- description: Security schemes must be defined.
  given: $.components
  name: security-schemes-defined
  severity: warn
rules_file: rules/amazon-swf-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-swf/refs/heads/main/rules/amazon-swf-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 5
slug: amazon-swf-spectral-rules
source_filename: amazon-swf-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info description must be present.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start with 'Amazon SWF'.\n    severity: warn\n    given: \"$.paths[*][*].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon SWF\"\n\n  operation-operationId-required:\n    description: Every operation must have an operationId.\n    severity: error\n\
  \    given: \"$.paths[*][*]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have at least one 2xx response.\n    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined.\n    severity: warn\n    given: \"$.components\"\n    then:\n      field:\
  \ securitySchemes\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-swf/refs/heads/main/rules/amazon-swf-spectral-rules.yml
tags:
- Automation
- Task Coordination
- Workflow
- Spectral
- Linting
- API Governance
---
