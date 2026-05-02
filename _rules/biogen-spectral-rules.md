---
api_specs:
- filename: biogen-developer-api-openapi.yml
  format: yaml
  label: Biogen Developer API
  slug: developer-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/biogen/refs/heads/main/openapi/biogen-developer-api-openapi.yml
categories:
- biogen
description: Spectral linting rules defining API design standards and conventions for Biogen.
layout: rules
name: Biogen API Rules
provider_name: Biogen
provider_slug: biogen
rule_count: 23
rules:
- description: API title must start with "Biogen"
  given: $.info.title
  name: biogen-info-title-prefix
  severity: error
- description: API info must have a version field
  given: $.info
  name: biogen-info-version-present
  severity: error
- description: API info must include contact details
  given: $.info
  name: biogen-info-contact-present
  severity: warn
- description: Operation summaries must start with "Biogen"
  given: $.paths[*][*].summary
  name: biogen-operation-summary-prefix
  severity: error
- description: Operation IDs must be camelCase
  given: $.paths[*][*].operationId
  name: biogen-operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][*]
  name: biogen-operation-tags-present
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][*]
  name: biogen-operation-description-present
  severity: warn
- description: Every operation must define a success response
  given: $.paths[*][*].responses
  name: biogen-response-success-present
  severity: error
- description: Operations should define a 401 response
  given: $.paths[*][*].responses
  name: biogen-response-401-present
  severity: warn
- description: All schemas must have a title
  given: $.components.schemas[*]
  name: biogen-schema-title-present
  severity: warn
- description: All schemas must have a description
  given: $.components.schemas[*]
  name: biogen-schema-description-present
  severity: warn
- description: Schema properties must have descriptions
  given: $.components.schemas[*].properties[*]
  name: biogen-schema-properties-described
  severity: warn
- description: API must define at least one security scheme
  given: $.components
  name: biogen-security-scheme-present
  severity: error
- description: Biogen API uses X-API-Key header authentication
  given: $.components.securitySchemes[*]
  name: biogen-api-key-auth
  severity: warn
- description: Operations must declare security
  given: $.paths[*][get,post,put,patch,delete]
  name: biogen-operation-security-present
  severity: warn
- description: All tags used in operations must be defined at top level
  given: $.tags
  name: biogen-tags-defined
  severity: warn
- description: API must define servers
  given: $
  name: biogen-servers-present
  severity: error
- description: Server URL must use HTTPS
  given: $.servers[*].url
  name: biogen-server-https
  severity: error
- description: Responses with content should include examples
  given: $.paths[*][*].responses[*].content[*]
  name: biogen-operation-examples-present
  severity: warn
- description: Every operation must include x-microcks-operation extension
  given: $.paths[*][*]
  name: biogen-microcks-operation-present
  severity: warn
- description: All components should be referenced
  given: $.components.schemas
  name: biogen-unused-components
  severity: warn
- description: API info must include license
  given: $.info
  name: biogen-license-present
  severity: warn
- description: Path segments should be lowercase
  given: $.paths
  name: biogen-path-kebab-case
  severity: warn
rules_file: rules/biogen-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/biogen/refs/heads/main/rules/biogen-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 16
slug: biogen-spectral-rules
source_filename: biogen-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  biogen-info-title-prefix:\n    description: API title must start with \"Biogen\"\n    message: 'Info title must start with \"Biogen\": {{value}}'\n    severity: error\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Biogen\"\n\n  biogen-info-version-present:\n    description: API info must have a version field\n    message: Info object must include a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  biogen-info-contact-present:\n    description: API info must include contact details\n    message: Info object must include contact\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  biogen-operation-summary-prefix:\n    description: Operation summaries must start with \"Biogen\"\n    message: 'Operation summary must start with \"Biogen\": {{value}}'\n    severity: error\n    given: \"$.paths[*][*].summary\"\
  \n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Biogen\"\n\n  biogen-operation-id-camel-case:\n    description: Operation IDs must be camelCase\n    message: 'OperationId must be camelCase: {{value}}'\n    severity: warn\n    given: \"$.paths[*][*].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  biogen-operation-tags-present:\n    description: Every operation must have at least one tag\n    message: Operations must include tags\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n\n  biogen-operation-description-present:\n    description: Every operation must have a description\n    message: Operations must include description\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: description\n      function: truthy\n\n  biogen-response-success-present:\n    description: Every operation must define a success response\n\
  \    message: Operations must include a 200 or 201 response\n    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n\n  biogen-response-401-present:\n    description: Operations should define a 401 response\n    message: Operations should include 401 unauthorized response\n    severity: warn\n    given: \"$.paths[*][*].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: ['401']\n            - required: ['403']\n\n  biogen-schema-title-present:\n    description: All schemas must have a title\n    message: Schemas must include title\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: title\n      function: truthy\n\n  biogen-schema-description-present:\n    description:\
  \ All schemas must have a description\n    message: Schemas must include description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  biogen-schema-properties-described:\n    description: Schema properties must have descriptions\n    message: Schema properties must include description\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  biogen-security-scheme-present:\n    description: API must define at least one security scheme\n    message: Components must include securitySchemes\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  biogen-api-key-auth:\n    description: Biogen API uses X-API-Key header authentication\n    message: Security scheme should use X-API-Key header\n    severity: warn\n    given: \"$.components.securitySchemes[*]\"\n    then:\n  \
  \    function: truthy\n\n  biogen-operation-security-present:\n    description: Operations must declare security\n    message: Operations must include security definition\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: security\n      function: truthy\n\n  biogen-tags-defined:\n    description: All tags used in operations must be defined at top level\n    message: Tags must be defined in the global tags section\n    severity: warn\n    given: \"$.tags\"\n    then:\n      function: truthy\n\n  biogen-servers-present:\n    description: API must define servers\n    message: Servers array must be present and non-empty\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  biogen-server-https:\n    description: Server URL must use HTTPS\n    message: 'Server URL must use HTTPS: {{value}}'\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n\
  \        match: \"^https://\"\n\n  biogen-operation-examples-present:\n    description: Responses with content should include examples\n    message: Response content should include examples\n    severity: warn\n    given: \"$.paths[*][*].responses[*].content[*]\"\n    then:\n      field: examples\n      function: truthy\n\n  biogen-microcks-operation-present:\n    description: Every operation must include x-microcks-operation extension\n    message: Operations must include x-microcks-operation\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  biogen-unused-components:\n    description: All components should be referenced\n    message: Unused components should be removed\n    severity: warn\n    given: \"$.components.schemas\"\n    then:\n      function: truthy\n\n  biogen-license-present:\n    description: API info must include license\n    message: Info must include license\n    severity: warn\n    given: \"$.info\"\
  \n    then:\n      field: license\n      function: truthy\n\n  biogen-path-kebab-case:\n    description: Path segments should be lowercase\n    message: 'Path segments should use lowercase: {{value}}'\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9-/{}]*)+$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/biogen/refs/heads/main/rules/biogen-spectral-rules.yml
tags:
- Biotechnology
- Healthcare
- Life Sciences
- Pharmaceuticals
- Neurology
- Spectral
- Linting
- API Governance
---
