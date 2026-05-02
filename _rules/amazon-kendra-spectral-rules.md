---
api_specs:
- filename: openapi.yaml
  format: yaml
  label: Amazon Kendra API
  slug: ''
  spec_type: OpenAPI
  url: https://api.apis.guru/v2/specs/amazonaws.com/kendra/2019-02-03/openapi.yaml
categories:
- info
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Kendra.
layout: rules
name: Amazon Kendra API Rules
provider_name: Amazon Kendra
provider_slug: amazon-kendra
rule_count: 17
rules:
- description: API title must start with "Amazon Kendra"
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Summaries must start with "Amazon Kendra"
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationid-required
  severity: error
- description: All operations must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All operations must have a 2xx response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-required
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-required
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Schema components should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
rules_file: rules/amazon-kendra-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-kendra/refs/heads/main/rules/amazon-kendra-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 0
  warn: 7
slug: amazon-kendra-spectral-rules
source_filename: amazon-kendra-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-format:\n    description: API title must start with \"Amazon Kendra\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Kendra\"\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n\
  \      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Summaries must start with \"Amazon Kendra\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Kendra\"\n\n  operation-description-required:\n    description: All operations must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n\
  \    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: All operations must have tags\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: All operations must have a 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  # SECURITY\n  security-schemes-required:\n\
  \    description: Security schemes must be defined\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-required:\n    description: Global security must be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n\n  # SCHEMAS\n  schema-description-required:\n    description: Schema components should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-kendra/refs/heads/main/rules/amazon-kendra-spectral-rules.yml
tags:
- AI
- Enterprise Search
- Knowledge Management
- Machine Learning
- Natural Language
- Spectral
- Linting
- API Governance
---
