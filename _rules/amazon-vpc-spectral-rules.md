---
api_specs:
- filename: amazon-vpc-openapi.yml
  format: yaml
  label: Amazon VPC API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc/refs/heads/main/openapi/amazon-vpc-openapi.yml
categories:
- info
- operation
- parameter
- security
description: Spectral linting rules defining API design standards and conventions for Amazon VPC.
layout: rules
name: Amazon VPC API Rules
provider_name: Amazon VPC
provider_slug: amazon-vpc
rule_count: 8
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
- description: Operation summaries must start with 'Amazon VPC'.
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
- description: Security schemes must be defined.
  given: $.components
  name: security-schemes-defined
  severity: warn
rules_file: rules/amazon-vpc-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc/refs/heads/main/rules/amazon-vpc-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 5
slug: amazon-vpc-spectral-rules
source_filename: amazon-vpc-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  info-title-required:\n    description: Info title must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  info-description-required:\n    description: Info description must be present.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: summary\n      function: truthy\n  operation-summary-prefix:\n    description: Operation summaries must start with 'Amazon VPC'.\n    severity: warn\n    given: \"$.paths[*][*].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon VPC\"\n  operation-operationId-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n   \
  \   field: operationId\n      function: truthy\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes must be defined.\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc/refs/heads/main/rules/amazon-vpc-spectral-rules.yml
tags:
- Networking
- Private Cloud
- Security
- Subnets
- VPC
- Spectral
- Linting
- API Governance
---
