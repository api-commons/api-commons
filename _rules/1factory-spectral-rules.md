---
api_specs:
- filename: 1factory-openapi.json
  format: json
  label: 1Factory API
  slug: 1factory
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/1factory/refs/heads/main/openapi/1factory-openapi.json
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
- tag
description: Spectral linting rules defining API design standards and conventions for 1Factory.
layout: rules
name: 1Factory API Rules
provider_name: 1Factory
provider_slug: 1factory
rule_count: 32
rules:
- description: Info title must be present and follow "1Factory ..." pattern.
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present and at least 50 characters.
  given: $.info
  name: info-description-required
  severity: warn
- description: API version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information must be provided.
  given: $.info
  name: info-contact-required
  severity: warn
- description: Terms of service URL should be provided.
  given: $.info
  name: info-terms-of-service
  severity: info
- description: Must use OpenAPI 3.0.x.
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
- description: Each server must have a description.
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Paths must not end with a trailing slash.
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Paths must not contain query strings.
  given: $.paths
  name: paths-no-query-string
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: warn
- description: Every operation summary should start with "1Factory".
  given: $.paths[*][get,post,put,patch,delete,options,head].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: error
- description: Global tags must have descriptions.
  given: $.tags[*]
  name: tag-descriptions-required
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][get,post,put,patch,delete,options,head].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should have a description.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete,options,head].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head].responses[*]
  name: response-description-required
  severity: error
- description: APIs using API key auth should define a 401 response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Rate-limited APIs should define a 429 response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-429-rate-limit
  severity: info
- description: Top-level component schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas should define a type.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: API keys should be passed in headers, not query parameters.
  given: $.components.securitySchemes[*][?(@.type == 'apiKey')]
  name: security-api-key-in-header
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions should not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/1factory-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/1factory/refs/heads/main/rules/1factory-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 4
  warn: 15
slug: 1factory-spectral-rules
source_filename: 1factory-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be present and follow \"1Factory ...\" pattern.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info description must be present and at least 50 characters.\n    severity: warn\n    given: $.info\n    then:\n      field: description\n      function: minLength\n      functionOptions:\n        value: 50\n\n  info-version-required:\n    description: API version must be defined.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Contact information must be provided.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  info-terms-of-service:\n    description: Terms of service URL should be provided.\n    severity: info\n    given: $.info\n    then:\n      field:\
  \ termsOfService\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.0.x.\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-must-be-defined:\n    description: Servers array must be defined and non-empty.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-required:\n    description: Production server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*]\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description-required:\n    description: Each server must have a description.\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-no-trailing-slash:\n    description: Paths must\
  \ not end with a trailing slash.\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  paths-no-query-string:\n    description: Paths must not contain query strings.\n    severity: error\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\?\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Every operation should have a description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: description\n      function: truthy\n\n  operation-summary-prefix:\n    description: Every operation summary should start with \"1Factory\".\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,options,head].summary\n\
  \    then:\n      function: pattern\n      functionOptions:\n        match: \"^1Factory \"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tag-descriptions-required:\n    description: Global tags must have descriptions.\n    severity: warn\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,options,head].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must have a schema.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head].parameters[*]\n    then:\n      field: schema\n\
  \      function: truthy\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have a description.\n    severity: info\n    given: $.paths[*][post,put,patch].requestBody\n    then:\n      field: description\n      function: truthy\n\n  request-body-json-content:\n    description: Request bodies should use application/json content type.\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - application/json\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one 2xx response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description:\
  \ Every response must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-401-required:\n    description: APIs using API key auth should define a 401 response.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            '401':\n              type: object\n\n  response-429-rate-limit:\n    description: Rate-limited APIs should define a 429 response.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            '429':\n              type: object\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description-required:\n    description: Top-level component\
  \ schemas should have descriptions.\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schemas should define a type.\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-api-key-in-header:\n    description: API keys should be passed in headers, not query parameters.\n    severity: warn\n    given: $.components.securitySchemes[*][?(@.type == 'apiKey')]\n    then:\n      field: in\n      function: enumeration\n      functionOptions:\n        values:\n          - header\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity:\
  \ error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions should not be empty strings.\n    severity: warn\n    given: $..description\n    then:\n      function: truthy\n\n  examples-encouraged:\n    description: Schema properties should include example values.\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: example\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/1factory/refs/heads/main/rules/1factory-spectral-rules.yml
tags:
- Analytics
- Data Collection
- Manufacturing
- Monitoring
- Quality
- Spectral
- Linting
- API Governance
---
