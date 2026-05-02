---
api_specs:
- filename: asyncapi.yaml
  format: yaml
  label: Zilla Gateway
  slug: zilla-gateway
  spec_type: AsyncAPI
  url: https://docs.aklivity.io/zilla/latest/concepts/config/
categories:
- get
- info
- operation
- paths
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Aklivity.
layout: rules
name: Aklivity API Rules
provider_name: Aklivity
provider_slug: aklivity
rule_count: 11
rules:
- description: ''
  given: $.info
  name: info-title-required
  severity: error
- description: ''
  given: $.info
  name: info-description-required
  severity: error
- description: ''
  given: $.info
  name: info-version-required
  severity: error
- description: ''
  given: $
  name: servers-defined
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: ''
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: ''
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: ''
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
- description: ''
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
rules_file: rules/aklivity-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aklivity/refs/heads/main/rules/aklivity-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 1
  warn: 2
slug: aklivity-spectral-rules
source_filename: aklivity-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Aklivity / Zilla AsyncAPI and OpenAPI Spectral Ruleset\n\nrules:\n  info-title-required:\n    message: \"API info must have a title\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    message: \"API info must have a description\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    message: \"API info must have a version\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  servers-defined:\n    message: \"Servers must be defined\"\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  operation-summary-required:\n    message: \"Every operation must have a summary\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-id-required:\n\
  \    message: \"Every operation must have an operationId\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    message: \"Every operation must have at least one tag\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  response-description-required:\n    message: \"All responses must have a description\"\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  get-no-request-body:\n    message: \"GET operations must not have a request body\"\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  paths-kebab-case:\n    message: \"Path segments should use kebab-case\"\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n\
  \        match: \"^(\\\\/([a-z0-9][a-z0-9\\\\-]*|\\\\{[a-zA-Z][a-zA-Z0-9_]*\\\\}))*$\"\n\n  schema-type-defined:\n    message: \"Schema properties should have a type\"\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/aklivity/refs/heads/main/rules/aklivity-spectral-rules.yml
tags:
- API Gateway
- Apache Kafka
- Event-Driven
- IoT
- Kafka Proxy
- Multi-Protocol
- Real-Time
- Spectral
- Linting
- API Governance
---
