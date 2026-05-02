---
categories:
- info
- operation
- parameter
- paths
- response
- schema
- security
description: Spectral linting rules defining API design standards and conventions for SAP Concur.
layout: rules
name: SAP Concur API Rules
provider_name: SAP Concur
provider_slug: concur
rule_count: 11
rules:
- description: Info title must be present and start with "SAP Concur"
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present with minimum length
  given: $.info
  name: info-description-required
  severity: error
- description: Paths should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "SAP Concur"
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have a success response
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
rules_file: rules/concur-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/concur/refs/heads/main/rules/concur-spectral-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 1
  warn: 4
slug: concur-spectral-rules
source_filename: concur-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be present and start with \"SAP Concur\"\n    given: $.info\n    severity: error\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^SAP Concur\"\n\n  info-description-required:\n    description: Info description must be present with minimum length\n    given: $.info\n    severity: error\n    then:\n      field: description\n      function: truthy\n\n  # PATHS\n  paths-kebab-case:\n    description: Paths should use kebab-case\n    given: $.paths\n    severity: warn\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^/[a-z0-9\\\\-/{}_]+$\"\n\n  # OPERATIONS\n  operation-operationId-required:\n    description: Every operation must have an operationId\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n\n  operation-summary-required:\n\
  \    description: Every operation must have a summary\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: error\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"SAP Concur\"\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: warn\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^SAP Concur\"\n\n  operation-tags-required:\n    description: Every operation must have tags\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description:\
  \ Every operation must have a success response\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  # SECURITY\n  security-global-defined:\n    description: Global security must be defined\n    given: \"$\"\n    severity: error\n    then:\n      field: security\n      function: truthy\n\n  # SCHEMAS\n  schema-properties-description:\n    description: Schema properties should have descriptions\n    given: \"$.components.schemas[*].properties[*]\"\n    severity: info\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/concur/refs/heads/main/rules/concur-spectral-rules.yml
tags:
- Expense Management
- Finance
- Invoice
- SAP
- Travel
- Spectral
- Linting
- API Governance
---
