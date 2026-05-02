---
categories:
- airwallex
description: Spectral linting rules defining API design standards and conventions for Airwallex.
layout: rules
name: Airwallex API Rules
provider_name: Airwallex
provider_slug: airwallex
rule_count: 29
rules:
- description: Payment intent must include id, amount, currency, and status.
  given: $.components.schemas.PaymentIntent.required
  name: airwallex-payment-intent-required-fields
  severity: error
- description: Transfer object must include id, source_amount, source_currency, and status.
  given: $.components.schemas.Transfer.required
  name: airwallex-transfer-required-fields
  severity: error
- description: Every API operation must have a non-empty summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: airwallex-operation-summary-exists
  severity: error
- description: Operation summaries must be in Title Case.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: airwallex-operation-summary-title-case
  severity: warn
- description: Every API operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: airwallex-operation-description-exists
  severity: warn
- description: Every operation must be tagged for grouping and documentation.
  given: $.paths[*][get,post,put,patch,delete]
  name: airwallex-operation-tags-exist
  severity: error
- description: Every operation must have a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: airwallex-operation-id-exists
  severity: error
- description: operationId must be in camelCase format.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: airwallex-operation-id-camel-case
  severity: warn
- description: Every GET operation must define a 200 success response.
  given: $.paths[*].get
  name: airwallex-response-200-exists
  severity: error
- description: Operations accepting request bodies should document 400 errors.
  given: $.paths[*][post,put]
  name: airwallex-response-400-documented
  severity: warn
- description: Currency fields must be ISO 4217 three-letter uppercase codes.
  given: $.components.schemas[*].properties[*currency*]
  name: airwallex-currency-iso4217-format
  severity: warn
- description: Amount fields must be typed as number.
  given: $.components.schemas[*].properties[*amount*]
  name: airwallex-amount-type-number
  severity: warn
- description: Status fields must use an enum of allowed values.
  given: $.components.schemas[*].properties.status
  name: airwallex-status-enum-defined
  severity: warn
- description: All schema components must include a description.
  given: $.components.schemas[*]
  name: airwallex-schema-description-exists
  severity: warn
- description: All schema properties should include descriptions.
  given: $.components.schemas[*].properties[*]
  name: airwallex-property-description-exists
  severity: info
- description: Timestamp fields must use date-time format.
  given: $.components.schemas[*].properties[*_at]
  name: airwallex-datetime-format
  severity: warn
- description: All operations should include x-microcks-operation for mock support.
  given: $.paths[*][get,post,put,patch,delete]
  name: airwallex-microcks-operation-extension
  severity: info
- description: API must define security schemes for authentication.
  given: $
  name: airwallex-security-defined
  severity: error
- description: Airwallex APIs must use Bearer token authentication.
  given: $.components.securitySchemes[*]
  name: airwallex-bearer-auth-scheme
  severity: warn
- description: API paths must be lowercase and use hyphens for word separation.
  given: $.paths[*]~
  name: airwallex-path-lowercase
  severity: warn
- description: API paths must not end with a trailing slash.
  given: $.paths[*]~
  name: airwallex-no-trailing-slash
  severity: warn
- description: API info block must include a title.
  given: $.info
  name: airwallex-info-title-exists
  severity: error
- description: API info block must include a version.
  given: $.info
  name: airwallex-info-version-exists
  severity: error
- description: API info block should include a description.
  given: $.info
  name: airwallex-info-description-exists
  severity: warn
- description: API info should include contact information.
  given: $.info
  name: airwallex-contact-info-exists
  severity: info
- description: API must define at least one server URL.
  given: $
  name: airwallex-servers-defined
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: airwallex-server-https
  severity: error
- description: List endpoints should support a limit query parameter.
  given: $.paths[*].get.parameters[*][?(@.in == 'query' && @.name == 'limit')]
  name: airwallex-pagination-limit-param
  severity: info
- description: Request bodies must specify application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: airwallex-request-body-content-type
  severity: warn
rules_file: rules/airwallex-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/rules/airwallex-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 4
  warn: 14
