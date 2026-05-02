---
api_specs:
- filename: azure-functions-management-api.json
  format: json
  label: Azure Functions Management API
  slug: azure-functions-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-functions/refs/heads/main/openapi/azure-functions-management-api.json
categories:
- get
- info
- 'no'
- operation
- parameter
- paths
- response
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Microsoft Azure Functions.
layout: rules
name: Microsoft Azure Functions API Rules
provider_name: Microsoft Azure Functions
provider_slug: microsoft-azure-functions
rule_count: 19
rules:
- description: API title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: API description must be present.
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be specified.
  given: $.info
  name: info-version-required
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Path segments should use camelCase (Azure convention).
  given: $.paths
  name: paths-camelcase
  severity: info
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operation IDs must be unique.
  given: $
  name: operation-operationid-unique
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Tag names should use Title Case.
  given: $.tags[*].name
  name: tags-title-case
  severity: info
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Azure APIs should include api-version as a query parameter.
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.name=='api-version')]
  name: parameter-api-version
  severity: info
- description: Every operation must define a success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Security schemes should be defined.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty.
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/azure-functions-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-functions/refs/heads/main/rules/azure-functions-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 3
  warn: 2
slug: azure-functions-spectral-rules
source_filename: azure-functions-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: API title must be present.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-description-required:\n    description: API description must be present.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API version must be specified.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n  servers-https-only:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n \
  \   severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n  paths-camelcase:\n    description: Path segments should use camelCase (Azure convention).\n    severity: info\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/[a-z]+_[a-z]\"\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  operation-operationid-unique:\n    description: Operation IDs must be unique.\n    severity: error\n    given: $\n    then:\n      function:\
  \ oasOpId\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  tags-title-case:\n    description: Tag names should use Title Case.\n    severity: info\n    given: $.tags[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*(\\\\s[A-Za-z0-9]+)*$\"\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n  parameter-api-version:\n    description: Azure APIs should include api-version as a query parameter.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].parameters[?(@.name=='api-version')]\n    then:\n      field: required\n      function: truthy\n  response-success-required:\n\
  \    description: Every operation must define a success response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"202\"]\n            - required: [\"204\"]\n  response-description-required:\n    description: All responses must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes should be defined.\n    severity: warn\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\
  \  no-empty-descriptions:\n    description: Descriptions must not be empty.\n    severity: error\n    given: \"$..description\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-functions/refs/heads/main/rules/azure-functions-spectral-rules.yml
tags:
- Azure
- Cloud
- Compute
- Event-Driven
- Microsoft
- Serverless
- Spectral
- Linting
- API Governance
---
