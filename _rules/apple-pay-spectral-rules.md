---
api_specs:
- filename: apple-pay-js-openapi.yml
  format: yaml
  label: Apple Pay JS API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apple-pay/refs/heads/main/openapi/apple-pay-js-openapi.yml
- filename: apple-pay-payment-token-openapi.yml
  format: yaml
  label: Apple Pay Payment Token API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apple-pay/refs/heads/main/openapi/apple-pay-payment-token-openapi.yml
categories:
- external
- http
- info
- 'no'
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Apple Pay.
layout: rules
name: Apple Pay API Rules
provider_name: Apple Pay
provider_slug: apple-pay
rule_count: 24
rules:
- description: API title should start with "Apple Pay"
  given: $.info
  name: info-title-apple-prefix
  severity: warn
- description: API version must be specified
  given: $.info
  name: info-version-required
  severity: error
- description: API description must be present
  given: $.info
  name: info-description-required
  severity: warn
- description: Contact information should be provided
  given: $.info
  name: info-contact-required
  severity: info
- description: Terms of service URL should be provided for payment APIs
  given: $.info
  name: info-terms-of-service
  severity: warn
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS for payment APIs
  given: $.servers[*]
  name: servers-https
  severity: error
- description: Each server must have a description distinguishing production from sandbox
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Global security scheme must be defined for payment APIs
  given: $
  name: security-defined
  severity: error
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Path segments must use camelCase or kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have a 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: operation-success-response-required
  severity: error
- description: Payment APIs must define 401 Unauthorized responses
  given: $.paths[*][post].responses
  name: response-401-for-payment-apis
  severity: warn
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Component schemas must have a title
  given: $.components.schemas[*]
  name: schema-title-required
  severity: warn
- description: Component schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: http-get-no-request-body
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: External documentation links are encouraged for payment APIs
  given: $
  name: external-docs-encouraged
  severity: info
rules_file: rules/apple-pay-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apple-pay/refs/heads/main/rules/apple-pay-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 2
  warn: 12
slug: apple-pay-spectral-rules
source_filename: apple-pay-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-apple-prefix:\n    description: API title should start with \"Apple Pay\"\n    severity: warn\n    given: $.info\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^Apple Pay\"\n\n  info-version-required:\n    description: API version must be specified\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-description-required:\n    description: API description must be present\n    severity: warn\n    given: $.info\n    then:\n      field: description\n      function: minLength\n      functionOptions:\n        min: 20\n\n  info-contact-required:\n    description: Contact information should be provided\n    severity: info\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  info-terms-of-service:\n    description: Terms of service URL should be provided for payment APIs\n    severity: warn\n    given: $.info\n\
  \    then:\n      field: termsOfService\n      function: truthy\n\n  # SERVERS\n  servers-required:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS for payment APIs\n    severity: error\n    given: $.servers[*]\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description-required:\n    description: Each server must have a description distinguishing production from sandbox\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-defined:\n    description: Global security scheme must be defined for payment APIs\n    severity: error\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined\
  \ in components\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # PATHS — NAMING\n  paths-kebab-case:\n    description: Path segments must use camelCase or kebab-case\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-zA-Z0-9{}/_-]+)+$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n\
  \    then:\n      field: description\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  operation-success-response-required:\n    description: Every operation must have a 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-401-for-payment-apis:\n    description: Payment APIs must define\
  \ 401 Unauthorized responses\n    severity: warn\n    given: $.paths[*][post].responses\n    then:\n      field: '401'\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-title-required:\n    description: Component schemas must have a title\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: title\n      function: truthy\n\n  schema-description-required:\n    description: Component schemas should have a description\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  http-get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n\
  \      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: warn\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  external-docs-encouraged:\n    description: External documentation links are encouraged for payment APIs\n    severity: info\n    given: $\n    then:\n      field: externalDocs\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apple-pay/refs/heads/main/rules/apple-pay-spectral-rules.yml
tags:
- Apple
- Contactless Payments
- Digital Wallet
- E-Commerce
- Mobile Payments
- Payments
- Spectral
- Linting
- API Governance
---
