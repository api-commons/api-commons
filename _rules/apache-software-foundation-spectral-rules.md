---
api_specs:
- filename: apache-software-foundation-projects-api-openapi.yml
  format: yaml
  label: Apache Software Foundation Projects API
  slug: projects-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-software-foundation/refs/heads/main/openapi/apache-software-foundation-projects-api-openapi.yml
- filename: apache-software-foundation-whimsy-api-openapi.yml
  format: yaml
  label: Apache Software Foundation Whimsy Public Data API
  slug: whimsy-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-software-foundation/refs/heads/main/openapi/apache-software-foundation-whimsy-api-openapi.yml
categories:
- info
- 'no'
- openapi
- operation
- paths
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Apache Software Foundation.
layout: rules
name: Apache Software Foundation API Rules
provider_name: Apache Software Foundation
provider_slug: apache-software-foundation
rule_count: 18
rules:
- description: Info title is required
  given: $.info
  name: info-title-required
  severity: error
- description: Info description is required and should be at least 30 characters
  given: $.info
  name: info-description-required
  severity: warn
- description: API version is required
  given: $.info
  name: info-version-required
  severity: error
- description: License information is required for ASF projects
  given: $.info
  name: info-license-required
  severity: warn
- description: Use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers array is required
  given: $
  name: servers-required
  severity: error
- description: All server URLs should use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: All operations should have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-operationid-required
  severity: error
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: warn
- description: Operation summaries should start with "Apache Software Foundation"
  given: $.paths[*][get,post,put,patch,delete,head,options].summary
  name: operation-summary-prefix
  severity: info
- description: Every operation should have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete,head,options].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options].responses[*]
  name: response-description-required
  severity: error
- description: All schema properties should have a type
  given: $.components.schemas[*].properties[*]
  name: schema-type-required
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
- description: Descriptions should not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/apache-software-foundation-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-software-foundation/refs/heads/main/rules/apache-software-foundation-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 3
  warn: 7
slug: apache-software-foundation-spectral-rules
source_filename: apache-software-foundation-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Apache Software Foundation API Spectral Rules\nrules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: Info title is required\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info description is required and should be at least 30 characters\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API version is required\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-license-required:\n    description: License information is required for ASF projects\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function:\
  \ pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: Servers array is required\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: All server URLs should use HTTPS\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: All operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: All\
  \ operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: tags\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Apache Software Foundation\"\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache Software Foundation\"\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation should have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].responses\"\n    then:\n      function: schema\n      functionOptions:\n\
  \        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-type-required:\n    description: All schema properties should have a type\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  schema-description-required:\n    description: Top-level schemas should have descriptions\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n\
  \      functionOptions:\n        match: \"^(/[a-z0-9./_-]+)+$\"\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions should not be empty strings\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-software-foundation/refs/heads/main/rules/apache-software-foundation-spectral-rules.yml
tags:
- ASF
- Open Source
- Governance
- Projects
- Apache
- Spectral
- Linting
- API Governance
---
