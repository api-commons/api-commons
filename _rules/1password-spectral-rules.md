---
api_specs:
- filename: 1password-connect-openapi.yml
  format: yaml
  label: 1Password Connect Server API
  slug: 1password-connect-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/openapi/1password-connect-openapi.yml
- filename: 1password-events-openapi.yml
  format: yaml
  label: 1Password Events API
  slug: 1password-events-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/openapi/1password-events-openapi.yml
- filename: 1password-partnership-openapi.yml
  format: yaml
  label: 1Password Partnership API
  slug: 1password-partnership-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/openapi/1password-partnership-openapi.yml
categories:
- delete
- examples
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- request
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for 1Password.
layout: rules
name: 1Password API Rules
provider_name: 1Password
provider_slug: 1password
rule_count: 30
rules:
- description: Info title should follow "1Password ..." pattern.
  given: $.info.title
  name: info-title-pattern
  severity: warn
- description: Info description must be present and at least 50 characters.
  given: $.info
  name: info-description-required
  severity: warn
- description: API version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information should be provided.
  given: $.info
  name: info-contact-required
  severity: info
- description: Must use OpenAPI 3.0.x or 3.1.x.
  given: $
  name: openapi-version-3
  severity: error
- description: Servers array must be defined and non-empty.
  given: $
  name: servers-must-be-defined
  severity: error
- description: Production server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https-required
  severity: error
- description: Paths must not end with a trailing slash.
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Path segments should use kebab-case.
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: warn
- description: Every operation summary should start with "1Password".
  given: $.paths[*][get,post,put,patch,delete,options,head].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-operationid-required
  severity: error
- description: OperationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete,options,head].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: error
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][get,post,put,patch,delete,options,head].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies must define content type.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-content-required
  severity: error
- description: Every operation must define at least one success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head].responses[*]
  name: response-description-required
  severity: error
- description: Authenticated APIs should define a 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-for-authenticated-apis
  severity: warn
- description: Component schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
- description: Schema properties should have explicit types.
  given: $.components.schemas[*].properties[*]
  name: schema-properties-typed
  severity: warn
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Bearer token security should use HTTP Bearer scheme.
  given: $.components.securitySchemes[?(@.type == 'http' && @.scheme == 'bearer')]
  name: security-bearer-format
  severity: info
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 204 No Content.
  given: $.paths[*].delete.responses
  name: delete-returns-204
  severity: info
- description: Descriptions must not be empty.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-on-schemas
  severity: info
- description: Global tags should use Title Case naming.
  given: $.tags[*].name
  name: tags-title-case
  severity: warn
rules_file: rules/1password-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/rules/1password-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 6
  warn: 11
slug: 1password-spectral-rules
source_filename: 1password-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-pattern:\n    description: Info title should follow \"1Password ...\" pattern.\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^1Password \"\n\n  info-description-required:\n    description: Info description must be present and at least 50 characters.\n    severity: warn\n    given: $.info\n    then:\n      field: description\n      function: minLength\n      functionOptions:\n        value: 50\n\n  info-version-required:\n    description: API version must be defined.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Contact information should be provided.\n    severity: info\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.0.x or 3.1.x.\n    severity: error\n\
  \    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-must-be-defined:\n    description: Servers array must be defined and non-empty.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-required:\n    description: Production server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*]\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash.\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  paths-kebab-case:\n    description: Path segments should use kebab-case.\n    severity: info\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        notMatch:\
  \ \"_\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Every operation should have a description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: description\n      function: truthy\n\n  operation-summary-prefix:\n    description: Every operation summary should start with \"1Password\".\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,options,head].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^1Password \"\n\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: operationId\n\
  \      function: truthy\n\n  operation-operationid-camelcase:\n    description: OperationId should use camelCase.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,options,head].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,options,head].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must have a schema.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head].parameters[*]\n    then:\n\
  \      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-content-required:\n    description: Request bodies must define content type.\n    severity: error\n    given: $.paths[*][post,put,patch].requestBody\n    then:\n      field: content\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one success response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-401-for-authenticated-apis:\n    description: Authenticated APIs should define a 401 Unauthorized response.\n  \
  \  severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            '401':\n              type: object\n\n  # SCHEMAS\n  schema-description-recommended:\n    description: Component schemas should have descriptions.\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-properties-typed:\n    description: Schema properties should have explicit types.\n    severity: warn\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-bearer-format:\n    description: Bearer token security should use HTTP\
  \ Bearer scheme.\n    severity: info\n    given: $.components.securitySchemes[?(@.type == 'http' && @.scheme == 'bearer')]\n    then:\n      field: bearerFormat\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-returns-204:\n    description: DELETE operations should return 204 No Content.\n    severity: info\n    given: $.paths[*].delete.responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            '204':\n              type: object\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty.\n    severity: warn\n    given: $..description\n    then:\n      function: truthy\n\n  examples-on-schemas:\n    description: Schema properties should include example values.\n\
  \    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: example\n      function: truthy\n\n  tags-title-case:\n    description: Global tags should use Title Case naming.\n    severity: warn\n    given: $.tags[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z]\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/rules/1password-spectral-rules.yml
tags:
- Password Manager
- Passwords
- Security
- Secrets
- Spectral
- Linting
- API Governance
---
