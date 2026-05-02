---
api_specs:
- filename: argo-cd-openapi.json
  format: json
  label: Argo CD API
  slug: argo-cd
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/argo-cd/refs/heads/main/openapi/argo-cd-openapi.json
categories:
- get
- info
- 'no'
- operation
- parameter
- paths
- response
- security
description: Spectral linting rules defining API design standards and conventions for Argo CD.
layout: rules
name: Argo CD API Rules
provider_name: Argo CD
provider_slug: argo-cd
rule_count: 18
rules:
- description: API title must start with "Argo CD"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Argo CD"
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-title-case
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationid-required
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: All paths should be versioned with /api/v1/
  given: $.paths[*]~
  name: paths-versioned
  severity: info
- description: All parameters must have a description
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have a success response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: API must define security schemes
  given: $
  name: security-definitions-required
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Summaries must not be empty strings
  given: $.paths[*][get,post,put,delete,patch].summary
  name: no-empty-summaries
  severity: error
- description: OperationIds should use camelCase or ServiceName_MethodName pattern
  given: $.paths[*][get,post,put,delete,patch].operationId
  name: operation-id-camel-case
  severity: info
rules_file: rules/argo-cd-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/argo-cd/refs/heads/main/rules/argo-cd-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 2
  warn: 9
slug: argo-cd-spectral-rules
source_filename: argo-cd-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Argo CD API Spectral Ruleset\n# Enforces conventions observed in the Argo CD REST API (swagger 2.0)\n\nrules:\n\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"Argo CD\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Argo CD\"\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-title-case:\n    description:\
  \ Operation summaries must start with \"Argo CD\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Argo CD\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PATHS - NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use\
  \ kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/api/v[0-9]+)?(/[a-z0-9{}-]+)*$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  paths-versioned:\n    description: All paths should be versioned with /api/v1/\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/api/v\"\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a success response\n    severity: error\n\
  \    given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description: All responses must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-definitions-required:\n    description: API must define security schemes\n    severity: warn\n    given: \"$\"\n    then:\n      field: securityDefinitions\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: body\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-summaries:\n    description: Summaries must not be empty strings\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\
  \n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  operation-id-camel-case:\n    description: OperationIds should use camelCase or ServiceName_MethodName pattern\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Za-z][A-Za-z0-9_]*$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/argo-cd/refs/heads/main/rules/argo-cd-spectral-rules.yml
tags:
- Continuous Delivery
- Containers
- Deployment
- GitOps
- Kubernetes
- CNCF
- Open Source
- Spectral
- Linting
- API Governance
---
