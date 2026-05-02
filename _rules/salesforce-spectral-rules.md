---
api_specs:
- filename: salesforce-openapi.yml
  format: yaml
  label: Salesforce REST API
  slug: salesforce-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/openapi/salesforce-openapi.yml
- filename: salesforce-bulk-api-2-openapi.yml
  format: yaml
  label: Salesforce Bulk API 2.0
  slug: salesforce-bulk-api-2
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/openapi/salesforce-bulk-api-2-openapi.yml
- filename: salesforce-streaming-asyncapi.yml
  format: yaml
  label: Salesforce Streaming API
  slug: salesforce-streaming-api
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/asyncapi/salesforce-streaming-asyncapi.yml
- filename: salesforce-platform-events-asyncapi.yml
  format: yaml
  label: Salesforce Platform Events API
  slug: salesforce-platform-events-api
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/asyncapi/salesforce-platform-events-asyncapi.yml
- filename: salesforce-change-data-capture-asyncapi.yml
  format: yaml
  label: Salesforce Change Data Capture API
  slug: salesforce-change-data-capture-api
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/asyncapi/salesforce-change-data-capture-asyncapi.yml
- filename: salesforce-ui-api-openapi.yml
  format: yaml
  label: Salesforce UI API
  slug: salesforce-ui-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/openapi/salesforce-ui-api-openapi.yml
- filename: salesforce-marketing-cloud-rest-openapi.yml
  format: yaml
  label: Salesforce Marketing Cloud REST API
  slug: salesforce-marketing-cloud-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/openapi/salesforce-marketing-cloud-rest-openapi.yml
- filename: salesforce-openapi.yml
  format: yaml
  label: Salesforce
  slug: salesforce-salesforce
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/openapi/salesforce-openapi.yml
categories:
- http
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- paths
- response
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Salesforce.
layout: rules
name: Salesforce API Rules
provider_name: Salesforce
provider_slug: salesforce
rule_count: 21
rules:
- description: Info title must be present and non-empty
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be specified
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information should be provided
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version should be 3.x
  given: $
  name: openapi-version
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Every parameter must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Every operation must have a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: http-get-no-body
  severity: error
- description: DELETE operations must not have a request body
  given: $.paths[*].delete
  name: http-delete-no-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have x-microcks-operation
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/salesforce-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/rules/salesforce-spectral-rules.yml
severity_counts:
  error: 19
  hint: 0
  info: 1
  warn: 1
slug: salesforce-spectral-rules
source_filename: salesforce-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present and non-empty\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API version must be specified\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  info-contact-required:\n    description: Contact information should be provided\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  openapi-version:\n    description: OpenAPI version should be 3.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: ^3\\.\n  servers-defined:\n    description: At least one server must be\
  \ defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: ^https://\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: .+\\/$$\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n  operation-description-required:\n\
  \    description: Every operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n  parameter-schema-required:\n    description: Every parameter must have a schema\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: schema\n      function: truthy\n  response-success-required:\n    description: Every operation must have a success response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n\
  \    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"202\"]\n            - required: [\"204\"]\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n  security-global-defined:\n    description: Global security must be defined\n    severity: error\n    given: $\n    then:\n      field: security\n      function: truthy\n  http-get-no-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n  http-delete-no-body:\n    description: DELETE operations must not have a request body\n    severity: error\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n\
  \      function: falsy\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: $..description\n    then:\n      function: truthy\n  microcks-operation-extension:\n    description: Operations should have x-microcks-operation\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/rules/salesforce-spectral-rules.yml
tags:
- AI
- Analytics
- Cloud
- Commerce
- CRM
- Customer Service
- Enterprise
- Marketing
- Platform
- Sales
- Spectral
- Linting
- API Governance
---
