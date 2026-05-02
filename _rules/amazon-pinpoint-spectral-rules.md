---
api_specs:
- filename: amazon-pinpoint-openapi.yml
  format: yaml
  label: Amazon Pinpoint API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-pinpoint/refs/heads/main/openapi/amazon-pinpoint-openapi.yml
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
description: Spectral linting rules defining API design standards and conventions for Amazon Pinpoint.
layout: rules
name: Amazon Pinpoint API Rules
provider_name: Amazon Pinpoint
provider_slug: amazon-pinpoint
rule_count: 35
rules:
- description: API title must reference Amazon Pinpoint
  given: $.info.title
  name: info-title-contains-amazon-pinpoint
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: API must provide contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: API should use OpenAPI 3.x
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Path segments must use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: All paths must start with /v1/
  given: $.paths
  name: paths-v1-prefix
  severity: info
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Summaries must begin with 'Amazon Pinpoint'
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amazon-pinpoint-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-id-required
  severity: error
- description: OperationId must use PascalCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-pascal-case
  severity: warn
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: error
- description: Global tags must be defined
  given: $
  name: tags-global-defined
  severity: warn
- description: Tag names must use Title Case
  given: $.tags[*].name
  name: tags-title-case
  severity: warn
- description: Tags must have descriptions
  given: $.tags[*]
  name: tags-description-required
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: All parameters must have a schema
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should have descriptions
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: Request bodies should support application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: All operations must have a success response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Operations should define 401 unauthorized responses
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-defined
  severity: info
- description: Operations should define 404 not found responses
  given: $.paths[*][get,put,patch,delete].responses
  name: response-404-defined
  severity: info
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schemas must define a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
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
- description: Operations should provide examples for responses
  given: $.paths[*][*].responses[*].content[*]
  name: operation-examples-encouraged
  severity: info
rules_file: rules/amazon-pinpoint-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-pinpoint/refs/heads/main/rules/amazon-pinpoint-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 5
  warn: 16
slug: amazon-pinpoint-spectral-rules
source_filename: amazon-pinpoint-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-contains-amazon-pinpoint:\n    description: API title must reference Amazon Pinpoint\n    message: Info title should contain 'Amazon Pinpoint'\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"Amazon Pinpoint\"\n\n  info-description-required:\n    description: API must have a description\n    message: Info object must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API version must be defined\n    message: Info object must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API must provide contact information\n    message: Info object should have contact information\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n\
  \      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: API should use OpenAPI 3.x\n    message: Spec must use OpenAPI 3.0 or higher\n    severity: error\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined\n    message: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS\n    message: Server URL must use HTTPS\n    severity: warn\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https\"\n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments must use kebab-case\n    message: Path segments must use kebab-case (lowercase, hyphens allowed)\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n  \
  \    function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}_/-]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    message: Path must not end with a slash\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  paths-v1-prefix:\n    description: All paths must start with /v1/\n    message: Paths must be prefixed with /v1/\n    severity: info\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^/v1/\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    message: Operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-amazon-pinpoint-prefix:\n    description: Summaries must\
  \ begin with 'Amazon Pinpoint'\n    message: Operation summary must start with 'Amazon Pinpoint'\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Pinpoint\"\n\n  operation-description-required:\n    description: All operations must have a description\n    message: Operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an operationId\n    message: Operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-pascal-case:\n    description: OperationId must use PascalCase\n    message: OperationId must be in PascalCase format\n    severity: warn\n   \
  \ given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: All operations must have tags\n    message: Operation must have at least one tag\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-global-defined:\n    description: Global tags must be defined\n    message: Global tags array should be defined\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  tags-title-case:\n    description: Tag names must use Title Case\n    message: Tag name must use Title Case\n    severity: warn\n    given: $.tags[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z]\"\n\n  tags-description-required:\n    description: Tags must have descriptions\n    message: Tag must have a\
  \ description\n    severity: warn\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have descriptions\n    message: Parameter must have a description\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema\n    message: Parameter must have a schema\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have descriptions\n    message: Request body should have a description\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody\n    then:\n      field: description\n      function: truthy\n\n  request-body-json-content:\n    description: Request bodies should\
  \ support application/json\n    message: Request body should have application/json content type\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: All operations must have a success response\n    message: Operation must define at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: All responses must have descriptions\n    message: Response must have a description\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-401-defined:\n    description: Operations should define 401 unauthorized responses\n    message: Operation should define a 401 Unauthorized response\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].responses\n\
  \    then:\n      field: \"401\"\n      function: truthy\n\n  response-404-defined:\n    description: Operations should define 404 not found responses\n    message: Operation should define a 404 Not Found response\n    severity: info\n    given: $.paths[*][get,put,patch,delete].responses\n    then:\n      field: \"404\"\n      function: truthy\n\n  # SCHEMAS\n  schema-property-description:\n    description: Schema properties should have descriptions\n    message: Schema property should have a description\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    description: Schemas must define a type\n    message: Schema must have a type defined\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined\n    message: Components must define\
  \ securitySchemes\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security must be defined\n    message: Global security requirements should be defined\n    severity: warn\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    message: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    message: DELETE operations should not have a request body\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not\
  \ be empty strings\n    message: Description must not be empty\n    severity: warn\n    given: $..description\n    then:\n      function: truthy\n\n  operation-examples-encouraged:\n    description: Operations should provide examples for responses\n    message: Consider adding examples to operation responses\n    severity: info\n    given: $.paths[*][*].responses[*].content[*]\n    then:\n      field: examples\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-pinpoint/refs/heads/main/rules/amazon-pinpoint-spectral-rules.yml
tags:
- Campaigns
- Communications
- Email
- Marketing
- Messaging
- Push Notifications
- SMS
- Voice
- Customer Engagement
- Segmentation
- Journeys
- Analytics
- Spectral
- Linting
- API Governance
---
