---
api_specs:
- filename: at-t-developer-hub-network-insights-api.yaml
  format: yaml
  label: AT&T Network Insights API
  slug: att-network-insights-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/at-t-developer-hub/refs/heads/main/openapi/at-t-developer-hub-network-insights-api.yaml
- filename: at-t-developer-hub-mobility-threat-anomaly-detection-api.yaml
  format: yaml
  label: AT&T Mobility Threat and Anomaly Detection API
  slug: att-mobility-threat-anomaly-detection-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/at-t-developer-hub/refs/heads/main/openapi/at-t-developer-hub-mobility-threat-anomaly-detection-api.yaml
- filename: at-t-developer-hub-sim-swap-api.yaml
  format: yaml
  label: AT&T SIM Swap API
  slug: att-sim-swap-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/at-t-developer-hub/refs/heads/main/openapi/at-t-developer-hub-sim-swap-api.yaml
- filename: at-t-developer-hub-device-status-api.yaml
  format: yaml
  label: AT&T Device Status API
  slug: att-device-status-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/at-t-developer-hub/refs/heads/main/openapi/at-t-developer-hub-device-status-api.yaml
- filename: at-t-developer-hub-quality-on-demand-api.yaml
  format: yaml
  label: AT&T Quality on Demand API
  slug: att-quality-on-demand-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/at-t-developer-hub/refs/heads/main/openapi/at-t-developer-hub-quality-on-demand-api.yaml
- filename: at-t-developer-hub-number-verification-api.yaml
  format: yaml
  label: AT&T Number Verification API
  slug: att-number-verification-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/at-t-developer-hub/refs/heads/main/openapi/at-t-developer-hub-number-verification-api.yaml
categories:
- camara
- get
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- paths
- post
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for AT&T Developer Hub.
layout: rules
name: AT&T Developer Hub API Rules
provider_name: AT&T Developer Hub
provider_slug: at-t-developer-hub
rule_count: 26
rules:
- description: API title must start with "AT&T"
  given: $.info.title
  name: info-title-pattern
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API info should have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Must use OpenAPI 3.0.x
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Summaries must start with "AT&T"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-att-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: API should define an ErrorInfo schema in components for CAMARA compliance
  given: $.components.schemas
  name: camara-error-schema
  severity: warn
- description: Phone number parameters should document E.164 format requirement
  given: $.components.schemas[*].properties.phoneNumber
  name: camara-phone-number-e164
  severity: info
- description: Every parameter must have a description
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Operations using security should document 401 responses
  given: $.paths[*][post,get,delete][?(@.security)]
  name: response-401-defined
  severity: warn
- description: Operations should document 429 Too Many Requests responses for rate limiting
  given: $.paths[*][post]
  name: response-429-defined
  severity: info
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: POST operations should have a request body
  given: $.paths[*].post
  name: post-has-request-body
  severity: warn
- description: Operations should include x-microcks-operation for mock server support
  given: $.paths[*][post,get,delete]
  name: microcks-operation-extension
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/at-t-developer-hub-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/at-t-developer-hub/refs/heads/main/rules/at-t-developer-hub-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 3
  warn: 9
slug: at-t-developer-hub-spectral-rules
source_filename: at-t-developer-hub-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # ===========================\n  # INFO / METADATA\n  # ===========================\n  info-title-pattern:\n    description: API title must start with \"AT&T\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: '^AT&T '\n\n  info-description-required:\n    description: API info must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should have contact information\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  # ===========================\n  # OPENAPI VERSION\n  # ===========================\n  openapi-version-3:\n    description: Must use OpenAPI 3.0.x\n\
  \    severity: error\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: '^3\\.0\\.'\n\n  # ===========================\n  # SERVERS\n  # ===========================\n  servers-required:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  # ===========================\n  # PATHS\n  # ===========================\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        match: '^(\\/[a-z0-9{}\\-]+)+$'\n\n  # ===========================\n  # OPERATIONS\n  # ===========================\n  operation-summary-required:\n    description:\
  \ Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-att-prefix:\n    description: Summaries must start with \"AT&T\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: '^AT&T '\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camelcase:\n    description: operationId must use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n\
  \    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]+$'\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # ===========================\n  # CAMARA COMPLIANCE\n  # ===========================\n  camara-error-schema:\n    description: API should define an ErrorInfo schema in components for CAMARA compliance\n    severity: warn\n    given: $.components.schemas\n    then:\n      field: ErrorInfo\n      function: truthy\n\n  camara-phone-number-e164:\n    description: Phone number parameters should document E.164 format requirement\n    severity: info\n    given: $.components.schemas[*].properties.phoneNumber\n    then:\n      field: description\n      function: truthy\n\n  # ===========================\n  # PARAMETERS\n  # ===========================\n  parameter-description-required:\n\
  \    description: Every parameter must have a description\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  # ===========================\n  # RESPONSES\n  # ===========================\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-401-defined:\n    description: Operations using security should document 401 responses\n    severity: warn\n    given: $.paths[*][post,get,delete][?(@.security)]\n    then:\n      field: responses.401\n      function: truthy\n\n  response-429-defined:\n    description: Operations should document 429 Too Many Requests responses for rate limiting\n    severity: info\n    given: $.paths[*][post]\n    then:\n      field: responses.429\n      function: truthy\n\n  # ===========================\n  # SCHEMAS\n  #\
  \ ===========================\n  schema-description-required:\n    description: Component schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  # ===========================\n  # SECURITY\n  # ===========================\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # ===========================\n  # HTTP METHOD CONVENTIONS\n  # ===========================\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  post-has-request-body:\n    description: POST operations should have a request body\n    severity: warn\n    given: $.paths[*].post\n    then:\n      field: requestBody\n      function: truthy\n\
  \n  # ===========================\n  # MICROCKS COMPATIBILITY\n  # ===========================\n  microcks-operation-extension:\n    description: Operations should include x-microcks-operation for mock server support\n    severity: info\n    given: $.paths[*][post,get,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  # ===========================\n  # GENERAL QUALITY\n  # ===========================\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: '.+'\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/at-t-developer-hub/refs/heads/main/rules/at-t-developer-hub-spectral-rules.yml
tags:
- 5G
- Network APIs
- CAMARA
- Connectivity
- Telecommunications
- Edge Computing
- Device Status
- SIM Swap
- Spectral
- Linting
- API Governance
---
