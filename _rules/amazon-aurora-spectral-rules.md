---
api_specs:
- filename: amazon-aurora-openapi.yml
  format: yaml
  label: Amazon Aurora API
  slug: amazon-aurora-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/openapi/amazon-aurora-openapi.yml
categories:
- aurora
description: Spectral linting rules defining API design standards and conventions for Amazon Aurora.
layout: rules
name: Amazon Aurora API Rules
provider_name: Amazon Aurora
provider_slug: amazon-aurora
rule_count: 14
rules:
- description: All operationIds must be camelCase
  given: $.paths[*][*].operationId
  name: aurora-operation-id-camel-case
  severity: warn
- description: All operation summaries must start with Amazon Aurora
  given: $.paths[*][*].summary
  name: aurora-summary-prefix
  severity: warn
- description: All operations must have tags
  given: $.paths[*][*]
  name: aurora-has-tags
  severity: warn
- description: All operations must have a 200 response
  given: $.paths[*][*].responses
  name: aurora-response-200
  severity: error
- description: CreateDBClusterInput must require DBClusterIdentifier and Engine
  given: $.components.schemas.CreateDBClusterInput
  name: aurora-create-cluster-required
  severity: error
- description: Engine must use valid enum values for Aurora
  given: $.components.schemas.CreateDBClusterInput.properties.Engine
  name: aurora-engine-enum
  severity: error
- description: CreateDBClusterEndpoint EndpointType must use valid enum values
  given: $.components.schemas.CreateDBClusterEndpointInput.properties.EndpointType
  name: aurora-endpoint-type-enum
  severity: error
- description: API must use sigv4 security scheme
  given: $.security[*]
  name: aurora-security-sigv4
  severity: error
- description: Server URL must be fixed without variables
  given: $.servers[*]
  name: aurora-server-url-fixed
  severity: warn
- description: All examples must have x-microcks-default set to true
  given: $.paths[*][*].responses[*].content[*].examples.default
  name: aurora-example-microcks-default
  severity: warn
- description: DBCluster DBClusterIdentifier must be string type
  given: $.components.schemas.DBCluster.properties.DBClusterIdentifier
  name: aurora-db-cluster-identifier-string
  severity: error
- description: Filter Values must be an array
  given: $.components.schemas.Filter.properties.Values
  name: aurora-filter-values-array
  severity: error
- description: GlobalCluster GlobalClusterIdentifier must be string type
  given: $.components.schemas.GlobalCluster.properties.GlobalClusterIdentifier
  name: aurora-global-cluster-identifier-string
  severity: error
- description: DBClusterSnapshot Status must be defined
  given: $.components.schemas.DBClusterSnapshot.properties
  name: aurora-snapshot-status-defined
  severity: warn
rules_file: rules/amazon-aurora-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/rules/amazon-aurora-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 0
  warn: 6
slug: amazon-aurora-spectral-rules
source_filename: amazon-aurora-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  aurora-operation-id-camel-case:\n    description: All operationIds must be camelCase\n    message: \"{{property}} must be camelCase\"\n    severity: warn\n    given: \"$.paths[*][*].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  aurora-summary-prefix:\n    description: All operation summaries must start with Amazon Aurora\n    message: Summary must start with Amazon Aurora\n    severity: warn\n    given: \"$.paths[*][*].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Aurora\"\n\n  aurora-has-tags:\n    description: All operations must have tags\n    message: Operation must have at least one tag\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n\n  aurora-response-200:\n    description: All operations must have a 200 response\n    message: Operation must define a 200 response\n    severity: error\n\
  \    given: \"$.paths[*][*].responses\"\n    then:\n      field: \"200\"\n      function: truthy\n\n  aurora-create-cluster-required:\n    description: CreateDBClusterInput must require DBClusterIdentifier and Engine\n    message: CreateDBClusterInput must have required fields\n    severity: error\n    given: \"$.components.schemas.CreateDBClusterInput\"\n    then:\n      field: required\n      function: truthy\n\n  aurora-engine-enum:\n    description: Engine must use valid enum values for Aurora\n    message: Engine must be aurora-mysql or aurora-postgresql\n    severity: error\n    given: \"$.components.schemas.CreateDBClusterInput.properties.Engine\"\n    then:\n      field: enum\n      function: truthy\n\n  aurora-endpoint-type-enum:\n    description: CreateDBClusterEndpoint EndpointType must use valid enum values\n    message: EndpointType must be READER or ANY\n    severity: error\n    given: \"$.components.schemas.CreateDBClusterEndpointInput.properties.EndpointType\"\n    then:\n\
  \      field: enum\n      function: truthy\n\n  aurora-security-sigv4:\n    description: API must use sigv4 security scheme\n    message: Security must include sigv4\n    severity: error\n    given: \"$.security[*]\"\n    then:\n      field: sigv4\n      function: defined\n\n  aurora-server-url-fixed:\n    description: Server URL must be fixed without variables\n    message: Server URL must not use variables\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: variables\n      function: falsy\n\n  aurora-example-microcks-default:\n    description: All examples must have x-microcks-default set to true\n    message: Example must have x-microcks-default true\n    severity: warn\n    given: \"$.paths[*][*].responses[*].content[*].examples.default\"\n    then:\n      field: x-microcks-default\n      function: truthy\n\n  aurora-db-cluster-identifier-string:\n    description: DBCluster DBClusterIdentifier must be string type\n    message: DBClusterIdentifier must be a string\n\
  \    severity: error\n    given: \"$.components.schemas.DBCluster.properties.DBClusterIdentifier\"\n    then:\n      field: type\n      function: truthy\n\n  aurora-filter-values-array:\n    description: Filter Values must be an array\n    message: Filter Values must be an array\n    severity: error\n    given: \"$.components.schemas.Filter.properties.Values\"\n    then:\n      field: type\n      function: enumeration\n      functionOptions:\n        values:\n          - array\n\n  aurora-global-cluster-identifier-string:\n    description: GlobalCluster GlobalClusterIdentifier must be string type\n    message: GlobalClusterIdentifier must be a string\n    severity: error\n    given: \"$.components.schemas.GlobalCluster.properties.GlobalClusterIdentifier\"\n    then:\n      field: type\n      function: truthy\n\n  aurora-snapshot-status-defined:\n    description: DBClusterSnapshot Status must be defined\n    message: DBClusterSnapshot must have a Status property\n    severity: warn\n  \
  \  given: \"$.components.schemas.DBClusterSnapshot.properties\"\n    then:\n      field: Status\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/rules/amazon-aurora-spectral-rules.yml
tags:
- Amazon Aurora
- MySQL
- PostgreSQL
- Relational Database
- Spectral
- Linting
- API Governance
---
