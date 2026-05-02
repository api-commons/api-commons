---
api_specs:
- filename: bindbee-api.yaml
  format: yaml
  label: Bindbee API
  slug: bindbee-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/openapi/bindbee-api.yaml
categories:
- bindbee
description: Spectral linting rules defining API design standards and conventions for Bindbee.
layout: rules
name: Bindbee API Rules
provider_name: Bindbee
provider_slug: bindbee
rule_count: 24
rules:
- description: API title must start with "Bindbee"
  given: $.info.title
  name: bindbee-info-title-prefix
  severity: error
- description: API info must have a version field
  given: $.info
  name: bindbee-info-version-present
  severity: error
- description: API info must include contact details
  given: $.info
  name: bindbee-info-contact-present
  severity: warn
- description: Operation summaries must start with "Bindbee"
  given: $.paths[*][*].summary
  name: bindbee-operation-summary-prefix
  severity: error
- description: Operation IDs must be camelCase
  given: $.paths[*][*].operationId
  name: bindbee-operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][*]
  name: bindbee-operation-tags-present
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][*]
  name: bindbee-operation-description-present
  severity: warn
- description: Path segments must use kebab-case
  given: $.paths
  name: bindbee-path-kebab-case
  severity: warn
- description: Operations must require x-connector-token header
  given: $.paths[*][*].parameters[?(@.name=='x-connector-token')]
  name: bindbee-connector-token-header
  severity: error
- description: Every operation must define a 200 response
  given: $.paths[*][*].responses
  name: bindbee-response-200-present
  severity: error
- description: Operations should define a 401 unauthorized response
  given: $.paths[*][*].responses
  name: bindbee-response-401-present
  severity: warn
- description: All schemas must have a title
  given: $.components.schemas[*]
  name: bindbee-schema-title-present
  severity: warn
- description: All schemas must have a description
  given: $.components.schemas[*]
  name: bindbee-schema-description-present
  severity: warn
- description: Schema properties must have descriptions
  given: $.components.schemas[*].properties[*]
  name: bindbee-schema-properties-described
  severity: warn
- description: API must define at least one security scheme
  given: $.components
  name: bindbee-security-scheme-present
  severity: error
- description: Operations must declare security
  given: $.paths[*][get,post,put,patch,delete]
  name: bindbee-operation-security-present
  severity: warn
- description: All tags must be defined at top level
  given: $.tags
  name: bindbee-tags-defined
  severity: warn
- description: API must define servers
  given: $
  name: bindbee-servers-present
  severity: error
- description: Server URL must use HTTPS
  given: $.servers[*].url
  name: bindbee-server-https
  severity: error
- description: List endpoints should support cursor-based pagination
  given: $.paths[?(@property.startsWith('/hris/') || @property.startsWith('/ats/'))][get].parameters[?(@.name=='cursor')]
  name: bindbee-pagination-cursor
  severity: warn
- description: List responses should return data in a data array
  given: $.components.schemas[?(@property.endsWith('Response'))].properties
  name: bindbee-response-data-array
  severity: warn
- description: Responses with content should include examples
  given: $.paths[*][*].responses[*].content[*]
  name: bindbee-operation-examples-present
  severity: warn
- description: Every operation must include x-microcks-operation extension
  given: $.paths[*][*]
  name: bindbee-microcks-operation-present
  severity: warn
- description: API info must include license
  given: $.info
  name: bindbee-license-present
  severity: warn
rules_file: rules/bindbee-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/rules/bindbee-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 0
  warn: 16
