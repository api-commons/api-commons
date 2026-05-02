---
api_specs:
- filename: beyondtrust-password-safe-api.yaml
  format: yaml
  label: BeyondTrust Password Safe API
  slug: beyondtrust-password-safe-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/beyondtrust/refs/heads/main/openapi/beyondtrust-password-safe-api.yaml
categories:
- credential
- http
- info
- 'no'
- openapi
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for BeyondTrust.
layout: rules
name: BeyondTrust API Rules
provider_name: BeyondTrust
provider_slug: beyondtrust
rule_count: 23
rules:
- description: API title should start with "BeyondTrust"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must specify a version
  given: $.info
  name: info-version-required
  severity: error
- description: Should use OpenAPI 3.0.x
  given: $.openapi
  name: openapi-version-3
  severity: warn
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "BeyondTrust"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: All operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operations should have descriptions
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Operations must define a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Response descriptions are required
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Auth endpoints should return 401 on failure
  given: $.paths[*][post].responses
  name: response-401-for-auth
  severity: info
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema names should use PascalCase
  given: $.components.schemas
  name: schema-pascal-case-names
  severity: info
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security should be defined
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations should not have request bodies
  given: $.paths[*].get
  name: http-get-no-body
  severity: error
- description: DELETE operations should not have request bodies
  given: $.paths[*].delete
  name: http-delete-no-body
  severity: warn
- description: Credential retrieval endpoints must require authentication
  given: $.paths['/requests/{requestId}/credentials'].get
  name: credential-endpoint-secured
  severity: error
- description: Descriptions should not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/beyondtrust-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/beyondtrust/refs/heads/main/rules/beyondtrust-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 2
  warn: 11
slug: beyondtrust-spectral-rules
source_filename: beyondtrust-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title should start with \"BeyondTrust\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^BeyondTrust\"\n\n  info-description-required:\n    description: API info must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must specify a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Should use OpenAPI 3.0.x\n    severity: warn\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n\
  \      function: truthy\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"BeyondTrust\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^BeyondTrust\"\n\n  operation-id-required:\n    description: All operations must have operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\
  \n\n  operation-tags-required:\n    description: Operations must have tags\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  operation-description-required:\n    description: Operations should have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Parameters must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must define a success response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n\
  \    description: Response descriptions are required\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-401-for-auth:\n    description: Auth endpoints should return 401 on failure\n    severity: info\n    given: $.paths[*][post].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n\n  # SCHEMAS\n  schema-description-required:\n    description: Component schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-pascal-case-names:\n    description: Schema names should use PascalCase\n    message: \"Schema name '{{path}}' should use PascalCase\"\n    severity: info\n    given: $.components.schemas\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n\n  # SECURITY\n  security-schemes-defined:\n\
  \    description: Security schemes must be defined\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security should be defined\n    severity: warn\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHODS\n  http-get-no-body:\n    description: GET operations should not have request bodies\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  http-delete-no-body:\n    description: DELETE operations should not have request bodies\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  # PAM-SPECIFIC\n  credential-endpoint-secured:\n    description: Credential retrieval endpoints must require authentication\n    severity: error\n    given: $.paths['/requests/{requestId}/credentials'].get\n    then:\n      field: security\n \
  \     function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 0\n\n  no-empty-descriptions:\n    description: Descriptions should not be empty\n    severity: warn\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/beyondtrust/refs/heads/main/rules/beyondtrust-spectral-rules.yml
tags:
- Access
- Access Management
- Compliance
- Credentials
- Privileged Access
- Security
- Secrets
- Zero Trust
- Spectral
- Linting
- API Governance
---
