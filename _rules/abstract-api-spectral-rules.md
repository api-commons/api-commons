---
api_specs:
- filename: abstract-api-email-reputation.yaml
  format: yaml
  label: Email Reputation API
  slug: email-reputation
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/openapi/abstract-api-email-reputation.yaml
- filename: abstract-api-phone-intelligence.yaml
  format: yaml
  label: Phone Intelligence API
  slug: phone-intelligence
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/openapi/abstract-api-phone-intelligence.yaml
- filename: abstract-api-ip-geolocation.yaml
  format: yaml
  label: IP Geolocation API
  slug: ip-geolocation
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/openapi/abstract-api-ip-geolocation.yaml
- filename: abstract-api-ip-intelligence.yaml
  format: yaml
  label: IP Intelligence API
  slug: ip-intelligence
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/openapi/abstract-api-ip-intelligence.yaml
- filename: abstract-api-company-enrichment.yaml
  format: yaml
  label: Company Enrichment API
  slug: company-enrichment
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/openapi/abstract-api-company-enrichment.yaml
- filename: abstract-api-exchange-rates.yaml
  format: yaml
  label: Exchange Rates API
  slug: exchange-rates
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/openapi/abstract-api-exchange-rates.yaml
- filename: abstract-api-public-holidays.yaml
  format: yaml
  label: Public Holidays API
  slug: public-holidays
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/openapi/abstract-api-public-holidays.yaml
- filename: abstract-api-timezones.yaml
  format: yaml
  label: Timezone API
  slug: timezones
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/openapi/abstract-api-timezones.yaml
- filename: abstract-api-vat-validation.yaml
  format: yaml
  label: VAT Validation API
  slug: vat-validation
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/openapi/abstract-api-vat-validation.yaml
- filename: abstract-api-iban-validation.yaml
  format: yaml
  label: IBAN Validation API
  slug: iban-validation
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/openapi/abstract-api-iban-validation.yaml
- filename: abstract-api-website-screenshot.yaml
  format: yaml
  label: Website Screenshot API
  slug: website-screenshot
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/openapi/abstract-api-website-screenshot.yaml
- filename: abstract-api-image-processing.yaml
  format: yaml
  label: Image Processing API
  slug: image-processing
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/openapi/abstract-api-image-processing.yaml
- filename: abstract-api-web-scraping.yaml
  format: yaml
  label: Web Scraping API
  slug: web-scraping
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/openapi/abstract-api-web-scraping.yaml
- filename: abstract-api-avatars.yaml
  format: yaml
  label: Avatars API
  slug: avatars
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/openapi/abstract-api-avatars.yaml
categories:
- delete
- generated
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
- tags
description: Spectral linting rules defining API design standards and conventions for Abstract API.
layout: rules
name: Abstract API API Rules
provider_name: Abstract API
provider_slug: abstract-api
rule_count: 34
rules:
- description: Info title must be present and start with "Abstract API"
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: Info version must be present
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https-only
  severity: error
- description: Server URLs should be under abstractapi.com domain
  given: $.servers[*]
  name: servers-abstractapi-domain
  severity: warn
- description: Path segments must use kebab-case (lowercase with hyphens)
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes (except root /)
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summary must start with "Abstract API"
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-title-case
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Operations should have x-microcks-operation extension for mock server compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
- description: Tags should use Title Case
  given: $.tags[*]
  name: tags-title-case
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Abstract API uses api_key as the query parameter name for authentication
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.name == "api_key")]
  name: parameter-api-key-query
  severity: warn
- description: Every parameter must have a schema with type
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Parameters should have example values
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-example-recommended
  severity: info
- description: Every operation must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations secured with API key should document 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Rate-limited APIs should document 429 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-429-recommended
  severity: info
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schema properties should have example values
  given: $.components.schemas[*].properties[*]
  name: schema-property-example
  severity: info
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-top-level-description
  severity: warn
- description: Security schemes must be defined in components
  given: $
  name: security-schemes-defined
  severity: error
- description: Abstract API uses apiKey security scheme
  given: $.components.securitySchemes[*]
  name: security-api-key-scheme
  severity: warn
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
  severity: error
- description: Generated specs should be marked with x-generated-from
  given: $.info
  name: generated-from-docs-marked
  severity: info
rules_file: rules/abstract-api-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/rules/abstract-api-spectral-rules.yml
severity_counts:
  error: 17
  hint: 0
  info: 6
  warn: 11
