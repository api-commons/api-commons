---
api_specs:
- filename: alpha-vantage-openapi.yml
  format: yaml
  label: Alpha Vantage Market Data API
  slug: market-data-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alpha-vantage/refs/heads/main/openapi/alpha-vantage-openapi.yml
categories:
- alpha
description: Spectral linting rules defining API design standards and conventions for Alpha Vantage.
layout: rules
name: Alpha Vantage API Rules
provider_name: Alpha Vantage
provider_slug: alpha-vantage
rule_count: 15
rules:
- description: All operation summaries must start with "Alpha Vantage"
  given: $.paths[*][*].summary
  name: alpha-vantage-operation-summary-prefix
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][*]
  name: alpha-vantage-operation-tags
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][*]
  name: alpha-vantage-operation-id
  severity: error
- description: All operations must have a description
  given: $.paths[*][*]
  name: alpha-vantage-operation-description
  severity: warn
- description: All operations must have the apikey parameter
  given: $.paths[*][get].parameters[*]
  name: alpha-vantage-apikey-param
  severity: error
- description: All query operations must have the function parameter
  given: $.paths[/query][get].parameters[?(@.name == 'function')]
  name: alpha-vantage-function-param
  severity: error
- description: The function parameter must have an enum of allowed values
  given: $.paths[/query][get].parameters[?(@.name == 'function')].schema
  name: alpha-vantage-function-enum
  severity: warn
- description: API must define the ApiKey security scheme
  given: $.components.securitySchemes
  name: alpha-vantage-apikey-security-scheme
  severity: error
- description: ApiKey must be passed as a query parameter
  given: $.components.securitySchemes.ApiKey
  name: alpha-vantage-apikey-in-query
  severity: error
- description: All schemas must have a title
  given: $.components.schemas[*]
  name: alpha-vantage-schema-title
  severity: warn
- description: All schemas must have a description
  given: $.components.schemas[*]
  name: alpha-vantage-schema-description
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: alpha-vantage-property-description
  severity: warn
- description: All operations must document a 200 success response
  given: $.paths[*][*].responses
  name: alpha-vantage-200-response
  severity: error
- description: All operations should have x-microcks-operation extension
  given: $.paths[*][*]
  name: alpha-vantage-microcks-operation
  severity: info
- description: API server must use HTTPS
  given: $.servers[*].url
  name: alpha-vantage-server-https
  severity: error
rules_file: rules/alpha-vantage-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/alpha-vantage/refs/heads/main/rules/alpha-vantage-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 1
  warn: 6
slug: alpha-vantage-spectral-rules
source_filename: alpha-vantage-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  alpha-vantage-operation-summary-prefix:\n    description: All operation summaries must start with \"Alpha Vantage\"\n    severity: warn\n    given: \"$.paths[*][*].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Alpha Vantage\"\n\n  alpha-vantage-operation-tags:\n    description: All operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n\n  alpha-vantage-operation-id:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: operationId\n      function: truthy\n\n  alpha-vantage-operation-description:\n    description: All operations must have a description\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: description\n      function: truthy\n\n  alpha-vantage-apikey-param:\n    description: All operations must have the apikey parameter\n\
  \    severity: error\n    given: \"$.paths[*][get].parameters[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            name:\n              type: string\n\n  alpha-vantage-function-param:\n    description: All query operations must have the function parameter\n    severity: error\n    given: \"$.paths[/query][get].parameters[?(@.name == 'function')]\"\n    then:\n      function: truthy\n\n  alpha-vantage-function-enum:\n    description: The function parameter must have an enum of allowed values\n    severity: warn\n    given: \"$.paths[/query][get].parameters[?(@.name == 'function')].schema\"\n    then:\n      field: enum\n      function: truthy\n\n  alpha-vantage-apikey-security-scheme:\n    description: API must define the ApiKey security scheme\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      field: ApiKey\n      function: truthy\n\n  alpha-vantage-apikey-in-query:\n\
  \    description: ApiKey must be passed as a query parameter\n    severity: error\n    given: \"$.components.securitySchemes.ApiKey\"\n    then:\n      field: in\n      function: enumeration\n      functionOptions:\n        values:\n          - query\n\n  alpha-vantage-schema-title:\n    description: All schemas must have a title\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: title\n      function: truthy\n\n  alpha-vantage-schema-description:\n    description: All schemas must have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  alpha-vantage-property-description:\n    description: Schema properties should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  alpha-vantage-200-response:\n    description: All operations must document a 200 success response\n\
  \    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      field: \"200\"\n      function: truthy\n\n  alpha-vantage-microcks-operation:\n    description: All operations should have x-microcks-operation extension\n    severity: info\n    given: \"$.paths[*][*]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  alpha-vantage-server-https:\n    description: API server must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/alpha-vantage/refs/heads/main/rules/alpha-vantage-spectral-rules.yml
tags:
- Financial
- Market Data
- Stocks
- Technical Indicators
- Economic Data
- Sentiment Analysis
- Spectral
- Linting
- API Governance
---
