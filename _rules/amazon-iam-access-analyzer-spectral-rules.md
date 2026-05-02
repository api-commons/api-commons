---
api_specs:
- filename: amazon-iam-access-analyzer-openapi-original.yml
  format: yaml
  label: AWS IAM Access Analyzer API
  slug: aws-access-analyzer-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-iam-access-analyzer/refs/heads/main/openapi/amazon-iam-access-analyzer-openapi-original.yml
categories:
- delete
- examples
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
description: Spectral linting rules defining API design standards and conventions for Amazon IAM Access Analyzer.
layout: rules
name: Amazon IAM Access Analyzer API Rules
provider_name: Amazon IAM Access Analyzer
provider_slug: amazon-iam-access-analyzer
rule_count: 23
rules:
- description: Info title must be present and non-empty.
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present and have at least 20 characters.
  given: $.info
  name: info-description-required
  severity: warn
- description: API version must be specified in info.version.
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x specification.
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
- description: Every operation must have a non-empty summary.
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-summary-required
  severity: error
- description: Every operation summary must start with 'Amazon IAM Access Analyzer'.
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-id-required
  severity: error
- description: operationId should use PascalCase (e.g. ListAnalyzers, CreateAnalyzer).
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,delete,patch,head,options].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must define a schema.
  given: $.paths[*][get,post,put,delete,patch,head,options].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Every operation must define at least one 2xx success response.
  given: $.paths[*][get,post,put,delete,patch,head,options].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,delete,patch,head,options].responses[*]
  name: response-description-required
  severity: warn
- description: Top-level component schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Schemas should define an explicit type.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: info
- description: Security schemes must be defined in components if security is used.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/amazon-iam-access-analyzer-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-iam-access-analyzer/refs/heads/main/rules/amazon-iam-access-analyzer-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 3
  warn: 10
slug: amazon-iam-access-analyzer-spectral-rules
source_filename: amazon-iam-access-analyzer-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be present and non-empty.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info description must be present and have at least 20 characters.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: minLength\n      functionOptions:\n        min: 20\n\n  info-version-required:\n    description: API version must be specified in info.version.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.x specification.\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server\
  \ must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a non-empty summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch,head,options]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Every operation summary must start with 'Amazon IAM Access Analyzer'.\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch,head,options]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Amazon IAM Access Analyzer\"\n\n  operation-description-required:\n    description: Every\
  \ operation must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch,head,options]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch,head,options]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use PascalCase (e.g. ListAnalyzers, CreateAnalyzer).\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch,head,options]\"\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch,head,options]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n\
  \  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch,head,options].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must define a schema.\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch,head,options].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one 2xx success response.\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch,head,options].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          minProperties: 1\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch,head,options].responses[*]\"\
  \n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level component schemas should have a description.\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    description: Schemas should define an explicit type.\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components if security is used.\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n\
  \    description: DELETE operations should not have a request body.\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: truthy\n\n  examples-encouraged:\n    description: Schema properties should include example values.\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-iam-access-analyzer/refs/heads/main/rules/amazon-iam-access-analyzer-spectral-rules.yml
tags:
- Access Control
- Compliance
- IAM
- Policy Management
- Security
- Spectral
- Linting
- API Governance
---