slug: airwallex-spectral-rules
source_filename: airwallex-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  airwallex-payment-intent-required-fields:\n    description: Payment intent must include id, amount, currency, and status.\n    message: \"Payment intent object is missing required field: {{property}}\"\n    severity: error\n    given: \"$.components.schemas.PaymentIntent.required\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type: string\n            enum: [id, amount, currency, status]\n\n  airwallex-transfer-required-fields:\n    description: Transfer object must include id, source_amount, source_currency, and status.\n    message: \"Transfer object is missing required field: {{property}}\"\n    severity: error\n    given: \"$.components.schemas.Transfer.required\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type: string\n            enum: [id, source_amount, source_currency, status]\n\n\
  \  airwallex-operation-summary-exists:\n    description: Every API operation must have a non-empty summary.\n    message: \"Operation is missing a summary: {{path}}\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  airwallex-operation-summary-title-case:\n    description: Operation summaries must be in Title Case.\n    message: \"Operation summary should be in Title Case: {{value}}\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*([ ][A-Z][a-zA-Z0-9]*)*$\"\n\n  airwallex-operation-description-exists:\n    description: Every API operation should have a description.\n    message: \"Operation is missing a description: {{path}}\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  airwallex-operation-tags-exist:\n\
  \    description: Every operation must be tagged for grouping and documentation.\n    message: \"Operation must have at least one tag: {{path}}\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  airwallex-operation-id-exists:\n    description: Every operation must have a unique operationId.\n    message: \"Operation is missing an operationId: {{path}}\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  airwallex-operation-id-camel-case:\n    description: operationId must be in camelCase format.\n    message: \"operationId should be camelCase: {{value}}\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  airwallex-response-200-exists:\n    description: Every GET operation must\
  \ define a 200 success response.\n    message: \"GET operation must define a 200 response: {{path}}\"\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: responses.200\n      function: truthy\n\n  airwallex-response-400-documented:\n    description: Operations accepting request bodies should document 400 errors.\n    message: \"POST/PUT operation should document 400 error response: {{path}}\"\n    severity: warn\n    given: \"$.paths[*][post,put]\"\n    then:\n      field: responses.400\n      function: truthy\n\n  airwallex-currency-iso4217-format:\n    description: Currency fields must be ISO 4217 three-letter uppercase codes.\n    message: \"Currency field should match ISO 4217 format (e.g., USD, GBP): {{path}}\"\n    severity: warn\n    given: \"$.components.schemas[*].properties[*currency*]\"\n    then:\n      field: pattern\n      function: truthy\n\n  airwallex-amount-type-number:\n    description: Amount fields must be typed as number.\n    message: \"\
  Amount field should be of type 'number': {{path}}\"\n    severity: warn\n    given: \"$.components.schemas[*].properties[*amount*]\"\n    then:\n      field: type\n      function: enumeration\n      functionOptions:\n        values: [number]\n\n  airwallex-status-enum-defined:\n    description: Status fields must use an enum of allowed values.\n    message: \"Status field should define allowed enum values: {{path}}\"\n    severity: warn\n    given: \"$.components.schemas[*].properties.status\"\n    then:\n      field: enum\n      function: truthy\n\n  airwallex-schema-description-exists:\n    description: All schema components must include a description.\n    message: \"Schema is missing a description: {{path}}\"\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  airwallex-property-description-exists:\n    description: All schema properties should include descriptions.\n    message: \"Property is missing a description:\
  \ {{path}}\"\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  airwallex-datetime-format:\n    description: Timestamp fields must use date-time format.\n    message: \"Timestamp field should specify format: date-time: {{path}}\"\n    severity: warn\n    given: \"$.components.schemas[*].properties[*_at]\"\n    then:\n      field: format\n      function: enumeration\n      functionOptions:\n        values: [date-time]\n\n  airwallex-microcks-operation-extension:\n    description: All operations should include x-microcks-operation for mock support.\n    message: \"Operation is missing x-microcks-operation extension: {{path}}\"\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  airwallex-security-defined:\n    description: API must define security schemes for authentication.\n    message: \"API is missing\
  \ security scheme definitions.\"\n    severity: error\n    given: \"$\"\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  airwallex-bearer-auth-scheme:\n    description: Airwallex APIs must use Bearer token authentication.\n    message: \"API should define a Bearer authentication scheme.\"\n    severity: warn\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      field: scheme\n      function: enumeration\n      functionOptions:\n        values: [bearer]\n\n  airwallex-path-lowercase:\n    description: API paths must be lowercase and use hyphens for word separation.\n    message: \"Path should be lowercase with hyphens: {{path}}\"\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}_-]+)+$\"\n\n  airwallex-no-trailing-slash:\n    description: API paths must not end with a trailing slash.\n    message: \"Path must not end with a trailing slash: {{path}}\"\n   \
  \ severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  airwallex-info-title-exists:\n    description: API info block must include a title.\n    message: \"API info is missing a title.\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  airwallex-info-version-exists:\n    description: API info block must include a version.\n    message: \"API info is missing a version.\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  airwallex-info-description-exists:\n    description: API info block should include a description.\n    message: \"API info is missing a description.\"\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  airwallex-contact-info-exists:\n    description: API info should include contact information.\n    message: \"API info is missing\
  \ contact details.\"\n    severity: info\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  airwallex-servers-defined:\n    description: API must define at least one server URL.\n    message: \"API is missing server definitions.\"\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  airwallex-server-https:\n    description: All server URLs must use HTTPS.\n    message: \"Server URL must use HTTPS: {{value}}\"\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  airwallex-pagination-limit-param:\n    description: List endpoints should support a limit query parameter.\n    message: \"List endpoint should accept a limit query parameter: {{path}}\"\n    severity: info\n    given: \"$.paths[*].get.parameters[*][?(@.in == 'query' && @.name == 'limit')]\"\n    then:\n      field: name\n      function: truthy\n\n  airwallex-request-body-content-type:\n\
  \    description: Request bodies must specify application/json content type.\n    message: \"Request body should specify application/json content type: {{path}}\"\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      field: application/json\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/rules/airwallex-spectral-rules.yml
tags:
- Cross-Border Payments
- FinTech
- Foreign Exchange
- Payments
- Global
- Embedded Finance
- Multi-Currency
- Spectral
- Linting
- API Governance
---
