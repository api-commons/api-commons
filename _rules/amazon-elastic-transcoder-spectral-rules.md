---
api_specs:
- filename: amazon-elastic-transcoder-openapi.yml
  format: yaml
  label: Amazon Elastic Transcoder API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-elastic-transcoder/refs/heads/main/openapi/amazon-elastic-transcoder-openapi.yml
categories:
- delete
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
description: Spectral linting rules defining API design standards and conventions for Amazon Elastic Transcoder.
layout: rules
name: Amazon Elastic Transcoder API Rules
provider_name: Amazon Elastic Transcoder
provider_slug: amazon-elastic-transcoder
rule_count: 20
rules:
- description: OpenAPI info must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: OpenAPI info must have a description.
  given: $.info
  name: info-description-required
  severity: warn
- description: OpenAPI info must have a version.
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: OpenAPI must define at least one server.
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https-required
  severity: error
- description: All operations must have a summary.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: All operations must have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: All operations must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-operationId-required
  severity: error
- description: operationId must use camelCase.
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-operationId-camelCase
  severity: warn
- description: All operations must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: warn
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All operations must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete,head,options].responses
  name: operation-success-response-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options].responses[*]
  name: response-description-required
  severity: error
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: Schema properties should specify a type.
  given: $.components.schemas[*].properties[*]
  name: schema-properties-have-types
  severity: warn
- description: Top-level component schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
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
rules_file: rules/amazon-elastic-transcoder-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-elastic-transcoder/refs/heads/main/rules/amazon-elastic-transcoder-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 1
  warn: 9
slug: amazon-elastic-transcoder-spectral-rules
source_filename: amazon-elastic-transcoder-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Spectral Ruleset for Amazon Elastic Transcoder\n# Enforces API design conventions for Amazon Elastic Transcoder APIs\n\nrules:\n  # INFO / METADATA\n  info-title-required:\n    description: OpenAPI info must have a title.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: OpenAPI info must have a description.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: OpenAPI info must have a version.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.x.\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: OpenAPI\
  \ must define at least one server.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-required:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: All operations must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-operationId-required:\n    description: All operations must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\
  \n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationId-camelCase:\n    description: operationId must use camelCase.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: All operations must have at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  operation-success-response-required:\n    description: All operations must define at least one 2xx response.\n    severity: error\n\
  \    given: \"$.paths[*][get,post,put,patch,delete,head,options].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description: All responses must have a description.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # SCHEMAS\n  schema-properties-have-types:\n    description: Schema properties should specify a type.\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  schema-description-required:\n    description: Top-level component schemas\
  \ should have a description.\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # HTTP METHODS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-elastic-transcoder/refs/heads/main/rules/amazon-elastic-transcoder-spectral-rules.yml
tags:
- Amazon Web Services
- Media
- Transcoding
- Video
- Spectral
- Linting
- API Governance
---
