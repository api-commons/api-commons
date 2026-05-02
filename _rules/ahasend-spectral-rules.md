---
api_specs:
- filename: ahasend-openapi.yml
  format: yaml
  label: AhaSend
  slug: ahasend
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/ahasend/refs/heads/main/openapi/ahasend-openapi.yml
categories:
- delete
- get
- idempotency
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
description: Spectral linting rules defining API design standards and conventions for AhaSend.
layout: rules
name: AhaSend API Rules
provider_name: AhaSend
provider_slug: ahasend
rule_count: 28
rules:
- description: API title must start with "AhaSend"
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API must have a non-empty description
  given: $.info
  name: info-description-required
  severity: error
- description: API must specify a version
  given: $.info
  name: info-version-required
  severity: error
- description: API contact email should be provided
  given: $.info.contact
  name: info-contact-email
  severity: warn
- description: Use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: warn
- description: Servers array must be defined and non-empty
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Path segments must use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not end with a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "AhaSend"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should have a description
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: Operations must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schema properties should have a type defined
  given: $.components.schemas[*].properties[*]
  name: schema-type-required
  severity: warn
- description: Security schemes must be defined
  given: $.components.securitySchemes
  name: security-schemes-defined
  severity: error
- description: Bearer auth token format should be documented
  given: $.components.securitySchemes[*][?(@.scheme == 'bearer')]
  name: security-bearer-format
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: POST endpoints should document idempotency key header support
  given: $.paths[*].post.parameters[*]
  name: idempotency-key-documented
  severity: info
rules_file: rules/ahasend-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/ahasend/refs/heads/main/rules/ahasend-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 3
  warn: 14
slug: ahasend-spectral-rules
source_filename: ahasend-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: \"spectral:oas\"\n\nrules:\n\n  # INFO / METADATA\n  info-title-format:\n    description: API title must start with \"AhaSend\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AhaSend\"\n\n  info-description-required:\n    description: API must have a non-empty description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must specify a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-email:\n    description: API contact email should be provided\n    severity: warn\n    given: \"$.info.contact\"\n    then:\n      field: email\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Use OpenAPI 3.x\n    severity: warn\n    given: \"$\"\n    then:\n      field: openapi\n      function:\
  \ truthy\n\n  # SERVERS\n  servers-defined:\n    description: Servers array must be defined and non-empty\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments must use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(\\/([a-z0-9{}-])+)*\\/?$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n\
  \    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"AhaSend\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AhaSend\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId must use camelCase\n    severity: warn\n    given:\
  \ \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have a description\n    severity:\
  \ warn\n    given: \"$.paths[*][post,put,patch].requestBody\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must have a 2xx success response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          oneOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-property-description:\n    description: Top-level schema properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function:\
  \ truthy\n\n  schema-type-required:\n    description: Schema properties should have a type defined\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  security-bearer-format:\n    description: Bearer auth token format should be documented\n    severity: info\n    given: \"$.components.securitySchemes[*][?(@.scheme == 'bearer')]\"\n    then:\n      field: bearerFormat\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n \
  \   severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: truthy\n\n  idempotency-key-documented:\n    description: POST endpoints should document idempotency key header support\n    severity: info\n    given: \"$.paths[*].post.parameters[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          properties:\n            name: {}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/ahasend/refs/heads/main/rules/ahasend-spectral-rules.yml
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
- Spectral
- Linting
- API Governance
---
