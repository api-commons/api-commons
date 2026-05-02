---
api_specs:
- filename: blob.json
  format: json
  label: Azure Blob Storage API
  slug: azure-blob-storage-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/storage/data-plane/Microsoft.BlobStorage/stable/2021-12-02/blob.json
- filename: azure-storage-account-management-openapi.yaml
  format: yaml
  label: Azure Queue Storage API
  slug: azure-queue-storage-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/azure-storage-account/refs/heads/main/openapi/azure-storage-account-management-openapi.yaml
- filename: azure-storage-account-management-openapi.yaml
  format: yaml
  label: Azure Table Storage API
  slug: azure-table-storage-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/azure-storage-account/refs/heads/main/openapi/azure-storage-account-management-openapi.yaml
- filename: azure-storage-account-management-openapi.yaml
  format: yaml
  label: Azure File Storage API
  slug: azure-file-storage-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/azure-storage-account/refs/heads/main/openapi/azure-storage-account-management-openapi.yaml
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
description: Spectral linting rules defining API design standards and conventions for Azure Storage Account.
layout: rules
name: Azure Storage Account API Rules
provider_name: Azure Storage Account
provider_slug: azure-storage-account
rule_count: 15
rules:
- description: API title must start with "Azure Storage Account"
  given: $.info.title
  name: info-title-format
  severity: warn
- description: Operation summaries must start with "Azure Storage Account"
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
- description: Paths must not end with a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: Must use OpenAPI 3.x or Swagger 2.x
  given: $
  name: openapi-version
  severity: warn
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Operations must define at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All inline parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[?(!@.$ref)]
  name: parameter-description-required
  severity: warn
- description: Top-level schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-properties-description
  severity: info
- description: All tags used in operations should be defined globally
  given: $.tags
  name: tags-global-definition
  severity: info
- description: OperationIds should use consistent naming
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: info
- description: Security schemes should be defined
  given: $.components.securitySchemes
  name: security-defined
  severity: info
rules_file: rules/azure-storage-account-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/azure-storage-account/refs/heads/main/rules/azure-storage-account-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 4
  warn: 6
slug: azure-storage-account-spectral-rules
source_filename: azure-storage-account-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  info-title-format:\n    description: API title must start with \"Azure Storage Account\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Azure\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"Azure Storage Account\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Azure\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n\
  \    description: All operations must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash\n    severity: error\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  openapi-version:\n    description: Must use OpenAPI 3.x or Swagger 2.x\n    severity: warn\n    given: $\n    then:\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  response-success-required:\n\
  \    description: Operations must define at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['202']\n            - required: ['204']\n\n  parameter-description-required:\n    description: All inline parameters must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[?(!@.$ref)]\n    then:\n      field: description\n      function: truthy\n\n  schema-properties-description:\n    description: Top-level schema properties should have descriptions\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: description\n      function: truthy\n\n  tags-global-definition:\n    description: All tags used in operations should be defined globally\n    severity: info\n    given:\
  \ $.tags\n    then:\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationIds should use consistent naming\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: truthy\n\n  security-defined:\n    description: Security schemes should be defined\n    severity: info\n    given: $.components.securitySchemes\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/azure-storage-account/refs/heads/main/rules/azure-storage-account-spectral-rules.yml
tags:
- Azure
- Blob Storage
- Cloud Storage
- File Storage
- Microsoft
- Storage
- Spectral
- Linting
- API Governance
---
