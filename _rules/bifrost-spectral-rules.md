---
api_specs:
- filename: bifrost-http-gateway-api.yaml
  format: yaml
  label: Bifrost HTTP Gateway API
  slug: bifrost-http-gateway-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/bifrost/refs/heads/main/openapi/bifrost-http-gateway-api.yaml
categories:
- bifrost
description: Spectral linting rules defining API design standards and conventions for Bifrost.
layout: rules
name: Bifrost API Rules
provider_name: Bifrost
provider_slug: bifrost
rule_count: 24
rules:
- description: API title must start with "Bifrost"
  given: $.info.title
  name: bifrost-info-title-prefix
  severity: error
- description: API info must have a version field
  given: $.info
  name: bifrost-info-version-present
  severity: error
- description: API info must include contact details
  given: $.info
  name: bifrost-info-contact-present
  severity: warn
- description: Operation summaries must start with "Bifrost"
  given: $.paths[*][*].summary
  name: bifrost-operation-summary-prefix
  severity: error
- description: Operation IDs must be camelCase
  given: $.paths[*][*].operationId
  name: bifrost-operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][*]
  name: bifrost-operation-tags-present
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][*]
  name: bifrost-operation-description-present
  severity: warn
- description: Paths must use kebab-case segments
  given: $.paths
  name: bifrost-path-kebab-case
  severity: warn
- description: POST operations must have a request body
  given: $.paths[*].post
  name: bifrost-request-body-required
  severity: error
- description: Every operation must define a 200 or 201 response
  given: $.paths[*][*].responses
  name: bifrost-response-200-present
  severity: error
- description: Error responses must reference ErrorResponse schema
  given: $.paths[*][*].responses[?(@property >= '400')].content.application/json.schema
  name: bifrost-response-error-schema
  severity: warn
- description: All schemas must have a title
  given: $.components.schemas[*]
  name: bifrost-schema-title-present
  severity: warn
- description: All schemas must have a description
  given: $.components.schemas[*]
  name: bifrost-schema-description-present
  severity: warn
- description: Schema properties must have descriptions
  given: $.components.schemas[*].properties[*]
  name: bifrost-schema-properties-described
  severity: warn
- description: API must define at least one security scheme
  given: $.components
  name: bifrost-security-scheme-present
  severity: error
- description: Operations should reference a security scheme
  given: $.paths[*][post,put,patch,delete]
  name: bifrost-operation-security-present
  severity: warn
- description: All tags used in operations must be defined at top level
  given: $.tags
  name: bifrost-tags-defined
  severity: warn
- description: Top-level tags must have a description
  given: $.tags[*]
  name: bifrost-tag-description-present
  severity: warn
- description: API must define servers
  given: $
  name: bifrost-servers-present
  severity: error
- description: Chat completion model must use provider/model format
  given: $.components.schemas.ChatCompletionRequest.properties.model
  name: bifrost-chat-model-format
  severity: warn
- description: Responses with content should include examples
  given: $.paths[*][*].responses[*].content[*]
  name: bifrost-operation-examples-present
  severity: warn
- description: Every operation must include x-microcks-operation extension
  given: $.paths[*][*]
  name: bifrost-microcks-operation-present
  severity: warn
- description: API info must include license
  given: $.info
  name: bifrost-license-present
  severity: warn
- description: License must be Apache 2.0
  given: $.info.license.name
  name: bifrost-license-apache
  severity: warn
