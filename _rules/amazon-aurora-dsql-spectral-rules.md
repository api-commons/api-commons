---
api_specs:
- filename: amazon-aurora-dsql-openapi.yml
  format: yaml
  label: Amazon Aurora DSQL API
  slug: amazon-aurora-dsql-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/openapi/amazon-aurora-dsql-openapi.yml
categories:
- aurora
description: Spectral linting rules defining API design standards and conventions for Amazon Aurora DSQL.
layout: rules
name: Amazon Aurora DSQL API Rules
provider_name: Amazon Aurora DSQL
provider_slug: amazon-aurora-dsql
rule_count: 10
rules:
- description: All operationIds must be camelCase
  given: $.paths[*][*].operationId
  name: aurora-dsql-operation-id-camel-case
  severity: warn
- description: All operation summaries must start with Amazon Aurora DSQL
  given: $.paths[*][*].summary
  name: aurora-dsql-summary-prefix
  severity: warn
- description: All operations must have tags
  given: $.paths[*][*]
  name: aurora-dsql-has-tags
  severity: warn
- description: All operations must have a 200 response
  given: $.paths[*][*].responses
  name: aurora-dsql-response-200
  severity: error
- description: ClusterStatus must use valid enum values
  given: $.components.schemas.ClusterStatus
  name: aurora-dsql-cluster-status-enum
  severity: error
- description: API must use sigv4 security scheme
  given: $.security[*]
  name: aurora-dsql-security-sigv4
  severity: error
- description: Server URL must be fixed without variables
  given: $.servers[*]
  name: aurora-dsql-server-url-fixed
  severity: warn
- description: All examples must have x-microcks-default set to true
  given: $.paths[*][*].responses[*].content[*].examples.default
  name: aurora-dsql-example-microcks-default
  severity: warn
- description: CreateMultiRegionClustersInput must require linkedRegionList
  given: $.components.schemas.CreateMultiRegionClustersInput
  name: aurora-dsql-multi-region-linked-list-required
  severity: error
- description: ClusterSummary identifier must be string type
  given: $.components.schemas.ClusterSummary.properties.identifier
  name: aurora-dsql-cluster-identifier-string
  severity: error
rules_file: rules/amazon-aurora-dsql-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/rules/amazon-aurora-dsql-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 0
  warn: 5
slug: amazon-aurora-dsql-spectral-rules
source_filename: amazon-aurora-dsql-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  aurora-dsql-operation-id-camel-case:\n    description: All operationIds must be camelCase\n    message: \"{{property}} must be camelCase\"\n    severity: warn\n    given: \"$.paths[*][*].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  aurora-dsql-summary-prefix:\n    description: All operation summaries must start with Amazon Aurora DSQL\n    message: Summary must start with Amazon Aurora DSQL\n    severity: warn\n    given: \"$.paths[*][*].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Aurora DSQL\"\n\n  aurora-dsql-has-tags:\n    description: All operations must have tags\n    message: Operation must have at least one tag\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n\n  aurora-dsql-response-200:\n    description: All operations must have a 200 response\n    message: Operation must define\
  \ a 200 response\n    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      field: \"200\"\n      function: truthy\n\n  aurora-dsql-cluster-status-enum:\n    description: ClusterStatus must use valid enum values\n    message: ClusterStatus must be CREATING, ACTIVE, IDLE, UPDATING, DELETING, DELETED, or FAILED\n    severity: error\n    given: \"$.components.schemas.ClusterStatus\"\n    then:\n      field: enum\n      function: truthy\n\n  aurora-dsql-security-sigv4:\n    description: API must use sigv4 security scheme\n    message: Security must include sigv4\n    severity: error\n    given: \"$.security[*]\"\n    then:\n      field: sigv4\n      function: defined\n\n  aurora-dsql-server-url-fixed:\n    description: Server URL must be fixed without variables\n    message: Server URL must not use variables\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: variables\n      function: falsy\n\n  aurora-dsql-example-microcks-default:\n    description:\
  \ All examples must have x-microcks-default set to true\n    message: Example must have x-microcks-default true\n    severity: warn\n    given: \"$.paths[*][*].responses[*].content[*].examples.default\"\n    then:\n      field: x-microcks-default\n      function: truthy\n\n  aurora-dsql-multi-region-linked-list-required:\n    description: CreateMultiRegionClustersInput must require linkedRegionList\n    message: CreateMultiRegionClustersInput must have linkedRegionList as required\n    severity: error\n    given: \"$.components.schemas.CreateMultiRegionClustersInput\"\n    then:\n      field: required\n      function: truthy\n\n  aurora-dsql-cluster-identifier-string:\n    description: ClusterSummary identifier must be string type\n    message: identifier must be a string\n    severity: error\n    given: \"$.components.schemas.ClusterSummary.properties.identifier\"\n    then:\n      field: type\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/rules/amazon-aurora-dsql-spectral-rules.yml
tags:
- Amazon Aurora DSQL
- Distributed SQL
- PostgreSQL
- Serverless
- Spectral
- Linting
- API Governance
---
