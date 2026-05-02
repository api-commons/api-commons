---
api_specs:
- filename: ballerina-central-api.yml
  format: yaml
  label: Ballerina
  slug: ballerina
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/openapi/ballerina-central-api.yml
categories:
- get
- info
- openapi
- operation
- parameter
- paths
- response
- schema
description: Spectral linting rules defining API design standards and conventions for Ballerina.
layout: rules
name: Ballerina API Rules
provider_name: Ballerina
provider_slug: ballerina
rule_count: 11
rules:
- description: Info must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All schemas should have a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Path segments should use kebab-case or snake_case
  given: $.paths
  name: paths-kebab-case
  severity: info
rules_file: rules/ballerina-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/rules/ballerina-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 1
  warn: 3
slug: ballerina-spectral-rules
source_filename: ballerina-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info must have a title\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-version-required:\n    description: Info must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  openapi-version-3:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n\
  \    description: Every operation must have tags\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n  schema-type-defined:\n    description: All schemas should have a type\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n\
  \      function: falsy\n  paths-kebab-case:\n    description: Path segments should use kebab-case or snake_case\n    severity: info\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/[a-z0-9/_{}.-]*$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/rules/ballerina-spectral-rules.yml
tags:
- Integrations
- Orchestrations
- Open Source
- Programming Language
- Spectral
- Linting
- API Governance
---
