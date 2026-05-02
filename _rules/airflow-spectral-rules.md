---
api_specs:
- filename: airflow-openapi.yml
  format: yaml
  label: Apache Airflow API
  slug: airflow
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/airflow/refs/heads/main/openapi/airflow-openapi.yml
categories:
- dag
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
- servers
description: Spectral linting rules defining API design standards and conventions for Apache Airflow.
layout: rules
name: Apache Airflow API Rules
provider_name: Apache Airflow
provider_slug: airflow
rule_count: 24
rules:
- description: Info title must be defined.
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be defined.
  given: $.info
  name: info-description-required
  severity: warn
- description: Info version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: OpenAPI version must be 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Stable API paths should start with /api/v2/.
  given: $.paths[*]~
  name: paths-api-v2-prefix
  severity: info
- description: Path segments should use snake_case or kebab-case.
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operation summaries should start with "Airflow".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-starts-with-airflow
  severity: info
- description: All parameters should have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have at least one success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Operations should document 401 Unauthorized responses.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-documented
  severity: info
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
- description: Schema property names should use snake_case.
  given: $.components.schemas[*].properties[*]~
  name: schema-properties-snake-case
  severity: info
- description: Security schemes should be defined.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations should not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 204 No Content.
  given: $.paths[*].delete.responses
  name: delete-returns-204
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should include x-microcks-operation for mock compatibility.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
- description: DAG endpoints are core to Airflow — they must be documented.
  given: $.paths
  name: dag-resource-required
  severity: info
rules_file: rules/airflow-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/airflow/refs/heads/main/rules/airflow-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 9
  warn: 7
slug: airflow-spectral-rules
source_filename: airflow-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be defined.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info description must be defined.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info version must be defined.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: OpenAPI version must be 3.x.\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  # PATHS\
  \ — NAMING CONVENTIONS\n  paths-api-v2-prefix:\n    description: Stable API paths should start with /api/v2/.\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/api/v2/|/ui/)\"\n\n  paths-kebab-case:\n    description: Path segments should use snake_case or kebab-case.\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9_{}/-]+)+$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Every operation should have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-operationId-required:\n\
  \    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  operation-summary-starts-with-airflow:\n    description: Operation summaries should start with \"Airflow\".\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Airflow \"\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters should have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n\
  \    description: Every operation must have at least one success response.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: truthy\n\n  response-description-required:\n    description: All responses must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-401-documented:\n    description: Operations should document 401 Unauthorized responses.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: truthy\n\n  # SCHEMAS\n  schema-description-recommended:\n    description: Top-level schemas should have a description.\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-properties-snake-case:\n    description: Schema property names should use snake_case.\n    severity:\
  \ info\n    given: \"$.components.schemas[*].properties[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes should be defined.\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations should not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-returns-204:\n    description: DELETE operations should return 204 No Content.\n    severity: info\n    given: \"$.paths[*].delete.responses\"\n    then:\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: truthy\n\n  microcks-operation-extension:\n\
  \    description: Operations should include x-microcks-operation for mock compatibility.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  dag-resource-required:\n    description: DAG endpoints are core to Airflow — they must be documented.\n    severity: info\n    given: \"$.paths\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/airflow/refs/heads/main/rules/airflow-spectral-rules.yml
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
- Spectral
- Linting
- API Governance
---
