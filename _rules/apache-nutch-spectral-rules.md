---
api_specs:
- filename: apache-nutch-openapi.yaml
  format: yaml
  label: Apache Nutch REST API
  slug: apache-nutch-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/openapi/apache-nutch-openapi.yaml
categories:
- delete
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
- tags
description: Spectral linting rules defining API design standards and conventions for Apache Nutch.
layout: rules
name: Apache Nutch API Rules
provider_name: Apache Nutch
provider_slug: apache-nutch
rule_count: 33
rules:
- description: OpenAPI info must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: OpenAPI info must have a non-empty description.
  given: $.info
  name: info-description-required
  severity: warn
- description: OpenAPI info must define a version.
  given: $.info
  name: info-version-required
  severity: error
- description: OpenAPI info should include contact information.
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI info should include license information.
  given: $.info
  name: info-license-required
  severity: warn
- description: Specs must use OpenAPI 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Each server should have a description.
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments must use kebab-case (lowercase letters, numbers, hyphens).
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths should not have trailing slashes (except root).
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-operationid-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: Operation summaries should start with "Apache Nutch".
  given: $.paths[*][get,post,put,patch,delete,head,options].summary
  name: operation-summary-apache-nutch-prefix
  severity: info
- description: Global tags array should be defined.
  given: $
  name: tags-global-defined
  severity: warn
- description: Each global tag should have a description.
  given: $.tags[*]
  name: tags-description
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should have a description.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: Request bodies should support application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-content-json
  severity: warn
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Secured operations should document 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Operations should document 500 Internal Server Error response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-500-defined
  severity: info
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level component schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should define a type.
  given: $.components.schemas[*].properties[*]
  name: schema-property-type-required
  severity: warn
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security requirements should be defined.
  given: $
  name: security-global-defined
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
rules_file: rules/apache-nutch-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/rules/apache-nutch-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 2
  warn: 19
slug: apache-nutch-spectral-rules
source_filename: apache-nutch-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Apache Nutch API Spectral Ruleset\n# Enforces conventions observed across the Apache Nutch REST API OpenAPI specification.\n\nrules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: OpenAPI info must have a title.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: OpenAPI info must have a non-empty description.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: OpenAPI info must define a version.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: OpenAPI info should include contact information.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  info-license-required:\n    description: OpenAPI info should include license\
  \ information.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Specs must use OpenAPI 3.x.\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-description:\n    description: Each server should have a description.\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments must use kebab-case (lowercase letters, numbers, hyphens).\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match:\
  \ \"^(\\\\/([a-z0-9][a-z0-9\\\\-]*|\\\\{[a-zA-Z0-9_]+\\\\}))*\\\\/?$\"\n\n  paths-no-trailing-slash:\n    description: Paths should not have trailing slashes (except root).\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \".+\\\\/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Every operation should have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n\
  \      field: operationId\n      function: truthy\n\n  operation-operationid-camel-case:\n    description: operationId should use camelCase.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: tags\n      function: truthy\n\n  operation-summary-apache-nutch-prefix:\n    description: Operation summaries should start with \"Apache Nutch\".\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache Nutch \"\n\n  # TAGS\n  tags-global-defined:\n    description: Global tags array should be defined.\n    severity: warn\n    given:\
  \ \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  tags-description:\n    description: Each global tag should have a description.\n    severity: warn\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must have a schema.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have a description.\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody\"\n    then:\n      field: description\n    \
  \  function: truthy\n\n  request-body-content-json:\n    description: Request bodies should support application/json content type.\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one 2xx response.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-401-required:\n    description: Secured operations should document 401 Unauthorized response.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n \
  \     functionOptions:\n        schema:\n          type: object\n          required: [\"401\"]\n\n  response-500-defined:\n    description: Operations should document 500 Internal Server Error response.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"500\"]\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level component schemas should have a description.\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-property-type-required:\n    description: Schema properties should define a type.\n  \
  \  severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security requirements should be defined.\n    severity: warn\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL\
  \ QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/rules/apache-nutch-spectral-rules.yml
tags:
- Web Crawler
- Indexing
- Search
- Apache
- Java
- Hadoop
- Open Source
- Spectral
- Linting
- API Governance
---
