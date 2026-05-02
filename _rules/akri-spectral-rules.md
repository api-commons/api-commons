---
api_specs:
- filename: akri-metrics-openapi.yaml
  format: yaml
  label: Akri Metrics API
  slug: metrics-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/openapi/akri-metrics-openapi.yaml
categories:
- examples
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Akri.
layout: rules
name: Akri API Rules
provider_name: Akri
provider_slug: akri
rule_count: 25
rules:
- description: Info title must be defined
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be defined and non-empty
  given: $.info
  name: info-description-required
  severity: warn
- description: Info version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: Info should include contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Info should include license information (Apache 2.0 for CNCF projects)
  given: $.info
  name: info-license-required
  severity: warn
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs should use HTTPS (or localhost for metrics)
  given: $.servers[*]
  name: servers-https-required
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-operationid-required
  severity: error
- description: OperationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: Operation summaries should start with 'Akri'
  given: $.paths[*][get,post,put,patch,delete,head,options].summary
  name: operation-summary-akri-prefix
  severity: warn
- description: Tags should be defined at the global level
  given: $
  name: tags-defined
  severity: warn
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tags-description-required
  severity: warn
- description: Parameters must have a description
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas should define a type
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should have examples
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/akri-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/rules/akri-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 1
  warn: 12
slug: akri-spectral-rules
source_filename: akri-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be defined\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info description must be defined and non-empty\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info version must be defined\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info should include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  info-license-required:\n    description: Info should include license information (Apache 2.0 for CNCF projects)\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  # OPENAPI\
  \ VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.0.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-required:\n    description: Server URLs should use HTTPS (or localhost for metrics)\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^(https://|http://localhost)\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9-{}]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not\
  \ have a trailing slash\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camel-case:\n    description: OperationId should use camelCase\n    severity: warn\n    given:\
  \ \"$.paths[*][get,post,put,patch,delete,head,options].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: Operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: tags\n      function: truthy\n\n  operation-summary-akri-prefix:\n    description: Operation summaries should start with 'Akri'\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Akri \"\n\n  # TAGS\n  tags-defined:\n    description: Tags should be defined at the global level\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  tags-description-required:\n    description: Global tags should have descriptions\n    severity: warn\n    given: \"$.tags[*]\"\n    then:\n\
  \      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Parameters must have a description\n    severity: error\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          patternProperties:\n            \"^2[0-9]{2}$\": {}\n          minProperties: 1\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level schemas should have descriptions\n\
  \    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schemas should define a type\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  examples-encouraged:\n    description: Schema properties should have examples\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/rules/akri-spectral-rules.yml
tags:
- Device Management
- Edge Computing
- IoT
- Kubernetes
- CNCF
- Open Source
- OPC UA
- ONVIF
- udev
- Spectral
- Linting
- API Governance
---
