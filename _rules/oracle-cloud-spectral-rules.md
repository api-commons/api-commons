---
api_specs:
- filename: oracle-cloud-compute-openapi.yaml
  format: yaml
  label: Compute API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/openapi/oracle-cloud-compute-openapi.yaml
- filename: oracle-cloud-object-storage-openapi.yaml
  format: yaml
  label: Object Storage API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/openapi/oracle-cloud-object-storage-openapi.yaml
- filename: oracle-cloud-networking-openapi.yaml
  format: yaml
  label: Networking API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/openapi/oracle-cloud-networking-openapi.yaml
- filename: oracle-cloud-database-openapi.yaml
  format: yaml
  label: Database API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/openapi/oracle-cloud-database-openapi.yaml
- filename: oracle-cloud-iam-openapi.yaml
  format: yaml
  label: Identity and Access Management API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/openapi/oracle-cloud-iam-openapi.yaml
- filename: oracle-cloud-oke-openapi.yaml
  format: yaml
  label: Container Engine for Kubernetes API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/openapi/oracle-cloud-oke-openapi.yaml
- filename: oracle-cloud-functions-openapi.yaml
  format: yaml
  label: Functions API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/openapi/oracle-cloud-functions-openapi.yaml
- filename: oracle-cloud-monitoring-openapi.yaml
  format: yaml
  label: Monitoring API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/openapi/oracle-cloud-monitoring-openapi.yaml
categories:
- delete
- get
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- server
- servers
description: Spectral linting rules defining API design standards and conventions for Oracle Cloud Infrastructure.
layout: rules
name: Oracle Cloud Infrastructure API Rules
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
rule_count: 25
rules:
- description: Info title must start with "Oracle Cloud"
  given: $.info.title
  name: info-title-format
  severity: error
- description: Info description is required
  given: $.info
  name: info-description-required
  severity: error
- description: API version is required
  given: $.info
  name: info-version-required
  severity: error
- description: OpenAPI version must be 3.0.x
  given: $
  name: openapi-version
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: server-https
  severity: error
- description: Path segments should use camelCase (OCI convention)
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Oracle Cloud"
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: warn
- description: Every operation must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: OperationId should use camelCase
  given: $.paths[*][get,post,put,delete,patch].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Operations must define at least one success response (2xx)
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: Schema property names should use camelCase (OCI convention)
  given: $.components.schemas[*].properties
  name: schema-properties-camel-case
  severity: info
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should include x-microcks-operation extension
  given: $.paths[*][get,post,put,delete,patch]
  name: microcks-operation-extension
  severity: info
rules_file: rules/oracle-cloud-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/rules/oracle-cloud-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 3
  warn: 8
slug: oracle-cloud-spectral-rules
source_filename: oracle-cloud-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-format:\n    description: Info title must start with \"Oracle Cloud\"\n    severity: error\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Oracle Cloud.*\n  info-description-required:\n    description: Info description is required\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API version is required\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  openapi-version:\n    description: OpenAPI version must be 3.0.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: ^3\\.0\\.\\d+$\n  servers-defined:\n    description: Servers array must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n  server-https:\n    description: Server\
  \ URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: ^https://\n  paths-kebab-case:\n    description: Path segments should use camelCase (OCI convention)\n    severity: info\n    given: $.paths\n    then:\n      function: truthy\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: summary\n      function: truthy\n  operation-summary-prefix:\n    description: Operation summaries must start with \"Oracle Cloud\"\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].summary\n    then:\n      function: pattern\n      functionOptions:\n\
  \        match: ^Oracle Cloud.*\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: description\n      function: truthy\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: tags\n      function: truthy\n  operation-operationid-camel-case:\n    description: OperationId should use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: ^[a-z][a-zA-Z0-9]*$\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].parameters[*]\n    then:\n      field: description\n      function: truthy\n  parameter-schema-required:\n    description:\
  \ Every parameter must have a schema\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch].parameters[*]\n    then:\n      field: schema\n      function: truthy\n  response-success-required:\n    description: Operations must define at least one success response (2xx)\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch].responses\n    then:\n      function: truthy\n  response-description-required:\n    description: Every response must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].responses[*]\n    then:\n      field: description\n      function: truthy\n  schema-properties-camel-case:\n    description: Schema property names should use camelCase (OCI convention)\n    severity: info\n    given: $.components.schemas[*].properties\n    then:\n      function: truthy\n  schema-description-required:\n    description: Top-level schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n\
  \    then:\n      field: description\n      function: truthy\n  security-global-defined:\n    description: Global security must be defined\n    severity: error\n    given: $\n    then:\n      field: security\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then:\n      function: truthy\n  microcks-operation-extension:\n\
  \    description: Operations should include x-microcks-operation extension\n    severity: info\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/rules/oracle-cloud-spectral-rules.yml
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
- Spectral
- Linting
- API Governance
---
