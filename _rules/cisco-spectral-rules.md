---
categories:
- info
- operation
- parameter
- paths
- response
- schema
- security
description: Spectral linting rules defining API design standards and conventions for Cisco.
layout: rules
name: Cisco API Rules
provider_name: Cisco
provider_slug: cisco
rule_count: 12
rules:
- description: Info title should start with "Cisco"
  given: $.info
  name: info-title-prefix
  severity: warn
- description: Info description must be present
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
- description: Operation summaries should start with "Cisco"
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
- description: API keys should be sent in headers
  given: $.components.securitySchemes[*]
  name: security-api-key-header
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-properties-description
  severity: info
rules_file: rules/cisco-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cisco/refs/heads/main/rules/cisco-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 1
  warn: 6
slug: cisco-spectral-rules
source_filename: cisco-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-prefix:\n    description: Info title should start with \"Cisco\"\n    given: $.info\n    severity: warn\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^Cisco\"\n\n  info-description-required:\n    description: Info description must be present\n    given: $.info\n    severity: error\n    then:\n      field: description\n      function: truthy\n\n  paths-kebab-case:\n    description: Paths should use kebab-case\n    given: $.paths\n    severity: warn\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^/[a-z0-9\\\\-/{}_]+$\"\n\n  operation-operationId-required:\n    description: Every operation must have an operationId\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    given: \"$.paths[*][get,post,put,patch,delete]\"\
  \n    severity: error\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Cisco\"\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: warn\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Cisco\"\n\n  operation-tags-required:\n    description: Every operation must have tags\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n\n  parameter-description-required:\n    description: Every parameter must have a description\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  response-success-required:\n    description: Every operation must have a success response\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    severity: error\n    then:\n\
  \      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  security-global-defined:\n    description: Global security must be defined\n    given: \"$\"\n    severity: error\n    then:\n      field: security\n      function: truthy\n\n  security-api-key-header:\n    description: API keys should be sent in headers\n    given: \"$.components.securitySchemes[*]\"\n    severity: warn\n    then:\n      field: in\n      function: enumeration\n      functionOptions:\n        values: [header]\n\n  schema-properties-description:\n    description: Schema properties should have descriptions\n    given: \"$.components.schemas[*].properties[*]\"\n    severity: info\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cisco/refs/heads/main/rules/cisco-spectral-rules.yml
tags:
- Collaboration
- Enterprise
- Networking
- Security
- SD-WAN
- Spectral
- Linting
- API Governance
---
