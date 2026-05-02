---
api_specs:
- filename: amazon-athena-openapi.yml
  format: yaml
  label: Amazon Athena API
  slug: amazon-athena-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/openapi/amazon-athena-openapi.yml
categories:
- athena
description: Spectral linting rules defining API design standards and conventions for Amazon Athena.
layout: rules
name: Amazon Athena API Rules
provider_name: Amazon Athena
provider_slug: amazon-athena
rule_count: 19
rules:
- description: StartQueryExecution must require QueryString
  given: $.components.schemas.StartQueryExecutionInput
  name: athena-query-string-required
  severity: error
- description: All operationIds must be camelCase
  given: $.paths[*][*].operationId
  name: athena-operation-id-camel-case
  severity: warn
- description: All operation summaries must start with Amazon Athena
  given: $.paths[*][*].summary
  name: athena-summary-prefix
  severity: warn
- description: All operations must have tags
  given: $.paths[*][*]
  name: athena-has-tags
  severity: warn
- description: Server URL must be fixed without variables
  given: $.servers[*]
  name: athena-server-url-fixed
  severity: warn
- description: All operations must have a 200 response
  given: $.paths[*][*].responses
  name: athena-response-200
  severity: error
- description: POST operations must have a request body
  given: $.paths[*].post
  name: athena-request-body-required
  severity: error
- description: QueryExecutionId must be of type string
  given: $.components.schemas[*].properties.QueryExecutionId
  name: athena-query-execution-id-string
  severity: error
- description: NamedQueryId must be of type string
  given: $.components.schemas[*].properties.NamedQueryId
  name: athena-named-query-id-string
  severity: error
- description: WorkGroup State must use valid enum values
  given: $.components.schemas.WorkGroup.properties.State
  name: athena-work-group-state-enum
  severity: error
- description: DataCatalog Type must use valid enum values
  given: $.components.schemas.DataCatalog.properties.Type
  name: athena-data-catalog-type-enum
  severity: error
- description: QueryExecutionStatus State must use valid enum values
  given: $.components.schemas.QueryExecutionStatus.properties.State
  name: athena-query-status-state-enum
  severity: error
- description: Tag schema must define Key property
  given: $.components.schemas.Tag.properties
  name: athena-tag-key-defined
  severity: error
- description: Tag schema must define Value property
  given: $.components.schemas.Tag.properties
  name: athena-tag-value-defined
  severity: error
- description: ResultConfiguration must have OutputLocation
  given: $.components.schemas.ResultConfiguration.properties
  name: athena-result-configuration-output-location
  severity: warn
- description: EngineVersion schema must be defined
  given: $.components.schemas
  name: athena-engine-version-defined
  severity: warn
- description: ColumnInfo must define Name property
  given: $.components.schemas.ColumnInfo.properties
  name: athena-column-info-name-defined
  severity: error
- description: All examples must have x-microcks-default set to true
  given: $.paths[*][*].requestBody.content[*].examples.default
  name: athena-example-microcks-default
  severity: warn
- description: API must use sigv4 security scheme
  given: $.security[*]
  name: athena-security-sigv4
  severity: error
rules_file: rules/amazon-athena-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/rules/amazon-athena-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 0
  warn: 7
