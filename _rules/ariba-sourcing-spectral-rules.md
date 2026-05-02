---
api_specs:
- filename: ariba-sourcing-external-approval-api.yaml
  format: yaml
  label: Ariba Sourcing - External Approval API
  slug: ariba-sourcing-external-approval-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/ariba-sourcing/refs/heads/main/openapi/ariba-sourcing-external-approval-api.yaml
categories:
- get
- info
- microcks
- openapi
- operation
- parameter
- paths
- rate
- request
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Ariba Sourcing.
layout: rules
name: Ariba Sourcing API Rules
provider_name: Ariba Sourcing
provider_slug: ariba-sourcing
rule_count: 28
rules:
- description: API title must be defined and follow the "Ariba Sourcing - {API Name}" pattern.
  given: $.info
  name: info-title-required
  severity: error
- description: API title should start with "Ariba Sourcing".
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API info must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: APIs must use OpenAPI 3.0.x.
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined.
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Production server should use openapi.ariba.com host.
  given: $.servers[*].url
  name: servers-openapi-ariba-host
  severity: warn
- description: Paths must not have a trailing slash.
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Ariba Sourcing".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: SAP Ariba APIs require a realm query parameter.
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.name == 'realm')]
  name: parameter-realm-required
  severity: info
- description: Request bodies should have a description.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description-recommended
  severity: warn
- description: Every operation must have a success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should define a 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-recommended
  severity: warn
- description: Operations should define a 500 Internal Server Error response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-500-recommended
  severity: warn
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Schema properties should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: schema-property-description-recommended
  severity: info
- description: Security schemes must be defined in components.
  given: $.components.securitySchemes
  name: security-schemes-defined
  severity: error
- description: OAuth2 token URL should use api.ariba.com.
  given: $.components.securitySchemes.OAuth2.flows.clientCredentials.tokenUrl
  name: security-oauth2-token-url
  severity: warn
- description: Rate limit information should be documented in the API description.
  given: $.info.description
  name: rate-limits-documented
  severity: info
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Operations should include x-microcks-operation.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/ariba-sourcing-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/ariba-sourcing/refs/heads/main/rules/ariba-sourcing-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 4
  warn: 9
slug: ariba-sourcing-spectral-rules
source_filename: ariba-sourcing-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: API title must be defined and follow the \"Ariba Sourcing - {API Name}\" pattern.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: API title should start with \"Ariba Sourcing\".\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Ariba Sourcing\"\n\n  info-description-required:\n    description: API info must have a description.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API version must be defined.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: APIs must use OpenAPI 3.0.x.\n    severity: error\n    given: $\n    then:\n      field:\
  \ openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: Servers must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-openapi-ariba-host:\n    description: Production server should use openapi.ariba.com host.\n    severity: warn\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"openapi\\\\.ariba\\\\.com\"\n\n  # PATHS\n  paths-no-trailing-slash:\n    description: Paths must not have a trailing slash.\n    severity: warn\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n\
  \    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Ariba Sourcing\".\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Ariba Sourcing\"\n\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase.\n    severity:\
  \ warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-realm-required:\n    description: SAP Ariba APIs require a realm query parameter.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].parameters[?(@.name == 'realm')]\n    then:\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-description-recommended:\n    description: Request bodies should have a description.\n\
  \    severity: warn\n    given: $.paths[*][post,put,patch].requestBody\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a success response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-401-recommended:\n    description: Operations should define a 401 Unauthorized response.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '401'\n      function: truthy\n\n  response-500-recommended:\n    description: Operations should define a 500 Internal Server Error response.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '500'\n      function: truthy\n\
  \n  response-description-required:\n    description: All responses must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-property-description-recommended:\n    description: Schema properties should have descriptions.\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: $.components.securitySchemes\n    then:\n      function: truthy\n\n  security-oauth2-token-url:\n    description: OAuth2 token URL should use api.ariba.com.\n    severity: warn\n    given: $.components.securitySchemes.OAuth2.flows.clientCredentials.tokenUrl\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api\\\\.ariba\\\\.com\"\n\n  #\
  \ RATE LIMITING\n  rate-limits-documented:\n    description: Rate limit information should be documented in the API description.\n    severity: info\n    given: $.info.description\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(?i)(rate limit|requests per)\"\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  microcks-operation-extension:\n    description: Operations should include x-microcks-operation.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/ariba-sourcing/refs/heads/main/rules/ariba-sourcing-spectral-rules.yml
tags:
- Approvals
- Auctions
- B2B
- Contracts
- Procurement
- RFx
- SAP
- Sourcing
- Supplier Management
- Supply Chain
- Spectral
- Linting
- API Governance
---
