---
categories:
- info
- operation
- parameter
- response
- schema
- security
description: Spectral linting rules defining API design standards and conventions for Harness.
layout: rules
name: Harness API Rules
provider_name: Harness
provider_slug: harness
rule_count: 8
rules:
- description: Info title should start with "Harness"
  given: $.info
  name: info-title-prefix
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: Every operation must have a summary starting with "Harness"
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Operations must have success responses
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-properties-description
  severity: info
rules_file: rules/harness-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/harness/refs/heads/main/rules/harness-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 3
slug: harness-spectral-rules
source_filename: harness-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-prefix:\n    description: Info title should start with \"Harness\"\n    given: $.info\n    severity: warn\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^Harness\"\n\n  operation-operationId-required:\n    description: Every operation must have an operationId\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary starting with \"Harness\"\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: error\n    then:\n      field: summary\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have tags\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n\n  parameter-description-required:\n    description: Every parameter\
  \ must have a description\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  response-success-required:\n    description: Operations must have success responses\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n\n  security-global-defined:\n    description: Global security must be defined\n    given: \"$\"\n    severity: error\n    then:\n      field: security\n      function: truthy\n\n  schema-properties-description:\n    description: Schema properties should have descriptions\n    given: \"$.components.schemas[*].properties[*]\"\n    severity: info\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/harness/refs/heads/main/rules/harness-spectral-rules.yml
tags:
- DevOps
- GitOps
- Internal Developer Portal
- Lifecycle
- Software Delivery
- Spectral
- Linting
- API Governance
---
