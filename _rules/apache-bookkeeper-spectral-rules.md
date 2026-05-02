---
api_specs:
- filename: apache-bookkeeper-admin-openapi.yaml
  format: yaml
  label: Apache BookKeeper Admin API
  slug: apache-bookkeeper-admin-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-bookkeeper/refs/heads/main/openapi/apache-bookkeeper-admin-openapi.yaml
categories:
- bookkeeper
description: Spectral linting rules defining API design standards and conventions for Apache BookKeeper.
layout: rules
name: Apache BookKeeper API Rules
provider_name: Apache BookKeeper
provider_slug: apache-bookkeeper
rule_count: 12
rules:
- description: API info must have a title
  given: $.info
  name: bookkeeper-admin-info-title
  severity: error
- description: API info must have a description
  given: $.info
  name: bookkeeper-admin-info-description
  severity: warn
- description: API info must have a version
  given: $.info
  name: bookkeeper-admin-info-version
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,put,post,delete,patch]
  name: bookkeeper-admin-operation-id
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,put,post,delete,patch]
  name: bookkeeper-admin-operation-summary
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,put,post,delete,patch]
  name: bookkeeper-admin-operation-tags
  severity: warn
- description: GET and PUT operations should have a 200 response
  given: $.paths[*][get,put]
  name: bookkeeper-admin-response-200
  severity: warn
- description: All component schemas must have a title
  given: $.components.schemas[*]
  name: bookkeeper-admin-schema-title
  severity: warn
- description: All component schemas must have a description
  given: $.components.schemas[*]
  name: bookkeeper-admin-schema-description
  severity: warn
- description: Operation summaries should start with Apache BookKeeper
  given: $.paths[*][get,put,post,delete,patch].summary
  name: bookkeeper-admin-summary-prefix
  severity: warn
- description: API paths should use lowercase letters
  given: $.paths
  name: bookkeeper-admin-path-lowercase
  severity: warn
- description: All operations should have x-microcks-operation extension
  given: $.paths[*][get,put,post,delete,patch]
  name: bookkeeper-admin-microcks-operation
  severity: info
rules_file: rules/apache-bookkeeper-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-bookkeeper/refs/heads/main/rules/apache-bookkeeper-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 1
  warn: 8
slug: apache-bookkeeper-spectral-rules
source_filename: apache-bookkeeper-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  bookkeeper-admin-info-title:\n    description: API info must have a title\n    message: API info.title is required\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  bookkeeper-admin-info-description:\n    description: API info must have a description\n    message: API info.description is required\n    severity: warn\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  bookkeeper-admin-info-version:\n    description: API info must have a version\n    message: API info.version is required\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  bookkeeper-admin-operation-id:\n    description: All operations must have an operationId\n    message: Operation must have an operationId\n    severity: error\n    given: $.paths[*][get,put,post,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n\n  bookkeeper-admin-operation-summary:\n\
  \    description: All operations must have a summary\n    message: Operation must have a summary\n    severity: warn\n    given: $.paths[*][get,put,post,delete,patch]\n    then:\n      field: summary\n      function: truthy\n\n  bookkeeper-admin-operation-tags:\n    description: All operations must have at least one tag\n    message: Operation must have at least one tag\n    severity: warn\n    given: $.paths[*][get,put,post,delete,patch]\n    then:\n      field: tags\n      function: truthy\n\n  bookkeeper-admin-response-200:\n    description: GET and PUT operations should have a 200 response\n    message: GET/PUT operations should define a 200 response\n    severity: warn\n    given: $.paths[*][get,put]\n    then:\n      field: responses.200\n      function: truthy\n\n  bookkeeper-admin-schema-title:\n    description: All component schemas must have a title\n    message: Schema must have a title\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: title\n\
  \      function: truthy\n\n  bookkeeper-admin-schema-description:\n    description: All component schemas must have a description\n    message: Schema must have a description\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  bookkeeper-admin-summary-prefix:\n    description: Operation summaries should start with Apache BookKeeper\n    message: Operation summary should begin with \"Apache BookKeeper\"\n    severity: warn\n    given: $.paths[*][get,put,post,delete,patch].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Apache BookKeeper\n\n  bookkeeper-admin-path-lowercase:\n    description: API paths should use lowercase letters\n    message: API path should be lowercase\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        match: ^[a-z0-9/_{}.-]+$\n\n  bookkeeper-admin-microcks-operation:\n    description: All operations should\
  \ have x-microcks-operation extension\n    message: Operation should include x-microcks-operation for mock support\n    severity: info\n    given: $.paths[*][get,put,post,delete,patch]\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-bookkeeper/refs/heads/main/rules/apache-bookkeeper-spectral-rules.yml
tags:
- Apache
- Distributed Systems
- Log Storage
- Open Source
- Storage
- Streaming
- Spectral
- Linting
- API Governance
---
