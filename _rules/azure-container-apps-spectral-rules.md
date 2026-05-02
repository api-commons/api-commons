---
api_specs:
- filename: azure-container-apps-openapi.yml
  format: yaml
  label: Azure Container Apps
  slug: azure-container-apps
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/openapi/azure-container-apps-openapi.yml
categories:
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
description: Spectral linting rules defining API design standards and conventions for Azure Container Apps.
layout: rules
name: Azure Container Apps API Rules
provider_name: Azure Container Apps
provider_slug: azure-container-apps
rule_count: 17
rules:
- description: API title must start with "Azure Container Apps"
  given: $.info.title
  name: info-title-format
  severity: warn
- description: Operation summaries must start with "Azure Container Apps"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Path segments must use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not end with a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: Must use OpenAPI 3.x
  given: $.openapi
  name: openapi-version
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Security schemes must be defined
  given: $.components.securitySchemes
  name: security-defined
  severity: warn
- description: Operations must define at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All schemas must define a type
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Global tag names should use Title Case
  given: $.tags[*].name
  name: tags-title-case
  severity: info
- description: OperationIds should use PascalCase with underscore separator
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: info
rules_file: rules/azure-container-apps-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/rules/azure-container-apps-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 2
  warn: 8
slug: azure-container-apps-spectral-rules
source_filename: azure-container-apps-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  info-title-format:\n    description: API title must start with \"Azure Container Apps\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Azure Container Apps\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"Azure Container Apps\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Azure Container Apps\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n\
  \    description: All operations must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  paths-kebab-case:\n    description: Path segments must use kebab-case\n    severity: warn\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash\n    severity: error\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n\
  \        match: \"^3\\\\.\"\n\n  servers-defined:\n    description: Servers must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  security-defined:\n    description: Security schemes must be defined\n    severity: warn\n    given: $.components.securitySchemes\n    then:\n      function: truthy\n\n  response-success-required:\n    description: Operations must define at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['202']\n            - required: ['204']\n\n  parameter-description-required:\n\
  \    description: All parameters must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: All schemas must define a type\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  tags-title-case:\n    description: Global tag names should use Title Case\n    severity: info\n    given: $.tags[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z]\"\n\n  operation-id-camel-case:\n    description: OperationIds should use PascalCase with underscore separator\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z]+_[A-Z][a-zA-Z]+$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/rules/azure-container-apps-spectral-rules.yml
tags:
- Azure
- Containers
- Dapr
- Kubernetes
- Microservices
- Serverless
- Spectral
- Linting
- API Governance
---
