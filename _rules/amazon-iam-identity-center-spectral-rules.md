---
api_specs:
- filename: amazon-iam-identity-center-sso-admin-openapi-original.yml
  format: yaml
  label: AWS IAM Identity Center SSO Admin API
  slug: aws-sso-admin-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-iam-identity-center/refs/heads/main/openapi/amazon-iam-identity-center-sso-admin-openapi-original.yml
- filename: amazon-iam-identity-center-identitystore-openapi-original.yml
  format: yaml
  label: AWS IAM Identity Center Identity Store API
  slug: aws-identitystore-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-iam-identity-center/refs/heads/main/openapi/amazon-iam-identity-center-identitystore-openapi-original.yml
categories:
- get
- info
- 'no'
- openapi
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon IAM Identity Center.
layout: rules
name: Amazon IAM Identity Center API Rules
provider_name: Amazon IAM Identity Center
provider_slug: amazon-iam-identity-center
rule_count: 18
rules:
- description: Info title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be at least 20 characters.
  given: $.info
  name: info-description-required
  severity: warn
- description: API version must be specified.
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https-only
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with 'Amazon IAM Identity Center'.
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must define a 2xx response.
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Security schemes should be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: operationId should use PascalCase.
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-pascal-case
  severity: warn
rules_file: rules/amazon-iam-identity-center-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-iam-identity-center/refs/heads/main/rules/amazon-iam-identity-center-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 1
  warn: 8
slug: amazon-iam-identity-center-spectral-rules
source_filename: amazon-iam-identity-center-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  info-description-required:\n    description: Info description must be at least 20 characters.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: minLength\n      functionOptions:\n        min: 20\n  info-version-required:\n    description: API version must be specified.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n  openapi-version-3:\n    description: Must use OpenAPI 3.x.\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n  servers-https-only:\n\
  \    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n  operation-summary-prefix:\n    description: Operation summaries must start with 'Amazon IAM Identity Center'.\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Amazon IAM Identity Center\"\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n    description:\
  \ Every operation must have at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n  response-success-required:\n    description: Every operation must define a 2xx response.\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          minProperties: 1\n  response-description-required:\n    description: Every response must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].responses[*]\"\n    then:\n      field: description\n      function: truthy\n  schema-description-required:\n    description: Top-level schemas\
  \ should have a description.\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes should be defined in components.\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n  operation-id-pascal-case:\n    description: operationId should use PascalCase.\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*$\"\
  \n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-iam-identity-center/refs/heads/main/rules/amazon-iam-identity-center-spectral-rules.yml
tags:
- Access Control
- Authentication
- Identity Management
- Single Sign-On
- Spectral
- Linting
- API Governance
---
