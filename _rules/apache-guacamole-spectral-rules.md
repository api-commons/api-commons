---
api_specs:
- filename: apache-guacamole-rest-openapi.yml
  format: yaml
  label: Apache Guacamole REST API
  slug: apache-guacamole-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-guacamole/refs/heads/main/openapi/apache-guacamole-rest-openapi.yml
categories:
- info
- operation
- parameter
- response
- schema
- security
description: Spectral linting rules defining API design standards and conventions for Apache Guacamole.
layout: rules
name: Apache Guacamole API Rules
provider_name: Apache Guacamole
provider_slug: apache-guacamole
rule_count: 10
rules:
- description: Info title must be defined
  given: $.info
  name: info-title-required
  severity: error
- description: API version must be specified
  given: $.info
  name: info-version-required
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with Apache Guacamole
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-apache-guacamole-prefix
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationId-required
  severity: error
- description: Operations should have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: All session operations require Guacamole-Token header
  given: $.paths./api/session[*][get,post,put,delete].parameters[?(@.name=='Guacamole-Token')]
  name: security-token-required
  severity: warn
- description: All responses must have descriptions
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
rules_file: rules/apache-guacamole-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-guacamole/refs/heads/main/rules/apache-guacamole-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 5
slug: apache-guacamole-spectral-rules
source_filename: apache-guacamole-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Apache Guacamole REST API Spectral Ruleset\nrules:\n  info-title-required:\n    description: Info title must be defined\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-version-required:\n    description: API version must be specified\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: summary\n      function: truthy\n  operation-summary-apache-guacamole-prefix:\n    description: Operation summaries should start with Apache Guacamole\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache Guacamole\"\n  operation-operationId-required:\n    description: All operations must have an operationId\n\
  \    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n    description: Operations should have tags\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: tags\n      function: truthy\n  security-token-required:\n    description: All session operations require Guacamole-Token header\n    severity: warn\n    given: \"$.paths./api/session[*][get,post,put,delete].parameters[?(@.name=='Guacamole-Token')]\"\n    then:\n      field: required\n      function: truthy\n  response-description-required:\n    description: All responses must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].responses[*]\n    then:\n      field: description\n      function: truthy\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].parameters[*]\n\
  \    then:\n      field: description\n      function: truthy\n  schema-description-recommended:\n    description: Schemas should have descriptions\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-guacamole/refs/heads/main/rules/apache-guacamole-spectral-rules.yml
tags:
- Apache
- Open Source
- RDP
- Remote Access
- Remote Desktop
- SSH
- VNC
- Web Gateway
- Spectral
- Linting
- API Governance
---