rules_file: rules/bifrost-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/bifrost/refs/heads/main/rules/bifrost-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 17
slug: bifrost-spectral-rules
source_filename: bifrost-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # Info rules\n  bifrost-info-title-prefix:\n    description: API title must start with \"Bifrost\"\n    message: 'Info title must start with \"Bifrost\": {{value}}'\n    severity: error\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Bifrost\"\n\n  bifrost-info-version-present:\n    description: API info must have a version field\n    message: Info object must include a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  bifrost-info-contact-present:\n    description: API info must include contact details\n    message: Info object must include contact\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  # Operation rules\n  bifrost-operation-summary-prefix:\n    description: Operation summaries must start with \"Bifrost\"\n    message: 'Operation summary must start with \"Bifrost\": {{value}}'\n    severity:\
  \ error\n    given: \"$.paths[*][*].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Bifrost\"\n\n  bifrost-operation-id-camel-case:\n    description: Operation IDs must be camelCase\n    message: 'OperationId must be camelCase: {{value}}'\n    severity: warn\n    given: \"$.paths[*][*].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  bifrost-operation-tags-present:\n    description: Every operation must have at least one tag\n    message: Operations must include tags\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n\n  bifrost-operation-description-present:\n    description: Every operation must have a description\n    message: Operations must include description\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: description\n      function: truthy\n\n  # Path rules\n  bifrost-path-kebab-case:\n  \
  \  description: Paths must use kebab-case segments\n    message: 'Path segments must be kebab-case: {{value}}'\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9-{}]*)+$\"\n\n  # Request body rules\n  bifrost-request-body-required:\n    description: POST operations must have a request body\n    message: POST operations must include requestBody\n    severity: error\n    given: \"$.paths[*].post\"\n    then:\n      field: requestBody\n      function: truthy\n\n  # Response rules\n  bifrost-response-200-present:\n    description: Every operation must define a 200 or 201 response\n    message: Operations must include a 200 response\n    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n\n  bifrost-response-error-schema:\n\
  \    description: Error responses must reference ErrorResponse schema\n    message: Error responses should reference the ErrorResponse schema\n    severity: warn\n    given: \"$.paths[*][*].responses[?(@property >= '400')].content.application/json.schema\"\n    then:\n      function: truthy\n\n  # Schema rules\n  bifrost-schema-title-present:\n    description: All schemas must have a title\n    message: Schemas must include title\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: title\n      function: truthy\n\n  bifrost-schema-description-present:\n    description: All schemas must have a description\n    message: Schemas must include description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  bifrost-schema-properties-described:\n    description: Schema properties must have descriptions\n    message: Schema properties must include description\n    severity: warn\n    given:\
  \ \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # Security rules\n  bifrost-security-scheme-present:\n    description: API must define at least one security scheme\n    message: Components must include securitySchemes\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  bifrost-operation-security-present:\n    description: Operations should reference a security scheme\n    message: Operations should include security definition\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete]\"\n    then:\n      field: security\n      function: truthy\n\n  # Tag rules\n  bifrost-tags-defined:\n    description: All tags used in operations must be defined at top level\n    message: Tags must be defined in the global tags section\n    severity: warn\n    given: \"$.tags\"\n    then:\n      function: truthy\n\n  bifrost-tag-description-present:\n    description:\
  \ Top-level tags must have a description\n    message: Tags must include a description\n    severity: warn\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # Server rules\n  bifrost-servers-present:\n    description: API must define servers\n    message: Servers array must be present and non-empty\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  # Model field rules\n  bifrost-chat-model-format:\n    description: Chat completion model must use provider/model format\n    message: Chat model field should use provider/model-name format\n    severity: warn\n    given: \"$.components.schemas.ChatCompletionRequest.properties.model\"\n    then:\n      field: description\n      function: truthy\n\n  # Examples rules\n  bifrost-operation-examples-present:\n    description: Responses with content should include examples\n    message: Response content should include examples\n    severity: warn\n    given:\
  \ \"$.paths[*][*].responses[*].content[*]\"\n    then:\n      field: examples\n      function: truthy\n\n  bifrost-microcks-operation-present:\n    description: Every operation must include x-microcks-operation extension\n    message: Operations must include x-microcks-operation\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  # License rules\n  bifrost-license-present:\n    description: API info must include license\n    message: Info must include license\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  bifrost-license-apache:\n    description: License must be Apache 2.0\n    message: 'License must be Apache 2.0: {{value}}'\n    severity: warn\n    given: \"$.info.license.name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"Apache\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/bifrost/refs/heads/main/rules/bifrost-spectral-rules.yml
tags:
- AI Gateway
- LLM
- Load Balancing
- Open Source
- OpenAI Compatible
- MCP
- Spectral
- Linting
- API Governance
---
