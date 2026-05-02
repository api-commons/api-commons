---
api_specs:
- filename: allianz-trade-payment-overdues.yaml
  format: yaml
  label: Allianz Trade Payment Overdues API
  slug: payment-overdues-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/allianz-trade-online/refs/heads/main/openapi/allianz-trade-payment-overdues.yaml
- filename: allianz-trade-company-grade.yaml
  format: yaml
  label: Allianz Trade Company Grade API
  slug: company-grade-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/allianz-trade-online/refs/heads/main/openapi/allianz-trade-company-grade.yaml
- filename: allianz-trade-claims.yaml
  format: yaml
  label: Allianz Trade Claims API
  slug: claims-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/allianz-trade-online/refs/heads/main/openapi/allianz-trade-claims.yaml
- filename: allianz-trade-policy.yaml
  format: yaml
  label: Allianz Trade Policy API
  slug: policy-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/allianz-trade-online/refs/heads/main/openapi/allianz-trade-policy.yaml
categories:
- allianz
description: Spectral linting rules defining API design standards and conventions for Allianz Trade.
layout: rules
name: Allianz Trade API Rules
provider_name: Allianz Trade
provider_slug: allianz-trade-online
rule_count: 22
rules:
- description: All operation summaries must start with "Allianz Trade"
  given: $.paths[*][*].summary
  name: allianz-trade-operation-summary-prefix
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][*]
  name: allianz-trade-operation-tags
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][*]
  name: allianz-trade-operation-id
  severity: error
- description: All operations must have a description
  given: $.paths[*][*]
  name: allianz-trade-operation-description
  severity: warn
- description: List operations must support pageSize query parameter
  given: $.paths[*].get
  name: allianz-trade-pagination-page-size
  severity: warn
- description: List operations must support page query parameter
  given: $.paths[*].get
  name: allianz-trade-pagination-page
  severity: warn
- description: List operations must support totalRequired query parameter
  given: $.paths[*].get
  name: allianz-trade-pagination-total-required
  severity: warn
- description: Write operations (POST/PATCH/DELETE) must return 202 for async processing
  given: $.paths[*][post,patch,delete]
  name: allianz-trade-async-202
  severity: warn
- description: 202 responses must reference JobResponse schema
  given: $.paths[*][post,patch,delete].responses.202.content.application/json.schema.$ref
  name: allianz-trade-async-job-response
  severity: warn
- description: All operations must document 401 Unauthorized response
  given: $.paths[*][*].responses
  name: allianz-trade-error-response-401
  severity: error
- description: ErrorResponse must have a code property
  given: $.components.schemas.ErrorResponse.properties
  name: allianz-trade-error-schema-code
  severity: warn
- description: ErrorResponse must have a message property
  given: $.components.schemas.ErrorResponse.properties
  name: allianz-trade-error-schema-message
  severity: warn
- description: API must use OAuth2 security scheme
  given: $.components.securitySchemes
  name: allianz-trade-oauth2-security
  severity: error
- description: OAuth2 must use client credentials flow
  given: $.components.securitySchemes.OAuth2.flows
  name: allianz-trade-oauth2-client-credentials
  severity: error
- description: All schemas must have a title
  given: $.components.schemas[*]
  name: allianz-trade-schema-title
  severity: warn
- description: All schemas must have a description
  given: $.components.schemas[*]
  name: allianz-trade-schema-description
  severity: warn
- description: All schema properties must have a description
  given: $.components.schemas[*].properties[*]
  name: allianz-trade-property-description
  severity: warn
- description: Schema properties should have examples
  given: $.components.schemas[*].properties[*]
  name: allianz-trade-property-example
  severity: info
- description: All operations should have x-microcks-operation extension
  given: $.paths[*][*]
  name: allianz-trade-microcks-operation
  severity: info
- description: Identifier fields should follow Allianz Trade ID pattern (PREFIX-NNNNNN)
  given: $.components.schemas[*].properties[?(@property.endsWith('Id'))].example
  name: allianz-trade-id-pattern
  severity: info
- description: Currency properties must use ISO 4217 format
  given: $.components.schemas[*].properties.currency.description
  name: allianz-trade-currency-iso
  severity: warn
- description: Date properties must specify date format
  given: $.components.schemas[*].properties[?(@property.endsWith('Date') || @property.endsWith('date'))].format
  name: allianz-trade-date-format
  severity: warn
rules_file: rules/allianz-trade-online-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/allianz-trade-online/refs/heads/main/rules/allianz-trade-online-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 3
  warn: 14
