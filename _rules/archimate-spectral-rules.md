---
api_specs:
- filename: archimate-model-exchange-api.yaml
  format: yaml
  label: ArchiMate Model Exchange API
  slug: archimate-model-exchange-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/openapi/archimate-model-exchange-api.yaml
- filename: archimate-repository-api.yaml
  format: yaml
  label: ArchiMate Repository API
  slug: archimate-repository-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/openapi/archimate-repository-api.yaml
categories:
- delete
- get
- info
- openapi
- operation
- parameter
- response
- security
- servers
description: Spectral linting rules defining API design standards and conventions for ArchiMate.
layout: rules
name: ArchiMate API Rules
provider_name: ArchiMate
provider_slug: archimate
rule_count: 14
rules:
- description: API title must start with "ArchiMate"
  given: $.info
  name: info-title-archimate-prefix
  severity: error
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: warn
- description: API must specify a version
  given: $.info
  name: info-version-required
  severity: error
- description: Use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: Server URLs must be defined
  given: $
  name: servers-defined
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "ArchiMate"
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-prefix
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: error
- description: All parameters must have a description
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All operations must define a success response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations must not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 204
  given: $.paths[*].delete.responses
  name: delete-returns-204
  severity: info
rules_file: rules/archimate-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/rules/archimate-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 1
  warn: 3
slug: archimate-spectral-rules
source_filename: archimate-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-archimate-prefix:\n    description: API title must start with \"ArchiMate\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^ArchiMate\"\n  info-description-required:\n    description: API must have a description\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API must specify a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n  openapi-version-3:\n    description: Use OpenAPI 3.0.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n  servers-defined:\n    description: Server URLs must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n  operation-id-required:\n\
  \    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n  operation-summary-prefix:\n    description: Operation summaries should start with \"ArchiMate\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^ArchiMate\"\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n  parameter-description-required:\n    description: All parameters must have a description\n\
  \    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n  response-success-required:\n    description: All operations must define a success response\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n  get-no-request-body:\n    description: GET operations must not have request bodies\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n  delete-returns-204:\n    description: DELETE operations should return 204\n    severity: info\n    given: \"$.paths[*].delete.responses\"\n    then:\n      field: \"204\"\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/rules/archimate-spectral-rules.yml
tags:
- Enterprise Architecture
- Architecture Framework
- Modeling Language
- Business Architecture
- Technology Architecture
- Standard
- Open Group
- Spectral
- Linting
- API Governance
---
