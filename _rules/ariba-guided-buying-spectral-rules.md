---
api_specs:
- filename: ariba-guided-buying-catalog-shop-api.yaml
  format: yaml
  label: Ariba Guided Buying - Public Catalogs Shop API
  slug: ariba-guided-buying-catalog-shop-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/ariba-guided-buying/refs/heads/main/openapi/ariba-guided-buying-catalog-shop-api.yaml
- filename: ariba-guided-buying-asset-management-api.yaml
  format: yaml
  label: Ariba Guided Buying - Asset Management API
  slug: ariba-guided-buying-asset-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/ariba-guided-buying/refs/heads/main/openapi/ariba-guided-buying-asset-management-api.yaml
categories:
- delete
- get
- info
- microcks
- openapi
- operation
- parameter
- paths
- request
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Ariba Guided Buying.
layout: rules
name: Ariba Guided Buying API Rules
provider_name: Ariba Guided Buying
provider_slug: ariba-guided-buying
rule_count: 34
rules:
- description: API title must be defined and follow the "Ariba Guided Buying - {API Name}" pattern.
  given: $.info
  name: info-title-required
  severity: error
- description: API title should start with "Ariba Guided Buying".
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
- description: API info should include contact information.
  given: $.info
  name: info-contact-required
  severity: warn
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
- description: Path segments must use kebab-case.
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have a trailing slash.
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Ariba Guided Buying".
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
- description: All parameters must have a schema.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Realm parameter should be named "realm" (SAP Ariba convention).
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-realm-naming
  severity: info
- description: Request bodies should have a description.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description-required
  severity: warn
- description: Request bodies should define application/json content.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must have a 200 or 201 success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should define a 400 Bad Request response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-400-recommended
  severity: warn
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
- description: Component schemas should define a type.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined in components.
  given: $.components.securitySchemes
  name: security-schemes-defined
  severity: error
- description: SAP Ariba APIs should use OAuth 2.0 with api.ariba.com token URL.
  given: $.components.securitySchemes.OAuth2.flows.clientCredentials.tokenUrl
  name: security-oauth2-ariba
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Operations should include x-microcks-operation for mock server configuration.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/ariba-guided-buying-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/ariba-guided-buying/refs/heads/main/rules/ariba-guided-buying-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 3
  warn: 15
slug: ariba-guided-buying-spectral-rules
source_filename: ariba-guided-buying-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: API title must be defined and follow the \"Ariba Guided Buying - {API Name}\" pattern.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: API title should start with \"Ariba Guided Buying\".\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Ariba Guided Buying\"\n\n  info-description-required:\n    description: API info must have a description.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API version must be defined.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should include contact information.\n    severity: warn\n    given: $.info\n    then:\n\
  \      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: APIs must use OpenAPI 3.0.x.\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: Servers must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-openapi-ariba-host:\n    description: Production server should use openapi.ariba.com host.\n    severity: warn\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"openapi\\\\.ariba\\\\.com\"\n\n  # PATHS - NAMING CONVENTIONS\n  paths-kebab-case:\n    description:\
  \ Path segments must use kebab-case.\n    severity: warn\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(\\\\/[a-zA-Z0-9{}\\\\$._-]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have a trailing slash.\n    severity: warn\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Ariba Guided Buying\".\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Ariba Guided Buying\"\n\n  operation-description-required:\n    description: Every operation\
  \ must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: error\n    given:\
  \ $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  parameter-realm-naming:\n    description: Realm parameter should be named \"realm\" (SAP Ariba convention).\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(realm|\\\\$filter|\\\\$count|\\\\$skip|\\\\$select|\\\\$expand|\\\\$search|shopID|entity_id|entity_type)$\"\n\n  # REQUEST BODIES\n  request-body-description-required:\n    description: Request bodies should have a description.\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody\n    then:\n      field: description\n      function: truthy\n\n  request-body-json-content:\n\
  \    description: Request bodies should define application/json content.\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a 200 or 201 success response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-400-recommended:\n    description: Operations should define a 400 Bad Request response.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '400'\n      function: truthy\n\n  response-401-recommended:\n    description: Operations should define a 401 Unauthorized response.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n\
  \    then:\n      field: '401'\n      function: truthy\n\n  response-500-recommended:\n    description: Operations should define a 500 Internal Server Error response.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '500'\n      function: truthy\n\n  response-description-required:\n    description: All responses must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-property-description-recommended:\n    description: Schema properties should have descriptions.\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    description: Component schemas should define a type.\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n\
  \  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: $.components.securitySchemes\n    then:\n      function: truthy\n\n  security-oauth2-ariba:\n    description: SAP Ariba APIs should use OAuth 2.0 with api.ariba.com token URL.\n    severity: warn\n    given: $.components.securitySchemes.OAuth2.flows.clientCredentials.tokenUrl\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api\\\\.ariba\\\\.com\"\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  microcks-operation-extension:\n  \
  \  description: Operations should include x-microcks-operation for mock server configuration.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/ariba-guided-buying/refs/heads/main/rules/ariba-guided-buying-spectral-rules.yml
tags:
- B2B
- Catalog
- ERP
- Procurement
- Requisitions
- SAP
- Supply Chain
- Spectral
- Linting
- API Governance
---
