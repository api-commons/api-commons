---
api_specs:
- filename: amazon-efs-openapi.yml
  format: yaml
  label: Amazon EFS API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-efs/refs/heads/main/openapi/amazon-efs-openapi.yml
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
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon EFS.
layout: rules
name: Amazon EFS API Rules
provider_name: Amazon EFS
provider_slug: amazon-efs
rule_count: 28
rules:
- description: API title should include the provider name (Amazon EFS).
  given: $.info
  name: info-title-matches-provider
  severity: warn
- description: API info must include a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: API info should include contact information.
  given: $.info
  name: info-contact-required
  severity: warn
- description: API info should include license information.
  given: $.info
  name: info-license-required
  severity: warn
- description: OpenAPI specification should use version 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS.
  given: $.servers[*]
  name: servers-https
  severity: warn
- description: Each server should have a description.
  given: $.servers[*]
  name: servers-description
  severity: info
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summary should begin with the provider name (Amazon EFS).
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-provider-prefix
  severity: warn
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: OperationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined.
  given: $
  name: tags-global-defined
  severity: warn
- description: Each global tag should have a description.
  given: $.tags[*]
  name: tag-description-required
  severity: info
- description: All parameters must have a description.
  given: $..parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema.
  given: $..parameters[*]
  name: parameter-schema-required
  severity: error
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schema properties should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schemas should define a type.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes should be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations should not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions should not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should include examples for better documentation.
  given: $.paths[*][get,post,put,patch,delete]
  name: examples-encouraged
  severity: info
rules_file: rules/amazon-efs-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-efs/refs/heads/main/rules/amazon-efs-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 4
  warn: 13
slug: amazon-efs-spectral-rules
source_filename: amazon-efs-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\n\nrules:\n  # INFO / METADATA\n  info-title-matches-provider:\n    description: API title should include the provider name (Amazon EFS).\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^Amazon EFS\"\n\n  info-description-required:\n    description: API info must include a description.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API version must be defined.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should include contact information.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  info-license-required:\n    description: API info should include license information.\n    severity: warn\n \
  \   given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: OpenAPI specification should use version 3.x.\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs should use HTTPS.\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description:\n    description: Each server should have a description.\n    severity: info\n    given: \"$.servers[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # OPERATIONS\n  operation-summary-required:\n    description:\
  \ Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-provider-prefix:\n    description: Operation summary should begin with the provider name (Amazon EFS).\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Amazon EFS\"\n\n  operation-description-required:\n    description: Every operation should have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n\
  \    description: OperationId should use camelCase.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-global-defined:\n    description: Global tags array should be defined.\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  tag-description-required:\n    description: Each global tag should have a description.\n    severity: info\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity:\
  \ warn\n    given: \"$..parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema.\n    severity: error\n    given: \"$..parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one 2xx response.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-property-description:\n    description: Schema properties should have descriptions.\n    severity: info\n    given:\
  \ \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    description: Schemas should define a type.\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes should be defined in components.\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations should not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n\
  \    description: Descriptions should not be empty strings.\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  examples-encouraged:\n    description: Operations should include examples for better documentation.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-efs/refs/heads/main/rules/amazon-efs-spectral-rules.yml
tags:
- Amazon Web Services
- EFS
- Elastic File System
- File Storage
- NFS
- Serverless
- Storage
- Spectral
- Linting
- API Governance
---
