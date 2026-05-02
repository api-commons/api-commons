---
api_specs:
- filename: facebook-graph-api.yaml
  format: yaml
  label: Facebook Graph API
  slug: facebook-graph-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/facebook/refs/heads/main/openapi/facebook-graph-api.yaml
- filename: facebook-marketing-api.yaml
  format: yaml
  label: Facebook Marketing API
  slug: facebook-marketing-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/facebook/refs/heads/main/openapi/facebook-marketing-api.yaml
- filename: facebook-instagram-api.yaml
  format: yaml
  label: Instagram API
  slug: instagram-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/facebook/refs/heads/main/openapi/facebook-instagram-api.yaml
- filename: facebook-messenger-api.yaml
  format: yaml
  label: Messenger Platform API
  slug: messenger-platform-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/facebook/refs/heads/main/openapi/facebook-messenger-api.yaml
- filename: facebook-threads-api.yaml
  format: yaml
  label: Threads API
  slug: threads-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/facebook/refs/heads/main/openapi/facebook-threads-api.yaml
- filename: facebook-whatsapp-api.yaml
  format: yaml
  label: WhatsApp Business API
  slug: whatsapp-business-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/facebook/refs/heads/main/openapi/facebook-whatsapp-api.yaml
categories:
- delete
- examples
- get
- info
- 'no'
- openapi
- operation
- pagination
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Facebook.
layout: rules
name: Facebook API Rules
provider_name: Facebook
provider_slug: facebook
rule_count: 30
rules:
- description: Info title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with Facebook.
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info description must be present.
  given: $.info
  name: info-description-required
  severity: error
- description: Info version must be present.
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information should be provided.
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version should be 3.0.x.
  given: $
  name: openapi-version
  severity: warn
- description: Servers array must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Paths should not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with Facebook.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have tags.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: OperationId should be camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameter names should use snake_case or kebab-case.
  given: $.paths[*][get,post,put,patch,delete].parameters[*].name
  name: parameter-snake-case
  severity: info
- description: Operations must have a success response (2xx).
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Schema property names should use snake_case.
  given: $.components.schemas[*].properties
  name: schema-properties-snake-case
  severity: info
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas must have a type defined.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: error
- description: Global security must be defined.
  given: $
  name: security-defined
  severity: error
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Bearer authentication should be used.
  given: $.components.securitySchemes[*]
  name: security-bearer-scheme
  severity: info
- description: GET operations should not have a request body.
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
  severity: error
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
- description: Pagination should use cursor-based pagination with before/after.
  given: $.components.schemas.Paging
  name: pagination-cursor-pattern
  severity: info
rules_file: rules/facebook-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/facebook/refs/heads/main/rules/facebook-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 5
  warn: 12
slug: facebook-spectral-rules
source_filename: facebook-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be present.\n    given: $.info\n    severity: error\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: Info title should start with Facebook.\n    given: $.info.title\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Facebook \"\n\n  info-description-required:\n    description: Info description must be present.\n    given: $.info\n    severity: error\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info version must be present.\n    given: $.info\n    severity: error\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Contact information should be provided.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n\
  \    description: OpenAPI version should be 3.0.x.\n    given: $\n    severity: warn\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers array must be defined.\n    given: $\n    severity: error\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs should use HTTPS.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS - NAMING CONVENTIONS\n  paths-no-trailing-slash:\n    description: Paths should not have trailing slashes.\n    given: $.paths\n    severity: error\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    given: \"$.paths[*][get,post,put,patch,delete]\"\
  \n    severity: error\n    then:\n      field: operationId\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary.\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: error\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with Facebook.\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Facebook \"\n\n  operation-description-required:\n    description: Every operation must have a description.\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have tags.\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: warn\n    then:\n      field: tags\n      function:\
  \ truthy\n\n  operation-operationid-camelcase:\n    description: OperationId should be camelCase.\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description.\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  parameter-snake-case:\n    description: Parameter names should use snake_case or kebab-case.\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*].name\"\n    severity: info\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_\\\\-]*$\"\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must have a success response (2xx).\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\
  \n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: Every response must have a description.\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS - PROPERTY NAMING\n  schema-properties-snake-case:\n    description: Schema property names should use snake_case.\n    given: \"$.components.schemas[*].properties\"\n    severity: info\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n\n  schema-description-required:\n    description: Top-level schemas should have descriptions.\n    given: \"$.components.schemas[*]\"\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\
  \n  schema-type-required:\n    description: Schemas must have a type defined.\n    given: \"$.components.schemas[*]\"\n    severity: error\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-defined:\n    description: Global security must be defined.\n    given: $\n    severity: error\n    then:\n      field: security\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    given: $.components\n    severity: error\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-bearer-scheme:\n    description: Bearer authentication should be used.\n    given: \"$.components.securitySchemes[*]\"\n    severity: info\n    then:\n      field: scheme\n      function: pattern\n      functionOptions:\n        match: \"^bearer$\"\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations should not have a request body.\n    given: \"$.paths[*].get\"\n  \
  \  severity: error\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    given: \"$.paths[*].delete\"\n    severity: warn\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    given: \"$..description\"\n    severity: error\n    then:\n      function: truthy\n\n  examples-encouraged:\n    description: Schema properties should include example values.\n    given: \"$.components.schemas[*].properties[*]\"\n    severity: info\n    then:\n      field: example\n      function: truthy\n\n  # PAGINATION\n  pagination-cursor-pattern:\n    description: Pagination should use cursor-based pagination with before/after.\n    given: \"$.components.schemas.Paging\"\n    severity: info\n    then:\n      field: properties\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/facebook/refs/heads/main/rules/facebook-spectral-rules.yml
tags:
- Advertising
- Content Publishing
- Messaging
- Social Media
- Social Networking
- Spectral
- Linting
- API Governance
---
