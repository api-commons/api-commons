---
api_specs:
- filename: swagger.json
  format: json
  label: Adobe Captivate Prime API
  slug: ''
  spec_type: OpenAPI
  url: https://learningmanager.adobe.com/primeapi/v2/swagger.json
- filename: adobe-captivate-learning-manager-webhooks-asyncapi.yml
  format: yaml
  label: Adobe Learning Manager Webhooks API
  slug: ''
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/adobe-captivate/refs/heads/main/asyncapi/adobe-captivate-learning-manager-webhooks-asyncapi.yml
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
- tags
description: Spectral linting rules defining API design standards and conventions for Adobe Captivate.
layout: rules
name: Adobe Captivate API Rules
provider_name: Adobe Captivate
provider_slug: adobe-captivate
rule_count: 34
rules:
- description: API title must start with "Adobe Captivate" or "Adobe Learning Manager"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API info must have a description of at least 50 characters
  given: $.info
  name: info-description-required
  severity: error
- description: API must declare a version
  given: $.info
  name: info-version-required
  severity: error
- description: API info should include contact details
  given: $.info
  name: info-contact-required
  severity: warn
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: API must define at least one server
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments should use kebab-case or camelCase (Adobe Learning Manager uses camelCase)
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
- description: Paths must not end with a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Adobe Captivate"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camelcase
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: API should define global tags
  given: $
  name: tags-defined
  severity: warn
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tags-description
  severity: info
- description: All parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: All parameters must have a schema
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: API keys should be passed in headers, not query parameters
  given: $.components.securitySchemes[*]
  name: parameter-api-key-in-header
  severity: warn
- description: Request bodies should have descriptions
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: Request bodies should include application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: info
- description: Every operation must define at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Operations should define 401 or 400 error responses
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-4xx-defined
  severity: warn
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Top-level component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: warn
- description: Schemas should define a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: API must define security schemes
  given: $.components
  name: security-schemes-defined
  severity: error
- description: API should define global security
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
  severity: error
- description: Operations should include examples for better documentation
  given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]
  name: examples-encouraged
  severity: info
rules_file: rules/adobe-captivate-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/adobe-captivate/refs/heads/main/rules/adobe-captivate-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 4
  warn: 14
slug: adobe-captivate-spectral-rules
source_filename: adobe-captivate-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"Adobe Captivate\" or \"Adobe Learning Manager\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Adobe (Captivate|Learning Manager)\"\n\n  info-description-required:\n    description: API info must have a description of at least 50 characters\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must declare a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should include contact details\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: $\n\
  \    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: API must define at least one server\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description:\n    description: Each server should have a description\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case or camelCase (Adobe Learning Manager uses camelCase)\n    severity: info\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/[a-zA-Z0-9{}/_-]+$\"\n\n \
  \ paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash\n    severity: warn\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Adobe Captivate\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Adobe Captivate\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n\
  \    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camelcase:\n    description: operationId should use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-defined:\n    description: API should define global tags\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  tags-description:\n    description: Global tags should have descriptions\n    severity: info\n    given: $.tags[*]\n    then:\n      field:\
  \ description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  parameter-api-key-in-header:\n    description: API keys should be passed in headers, not query parameters\n    severity: warn\n    given: $.components.securitySchemes[*]\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          not:\n            properties:\n              in:\n                const: query\n              type:\n                const: apiKey\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have descriptions\n    severity: warn\n    given:\
  \ $.paths[*][post,put,patch].requestBody\n    then:\n      field: description\n      function: truthy\n\n  request-body-json-content:\n    description: Request bodies should include application/json content type\n    severity: info\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"application/json\"]\n            - required: [\"application/vnd.api+json\"]\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"202\"]\n            - required: [\"204\"]\n\n  response-4xx-defined:\n    description: Operations should\
  \ define 401 or 400 error responses\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description:\n    description: Top-level component schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    description: Schemas should define a type\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: API must define security\
  \ schemes\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: API should define global security\n    severity: warn\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: $..description\n    then:\n      function: truthy\n\n  examples-encouraged:\n    description: Operations should include examples for better\
  \ documentation\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"example\"]\n            - required: [\"examples\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/adobe-captivate/refs/heads/main/rules/adobe-captivate-spectral-rules.yml
tags:
- Authoring
- Education
- eLearning
- LMS
- SCORM
- Training
- xAPI
- Spectral
- Linting
- API Governance
---