slug: allianz-trade-online-spectral-rules
source_filename: allianz-trade-online-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  allianz-trade-operation-summary-prefix:\n    description: All operation summaries must start with \"Allianz Trade\"\n    severity: warn\n    given: \"$.paths[*][*].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Allianz Trade\"\n\n  allianz-trade-operation-tags:\n    description: All operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n\n  allianz-trade-operation-id:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: operationId\n      function: truthy\n\n  allianz-trade-operation-description:\n    description: All operations must have a description\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: description\n      function: truthy\n\n  allianz-trade-pagination-page-size:\n    description: List operations must support pageSize\
  \ query parameter\n    severity: warn\n    given: \"$.paths[*].get\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          properties:\n            parameters:\n              type: array\n              contains:\n                type: object\n                properties:\n                  name:\n                    const: pageSize\n\n  allianz-trade-pagination-page:\n    description: List operations must support page query parameter\n    severity: warn\n    given: \"$.paths[*].get\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          properties:\n            parameters:\n              type: array\n              contains:\n                type: object\n                properties:\n                  name:\n                    const: page\n\n  allianz-trade-pagination-total-required:\n    description: List operations must support totalRequired query parameter\n    severity: warn\n    given: \"$.paths[*].get\"\n    then:\n\
  \      function: schema\n      functionOptions:\n        schema:\n          properties:\n            parameters:\n              type: array\n              contains:\n                type: object\n                properties:\n                  name:\n                    const: totalRequired\n\n  allianz-trade-async-202:\n    description: Write operations (POST/PATCH/DELETE) must return 202 for async processing\n    severity: warn\n    given: \"$.paths[*][post,patch,delete]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          properties:\n            responses:\n              type: object\n              required:\n                - \"202\"\n\n  allianz-trade-async-job-response:\n    description: 202 responses must reference JobResponse schema\n    severity: warn\n    given: \"$.paths[*][post,patch,delete].responses.202.content.application/json.schema.$ref\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"JobResponse\"\n\n\
  \  allianz-trade-error-response-401:\n    description: All operations must document 401 Unauthorized response\n    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      field: \"401\"\n      function: truthy\n\n  allianz-trade-error-schema-code:\n    description: ErrorResponse must have a code property\n    severity: warn\n    given: \"$.components.schemas.ErrorResponse.properties\"\n    then:\n      field: code\n      function: truthy\n\n  allianz-trade-error-schema-message:\n    description: ErrorResponse must have a message property\n    severity: warn\n    given: \"$.components.schemas.ErrorResponse.properties\"\n    then:\n      field: message\n      function: truthy\n\n  allianz-trade-oauth2-security:\n    description: API must use OAuth2 security scheme\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      field: OAuth2\n      function: truthy\n\n  allianz-trade-oauth2-client-credentials:\n    description: OAuth2 must use client\
  \ credentials flow\n    severity: error\n    given: \"$.components.securitySchemes.OAuth2.flows\"\n    then:\n      field: clientCredentials\n      function: truthy\n\n  allianz-trade-schema-title:\n    description: All schemas must have a title\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: title\n      function: truthy\n\n  allianz-trade-schema-description:\n    description: All schemas must have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  allianz-trade-property-description:\n    description: All schema properties must have a description\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  allianz-trade-property-example:\n    description: Schema properties should have examples\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n    \
  \  field: example\n      function: truthy\n\n  allianz-trade-microcks-operation:\n    description: All operations should have x-microcks-operation extension\n    severity: info\n    given: \"$.paths[*][*]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  allianz-trade-id-pattern:\n    description: Identifier fields should follow Allianz Trade ID pattern (PREFIX-NNNNNN)\n    severity: info\n    given: \"$.components.schemas[*].properties[?(@property.endsWith('Id'))].example\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z]+-[0-9]+$\"\n\n  allianz-trade-currency-iso:\n    description: Currency properties must use ISO 4217 format\n    severity: warn\n    given: \"$.components.schemas[*].properties.currency.description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"ISO 4217\"\n\n  allianz-trade-date-format:\n    description: Date properties must specify date format\n    severity: warn\n    given:\
  \ \"$.components.schemas[*].properties[?(@property.endsWith('Date') || @property.endsWith('date'))].format\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - date\n          - date-time\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/allianz-trade-online/refs/heads/main/rules/allianz-trade-online-spectral-rules.yml
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
- Spectral
- Linting
- API Governance
---
