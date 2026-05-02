---
api_specs:
- filename: avalara-avatax-rest-openapi.yml
  format: yaml
  label: AvaTax APIs
  slug: avatax-apis
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-avatax-rest-openapi.yml
- filename: avalara-communications-openapi.yml
  format: yaml
  label: Communications Tax API
  slug: communications-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-communications-openapi.yml
- filename: avalara-excise-openapi.yml
  format: yaml
  label: Excise Platform API
  slug: excise-tax-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-excise-openapi.yml
- filename: avalara-item-classification-openapi.yml
  format: yaml
  label: Item Classification API
  slug: item-classification-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-item-classification-openapi.yml
- filename: avalara-avatax-brazil-openapi.yml
  format: yaml
  label: AvaTax Brazil API
  slug: avatax-brazil-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-avatax-brazil-openapi.yml
- filename: avalara-vat-reporting-openapi.yml
  format: yaml
  label: VAT Reporting API
  slug: vat-reporting-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-vat-reporting-openapi.yml
- filename: avalara-mylodgetax-openapi.yml
  format: yaml
  label: MyLodgeTax API
  slug: mylodgetax-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-mylodgetax-openapi.yml
- filename: avalara-certcapture-openapi.yml
  format: yaml
  label: CertCapture API
  slug: certcapture-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-certcapture-openapi.yml
- filename: avalara-e-invoicing-openapi.yml
  format: yaml
  label: E-Invoicing REST API
  slug: e-invoicing-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-e-invoicing-openapi.yml
- filename: avalara-activation-service-openapi.yml
  format: yaml
  label: Activation Service API
  slug: activation-service-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-activation-service-openapi.yml
- filename: avalara-business-openapi.yml
  format: yaml
  label: Avalara Business API
  slug: business-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-business-openapi.yml
- filename: avalara-portal-oauth-openapi.yml
  format: yaml
  label: Portal OAuth API
  slug: portal-oauth-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-portal-oauth-openapi.yml
- filename: avalara-shared-company-service-openapi.yml
  format: yaml
  label: Shared Company Service API
  slug: shared-company-service-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-shared-company-service-openapi.yml
- filename: avalara-hs-code-classification-openapi.yml
  format: yaml
  label: Automated Tariff Code Classification API
  slug: hs-code-classification-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-hs-code-classification-openapi.yml
- filename: avalara-1099-w9-openapi.yml
  format: yaml
  label: 1099 & W-9 API
  slug: 1099-w9-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/openapi/avalara-1099-w9-openapi.yml
categories:
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
- servers
description: Spectral linting rules defining API design standards and conventions for Avalara.
layout: rules
name: Avalara API Rules
provider_name: Avalara
provider_slug: avalara
rule_count: 21
rules:
- description: API title should reference Avalara or a named product
  given: $.info.title
  name: info-title-avalara-prefix
  severity: warn
- description: API info description must be present and non-empty
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be present
  given: $.info
  name: info-version-required
  severity: error
- description: API contact information should be provided
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version must be 3.x
  given: $
  name: openapi-version-3x
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Paths should not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Paths should not contain query strings
  given: $.paths[*]~
  name: paths-no-query-strings
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with Avalara
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-avalara-prefix
  severity: info
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Request bodies should include application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-on-top-level
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/avalara-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/rules/avalara-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 2
  warn: 9
slug: avalara-spectral-rules
source_filename: avalara-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Avalara API Spectral Ruleset\n\nrules:\n\n  info-title-avalara-prefix:\n    description: API title should reference Avalara or a named product\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(Avalara|AvaTax|CertCapture|MyLodgeTax|Communications)\"\n\n  info-description-required:\n    description: API info description must be present and non-empty\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API version must be present\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API contact information should be provided\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  openapi-version-3x:\n    description: OpenAPI version must be 3.x\n    severity: error\n\
  \    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  servers-required:\n    description: At least one server must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  paths-no-trailing-slash:\n    description: Paths should not have trailing slashes\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  paths-no-query-strings:\n    description: Paths should not contain query strings\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\?\"\n\n  operation-summary-required:\n \
  \   description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-avalara-prefix:\n    description: Operation summaries should start with Avalara\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Avalara\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase\n    severity:\
  \ warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  request-body-json-content:\n    description: Request bodies should include application/json content type\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      field: application/json\n      function: truthy\n\n  response-description-required:\n    description: All responses must have a description\n    severity:\
  \ error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-description-on-top-level:\n    description: Top-level schemas should have a description\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/rules/avalara-spectral-rules.yml
tags:
- Taxes
- Spectral
- Linting
- API Governance
---
