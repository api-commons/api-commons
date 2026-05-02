---
api_specs:
- filename: aws-redshift-openapi.json
  format: json
  label: Amazon Redshift API
  slug: amazon-redshift-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aws-redshift/refs/heads/main/openapi/aws-redshift-openapi.json
- filename: aws-redshift-data-openapi.json
  format: json
  label: Amazon Redshift Data API
  slug: amazon-redshift-data-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aws-redshift/refs/heads/main/openapi/aws-redshift-data-openapi.json
categories:
- redshift
description: Spectral linting rules defining API design standards and conventions for AWS Redshift.
layout: rules
name: AWS Redshift API Rules
provider_name: AWS Redshift
provider_slug: aws-redshift
rule_count: 11
rules:
- description: All operations must have a summary starting with "Amazon Redshift"
  given: $.paths[*][get,post,put,delete,patch]
  name: redshift-operation-summary
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: redshift-operation-id
  severity: error
- description: All operations should have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: redshift-operation-description
  severity: warn
- description: Components schemas should be defined
  given: $.components
  name: redshift-components-schemas
  severity: warn
- description: API security schemes should be defined
  given: $
  name: redshift-security-defined
  severity: warn
- description: Info object must have a title
  given: $.info
  name: redshift-info-title
  severity: error
- description: Info object must have a version
  given: $.info
  name: redshift-info-version
  severity: error
- description: All parameters should have a description
  given: $.paths[*][*].parameters[*]
  name: redshift-parameter-description
  severity: warn
- description: All response objects must have a description
  given: $.paths[*][*].responses[*]
  name: redshift-response-description
  severity: error
- description: Schema properties should have a type
  given: $.components.schemas[*]
  name: redshift-schema-type
  severity: warn
- description: Operations should have x-microcks-operation annotation
  given: $.paths[*][get,post,put,delete,patch]
  name: redshift-microcks-annotation
  severity: info
rules_file: rules/aws-redshift-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aws-redshift/refs/heads/main/rules/aws-redshift-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 6
slug: aws-redshift-spectral-rules
source_filename: aws-redshift-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  redshift-operation-summary:\n    description: All operations must have a summary starting with \"Amazon Redshift\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Redshift\"\n\n  redshift-operation-id:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  redshift-operation-description:\n    description: All operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: description\n      function: truthy\n\n  redshift-components-schemas:\n    description: Components schemas should be defined\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: schemas\n      function: truthy\n\n  redshift-security-defined:\n\
  \    description: API security schemes should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  redshift-info-title:\n    description: Info object must have a title\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  redshift-info-version:\n    description: Info object must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  redshift-parameter-description:\n    description: All parameters should have a description\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  redshift-response-description:\n    description: All response objects must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  redshift-schema-type:\n   \
  \ description: Schema properties should have a type\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  redshift-microcks-annotation:\n    description: Operations should have x-microcks-operation annotation\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/aws-redshift/refs/heads/main/rules/aws-redshift-spectral-rules.yml
tags:
- Analytics
- Big Data
- Cloud Database
- Data Warehouse
- SQL
- Spectral
- Linting
- API Governance
---
