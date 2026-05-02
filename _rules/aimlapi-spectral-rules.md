---
api_specs:
- filename: aimlapi-openapi.yml
  format: yaml
  label: AIMLAPI
  slug: aimlapi
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aimlapi/refs/heads/main/openapi/aimlapi-openapi.yml
categories:
- info
- 'no'
- openai
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for AIMLAPI.
layout: rules
name: AIMLAPI API Rules
provider_name: AIMLAPI
provider_slug: aimlapi
rule_count: 15
rules:
- description: Title should start with AIMLAPI
  given: $.info.title
  name: info-title-aimlapi
  severity: warn
- description: Operation summaries must start with "AIMLAPI"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation should have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Operations must define at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Parameters should have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description
  severity: warn
- description: Schema properties should have types defined
  given: $.components.schemas[*].properties[*]
  name: schema-property-type
  severity: warn
- description: Bearer auth security scheme should be defined
  given: $.components.securitySchemes
  name: security-bearer-defined
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Chat completion operations should have a model parameter
  given: $.paths['/chat/completions'].post
  name: openai-compatible-model-param
  severity: info
rules_file: rules/aimlapi-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aimlapi/refs/heads/main/rules/aimlapi-spectral-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 1
  warn: 8
slug: aimlapi-spectral-rules
source_filename: aimlapi-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: \"spectral:oas\"\n\nrules:\n  info-title-aimlapi:\n    description: Title should start with AIMLAPI\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AIMLAPI\"\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"AIMLAPI\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AIMLAPI\"\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n\
  \    description: Every operation should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation should have tags\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  response-success-required:\n    description: Operations must define at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          oneOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n\
  \  parameter-description:\n    description: Parameters should have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-property-type:\n    description: Schema properties should have types defined\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  security-bearer-defined:\n    description: Bearer auth security scheme should be defined\n    severity: warn\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  no-empty-descriptions:\n\
  \    description: Descriptions must not be empty\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: truthy\n\n  openai-compatible-model-param:\n    description: Chat completion operations should have a model parameter\n    severity: info\n    given: \"$.paths['/chat/completions'].post\"\n    then:\n      field: requestBody\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/aimlapi/refs/heads/main/rules/aimlapi-spectral-rules.yml
tags:
- Artificial Intelligence
- Machine Learning
- AI Models
- LLM
- Image Generation
- Video Generation
- Speech
- Embeddings
- API Gateway
- Developer Tools
- Spectral
- Linting
- API Governance
---