slug: amazon-athena-spectral-rules
source_filename: amazon-athena-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  athena-query-string-required:\n    description: StartQueryExecution must require QueryString\n    message: StartQueryExecutionInput must have QueryString as required\n    severity: error\n    given: \"$.components.schemas.StartQueryExecutionInput\"\n    then:\n      field: required\n      function: truthy\n\n  athena-operation-id-camel-case:\n    description: All operationIds must be camelCase\n    message: \"{{property}} must be camelCase\"\n    severity: warn\n    given: \"$.paths[*][*].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  athena-summary-prefix:\n    description: All operation summaries must start with Amazon Athena\n    message: Summary must start with Amazon Athena\n    severity: warn\n    given: \"$.paths[*][*].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Athena\"\n\n  athena-has-tags:\n    description: All operations must have\
  \ tags\n    message: Operation must have at least one tag\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n\n  athena-server-url-fixed:\n    description: Server URL must be fixed without variables\n    message: Server URL must not use variables\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: variables\n      function: falsy\n\n  athena-response-200:\n    description: All operations must have a 200 response\n    message: Operation must define a 200 response\n    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      field: \"200\"\n      function: truthy\n\n  athena-request-body-required:\n    description: POST operations must have a request body\n    message: POST operation must have a requestBody\n    severity: error\n    given: \"$.paths[*].post\"\n    then:\n      field: requestBody\n      function: truthy\n\n  athena-query-execution-id-string:\n    description: QueryExecutionId must\
  \ be of type string\n    message: QueryExecutionId must be a string\n    severity: error\n    given: \"$.components.schemas[*].properties.QueryExecutionId\"\n    then:\n      field: type\n      function: enumeration\n      functionOptions:\n        values:\n          - string\n\n  athena-named-query-id-string:\n    description: NamedQueryId must be of type string\n    message: NamedQueryId must be a string\n    severity: error\n    given: \"$.components.schemas[*].properties.NamedQueryId\"\n    then:\n      field: type\n      function: enumeration\n      functionOptions:\n        values:\n          - string\n\n  athena-work-group-state-enum:\n    description: WorkGroup State must use valid enum values\n    message: WorkGroup State must be ENABLED or DISABLED\n    severity: error\n    given: \"$.components.schemas.WorkGroup.properties.State\"\n    then:\n      field: enum\n      function: truthy\n\n  athena-data-catalog-type-enum:\n    description: DataCatalog Type must use valid enum values\n\
  \    message: DataCatalog Type must be LAMBDA, GLUE, or HIVE\n    severity: error\n    given: \"$.components.schemas.DataCatalog.properties.Type\"\n    then:\n      field: enum\n      function: truthy\n\n  athena-query-status-state-enum:\n    description: QueryExecutionStatus State must use valid enum values\n    message: State must be QUEUED, RUNNING, SUCCEEDED, FAILED, or CANCELLED\n    severity: error\n    given: \"$.components.schemas.QueryExecutionStatus.properties.State\"\n    then:\n      field: enum\n      function: truthy\n\n  athena-tag-key-defined:\n    description: Tag schema must define Key property\n    message: Tag must have a Key property\n    severity: error\n    given: \"$.components.schemas.Tag.properties\"\n    then:\n      field: Key\n      function: truthy\n\n  athena-tag-value-defined:\n    description: Tag schema must define Value property\n    message: Tag must have a Value property\n    severity: error\n    given: \"$.components.schemas.Tag.properties\"\n    then:\n\
  \      field: Value\n      function: truthy\n\n  athena-result-configuration-output-location:\n    description: ResultConfiguration must have OutputLocation\n    message: ResultConfiguration must define OutputLocation\n    severity: warn\n    given: \"$.components.schemas.ResultConfiguration.properties\"\n    then:\n      field: OutputLocation\n      function: truthy\n\n  athena-engine-version-defined:\n    description: EngineVersion schema must be defined\n    message: EngineVersion must be defined in components\n    severity: warn\n    given: \"$.components.schemas\"\n    then:\n      field: EngineVersion\n      function: truthy\n\n  athena-column-info-name-defined:\n    description: ColumnInfo must define Name property\n    message: ColumnInfo must have Name\n    severity: error\n    given: \"$.components.schemas.ColumnInfo.properties\"\n    then:\n      field: Name\n      function: truthy\n\n  athena-example-microcks-default:\n    description: All examples must have x-microcks-default\
  \ set to true\n    message: Example must have x-microcks-default true\n    severity: warn\n    given: \"$.paths[*][*].requestBody.content[*].examples.default\"\n    then:\n      field: x-microcks-default\n      function: truthy\n\n  athena-security-sigv4:\n    description: API must use sigv4 security scheme\n    message: Security must include sigv4\n    severity: error\n    given: \"$.security[*]\"\n    then:\n      field: sigv4\n      function: defined\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/rules/amazon-athena-spectral-rules.yml
tags:
- Amazon Athena
- SQL
- Analytics
- Serverless
- Spectral
- Linting
- API Governance
---
