---
api_specs:
- filename: allianz-future-cloud-platform-services.yaml
  format: yaml
  label: Allianz Future Cloud Platform Services API
  slug: platform-services-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/allianz-future-cloud-platform/refs/heads/main/openapi/allianz-future-cloud-platform-services.yaml
categories:
- async
- get
- info
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Allianz Future Cloud Platform.
layout: rules
name: Allianz Future Cloud Platform API Rules
provider_name: Allianz Future Cloud Platform
provider_slug: allianz-future-cloud-platform
rule_count: 24
rules:
- description: API title must start with "Allianz"
  given: $.info.title
  name: info-title-allianz-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API info must define a version
  given: $.info
  name: info-version-required
  severity: error
- description: Specs must use OpenAPI 3.x
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Path segments must use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: API paths should be prefixed with /api or contain versioning
  given: $.paths
  name: paths-versioned
  severity: info
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Summaries must start with "Allianz Future Cloud Platform"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-allianz-prefix
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
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined
  given: $
  name: tags-defined
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Every operation must define a success response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Operations should define a 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: All responses must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations must not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-properties-described
  severity: info
- description: Async operations should return 202 Accepted
  given: $.paths[*].post.operationId
  name: async-operations-return-202
  severity: info
rules_file: rules/allianz-future-cloud-platform-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/allianz-future-cloud-platform/refs/heads/main/rules/allianz-future-cloud-platform-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 3
  warn: 6
slug: allianz-future-cloud-platform-spectral-rules
source_filename: allianz-future-cloud-platform-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Allianz Future Cloud Platform Spectral Rules\n# Enforces API conventions for the Allianz Future Cloud Platform Services API\n\nrules:\n\n  info-title-allianz-prefix:\n    description: API title must start with \"Allianz\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Allianz\"\n\n  info-description-required:\n    description: API info must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must define a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  openapi-version-3:\n    description: Specs must use OpenAPI 3.x\n    severity: error\n    given: \"$.openapi\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  servers-defined:\n    description: At least one server\
  \ must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  paths-kebab-case:\n    description: Path segments must use kebab-case\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(\\\\/([a-z0-9][a-z0-9-]*|\\\\{[a-zA-Z_]+\\\\}))+$\"\n\n  paths-versioned:\n    description: API paths should be prefixed with /api or contain versioning\n    severity: info\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^\\\\/[a-z]\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: error\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n\
  \        notMatch: \"\\\\/$\"\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-allianz-prefix:\n    description: Summaries must start with \"Allianz Future Cloud Platform\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Allianz Future Cloud Platform\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function:\
  \ truthy\n\n  operation-id-camel-case:\n    description: operationId must use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  tags-defined:\n    description: Global tags array should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-success-required:\n    description: Every operation must define a success response\n\
  \    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: truthy\n\n  response-401-required:\n    description: Operations should define a 401 response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - \"401\"\n\n  response-description-required:\n    description: All responses must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  get-no-request-body:\n    description: GET operations must not have request bodies\n    severity: error\n    given:\
  \ \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  schema-properties-described:\n    description: Schema properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  async-operations-return-202:\n    description: Async operations should return 202 Accepted\n    severity: info\n    given: \"$.paths[*].post.operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(deploy|provision|register)\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/allianz-future-cloud-platform/refs/heads/main/rules/allianz-future-cloud-platform-spectral-rules.yml
tags:
- Cloud Platform
- Enterprise
- Financial Services
- Insurance
- Platform Engineering
- Kubernetes
- Spectral
- Linting
- API Governance
---
