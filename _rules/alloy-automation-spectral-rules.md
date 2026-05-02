---
api_specs:
- filename: alloy-automation-embedded.yaml
  format: yaml
  label: Alloy Automation Embedded API
  slug: embedded-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alloy-automation/refs/heads/main/openapi/alloy-automation-embedded.yaml
- filename: alloy-automation-connectivity.yaml
  format: yaml
  label: Alloy Automation Connectivity API
  slug: connectivity-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alloy-automation/refs/heads/main/openapi/alloy-automation-connectivity.yaml
categories:
- alloy
description: Spectral linting rules defining API design standards and conventions for Alloy Automation.
layout: rules
name: Alloy Automation API Rules
provider_name: Alloy Automation
provider_slug: alloy-automation
rule_count: 16
rules:
- description: All operation summaries must start with "Alloy"
  given: $.paths[*][*].summary
  name: alloy-operation-summary-prefix
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][*]
  name: alloy-operation-tags
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][*]
  name: alloy-operation-id
  severity: error
- description: All operations must have a description
  given: $.paths[*][*]
  name: alloy-operation-description
  severity: warn
- description: All operations must document 401 Unauthorized response
  given: $.paths[*][*].responses
  name: alloy-error-response-401
  severity: error
- description: API must use bearer API key security
  given: $.components.securitySchemes
  name: alloy-api-key-security
  severity: error
- description: API version should be specified in server URL or via x-api-version header
  given: $.servers[0].url
  name: alloy-api-version-header
  severity: info
- description: All schemas must have a title
  given: $.components.schemas[*]
  name: alloy-schema-title
  severity: warn
- description: All schemas must have a description
  given: $.components.schemas[*]
  name: alloy-schema-description
  severity: warn
- description: All schema properties must have a description
  given: $.components.schemas[*].properties[*]
  name: alloy-property-description
  severity: warn
- description: Schema properties should have examples
  given: $.components.schemas[*].properties[*]
  name: alloy-property-example
  severity: info
- description: All operations should have x-microcks-operation extension
  given: $.paths[*][*]
  name: alloy-microcks-operation
  severity: info
- description: User ID fields should follow usr_ prefix pattern
  given: $.components.schemas[*].properties.userId.example
  name: alloy-user-id-pattern
  severity: info
- description: POST operations should return 201 (created) or 200
  given: $.paths[*].post.responses
  name: alloy-post-201-or-200
  severity: warn
- description: Error responses must reference ErrorResponse schema
  given: $.paths[*][*].responses[4XX,5XX].content.application/json.schema.$ref
  name: alloy-error-response-schema
  severity: warn
- description: Connector IDs should use kebab-case
  given: $.components.schemas[*].properties.connectorId.example
  name: alloy-connector-id-kebab-case
  severity: info
rules_file: rules/alloy-automation-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/alloy-automation/refs/heads/main/rules/alloy-automation-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 5
  warn: 7
slug: alloy-automation-spectral-rules
source_filename: alloy-automation-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  alloy-operation-summary-prefix:\n    description: All operation summaries must start with \"Alloy\"\n    severity: warn\n    given: \"$.paths[*][*].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Alloy\"\n\n  alloy-operation-tags:\n    description: All operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n\n  alloy-operation-id:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: operationId\n      function: truthy\n\n  alloy-operation-description:\n    description: All operations must have a description\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: description\n      function: truthy\n\n  alloy-error-response-401:\n    description: All operations must document 401 Unauthorized response\n    severity: error\n    given: \"$.paths[*][*].responses\"\
  \n    then:\n      field: \"401\"\n      function: truthy\n\n  alloy-api-key-security:\n    description: API must use bearer API key security\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      field: ApiKey\n      function: truthy\n\n  alloy-api-version-header:\n    description: API version should be specified in server URL or via x-api-version header\n    severity: info\n    given: \"$.servers[0].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"\\\\d{4}-\\\\d{2}\"\n\n  alloy-schema-title:\n    description: All schemas must have a title\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: title\n      function: truthy\n\n  alloy-schema-description:\n    description: All schemas must have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  alloy-property-description:\n    description: All schema properties\
  \ must have a description\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  alloy-property-example:\n    description: Schema properties should have examples\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: truthy\n\n  alloy-microcks-operation:\n    description: All operations should have x-microcks-operation extension\n    severity: info\n    given: \"$.paths[*][*]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  alloy-user-id-pattern:\n    description: User ID fields should follow usr_ prefix pattern\n    severity: info\n    given: \"$.components.schemas[*].properties.userId.example\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^usr_\"\n\n  alloy-post-201-or-200:\n    description: POST operations should return 201 (created) or 200\n    severity: warn\n    given:\
  \ \"$.paths[*].post.responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"201\"]\n            - required: [\"200\"]\n            - required: [\"202\"]\n\n  alloy-error-response-schema:\n    description: Error responses must reference ErrorResponse schema\n    severity: warn\n    given: \"$.paths[*][*].responses[4XX,5XX].content.application/json.schema.$ref\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"ErrorResponse\"\n\n  alloy-connector-id-kebab-case:\n    description: Connector IDs should use kebab-case\n    severity: info\n    given: \"$.components.schemas[*].properties.connectorId.example\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9-]*$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/alloy-automation/refs/heads/main/rules/alloy-automation-spectral-rules.yml
tags:
- Automation
- Embedded Integrations
- Integrations
- iPaaS
- Unified API
- Workflows
- Spectral
- Linting
- API Governance
---
