---
api_specs:
- filename: amqp-messaging.yml
  format: yaml
  label: AMQP Messaging API
  slug: ''
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/amqp/refs/heads/main/asyncapi/amqp-messaging.yml
categories:
- asyncapi
description: Spectral linting rules defining API design standards and conventions for AMQP.
layout: rules
name: AMQP API Rules
provider_name: AMQP
provider_slug: amqp
rule_count: 9
rules:
- description: AsyncAPI info must have a description
  given: $.info
  name: asyncapi-info-description
  severity: error
- description: AsyncAPI info must have a version
  given: $.info
  name: asyncapi-info-version
  severity: error
- description: At least one server must be defined
  given: $
  name: asyncapi-servers-defined
  severity: warn
- description: Every channel should have a description
  given: $.channels[*]
  name: asyncapi-channel-description
  severity: warn
- description: Every message should have a description
  given: $.components.messages[*]
  name: asyncapi-message-description
  severity: warn
- description: Schema properties should have explicit types
  given: $.components.schemas[*].properties[*]
  name: asyncapi-schema-type
  severity: info
- description: AMQP bindings should define exchange type
  given: $.channels[*].bindings.amqp.exchange
  name: asyncapi-amqp-exchange-type
  severity: info
- description: Operations should have an operationId
  given: $.channels[*].messages[*]
  name: asyncapi-operation-id
  severity: warn
- description: Descriptions must not be empty
  given: $..description
  name: asyncapi-no-empty-description
  severity: warn
rules_file: rules/amqp-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amqp/refs/heads/main/rules/amqp-spectral-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 2
  warn: 5
slug: amqp-spectral-rules
source_filename: amqp-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  asyncapi-info-description:\n    description: AsyncAPI info must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  asyncapi-info-version:\n    description: AsyncAPI info must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  asyncapi-servers-defined:\n    description: At least one server must be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  asyncapi-channel-description:\n    description: Every channel should have a description\n    severity: warn\n    given: \"$.channels[*]\"\n    then:\n      field: description\n      function: truthy\n\n  asyncapi-message-description:\n    description: Every message should have a description\n    severity: warn\n    given: \"$.components.messages[*]\"\n    then:\n      field: description\n      function:\
  \ truthy\n\n  asyncapi-schema-type:\n    description: Schema properties should have explicit types\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  asyncapi-amqp-exchange-type:\n    description: AMQP bindings should define exchange type\n    severity: info\n    given: \"$.channels[*].bindings.amqp.exchange\"\n    then:\n      field: type\n      function: truthy\n\n  asyncapi-operation-id:\n    description: Operations should have an operationId\n    severity: warn\n    given: \"$.channels[*].messages[*]\"\n    then:\n      field: name\n      function: truthy\n\n  asyncapi-no-empty-description:\n    description: Descriptions must not be empty\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amqp/refs/heads/main/rules/amqp-spectral-rules.yml
tags:
- AMQP
- Asynchronous
- Message Queue
- Messaging
- Middleware
- Open Standard
- Publish Subscribe
- Spectral
- Linting
- API Governance
---
