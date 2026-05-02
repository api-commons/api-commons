---
api_specs:
- filename: akka-management.json
  format: json
  label: Akka Management
  slug: akka-management
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/akka/refs/heads/main/openapi/akka-management.json
categories:
- get
- info
- openapi
- operation
- paths
- response
- servers
description: Spectral linting rules defining API design standards and conventions for Akka.
layout: rules
name: Akka API Rules
provider_name: Akka
provider_slug: akka
rule_count: 12
rules:
- description: ''
  given: $.info.title
  name: info-title-akka-prefix
  severity: warn
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
  name: openapi-version-3
  severity: error
- description: ''
  given: $
  name: servers-defined
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-akka-prefix
  severity: warn
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
rules_file: rules/akka-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/akka/refs/heads/main/rules/akka-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 1
  warn: 4
slug: akka-spectral-rules
source_filename: akka-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Akka Management API Spectral Ruleset\n\nrules:\n  info-title-akka-prefix:\n    message: \"API title should start with 'Akka'\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Akka\"\n\n  info-description-required:\n    message: \"API info must have a description\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    message: \"API info must have a version\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  openapi-version-3:\n    message: \"Must use OpenAPI 3.x\"\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  servers-defined:\n    message: \"Servers must be defined\"\n    severity: warn\n    given: \"$\"\n    then:\n      field: servers\n      function:\
  \ truthy\n\n  operation-summary-required:\n    message: \"Every operation must have a summary\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-akka-prefix:\n    message: \"Operation summaries should start with 'Akka'\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Akka\"\n\n  operation-id-required:\n    message: \"Every operation must have an operationId\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    message: \"Every operation must have at least one tag\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  response-description-required:\n    message: \"All responses\
  \ must have a description\"\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  get-no-request-body:\n    message: \"GET operations must not have a request body\"\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  paths-kebab-case:\n    message: \"Path segments should use kebab-case\"\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(\\\\/([a-z0-9][a-z0-9\\\\-]*|\\\\{[a-zA-Z][a-zA-Z0-9_]*\\\\}))*$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/akka/refs/heads/main/rules/akka-spectral-rules.yml
tags:
- Actor Model
- Distributed Systems
- Frameworks
- Java
- Microservices
- Reactive
- Scala
- Spectral
- Linting
- API Governance
---