slug: bindbee-spectral-rules
source_filename: bindbee-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  bindbee-info-title-prefix:\n    description: API title must start with \"Bindbee\"\n    message: 'Info title must start with \"Bindbee\": {{value}}'\n    severity: error\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Bindbee\"\n\n  bindbee-info-version-present:\n    description: API info must have a version field\n    message: Info object must include a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  bindbee-info-contact-present:\n    description: API info must include contact details\n    message: Info object must include contact\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  bindbee-operation-summary-prefix:\n    description: Operation summaries must start with \"Bindbee\"\n    message: 'Operation summary must start with \"Bindbee\": {{value}}'\n    severity: error\n    given: \"$.paths[*][*].summary\"\
  \n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Bindbee\"\n\n  bindbee-operation-id-camel-case:\n    description: Operation IDs must be camelCase\n    message: 'OperationId must be camelCase: {{value}}'\n    severity: warn\n    given: \"$.paths[*][*].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  bindbee-operation-tags-present:\n    description: Every operation must have at least one tag\n    message: Operations must include tags\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n\n  bindbee-operation-description-present:\n    description: Every operation must have a description\n    message: Operations must include description\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: description\n      function: truthy\n\n  bindbee-path-kebab-case:\n    description: Path segments must use kebab-case\n    message:\
  \ 'Path segments must be kebab-case: {{value}}'\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9-{}]*)+$\"\n\n  bindbee-connector-token-header:\n    description: Operations must require x-connector-token header\n    message: Operations must include x-connector-token header parameter\n    severity: error\n    given: \"$.paths[*][*].parameters[?(@.name=='x-connector-token')]\"\n    then:\n      function: truthy\n\n  bindbee-response-200-present:\n    description: Every operation must define a 200 response\n    message: Operations must include a 200 response\n    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: ['200']\n\n  bindbee-response-401-present:\n    description: Operations should define a 401 unauthorized response\n    message: Operations should include 401 response\n   \
  \ severity: warn\n    given: \"$.paths[*][*].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: ['401']\n            - required: ['403']\n\n  bindbee-schema-title-present:\n    description: All schemas must have a title\n    message: Schemas must include title\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: title\n      function: truthy\n\n  bindbee-schema-description-present:\n    description: All schemas must have a description\n    message: Schemas must include description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  bindbee-schema-properties-described:\n    description: Schema properties must have descriptions\n    message: Schema properties must include description\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field:\
  \ description\n      function: truthy\n\n  bindbee-security-scheme-present:\n    description: API must define at least one security scheme\n    message: Components must include securitySchemes\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  bindbee-operation-security-present:\n    description: Operations must declare security\n    message: Operations must include security definition\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: security\n      function: truthy\n\n  bindbee-tags-defined:\n    description: All tags must be defined at top level\n    message: Tags must be defined in the global tags section\n    severity: warn\n    given: \"$.tags\"\n    then:\n      function: truthy\n\n  bindbee-servers-present:\n    description: API must define servers\n    message: Servers array must be present and non-empty\n    severity: error\n    given: \"$\"\n    then:\n     \
  \ field: servers\n      function: truthy\n\n  bindbee-server-https:\n    description: Server URL must use HTTPS\n    message: 'Server URL must use HTTPS: {{value}}'\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  bindbee-pagination-cursor:\n    description: List endpoints should support cursor-based pagination\n    message: List endpoints should include cursor parameter\n    severity: warn\n    given: \"$.paths[?(@property.startsWith('/hris/') || @property.startsWith('/ats/'))][get].parameters[?(@.name=='cursor')]\"\n    then:\n      function: truthy\n\n  bindbee-response-data-array:\n    description: List responses should return data in a data array\n    message: List response schemas should include a data array property\n    severity: warn\n    given: \"$.components.schemas[?(@property.endsWith('Response'))].properties\"\n    then:\n      field: data\n      function: truthy\n\n  bindbee-operation-examples-present:\n\
  \    description: Responses with content should include examples\n    message: Response content should include examples\n    severity: warn\n    given: \"$.paths[*][*].responses[*].content[*]\"\n    then:\n      field: examples\n      function: truthy\n\n  bindbee-microcks-operation-present:\n    description: Every operation must include x-microcks-operation extension\n    message: Operations must include x-microcks-operation\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  bindbee-license-present:\n    description: API info must include license\n    message: Info must include license\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/rules/bindbee-spectral-rules.yml
tags:
- ATS
- HR Integration
- HRIS
- Workforce
- Spectral
- Linting
- API Governance
---
