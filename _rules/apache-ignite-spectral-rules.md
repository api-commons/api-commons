---
api_specs:
- filename: apache-ignite-rest-api.yaml
  format: yaml
  label: Apache Ignite REST API
  slug: rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-ignite/refs/heads/main/openapi/apache-ignite-rest-api.yaml
categories:
- examples
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Apache Ignite.
layout: rules
name: Apache Ignite API Rules
provider_name: Apache Ignite
provider_slug: apache-ignite
rule_count: 23
rules:
- description: Info title must be present and start with Apache Ignite
  given: $.info
  name: info-title-required
  severity: error
- description: Info must have a description
  given: $.info
  name: info-description-required
  severity: warn
- description: Info must have a version field
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with Apache Ignite
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-prefix
  severity: warn
- description: Every operation should have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: Parameters should have descriptions
  given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete,head,options].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Security schemes should be defined
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: POST/PUT operations should document 400 responses
  given: $.paths[*][post,put].responses
  name: response-error-400
  severity: info
- description: GET operations should document 404 responses
  given: $.paths[*].get.responses
  name: response-error-404
  severity: info
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Schema properties should include examples
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/apache-ignite-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-ignite/refs/heads/main/rules/apache-ignite-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 4
  warn: 9
slug: apache-ignite-spectral-rules
source_filename: apache-ignite-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present and start with Apache Ignite\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^Apache Ignite\"\n\n  info-description-required:\n    description: Info must have a description\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info must have a version field\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  servers-defined:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function:\
  \ truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with Apache Ignite\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Apache Ignite\"\n\n  operation-description-required:\n    description: Every operation should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: operationId\n\
  \      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: tags\n      function: truthy\n\n  parameter-description-required:\n    description: Parameters should have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-success-required:\n    description: Every operation must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].responses\"\
  \n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-description-required:\n    description: Top-level schemas should have descriptions\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths\"\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(\\/([a-z0-9{}_-]+))*$\"\n\n  get-no-request-body:\n    description: GET operations must not have a request\
  \ body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  security-schemes-defined:\n    description: Security schemes should be defined\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  response-error-400:\n    description: POST/PUT operations should document 400 responses\n    severity: info\n    given: \"$.paths[*][post,put].responses\"\n    then:\n      field: \"400\"\n      function: truthy\n\n  response-error-404:\n    description: GET operations should document 404 responses\n    severity: info\n    given: \"$.paths[*].get.responses\"\n    then:\n      field: \"404\"\n      function: truthy\n\n  paths-no-trailing-slash:\n    description: Paths\
  \ must not have trailing slashes\n    severity: warn\n    given: \"$.paths\"\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  examples-encouraged:\n    description: Schema properties should include examples\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-ignite/refs/heads/main/rules/apache-ignite-spectral-rules.yml
tags:
- Caching
- Compute Grid
- Distributed Database
- In-Memory
- Open Source
- SQL
- Spectral
- Linting
- API Governance
---
