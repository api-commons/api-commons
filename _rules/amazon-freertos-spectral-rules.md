---
api_specs:
- filename: amazon-freertos-openapi.yml
  format: yaml
  label: Amazon FreeRTOS API
  slug: amazon-freertos-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-freertos/refs/heads/main/openapi/amazon-freertos-openapi.yml
categories:
- freertos
description: Spectral linting rules defining API design standards and conventions for Amazon FreeRTOS.
layout: rules
name: Amazon FreeRTOS API Rules
provider_name: Amazon FreeRTOS
provider_slug: amazon-freertos
rule_count: 25
rules:
- description: API must include contact information
  given: $.info
  name: freertos-info-contact
  severity: warn
- description: API must have a description
  given: $.info
  name: freertos-info-description
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: freertos-server-https
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: freertos-operation-summary
  severity: error
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: freertos-operation-description
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: freertos-operation-tags
  severity: error
- description: Operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: freertos-operation-id
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: freertos-operation-id-camel-case
  severity: warn
- description: POST operations should define 200 response
  given: $.paths[*][post]
  name: freertos-response-200
  severity: warn
- description: Operations should define 400 response
  given: $.paths[*][get,post,put,patch,delete]
  name: freertos-response-400
  severity: warn
- description: Operations should define 500 response
  given: $.paths[*][get,post,put,patch,delete]
  name: freertos-response-500
  severity: warn
- description: Resource-by-ID operations should define 404
  given: $.paths[*~'\{[^}]+\}'][get,put,patch,delete].responses
  name: freertos-response-404
  severity: warn
- description: DELETE operations should return 204
  given: $.paths[*].delete
  name: freertos-delete-204
  severity: info
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: freertos-parameter-description
  severity: error
- description: Path parameters must be required
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]
  name: freertos-path-param-required
  severity: error
- description: Schema components should have descriptions
  given: $.components.schemas[*]
  name: freertos-schema-description
  severity: warn
- description: Operation tags should use Title Case
  given: $.paths[*][*].tags[*]
  name: freertos-tags-title-case
  severity: warn
- description: OTA update schema must require targets
  given: $.components.schemas.OtaUpdate.required
  name: freertos-ota-targets-required
  severity: warn
- description: OTA update status should define enum values
  given: $.components.schemas.OtaUpdate.properties.otaUpdateStatus
  name: freertos-ota-status-enum
  severity: warn
- description: Software configuration must document hardware platform
  given: $.components.schemas.SoftwareConfiguration.required
  name: freertos-sw-config-hardware-platform
  severity: warn
- description: POST creation operationIds should start with 'create'
  given: $.paths[*].post.operationId
  name: freertos-create-prefix
  severity: warn
- description: Collection GET operationIds should start with 'list'
  given: $.paths[*~'[^}]$'].get.operationId
  name: freertos-list-prefix
  severity: warn
- description: Object schemas should define properties
  given: $.components.schemas[?(@.type=='object')]
  name: freertos-schema-properties
  severity: warn
- description: POST/PUT request bodies should define application/json
  given: $.paths[*][post,put].requestBody.content
  name: freertos-request-body-json
  severity: warn
- description: OTA update create request should document protocols
  given: $.components.schemas.CreateOtaUpdateRequest.properties
  name: freertos-ota-protocols-documented
  severity: info
rules_file: rules/amazon-freertos-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-freertos/refs/heads/main/rules/amazon-freertos-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 2
  warn: 16
slug: amazon-freertos-spectral-rules
source_filename: amazon-freertos-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Amazon FreeRTOS Spectral Rules\nextends: spectral:oas\nrules:\n  freertos-info-contact:\n    description: API must include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n  freertos-info-description:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  freertos-server-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  freertos-operation-summary:\n    description: Operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n  freertos-operation-description:\n    description: Operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\
  \n    then:\n      field: description\n      function: truthy\n  freertos-operation-tags:\n    description: Operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n  freertos-operation-id:\n    description: Operations must have operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  freertos-operation-id-camel-case:\n    description: operationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n  freertos-response-200:\n    description: POST operations should define 200 response\n    severity: warn\n    given: \"$.paths[*][post]\"\n    then:\n      field: responses.200\n      function: truthy\n  freertos-response-400:\n    description:\
  \ Operations should define 400 response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses.400\n      function: truthy\n  freertos-response-500:\n    description: Operations should define 500 response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses.500\n      function: truthy\n  freertos-response-404:\n    description: Resource-by-ID operations should define 404\n    severity: warn\n    given: \"$.paths[*~'\\\\{[^}]+\\\\}'][get,put,patch,delete].responses\"\n    then:\n      field: \"404\"\n      function: truthy\n  freertos-delete-204:\n    description: DELETE operations should return 204\n    severity: info\n    given: \"$.paths[*].delete\"\n    then:\n      field: responses.204\n      function: truthy\n  freertos-parameter-description:\n    description: Parameters must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\
  \n    then:\n      field: description\n      function: truthy\n  freertos-path-param-required:\n    description: Path parameters must be required\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]\"\n    then:\n      field: required\n      function: truthy\n  freertos-schema-description:\n    description: Schema components should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n  freertos-tags-title-case:\n    description: Operation tags should use Title Case\n    severity: warn\n    given: \"$.paths[*][*].tags[*]\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9 ]*$\"\n  freertos-ota-targets-required:\n    description: OTA update schema must require targets\n    severity: warn\n    given: \"$.components.schemas.OtaUpdate.required\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n\
  \          type: array\n          contains:\n            const: targets\n  freertos-ota-status-enum:\n    description: OTA update status should define enum values\n    severity: warn\n    given: \"$.components.schemas.OtaUpdate.properties.otaUpdateStatus\"\n    then:\n      field: enum\n      function: truthy\n  freertos-sw-config-hardware-platform:\n    description: Software configuration must document hardware platform\n    severity: warn\n    given: \"$.components.schemas.SoftwareConfiguration.required\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            const: hardwarePlatform\n  freertos-create-prefix:\n    description: POST creation operationIds should start with 'create'\n    severity: warn\n    given: \"$.paths[*].post.operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(create|list|tag|get|describe)\"\n  freertos-list-prefix:\n    description: Collection GET\
  \ operationIds should start with 'list'\n    severity: warn\n    given: \"$.paths[*~'[^}]$'].get.operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^list\"\n  freertos-schema-properties:\n    description: Object schemas should define properties\n    severity: warn\n    given: \"$.components.schemas[?(@.type=='object')]\"\n    then:\n      field: properties\n      function: truthy\n  freertos-request-body-json:\n    description: POST/PUT request bodies should define application/json\n    severity: warn\n    given: \"$.paths[*][post,put].requestBody.content\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"application/json\"]\n  freertos-ota-protocols-documented:\n    description: OTA update create request should document protocols\n    severity: info\n    given: \"$.components.schemas.CreateOtaUpdateRequest.properties\"\n    then:\n      field: protocols\n      function:\
  \ truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-freertos/refs/heads/main/rules/amazon-freertos-spectral-rules.yml
tags:
- Embedded Systems
- IoT
- Microcontrollers
- RTOS
- Spectral
- Linting
- API Governance
---
