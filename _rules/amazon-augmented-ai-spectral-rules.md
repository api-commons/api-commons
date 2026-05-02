---
api_specs:
- filename: amazon-augmented-ai-openapi.yml
  format: yaml
  label: Amazon Augmented AI API
  slug: amazon-augmented-ai-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/openapi/amazon-augmented-ai-openapi.yml
categories:
- a2i
description: Spectral linting rules defining API design standards and conventions for Amazon Augmented AI.
layout: rules
name: Amazon Augmented AI API Rules
provider_name: Amazon Augmented AI
provider_slug: amazon-augmented-ai
rule_count: 11
rules:
- description: All operationIds must be camelCase
  given: $.paths[*][*].operationId
  name: a2i-operation-id-camel-case
  severity: warn
- description: All operation summaries must start with Amazon Augmented AI
  given: $.paths[*][*].summary
  name: a2i-summary-prefix
  severity: warn
- description: All operations must have tags
  given: $.paths[*][*]
  name: a2i-has-tags
  severity: warn
- description: All operations must have a 200 response
  given: $.paths[*][*].responses
  name: a2i-response-200
  severity: error
- description: StartHumanLoopRequest must require HumanLoopName
  given: $.components.schemas.StartHumanLoopRequest
  name: a2i-human-loop-name-required
  severity: error
- description: HumanLoopStatus must use valid enum values
  given: $.components.schemas.HumanLoopSummary.properties.HumanLoopStatus
  name: a2i-human-loop-status-enum
  severity: error
- description: API must use sigv4 security scheme
  given: $.security[*]
  name: a2i-security-sigv4
  severity: error
- description: Server URL must be fixed without variables
  given: $.servers[*]
  name: a2i-server-url-fixed
  severity: warn
- description: All examples must have x-microcks-default set to true
  given: $.paths[*][*].responses[*].content[*].examples.default
  name: a2i-example-microcks-default
  severity: warn
- description: StartHumanLoopRequest must require HumanLoopInput
  given: $.components.schemas.StartHumanLoopRequest.required
  name: a2i-human-loop-input-required
  severity: error
- description: StartHumanLoopRequest must require FlowDefinitionArn
  given: $.components.schemas.StartHumanLoopRequest.properties.FlowDefinitionArn
  name: a2i-flow-definition-arn-required
  severity: error
rules_file: rules/amazon-augmented-ai-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/rules/amazon-augmented-ai-spectral-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 0
  warn: 5
slug: amazon-augmented-ai-spectral-rules
source_filename: amazon-augmented-ai-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  a2i-operation-id-camel-case:\n    description: All operationIds must be camelCase\n    message: \"{{property}} must be camelCase\"\n    severity: warn\n    given: \"$.paths[*][*].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  a2i-summary-prefix:\n    description: All operation summaries must start with Amazon Augmented AI\n    message: Summary must start with Amazon Augmented AI\n    severity: warn\n    given: \"$.paths[*][*].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Augmented AI\"\n\n  a2i-has-tags:\n    description: All operations must have tags\n    message: Operation must have at least one tag\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n\n  a2i-response-200:\n    description: All operations must have a 200 response\n    message: Operation must define a 200 response\n    severity:\
  \ error\n    given: \"$.paths[*][*].responses\"\n    then:\n      field: \"200\"\n      function: truthy\n\n  a2i-human-loop-name-required:\n    description: StartHumanLoopRequest must require HumanLoopName\n    message: StartHumanLoopRequest must have HumanLoopName as required\n    severity: error\n    given: \"$.components.schemas.StartHumanLoopRequest\"\n    then:\n      field: required\n      function: truthy\n\n  a2i-human-loop-status-enum:\n    description: HumanLoopStatus must use valid enum values\n    message: HumanLoopStatus must be InProgress, Failed, Completed, Stopped, or Stopping\n    severity: error\n    given: \"$.components.schemas.HumanLoopSummary.properties.HumanLoopStatus\"\n    then:\n      field: enum\n      function: truthy\n\n  a2i-security-sigv4:\n    description: API must use sigv4 security scheme\n    message: Security must include sigv4\n    severity: error\n    given: \"$.security[*]\"\n    then:\n      field: sigv4\n      function: defined\n\n  a2i-server-url-fixed:\n\
  \    description: Server URL must be fixed without variables\n    message: Server URL must not use variables\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: variables\n      function: falsy\n\n  a2i-example-microcks-default:\n    description: All examples must have x-microcks-default set to true\n    message: Example must have x-microcks-default true\n    severity: warn\n    given: \"$.paths[*][*].responses[*].content[*].examples.default\"\n    then:\n      field: x-microcks-default\n      function: truthy\n\n  a2i-human-loop-input-required:\n    description: StartHumanLoopRequest must require HumanLoopInput\n    message: StartHumanLoopRequest must have HumanLoopInput as required\n    severity: error\n    given: \"$.components.schemas.StartHumanLoopRequest.required\"\n    then:\n      function: truthy\n\n  a2i-flow-definition-arn-required:\n    description: StartHumanLoopRequest must require FlowDefinitionArn\n    message: StartHumanLoopRequest must have FlowDefinitionArn\
  \ as required\n    severity: error\n    given: \"$.components.schemas.StartHumanLoopRequest.properties.FlowDefinitionArn\"\n    then:\n      field: type\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/rules/amazon-augmented-ai-spectral-rules.yml
tags:
- Amazon Augmented AI
- Human In The Loop
- Machine Learning
- AI Review
- Spectral
- Linting
- API Governance
---
