---
api_specs:
- filename: apache-dubbo-admin-openapi-original.json
  format: json
  label: Apache Dubbo Admin API
  slug: apache-dubbo-admin
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-dubbo/refs/heads/main/openapi/apache-dubbo-admin-openapi-original.json
categories:
- info
- 'no'
- operation
- parameter
- paths
- response
- schema
description: Spectral linting rules defining API design standards and conventions for Apache Dubbo.
layout: rules
name: Apache Dubbo API Rules
provider_name: Apache Dubbo
provider_slug: apache-dubbo
rule_count: 15
rules:
- description: Info title must be defined
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: warn
- description: API version must be specified
  given: $.info
  name: info-version-required
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with Apache Dubbo
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-apache-dubbo-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationId-required
  severity: error
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Operations must define at least one 2xx response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: Schema properties should have descriptions
  given: $.definitions[*].properties[*]
  name: schema-property-description
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/apache-dubbo-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-dubbo/refs/heads/main/rules/apache-dubbo-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 1
  warn: 9
slug: apache-dubbo-spectral-rules
source_filename: apache-dubbo-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Apache Dubbo Admin API Spectral Ruleset\n# Enforces conventions observed across the Dubbo Admin API specification\n\nrules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be defined\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info description must be present\n    severity: warn\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API version must be specified\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-apache-dubbo-prefix:\n    description: Operation summaries should\
  \ start with Apache Dubbo\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache Dubbo\"\n\n  operation-description-required:\n    description: All operations must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: description\n      function: truthy\n\n  operation-operationId-required:\n    description: All operations must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: tags\n      function: truthy\n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: $.paths\n    then:\n\
  \      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}_-]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must define at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          minProperties: 1\n\n  response-description-required:\n    description: All responses must have descriptions\n    severity:\
  \ warn\n    given: $.paths[*][get,post,put,delete,patch].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-property-description:\n    description: Schema properties should have descriptions\n    severity: info\n    given: $.definitions[*].properties[*]\n    then:\n      field: description\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-dubbo/refs/heads/main/rules/apache-dubbo-spectral-rules.yml
tags:
- Apache
- Go
- Java
- Microservices
- Open Source
- RPC
- Service Discovery
- Service Mesh
- Spectral
- Linting
- API Governance
---
