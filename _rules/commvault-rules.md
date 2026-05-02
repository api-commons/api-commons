---
api_specs:
- filename: commvault-rest-openapi.yml
  format: yaml
  label: Commvault REST API
  slug: rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/commvault/refs/heads/main/openapi/commvault-rest-openapi.yml
- filename: commvault-command-center-openapi.yml
  format: yaml
  label: Commvault Command Center API
  slug: command-center-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/commvault/refs/heads/main/openapi/commvault-command-center-openapi.yml
- filename: commvault-automation-openapi.yml
  format: yaml
  label: Commvault Automation API
  slug: automation-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/commvault/refs/heads/main/openapi/commvault-automation-openapi.yml
categories:
- commvault
description: Spectral linting rules defining API design standards and conventions for Commvault.
layout: rules
name: Commvault API Rules
provider_name: Commvault
provider_slug: commvault
rule_count: 10
rules:
- description: API contact information must be present.
  given: $.info
  name: commvault-info-contact
  severity: error
- description: API terms of service must be declared.
  given: $.info
  name: commvault-info-terms
  severity: warn
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: commvault-server-https
  severity: error
- description: Server URLs should resolve to a Commvault Web Server endpoint.
  given: $.servers[*].url
  name: commvault-server-webconsole
  severity: warn
- description: An Authtoken QSDK security scheme must be defined.
  given: $.components.securitySchemes
  name: commvault-authtoken-security
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: commvault-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: commvault-operation-summary
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: commvault-operation-id
  severity: error
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: commvault-error-responses
  severity: warn
- description: Backup, restore, and reporting paths should expose job resources.
  given: $.paths
  name: commvault-job-resources
  severity: info
rules_file: rules/commvault-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/commvault/refs/heads/main/rules/commvault-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 5
slug: commvault-rules
source_filename: commvault-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules tuned for Commvault REST APIs.\n# Enforces conventions described at\n# https://documentation.commvault.com/v11/essential/rest_api_overview.html\n# Authentication is via QSDK token sent in the Authtoken header,\n# JSON request and response bodies, and resource-oriented paths.\nrules:\n  commvault-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  commvault-info-terms:\n    description: API terms of service must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: termsOfService\n      function: truthy\n\n  commvault-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  commvault-server-webconsole:\n    description:\
  \ Server URLs should resolve to a Commvault Web Server endpoint.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/(webconsole|commandcenter)/api\"\n\n  commvault-authtoken-security:\n    description: An Authtoken QSDK security scheme must be defined.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  commvault-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  commvault-operation-summary:\n    description: Every operation must include a short summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  commvault-operation-id:\n\
  \    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  commvault-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n\n  commvault-job-resources:\n    description: Backup, restore, and reporting paths should expose job resources.\n    severity: info\n    given: \"$.paths\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/commvault/refs/heads/main/rules/commvault-rules.yml
tags:
- Backup
- Cloud Storage
- Cyber Recovery
- Data Management
- Data Protection
- Disaster Recovery
- Enterprise Software
- Spectral
- Linting
- API Governance
---
