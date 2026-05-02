---
api_specs:
- filename: bigpanda-openapi.yml
  format: yaml
  label: BigPanda
  slug: bigpanda
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/openapi/bigpanda-openapi.yml
categories:
- bigpanda
description: Spectral linting rules defining API design standards and conventions for BigPanda.
layout: rules
name: BigPanda API Rules
provider_name: BigPanda
provider_slug: bigpanda
rule_count: 23
rules:
- description: API title must start with "BigPanda"
  given: $.info.title
  name: bigpanda-info-title-prefix
  severity: error
- description: API info must have a version field
  given: $.info
  name: bigpanda-info-version-present
  severity: error
- description: API info must include contact details
  given: $.info
  name: bigpanda-info-contact-present
  severity: warn
- description: Operation summaries must start with "BigPanda"
  given: $.paths[*][*].summary
  name: bigpanda-operation-summary-prefix
  severity: error
- description: Operation IDs must be camelCase
  given: $.paths[*][*].operationId
  name: bigpanda-operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][*]
  name: bigpanda-operation-tags-present
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][*]
  name: bigpanda-operation-description-present
  severity: warn
- description: Paths must not end with a slash
  given: $.paths
  name: bigpanda-path-no-trailing-slash
  severity: warn
- description: POST operations must have a request body
  given: $.paths[*].post
  name: bigpanda-request-body-required
  severity: error
- description: Every operation must define a success response
  given: $.paths[*][*].responses
  name: bigpanda-response-success-present
  severity: error
- description: All schemas must have a title
  given: $.components.schemas[*]
  name: bigpanda-schema-title-present
  severity: warn
- description: All schemas must have a description
  given: $.components.schemas[*]
  name: bigpanda-schema-description-present
  severity: warn
- description: Schema properties must have descriptions
  given: $.components.schemas[*].properties[*]
  name: bigpanda-schema-properties-described
  severity: warn
- description: API must define at least one security scheme
  given: $.components
  name: bigpanda-security-scheme-present
  severity: error
- description: Security scheme must be bearer auth
  given: $.components.securitySchemes[*]
  name: bigpanda-bearer-auth-used
  severity: warn
- description: Operations must declare security
  given: $.paths[*][get,post,put,patch,delete]
  name: bigpanda-operation-security-present
  severity: warn
- description: All tags used in operations must be defined at top level
  given: $.tags
  name: bigpanda-tags-defined
  severity: warn
- description: API must define servers
  given: $
  name: bigpanda-servers-present
  severity: error
- description: Server URL must use HTTPS
  given: $.servers[*].url
  name: bigpanda-server-https
  severity: error
- description: Responses with content should include examples
  given: $.paths[*][*].responses[*].content[*]
  name: bigpanda-operation-examples-present
  severity: warn
- description: Every operation must include x-microcks-operation extension
  given: $.paths[*][*]
  name: bigpanda-microcks-operation-present
  severity: warn
- description: Alert requests must include app_key field
  given: $.components.schemas.AlertRequest.required
  name: bigpanda-alert-app-key-required
  severity: warn
- description: API info must include license
  given: $.info
  name: bigpanda-license-present
  severity: warn
rules_file: rules/bigpanda-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/rules/bigpanda-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 0
  warn: 15
slug: bigpanda-spectral-rules
source_filename: bigpanda-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  bigpanda-info-title-prefix:\n    description: API title must start with \"BigPanda\"\n    message: 'Info title must start with \"BigPanda\": {{value}}'\n    severity: error\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^BigPanda\"\n\n  bigpanda-info-version-present:\n    description: API info must have a version field\n    message: Info object must include a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  bigpanda-info-contact-present:\n    description: API info must include contact details\n    message: Info object must include contact\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  bigpanda-operation-summary-prefix:\n    description: Operation summaries must start with \"BigPanda\"\n    message: 'Operation summary must start with \"BigPanda\": {{value}}'\n    severity: error\n    given: \"$.paths[*][*].summary\"\
  \n    then:\n      function: pattern\n      functionOptions:\n        match: \"^BigPanda\"\n\n  bigpanda-operation-id-camel-case:\n    description: Operation IDs must be camelCase\n    message: 'OperationId must be camelCase: {{value}}'\n    severity: warn\n    given: \"$.paths[*][*].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  bigpanda-operation-tags-present:\n    description: Every operation must have at least one tag\n    message: Operations must include tags\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n\n  bigpanda-operation-description-present:\n    description: Every operation must have a description\n    message: Operations must include description\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: description\n      function: truthy\n\n  bigpanda-path-no-trailing-slash:\n    description: Paths must not end with a slash\n \
  \   message: 'Path must not end with slash: {{value}}'\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  bigpanda-request-body-required:\n    description: POST operations must have a request body\n    message: POST operations must include requestBody\n    severity: error\n    given: \"$.paths[*].post\"\n    then:\n      field: requestBody\n      function: truthy\n\n  bigpanda-response-success-present:\n    description: Every operation must define a success response\n    message: Operations must include a 200 or 201 response\n    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n\n  bigpanda-schema-title-present:\n    description: All schemas must have a title\n    message: Schemas must include title\n    severity:\
  \ warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: title\n      function: truthy\n\n  bigpanda-schema-description-present:\n    description: All schemas must have a description\n    message: Schemas must include description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  bigpanda-schema-properties-described:\n    description: Schema properties must have descriptions\n    message: Schema properties must include description\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  bigpanda-security-scheme-present:\n    description: API must define at least one security scheme\n    message: Components must include securitySchemes\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  bigpanda-bearer-auth-used:\n    description: Security scheme must\
  \ be bearer auth\n    message: BigPanda uses Bearer token authentication\n    severity: warn\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            scheme:\n              enum: [bearer]\n\n  bigpanda-operation-security-present:\n    description: Operations must declare security\n    message: Operations must include security definition\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: security\n      function: truthy\n\n  bigpanda-tags-defined:\n    description: All tags used in operations must be defined at top level\n    message: Tags must be defined in the global tags section\n    severity: warn\n    given: \"$.tags\"\n    then:\n      function: truthy\n\n  bigpanda-servers-present:\n    description: API must define servers\n    message: Servers array must be present and non-empty\n    severity: error\n    given:\
  \ \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  bigpanda-server-https:\n    description: Server URL must use HTTPS\n    message: 'Server URL must use HTTPS: {{value}}'\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  bigpanda-operation-examples-present:\n    description: Responses with content should include examples\n    message: Response content should include examples\n    severity: warn\n    given: \"$.paths[*][*].responses[*].content[*]\"\n    then:\n      field: examples\n      function: truthy\n\n  bigpanda-microcks-operation-present:\n    description: Every operation must include x-microcks-operation extension\n    message: Operations must include x-microcks-operation\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  bigpanda-alert-app-key-required:\n    description: Alert requests must\
  \ include app_key field\n    message: AlertRequest schema must have app_key as required\n    severity: warn\n    given: \"$.components.schemas.AlertRequest.required\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type: string\n            enum: [app_key]\n\n  bigpanda-license-present:\n    description: API info must include license\n    message: Info must include license\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/rules/bigpanda-spectral-rules.yml
tags:
- Incidents
- Monitoring
- Platform
- Spectral
- Linting
- API Governance
---
