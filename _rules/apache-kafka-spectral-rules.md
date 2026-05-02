---
api_specs:
- filename: kafka-rest-proxy.yml
  format: yaml
  label: Kafka REST Proxy API
  slug: kafka-rest-proxy-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-kafka/refs/heads/main/openapi/kafka-rest-proxy.yml
- filename: kafka-connect.yml
  format: yaml
  label: Kafka Connect REST API
  slug: kafka-connect-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-kafka/refs/heads/main/openapi/kafka-connect.yml
- filename: kafka-messaging.yml
  format: yaml
  label: Apache Kafka Messaging API
  slug: kafka-messaging-api
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-kafka/refs/heads/main/asyncapi/kafka-messaging.yml
categories:
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Apache Kafka.
layout: rules
name: Apache Kafka API Rules
provider_name: Apache Kafka
provider_slug: apache-kafka
rule_count: 16
rules:
- description: Info title should start with Kafka or Apache Kafka
  given: $.info
  name: info-title-prefix
  severity: warn
- description: Info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Responses must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Every operation must have a 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-2xx-required
  severity: error
- description: GET operations must not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Path segments should use kebab-case or snake_case
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Parameters should have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: GET operations should document 404 responses
  given: $.paths[*].get.responses
  name: response-error-404
  severity: info
- description: POST operations should document 400 responses
  given: $.paths[*].post.responses
  name: response-error-400
  severity: info
rules_file: rules/apache-kafka-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-kafka/refs/heads/main/rules/apache-kafka-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 4
  warn: 3
slug: apache-kafka-spectral-rules
source_filename: apache-kafka-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-prefix:\n    description: Info title should start with Kafka or Apache Kafka\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^(Apache )?Kafka\"\n\n  info-version-required:\n    description: Info must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  servers-defined:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n\
  \      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  response-description-required:\n    description: Responses must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-2xx-required:\n    description: Every operation must have a 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n      \
  \      - required: [\"201\"]\n            - required: [\"204\"]\n\n  get-no-request-body:\n    description: GET operations must not have request bodies\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  paths-kebab-case:\n    description: Path segments should use kebab-case or snake_case\n    severity: info\n    given: \"$.paths\"\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(\\/([a-z0-9{}_-]+))*$\"\n\n  schema-description-required:\n    description: Component schemas should have descriptions\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  parameter-description-required:\n    description:\
  \ Parameters should have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-error-404:\n    description: GET operations should document 404 responses\n    severity: info\n    given: \"$.paths[*].get.responses\"\n    then:\n      field: \"404\"\n      function: truthy\n\n  response-error-400:\n    description: POST operations should document 400 responses\n    severity: info\n    given: \"$.paths[*].post.responses\"\n    then:\n      field: \"400\"\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-kafka/refs/heads/main/rules/apache-kafka-spectral-rules.yml
tags:
- Distributed Systems
- Event Streaming
- Messaging
- Open Source
- Pub-Sub
- Spectral
- Linting
- API Governance
---
