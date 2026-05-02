---
api_specs:
- filename: apache-couchdb-http-api-openapi.yaml
  format: yaml
  label: Apache CouchDB HTTP API
  slug: apache-couchdb-http-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/openapi/apache-couchdb-http-api-openapi.yaml
categories:
- delete
- examples
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- request
- response
- schema
- security
- servers
- tag
description: Spectral linting rules defining API design standards and conventions for Apache CouchDB.
layout: rules
name: Apache CouchDB API Rules
provider_name: Apache CouchDB
provider_slug: apache-couchdb
rule_count: 28
rules:
- description: OpenAPI info title must be present
  given: $.info
  name: info-title-required
  severity: error
- description: OpenAPI info must have a description
  given: $.info
  name: info-description-required
  severity: warn
- description: OpenAPI info must include a version
  given: $.info
  name: info-version-required
  severity: error
- description: All specs must use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: warn
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: Production servers should use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: warn
- description: Path segments should use kebab-case (lowercase, hyphens allowed)
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Apache CouchDB"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: All tags used in operations should be defined globally
  given: $
  name: tag-global-defined
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-content-type
  severity: warn
- description: Every operation must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: GET operations on resource paths should include a 404 response
  given: $.paths[*].get.responses
  name: response-404-for-get
  severity: warn
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Top-level schemas should have a type defined
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined if security is declared
  given: $
  name: security-schemes-defined
  severity: error
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
  severity: warn
- description: Schema properties are encouraged to have examples
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/apache-couchdb-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/rules/apache-couchdb-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 2
  warn: 15
slug: apache-couchdb-spectral-rules
source_filename: apache-couchdb-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: OpenAPI info title must be present\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: OpenAPI info must have a description\n    severity: warn\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: OpenAPI info must include a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: All specs must use OpenAPI 3.0.x\n    severity: warn\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\
  \n  servers-https:\n    description: Production servers should use HTTPS\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^(https://|http://localhost)\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case (lowercase, hyphens allowed)\n    severity: warn\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9_{}\\\\-]+)+$|^/$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have a trailing slash\n    severity: warn\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n\
  \  operation-operationid-camel-case:\n    description: operationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Apache CouchDB\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache CouchDB \"\n\n  operation-description-required:\n    description: Every operation should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function:\
  \ truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tag-global-defined:\n    description: All tags used in operations should be defined globally\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-content-type:\n    description: Request bodies should\
  \ use application/json content type\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-404-for-get:\n    description: GET operations on resource paths should include a 404 response\n    severity: warn\n    given: \"$.paths[*].get.responses\"\n    then:\n      field: \"404\"\n      function: defined\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n\
  \      field: description\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-property-description:\n    description: Schema properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    description: Top-level schemas should have a type defined\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined if security is declared\n    severity: error\n    given: $\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n\
  \    description: DELETE operations should not have a request body\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  examples-encouraged:\n    description: Schema properties are encouraged to have examples\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: defined\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/rules/apache-couchdb-spectral-rules.yml
tags:
- Apache
- Database
- Document Store
- JSON
- NoSQL
- Open Source
- Replication
- REST
- Spectral
- Linting
- API Governance
---
