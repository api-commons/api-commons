---
api_specs:
- filename: apis-guru-openapi.yaml
  format: yaml
  label: APIs.guru REST API
  slug: apis-guru-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apis-guru/refs/heads/main/openapi/apis-guru-openapi.yaml
categories:
- delete
- examples
- external
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for APIs.guru.
layout: rules
name: APIs.guru API Rules
provider_name: APIs.guru
provider_slug: apis-guru
rule_count: 30
rules:
- description: Info title should start with "APIs.guru"
  given: $.info.title
  name: info-title-format
  severity: warn
- description: Info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Info should have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Info should have license information
  given: $.info
  name: info-license-required
  severity: warn
- description: Specs should use OpenAPI 3.0.x
  given: $.openapi
  name: openapi-version-3
  severity: warn
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "APIs.guru"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: All operations should have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: OperationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined
  given: $
  name: tags-defined
  severity: warn
- description: All tags should have descriptions
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: All parameters must have a schema type
  given: $.paths[*][*].parameters[*].schema
  name: parameter-schema-type-required
  severity: error
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
- description: Schema objects should have a type defined
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security defined at operation or global level
  given: $
  name: no-global-security-required
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: External documentation is encouraged
  given: $
  name: external-docs-encouraged
  severity: info
- description: Schema properties should have examples
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/apis-guru-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apis-guru/refs/heads/main/rules/apis-guru-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 4
  warn: 13
slug: apis-guru-spectral-rules
source_filename: apis-guru-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-format:\n    description: Info title should start with \"APIs.guru\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^APIs\\\\.guru\"\n\n  info-description-required:\n    description: Info must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info should have contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  info-license-required:\n    description: Info should have license information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  # OPENAPI\
  \ VERSION\n  openapi-version-3:\n    description: Specs should use OpenAPI 3.0.x\n    severity: warn\n    given: \"$.openapi\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers array must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(\\\\/([a-z0-9-{}._]+))*$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have a trailing slash\n    severity: warn\n    given: \"$.paths[*]~\"\
  \n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"APIs.guru\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^APIs\\\\.guru\"\n\n  operation-description-required:\n    description: All operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\
  \n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-defined:\n    description: Global tags array should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  tag-description-required:\n    description: All tags should have descriptions\n    severity: warn\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All\
  \ parameters must have descriptions\n    severity: error\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-type-required:\n    description: All parameters must have a schema type\n    severity: error\n    given: \"$.paths[*][*].parameters[*].schema\"\n    then:\n      field: type\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: All responses must have descriptions\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description-recommended:\n    description: Component schemas should have descriptions\n    severity: info\n    given:\
  \ \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    description: Schema objects should have a type defined\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  no-global-security-required:\n    description: Security defined at operation or global level\n    severity: info\n    given: \"$\"\n    then:\n      field: security\n      function: defined\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description:\
  \ Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  external-docs-encouraged:\n    description: External documentation is encouraged\n    severity: info\n    given: \"$\"\n    then:\n      field: externalDocs\n      function: truthy\n\n  examples-encouraged:\n    description: Schema properties should have examples\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apis-guru/refs/heads/main/rules/apis-guru-spectral-rules.yml
tags:
- API Catalog
- API Directory
- API Discovery
- Community
- GraphQL
- Open Source
- OpenAPI
- Spectral
- Linting
- API Governance
---
