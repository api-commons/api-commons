---
api_specs:
- filename: amazon-polly-openapi.yml
  format: yaml
  label: Amazon Polly API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-polly/refs/heads/main/openapi/amazon-polly-openapi.yml
categories:
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Polly.
layout: rules
name: Amazon Polly API Rules
provider_name: Amazon Polly
provider_slug: amazon-polly
rule_count: 22
rules:
- description: API title must reference Amazon Polly
  given: $.info.title
  name: info-title-contains-amazon-polly
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: API should use OpenAPI 3.x
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Path segments must use kebab-case or camelCase
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: All paths should start with /v1/
  given: $.paths
  name: paths-v1-prefix
  severity: info
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Summaries must begin with 'Amazon Polly'
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amazon-polly-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: All operations must have a success response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schemas must define a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should provide examples
  given: $.paths[*][*].responses[*].content[*]
  name: operation-examples-encouraged
  severity: info
rules_file: rules/amazon-polly-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-polly/refs/heads/main/rules/amazon-polly-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 3
  warn: 7
slug: amazon-polly-spectral-rules
source_filename: amazon-polly-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-contains-amazon-polly:\n    description: API title must reference Amazon Polly\n    message: Info title should contain 'Amazon Polly'\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"Amazon Polly\"\n\n  info-description-required:\n    description: API must have a description\n    message: Info object must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API version must be defined\n    message: Info object must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: API should use OpenAPI 3.x\n    message: Spec must use OpenAPI 3.0 or higher\n    severity: error\n    given: $.openapi\n    then:\n      function: pattern\n     \
  \ functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined\n    message: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS\n    message: Server URL must use HTTPS\n    severity: warn\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https\"\n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments must use kebab-case or camelCase\n    message: Path segments must use lowercase characters\n    severity: info\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-zA-Z0-9{}_/-]+)+$\"\n\n  paths-v1-prefix:\n    description: All paths should start with /v1/\n    message: Paths should be prefixed with /v1/\n    severity: info\n    given: $.paths\n \
  \   then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^/v1/\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    message: Operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-amazon-polly-prefix:\n    description: Summaries must begin with 'Amazon Polly'\n    message: Operation summary must start with 'Amazon Polly'\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Polly\"\n\n  operation-description-required:\n    description: All operations must have a description\n    message: Operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n\
  \    description: All operations must have an operationId\n    message: Operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: All operations must have tags\n    message: Operation must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have descriptions\n    message: Parameter must have a description\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: All operations must have a success response\n    message: Operation must define at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n\
  \    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: All responses must have descriptions\n    message: Response must have a description\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-type-defined:\n    description: Schemas must define a type\n    message: Schema must have a type defined\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined\n    message: Components must define securitySchemes\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security must be defined\n    message: Global security requirements should be defined\n    severity: warn\n    given: $\n    then:\n\
  \      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    message: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    message: Description must not be empty\n    severity: warn\n    given: $..description\n    then:\n      function: truthy\n\n  operation-examples-encouraged:\n    description: Operations should provide examples\n    message: Consider adding examples to operation responses\n    severity: info\n    given: $.paths[*][*].responses[*].content[*]\n    then:\n      field: examples\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-polly/refs/heads/main/rules/amazon-polly-spectral-rules.yml
tags:
- AI
- Machine Learning
- Speech Synthesis
- Text-To-Speech
- TTS
- Voice
- SSML
- Neural Engine
- Generative AI
- Spectral
- Linting
- API Governance
---
