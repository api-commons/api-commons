---
categories:
- cloudhealth
description: Spectral linting rules defining API design standards and conventions for CloudHealth.
layout: rules
name: CloudHealth API Rules
provider_name: CloudHealth
provider_slug: cloudhealth
rule_count: 10
rules:
- description: API contact information must be present.
  given: $.info
  name: cloudhealth-info-contact
  severity: error
- description: API license must be declared.
  given: $.info
  name: cloudhealth-info-license
  severity: warn
- description: All server URLs must use HTTPS for the chapi.cloudhealthtech.com control plane.
  given: $.servers[*].url
  name: cloudhealth-server-https
  severity: error
- description: Server URLs should target chapi.cloudhealthtech.com.
  given: $.servers[*].url
  name: cloudhealth-server-host
  severity: warn
- description: CloudHealth REST API paths should be versioned (/v{N}/) where applicable.
  given: $.paths
  name: cloudhealth-versioned-paths
  severity: warn
- description: A bearer security scheme must be declared.
  given: $.components.securitySchemes
  name: cloudhealth-auth-required
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudhealth-operation-id
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudhealth-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudhealth-operation-summary
  severity: warn
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: cloudhealth-error-responses
  severity: warn
rules_file: rules/cloudhealth-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/rules/cloudhealth-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 6
slug: cloudhealth-rules
source_filename: cloudhealth-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for any OpenAPI describing the CloudHealth REST\n# API at chapi.cloudhealthtech.com.\nrules:\n  cloudhealth-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cloudhealth-info-license:\n    description: API license must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  cloudhealth-server-https:\n    description: All server URLs must use HTTPS for the chapi.cloudhealthtech.com control plane.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cloudhealth-server-host:\n    description: Server URLs should target chapi.cloudhealthtech.com.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n\
  \        match: \"chapi\\\\.cloudhealthtech\\\\.com\"\n\n  cloudhealth-versioned-paths:\n    description: CloudHealth REST API paths should be versioned (/v{N}/) where applicable.\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          patternProperties:\n            \"^/(v\\\\d+/.*|olap_reports/.*)\": {}\n          additionalProperties: true\n\n  cloudhealth-auth-required:\n    description: A bearer security scheme must be declared.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  cloudhealth-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  cloudhealth-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given:\
  \ \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cloudhealth-operation-summary:\n    description: Every operation must include a short summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  cloudhealth-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/rules/cloudhealth-rules.yml
tags:
- Cloud Cost
- Cloud Governance
- Cloud Management
- Cost Optimization
- FinOps
- Multi-Cloud
- Spectral
- Linting
- API Governance
---
