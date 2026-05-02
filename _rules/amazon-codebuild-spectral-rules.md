---
api_specs:
- filename: amazon-codebuild-openapi-original.yaml
  format: yaml
  label: Amazon CodeBuild API
  slug: amazon-codebuild-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-codebuild/refs/heads/main/openapi/amazon-codebuild-openapi-original.yaml
categories:
- info
- 'no'
- openapi
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon CodeBuild.
layout: rules
name: Amazon CodeBuild API Rules
provider_name: Amazon CodeBuild
provider_slug: amazon-codebuild
rule_count: 18
rules:
- description: API title should identify Amazon CodeBuild service
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.0.x
  given: $.openapi
  name: openapi-version-3
  severity: warn
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with Amazon CodeBuild
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-company-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationId-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must define at least one 2xx response
  given: $.paths[*][get,post,put,delete,patch]
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schema components should have a type defined
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should include x-microcks-operation for mock compatibility
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-microcks-operation
  severity: info
rules_file: rules/amazon-codebuild-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-codebuild/refs/heads/main/rules/amazon-codebuild-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 1
  warn: 8
slug: amazon-codebuild-spectral-rules
source_filename: amazon-codebuild-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: \"spectral:oas\"\n\nrules:\n\n  # INFO / METADATA\n  info-title-format:\n    description: API title should identify Amazon CodeBuild service\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^CodeBuild\"\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.0.x\n    severity: warn\n    given: \"$.openapi\"\n    then:\n      function: pattern\n      functionOptions:\n        match: '^3\\.0\\.'\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n\
  \      field: servers\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-company-prefix:\n    description: Operation summaries should start with Amazon CodeBuild\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon CodeBuild\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: description\n      function:\
  \ truthy\n\n  operation-operationId-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: Every response\
  \ must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-type-required:\n    description: Schema components should have a type defined\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  operation-microcks-operation:\n    description: Operations should include x-microcks-operation for mock compatibility\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch]\"\
  \n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-codebuild/refs/heads/main/rules/amazon-codebuild-spectral-rules.yml
tags:
- Amazon
- CI/CD
- Build
- Continuous Integration
- DevOps
- Testing
- Spectral
- Linting
- API Governance
---