slug: abstract-api-spectral-rules
source_filename: abstract-api-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be present and start with \"Abstract API\"\n    severity: error\n    given: '$.info'\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: '^Abstract API'\n\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: '$.info'\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info version must be present\n    severity: error\n    given: '$.info'\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.0.x\n    severity: error\n    given: '$'\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: '^3\\.0\\.'\n\n  # SERVERS\n  servers-required:\n    description: At least one server must be defined\n    severity: error\n\
  \    given: '$'\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: '$.servers[*]'\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  servers-abstractapi-domain:\n    description: Server URLs should be under abstractapi.com domain\n    severity: warn\n    given: '$.servers[*]'\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: 'abstractapi\\.com'\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments must use kebab-case (lowercase with hyphens)\n    severity: warn\n    given: '$.paths'\n    then:\n      field: '@key'\n      function: pattern\n      functionOptions:\n        match: '^(\\/[a-z0-9_\\-\\{\\}]*)*$'\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes (except root /)\n    severity: warn\n    given: '$.paths'\n\
  \    then:\n      field: '@key'\n      function: pattern\n      functionOptions:\n        notMatch: '.+\\/$'\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-title-case:\n    description: Operation summary must start with \"Abstract API\"\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: '^Abstract API'\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n\
  \    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId must use camelCase\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]+$'\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: tags\n      function: truthy\n\n  operation-microcks-extension:\n    description: Operations should have x-microcks-operation extension for mock server compatibility\n    severity: info\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  # TAGS\n  tags-title-case:\n    description: Tags should use Title Case\n    severity: warn\n    given: '$.tags[*]'\n    then:\n      field: name\n      function:\
  \ pattern\n      functionOptions:\n        match: '^[A-Z]'\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: description\n      function: truthy\n\n  parameter-api-key-query:\n    description: Abstract API uses api_key as the query parameter name for authentication\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].parameters[?(@.name == \"api_key\")]'\n    then:\n      field: in\n      function: enumeration\n      functionOptions:\n        values:\n          - query\n          - header\n\n  parameter-schema-required:\n    description: Every parameter must have a schema with type\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: schema\n      function: truthy\n\n  parameter-example-recommended:\n    description: Parameters should have\
  \ example values\n    severity: info\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: example\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a 2xx success response\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-401-required:\n    description: Operations secured with API key should document 401 response\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n    then:\n      field: '401'\n      function: truthy\n\n  response-429-recommended:\n    description: Rate-limited APIs should document 429 response\n    severity: info\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n    then:\n      field: '429'\n\
  \      function: truthy\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].responses[*]'\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-property-description:\n    description: Schema properties should have descriptions\n    severity: info\n    given: '$.components.schemas[*].properties[*]'\n    then:\n      field: description\n      function: truthy\n\n  schema-property-example:\n    description: Schema properties should have example values\n    severity: info\n    given: '$.components.schemas[*].properties[*]'\n    then:\n      field: example\n      function: truthy\n\n  schema-top-level-description:\n    description: Top-level schemas should have descriptions\n    severity: warn\n    given: '$.components.schemas[*]'\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n\
  \    description: Security schemes must be defined in components\n    severity: error\n    given: '$'\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  security-api-key-scheme:\n    description: Abstract API uses apiKey security scheme\n    severity: warn\n    given: '$.components.securitySchemes[*]'\n    then:\n      field: type\n      function: enumeration\n      functionOptions:\n        values:\n          - apiKey\n          - http\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: '$.paths[*].get'\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: '$.paths[*].delete'\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty\
  \ strings\n    severity: error\n    given: '$..description'\n    then:\n      function: pattern\n      functionOptions:\n        match: '.+'\n\n  generated-from-docs-marked:\n    description: Generated specs should be marked with x-generated-from\n    severity: info\n    given: '$.info'\n    then:\n      field: x-generated-from\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/rules/abstract-api-spectral-rules.yml
tags:
- Avatars
- Company Enrichment
- Contacts
- Currencies
- Email Validation
- Exchange Rates
- IBAN Validation
- Image Processing
- IP Geolocation
- IP Intelligence
- Phone Validation
- Public Holidays
- Screenshots
- Timezones
- VAT Validation
- Web Scraping
- Spectral
- Linting
- API Governance
---
