---
api_specs:
- filename: apache-cloudstack-api-openapi.yaml
  format: yaml
  label: Apache CloudStack API
  slug: apache-cloudstack-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-cloudstack/refs/heads/main/openapi/apache-cloudstack-api-openapi.yaml
categories:
- cloudstack
description: Spectral linting rules defining API design standards and conventions for Apache CloudStack.
layout: rules
name: Apache CloudStack API Rules
provider_name: Apache CloudStack
provider_slug: apache-cloudstack
rule_count: 12
rules:
- description: API info must have a title
  given: $.info
  name: cloudstack-api-info-title
  severity: error
- description: API info must have a description
  given: $.info
  name: cloudstack-api-info-description
  severity: warn
- description: API info must have a version
  given: $.info
  name: cloudstack-api-info-version
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,put,post,delete,patch]
  name: cloudstack-api-operation-id
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,put,post,delete,patch]
  name: cloudstack-api-operation-summary
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,put,post,delete,patch]
  name: cloudstack-api-operation-tags
  severity: warn
- description: GET operations should have a 200 response
  given: $.paths[*][get]
  name: cloudstack-api-response-200
  severity: warn
- description: All component schemas must have a title
  given: $.components.schemas[*]
  name: cloudstack-api-schema-title
  severity: warn
- description: All component schemas must have a description
  given: $.components.schemas[*]
  name: cloudstack-api-schema-description
  severity: warn
- description: Operation summaries should start with Apache CloudStack
  given: $.paths[*][get,put,post,delete,patch].summary
  name: cloudstack-api-summary-prefix
  severity: warn
- description: All operations should use apiKeyAuth security
  given: $.paths[*][get,put,post,delete,patch]
  name: cloudstack-api-apikey-security
  severity: warn
- description: All operations should have x-microcks-operation extension
  given: $.paths[*][get,put,post,delete,patch]
  name: cloudstack-api-microcks-operation
  severity: info
rules_file: rules/apache-cloudstack-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-cloudstack/refs/heads/main/rules/apache-cloudstack-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 1
  warn: 8
slug: apache-cloudstack-spectral-rules
source_filename: apache-cloudstack-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  cloudstack-api-info-title:\n    description: API info must have a title\n    message: API info.title is required\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  cloudstack-api-info-description:\n    description: API info must have a description\n    message: API info.description is required\n    severity: warn\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  cloudstack-api-info-version:\n    description: API info must have a version\n    message: API info.version is required\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  cloudstack-api-operation-id:\n    description: All operations must have an operationId\n    message: Operation must have an operationId\n    severity: error\n    given: $.paths[*][get,put,post,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n\n  cloudstack-api-operation-summary:\n\
  \    description: All operations must have a summary\n    message: Operation must have a summary\n    severity: warn\n    given: $.paths[*][get,put,post,delete,patch]\n    then:\n      field: summary\n      function: truthy\n\n  cloudstack-api-operation-tags:\n    description: All operations must have at least one tag\n    message: Operation must have at least one tag\n    severity: warn\n    given: $.paths[*][get,put,post,delete,patch]\n    then:\n      field: tags\n      function: truthy\n\n  cloudstack-api-response-200:\n    description: GET operations should have a 200 response\n    message: GET operations should define a 200 response\n    severity: warn\n    given: $.paths[*][get]\n    then:\n      field: responses.200\n      function: truthy\n\n  cloudstack-api-schema-title:\n    description: All component schemas must have a title\n    message: Schema must have a title\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: title\n      function: truthy\n\
  \n  cloudstack-api-schema-description:\n    description: All component schemas must have a description\n    message: Schema must have a description\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  cloudstack-api-summary-prefix:\n    description: Operation summaries should start with Apache CloudStack\n    message: Operation summary should begin with \"Apache CloudStack\"\n    severity: warn\n    given: $.paths[*][get,put,post,delete,patch].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Apache CloudStack\n\n  cloudstack-api-apikey-security:\n    description: All operations should use apiKeyAuth security\n    message: Operation should declare apiKeyAuth security\n    severity: warn\n    given: $.paths[*][get,put,post,delete,patch]\n    then:\n      field: security\n      function: truthy\n\n  cloudstack-api-microcks-operation:\n    description: All operations should have x-microcks-operation\
  \ extension\n    message: Operation should include x-microcks-operation for mock support\n    severity: info\n    given: $.paths[*][get,put,post,delete,patch]\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-cloudstack/refs/heads/main/rules/apache-cloudstack-spectral-rules.yml
tags:
- Apache
- Cloud
- IaaS
- Infrastructure
- Open Source
- Virtualization
- Spectral
- Linting
- API Governance
---
