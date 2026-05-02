---
api_specs:
- filename: apache-activemq-rest-openapi.yaml
  format: yaml
  label: Apache ActiveMQ REST API
  slug: apache-activemq-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-activemq/refs/heads/main/openapi/apache-activemq-rest-openapi.yaml
categories:
- delete
- get
- info
- operation
- parameter
- response
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Apache ActiveMQ.
layout: rules
name: Apache ActiveMQ API Rules
provider_name: Apache ActiveMQ
provider_slug: apache-activemq
rule_count: 19
rules:
- description: API title must start with "Apache ActiveMQ"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API must have a description of at least 50 characters.
  given: $.info
  name: info-description-required
  severity: error
- description: API info must include a version.
  given: $.info
  name: info-version-required
  severity: error
- description: API must declare an Apache 2.0 license.
  given: $.info
  name: info-license-required
  severity: warn
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS in production.
  given: $.servers[*].url
  name: servers-https-only
  severity: info
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Apache ActiveMQ".
  given: $.paths[*][get,post,put,patch,delete,options,head].summary
  name: operation-summary-title-case
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-operationId-required
  severity: error
- description: operationId must be camelCase.
  given: $.paths[*][get,post,put,patch,delete,options,head].operationId
  name: operation-operationId-camelCase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete,options,head].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head].responses[*]
  name: response-description-required
  severity: error
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Operations should include x-microcks-operation extension for mock server compatibility.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
rules_file: rules/apache-activemq-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-activemq/refs/heads/main/rules/apache-activemq-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 2
  warn: 9
slug: apache-activemq-spectral-rules
source_filename: apache-activemq-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"Apache ActiveMQ\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache ActiveMQ\"\n  info-description-required:\n    description: API must have a description of at least 50 characters.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API info must include a version.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n  info-license-required:\n    description: API must declare an Apache 2.0 license.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: \"$\"\n    then:\n\
  \      field: servers\n      function: truthy\n  servers-https-only:\n    description: Server URLs should use HTTPS in production.\n    severity: info\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"^http://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: summary\n      function: truthy\n  operation-summary-title-case:\n    description: Operation summaries must start with \"Apache ActiveMQ\".\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache ActiveMQ\"\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\
  \n    then:\n      field: description\n      function: truthy\n  operation-operationId-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-operationId-camelCase:\n    description: operationId must be camelCase.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head].parameters[*]\"\
  \n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one 2xx response.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHODS\n  get-no-request-body:\n  \
  \  description: GET operations must not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # MICROCKS\n  operation-microcks-extension:\n    description: Operations should include x-microcks-operation extension for mock server compatibility.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-activemq/refs/heads/main/rules/apache-activemq-spectral-rules.yml
tags:
- AMQP
- Apache
- Java
- JMS
- Message Broker
- Messaging
- MQTT
- Open Source
- STOMP
- Spectral
- Linting
- API Governance
---
